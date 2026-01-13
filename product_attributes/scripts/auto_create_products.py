#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script tự động tạo sản phẩm với attributes và variants
Chạy qua Odoo shell
"""

import sys
import os

# Thêm đường dẫn Odoo vào sys.path
odoo_path = '/Users/baonguyen/Desktop/app/odoo-source'
sys.path.insert(0, odoo_path)

# Import Odoo
import odoo
from odoo import api, SUPERUSER_ID

def create_products():
    """Tạo sản phẩm với attributes và variants"""
    
    # Lấy database name từ command line hoặc dùng default
    db_name = sys.argv[1] if len(sys.argv) > 1 else 'odoo_db'
    
    print(f"🔌 Kết nối database: {db_name}")
    
    try:
        # Kết nối Odoo
        odoo.tools.config.parse_config(['-d', db_name])
        registry = odoo.registry(db_name)
        
        with registry.cursor() as cr:
            env = api.Environment(cr, SUPERUSER_ID, {})
            
            print("✅ Đã kết nối thành công!")
            print("\n📦 Bắt đầu tạo attributes và sản phẩm...\n")
            
            # 1. Tạo hoặc tìm attribute "Đường kính"
            diameter_attr = env['product.attribute'].search([
                ('name', '=', 'Đường kính')
            ], limit=1)
            
            if not diameter_attr:
                diameter_attr = env['product.attribute'].create({
                    'name': 'Đường kính',
                    'display_type': 'radio',
                    'create_variant': 'always',
                })
                print("✅ Đã tạo attribute: Đường kính")
            else:
                print("✅ Đã tìm thấy attribute: Đường kính")
            
            # 2. Tạo hoặc tìm attribute "Chiều dài"
            length_attr = env['product.attribute'].search([
                ('name', '=', 'Chiều dài')
            ], limit=1)
            
            if not length_attr:
                length_attr = env['product.attribute'].create({
                    'name': 'Chiều dài',
                    'display_type': 'radio',
                    'create_variant': 'always',
                })
                print("✅ Đã tạo attribute: Chiều dài")
            else:
                print("✅ Đã tìm thấy attribute: Chiều dài")
            
            # 3. Tạo attribute values cho đường kính
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
            
            print(f"✅ Đã tạo {len(diameter_values)} giá trị đường kính: {', '.join(diameters[:3])}...{diameters[-1]}")
            
            # 4. Tạo attribute values cho chiều dài
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
            
            print(f"✅ Đã tạo {len(length_values)} giá trị chiều dài: {', '.join(lengths[:3])}...{lengths[-1]}")
            
            # 5. Xóa sản phẩm cũ (nếu có)
            print("\n🗑️  Xóa sản phẩm cũ...")
            old_products = env['product.template'].search([
                ('name', 'ilike', 'Bulong A193')
            ])
            if old_products:
                count = len(old_products)
                old_products.unlink()
                print(f"✅ Đã xóa {count} sản phẩm cũ")
            else:
                print("ℹ️  Không có sản phẩm cũ để xóa")
            
            # 6. Tạo sản phẩm B7
            print("\n📦 Tạo sản phẩm: Bulong A193M B7")
            product_b7 = env['product.template'].create({
                'name': 'Bulong A193M B7',
                'default_code': 'HB A193M B7',
                'sale_ok': True,
                'purchase_ok': True,
                'type': 'product',
            })
            
            # Gán attributes
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
            
            # 7. Tạo sản phẩm B8
            print("\n📦 Tạo sản phẩm: Bulong A193M B8")
            product_b8 = env['product.template'].create({
                'name': 'Bulong A193M B8',
                'default_code': 'HB A193M B8',
                'sale_ok': True,
                'purchase_ok': True,
                'type': 'product',
            })
            
            # Gán attributes
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
            print(f"\n🎉 Hoàn thành!")
            print(f"   ✅ Đã tạo 2 sản phẩm")
            print(f"   ✅ Tổng cộng {total_variants} variants")
            print(f"   - Bulong A193M B7: {len(diameters) * len(lengths)} variants")
            print(f"   - Bulong A193M B8: {len(diameters) * len(lengths)} variants")
            print(f"\n🌐 Truy cập: http://localhost:8069")
            print(f"   Vào Inventory > Products để xem kết quả!")
            
            return True
            
    except Exception as e:
        print(f"❌ Lỗi: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == '__main__':
    print("=" * 60)
    print("Tự động tạo sản phẩm với Attributes & Variants")
    print("=" * 60)
    print()
    
    # Lấy database name
    if len(sys.argv) > 1:
        db_name = sys.argv[1]
    else:
        print("⚠️  Chưa chỉ định database name!")
        print("   Sử dụng: python3 auto_create_products.py <database_name>")
        print("   Ví dụ: python3 auto_create_products.py odoo_db")
        print()
        db_name = input("Nhập tên database (hoặc Enter để dùng 'odoo_db'): ").strip()
        if not db_name:
            db_name = 'odoo_db'
    
    create_products()
