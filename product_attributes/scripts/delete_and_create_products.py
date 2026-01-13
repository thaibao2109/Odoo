#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script xóa toàn bộ sản phẩm cũ và tạo lại sản phẩm mới với attributes
"""

import sys
import os

# Thêm đường dẫn Odoo
odoo_path = '/Users/baonguyen/Desktop/app/odoo-source'
sys.path.insert(0, odoo_path)

import odoo
from odoo import api, SUPERUSER_ID

def delete_all_and_create():
    """Xóa tất cả sản phẩm và tạo lại"""
    
    # Lấy database name
    db_name = sys.argv[1] if len(sys.argv) > 1 else None
    
    if not db_name:
        # Tìm database từ config hoặc list databases
        import subprocess
        try:
            result = subprocess.run(
                ['/opt/homebrew/opt/postgresql@14/bin/psql', '-U', 'odoo', '-d', 'postgres', '-t', '-c', 
                 "SELECT datname FROM pg_database WHERE datname NOT IN ('template0', 'template1', 'postgres') LIMIT 1;"],
                capture_output=True, text=True, timeout=5
            )
            db_name = result.stdout.strip()
        except:
            pass
        
        if not db_name:
            db_name = input("Nhập tên database: ").strip()
            if not db_name:
                print("❌ Cần tên database!")
                return False
    
    print(f"🔌 Kết nối database: {db_name}")
    
    try:
        odoo.tools.config.parse_config(['-d', db_name])
        registry = odoo.registry(db_name)
        
        with registry.cursor() as cr:
            env = api.Environment(cr, SUPERUSER_ID, {})
            
            print("✅ Đã kết nối thành công!\n")
            
            # 1. XÓA CÁC BẢN GHI LIÊN QUAN TRƯỚC (bằng SQL)
            print("🗑️  Đang xóa các bản ghi liên quan...")
            
            # Xóa BOM lines trước
            try:
                cr.execute("DELETE FROM mrp_bom_line")
                print(f"✅ Đã xóa BOM lines")
            except Exception as e:
                print(f"⚠️  BOM lines: {e}")
            
            # Xóa BOM
            try:
                cr.execute("DELETE FROM mrp_bom")
                print(f"✅ Đã xóa BOM")
            except Exception as e:
                print(f"⚠️  BOM: {e}")
            
            # Xóa sale order lines
            try:
                cr.execute("DELETE FROM sale_order_line")
                print(f"✅ Đã xóa sale order lines")
            except Exception as e:
                print(f"⚠️  Sale lines: {e}")
            
            # Xóa purchase order lines
            try:
                cr.execute("DELETE FROM purchase_order_line")
                print(f"✅ Đã xóa purchase order lines")
            except Exception as e:
                print(f"⚠️  Purchase lines: {e}")
            
            # Xóa stock moves
            try:
                cr.execute("DELETE FROM stock_move")
                print(f"✅ Đã xóa stock moves")
            except Exception as e:
                print(f"⚠️  Stock moves: {e}")
            
            # Xóa manufacturing orders
            try:
                cr.execute("DELETE FROM mrp_production")
                print(f"✅ Đã xóa manufacturing orders")
            except Exception as e:
                print(f"⚠️  MO: {e}")
            
            cr.commit()
            
            # 2. XÓA TẤT CẢ SẢN PHẨM
            print("\n🗑️  Đang xóa TẤT CẢ sản phẩm...")
            all_products = env['product.template'].search([])
            count = len(all_products)
            if count > 0:
                # Xóa tất cả cùng lúc
                try:
                    all_products.unlink()
                    print(f"✅ Đã xóa {count} sản phẩm")
                except Exception as e:
                    print(f"⚠️  Lỗi khi xóa: {e}")
                    # Thử xóa từng cái
                    deleted = 0
                    for product in all_products:
                        try:
                            product.unlink()
                            deleted += 1
                        except:
                            pass
                    print(f"✅ Đã xóa {deleted}/{count} sản phẩm")
            else:
                print("ℹ️  Không có sản phẩm nào để xóa")
            
            cr.commit()
            
            # 2. TẠO ATTRIBUTES
            print("\n📦 Tạo attributes...")
            
            # Đường kính
            diameter_attr = env['product.attribute'].search([('name', '=', 'Đường kính')], limit=1)
            if not diameter_attr:
                diameter_attr = env['product.attribute'].create({
                    'name': 'Đường kính',
                    'display_type': 'radio',
                    'create_variant': 'always',
                })
                print("✅ Đã tạo attribute: Đường kính")
            else:
                print("✅ Đã có attribute: Đường kính")
            
            # Chiều dài
            length_attr = env['product.attribute'].search([('name', '=', 'Chiều dài')], limit=1)
            if not length_attr:
                length_attr = env['product.attribute'].create({
                    'name': 'Chiều dài',
                    'display_type': 'radio',
                    'create_variant': 'always',
                })
                print("✅ Đã tạo attribute: Chiều dài")
            else:
                print("✅ Đã có attribute: Chiều dài")
            
            # 3. TẠO ATTRIBUTE VALUES
            print("\n📋 Tạo attribute values...")
            
            # Đường kính values
            diameters = ['M12', 'M14', 'M16', 'M18', 'M20', 'M22', 'M24', 'M27', 'M30', 'M32', 'M36']
            diameter_values = []
            for dia in diameters:
                value = env['product.attribute.value'].search([
                    ('name', '=', dia),
                    ('attribute_id', '=', diameter_attr.id)
                ], limit=1)
                if not value:
                    value = env['product.attribute.value'].create({
                        'name': dia,
                        'attribute_id': diameter_attr.id,
                    })
                diameter_values.append(value)
            print(f"✅ Đã tạo {len(diameter_values)} giá trị đường kính")
            
            # Chiều dài values
            lengths = ['100', '150', '200', '250', '300', '350', '400', '450', '500']
            length_values = []
            for len_val in lengths:
                value = env['product.attribute.value'].search([
                    ('name', '=', len_val),
                    ('attribute_id', '=', length_attr.id)
                ], limit=1)
                if not value:
                    value = env['product.attribute.value'].create({
                        'name': len_val,
                        'attribute_id': length_attr.id,
                    })
                length_values.append(value)
            print(f"✅ Đã tạo {len(length_values)} giá trị chiều dài")
            
            cr.commit()
            
            # 4. TẠO SẢN PHẨM B7
            print("\n📦 Tạo sản phẩm: Bulong A193M B7")
            product_b7 = env['product.template'].create({
                'name': 'Bulong A193M B7',
                'default_code': 'HB A193M B7',
                'sale_ok': True,
                'purchase_ok': True,
                'type': 'product',
            })
            
            env['product.template.attribute.line'].create({
                'product_tmpl_id': product_b7.id,
                'attribute_id': diameter_attr.id,
                'value_ids': [(6, 0, [v.id for v in diameter_values])],
            })
            
            env['product.template.attribute.line'].create({
                'product_tmpl_id': product_b7.id,
                'attribute_id': length_attr.id,
                'value_ids': [(6, 0, [v.id for v in length_values])],
            })
            
            cr.commit()
            print(f"✅ Đã tạo sản phẩm B7 với {len(diameters) * len(lengths)} variants")
            
            # 5. TẠO SẢN PHẨM B8
            print("\n📦 Tạo sản phẩm: Bulong A193M B8")
            product_b8 = env['product.template'].create({
                'name': 'Bulong A193M B8',
                'default_code': 'HB A193M B8',
                'sale_ok': True,
                'purchase_ok': True,
                'type': 'product',
            })
            
            env['product.template.attribute.line'].create({
                'product_tmpl_id': product_b8.id,
                'attribute_id': diameter_attr.id,
                'value_ids': [(6, 0, [v.id for v in diameter_values])],
            })
            
            env['product.template.attribute.line'].create({
                'product_tmpl_id': product_b8.id,
                'attribute_id': length_attr.id,
                'value_ids': [(6, 0, [v.id for v in length_values])],
            })
            
            cr.commit()
            print(f"✅ Đã tạo sản phẩm B8 với {len(diameters) * len(lengths)} variants")
            
            total_variants = len(diameters) * len(lengths) * 2
            print(f"\n🎉 HOÀN THÀNH!")
            print(f"   ✅ Đã xóa {count} sản phẩm cũ")
            print(f"   ✅ Đã tạo 2 sản phẩm mới")
            print(f"   ✅ Tổng cộng {total_variants} variants")
            print(f"   - Bulong A193M B7: {len(diameters) * len(lengths)} variants")
            print(f"   - Bulong A193M B8: {len(diameters) * len(lengths)} variants")
            print(f"\n🌐 Truy cập: http://localhost:8069")
            print(f"   Vào Inventory > Products để xem!")
            
            return True
            
    except Exception as e:
        print(f"❌ Lỗi: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == '__main__':
    print("=" * 60)
    print("XÓA TẤT CẢ SẢN PHẨM VÀ TẠO LẠI")
    print("=" * 60)
    print()
    print("⚠️  CẢNH BÁO: Script này sẽ XÓA TẤT CẢ sản phẩm!")
    print()
    
    if len(sys.argv) > 1:
        db_name = sys.argv[1]
    else:
        db_name = input("Nhập tên database (hoặc Enter để tự tìm): ").strip()
    
    delete_all_and_create()
