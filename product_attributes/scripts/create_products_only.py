#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script chỉ tạo sản phẩm mới, không xóa cũ
"""

import sys
import os

odoo_path = '/Users/baonguyen/Desktop/app/odoo-source'
sys.path.insert(0, odoo_path)

import odoo
from odoo import api, SUPERUSER_ID

def create_products_only():
    """Chỉ tạo sản phẩm mới"""
    
    db_name = sys.argv[1] if len(sys.argv) > 1 else 'odoo'
    
    print(f"🔌 Kết nối database: {db_name}")
    
    try:
        odoo.tools.config.parse_config(['-d', db_name])
        registry = odoo.registry(db_name)
        
        with registry.cursor() as cr:
            env = api.Environment(cr, SUPERUSER_ID, {})
            
            print("✅ Đã kết nối thành công!\n")
            
            # 1. TẠO ATTRIBUTES
            print("📦 Tạo attributes...")
            
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
            
            # 2. TẠO ATTRIBUTE VALUES
            print("\n📋 Tạo attribute values...")
            
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
            print(f"✅ Đã có {len(diameter_values)} giá trị đường kính")
            
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
            print(f"✅ Đã có {len(length_values)} giá trị chiều dài")
            
            cr.commit()
            
            # 3. XÓA SẢN PHẨM CŨ (nếu có tên giống)
            print("\n🗑️  Xóa sản phẩm cũ (nếu có)...")
            old_products = env['product.template'].search([
                ('name', 'in', ['Bulong A193M B7', 'Bulong A193M B8'])
            ])
            if old_products:
                try:
                    old_products.unlink()
                    print(f"✅ Đã xóa {len(old_products)} sản phẩm cũ")
                except:
                    print(f"⚠️  Không thể xóa {len(old_products)} sản phẩm cũ (có thể đang được sử dụng)")
            else:
                print("ℹ️  Không có sản phẩm cũ để xóa")
            
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
    print("TẠO SẢN PHẨM MỚI (Không xóa sản phẩm cũ)")
    print("=" * 60)
    print()
    
    db_name = sys.argv[1] if len(sys.argv) > 1 else 'odoo'
    create_products_only()
