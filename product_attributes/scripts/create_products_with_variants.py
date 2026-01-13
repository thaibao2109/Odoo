#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script tạo sản phẩm với attributes và variants như trong ảnh
Sử dụng Odoo's native product.attribute system
"""

import xmlrpc.client
import sys

# Cấu hình
ODOO_URL = 'http://localhost:8069'
ODOO_DB = 'odoo_db'  # Thay đổi theo database
ODOO_USERNAME = 'admin'
ODOO_PASSWORD = 'admin'

def create_products_with_variants():
    """Tạo sản phẩm với attributes và variants"""
    
    try:
        # Kết nối
        common = xmlrpc.client.ServerProxy(f'{ODOO_URL}/xmlrpc/2/common')
        uid = common.authenticate(ODOO_DB, ODOO_USERNAME, ODOO_PASSWORD, {})
        
        if not uid:
            print("❌ Lỗi xác thực!")
            return False
        
        models = xmlrpc.client.ServerProxy(f'{ODOO_URL}/xmlrpc/2/object')
        
        print("📦 Đang tạo attributes và sản phẩm...")
        
        # 1. Tạo hoặc tìm attribute "Đường kính"
        diameter_attr_id = models.execute_kw(
            ODOO_DB, uid, ODOO_PASSWORD,
            'product.attribute', 'search',
            [[('name', '=', 'Đường kính')]]
        )
        
        if not diameter_attr_id:
            diameter_attr_id = models.execute_kw(
                ODOO_DB, uid, ODOO_PASSWORD,
                'product.attribute', 'create',
                [{
                    'name': 'Đường kính',
                    'display_type': 'radio',
                    'create_variant': 'always',
                }]
            )
            print("✅ Đã tạo attribute: Đường kính")
        else:
            diameter_attr_id = diameter_attr_id[0]
            print("✅ Đã tìm thấy attribute: Đường kính")
        
        # 2. Tạo hoặc tìm attribute "Chiều dài"
        length_attr_id = models.execute_kw(
            ODOO_DB, uid, ODOO_PASSWORD,
            'product.attribute', 'search',
            [[('name', '=', 'Chiều dài')]]
        )
        
        if not length_attr_id:
            length_attr_id = models.execute_kw(
                ODOO_DB, uid, ODOO_PASSWORD,
                'product.attribute', 'create',
                [{
                    'name': 'Chiều dài',
                    'display_type': 'radio',
                    'create_variant': 'always',
                }]
            )
            print("✅ Đã tạo attribute: Chiều dài")
        else:
            length_attr_id = length_attr_id[0]
            print("✅ Đã tìm thấy attribute: Chiều dài")
        
        # 3. Tạo attribute values cho đường kính
        diameters = ['M12', 'M14', 'M16', 'M18', 'M20', 'M22', 'M24', 'M27', 'M30', 'M32', 'M36']
        diameter_value_ids = []
        
        for dia in diameters:
            existing = models.execute_kw(
                ODOO_DB, uid, ODOO_PASSWORD,
                'product.attribute.value', 'search',
                [[('name', '=', dia), ('attribute_id', '=', diameter_attr_id)]]
            )
            if existing:
                diameter_value_ids.append(existing[0])
            else:
                value_id = models.execute_kw(
                    ODOO_DB, uid, ODOO_PASSWORD,
                    'product.attribute.value', 'create',
                    [{
                        'name': dia,
                        'attribute_id': diameter_attr_id,
                    }]
                )
                diameter_value_ids.append(value_id)
        
        print(f"✅ Đã tạo {len(diameter_value_ids)} giá trị đường kính")
        
        # 4. Tạo attribute values cho chiều dài
        lengths = ['100', '150', '200', '250', '300', '350', '400', '450', '500']
        length_value_ids = []
        
        for len_val in lengths:
            existing = models.execute_kw(
                ODOO_DB, uid, ODOO_PASSWORD,
                'product.attribute.value', 'search',
                [[('name', '=', len_val), ('attribute_id', '=', length_attr_id)]]
            )
            if existing:
                length_value_ids.append(existing[0])
            else:
                value_id = models.execute_kw(
                    ODOO_DB, uid, ODOO_PASSWORD,
                    'product.attribute.value', 'create',
                    [{
                        'name': len_val,
                        'attribute_id': length_attr_id,
                    }]
                )
                length_value_ids.append(value_id)
        
        print(f"✅ Đã tạo {len(length_value_ids)} giá trị chiều dài")
        
        # 5. Xóa sản phẩm cũ (nếu có)
        print("\n⚠️  Xóa sản phẩm cũ...")
        old_products = models.execute_kw(
            ODOO_DB, uid, ODOO_PASSWORD,
            'product.template', 'search',
            [[('name', 'ilike', 'Bulong A193')]]
        )
        if old_products:
            models.execute_kw(
                ODOO_DB, uid, ODOO_PASSWORD,
                'product.template', 'unlink',
                [old_products]
            )
            print(f"✅ Đã xóa {len(old_products)} sản phẩm cũ")
        
        # 6. Tạo sản phẩm B7
        print("\n📦 Tạo sản phẩm: Bulong A193M B7")
        product_b7_id = models.execute_kw(
            ODOO_DB, uid, ODOO_PASSWORD,
            'product.template', 'create',
            [{
                'name': 'Bulong A193M B7',
                'default_code': 'HB A193M B7',
                'sale_ok': True,
                'purchase_ok': True,
                'type': 'product',
            }]
        )
        
        # Gán attributes
        models.execute_kw(
            ODOO_DB, uid, ODOO_PASSWORD,
            'product.template.attribute.line', 'create',
            [{
                'product_tmpl_id': product_b7_id,
                'attribute_id': diameter_attr_id,
                'value_ids': [(6, 0, diameter_value_ids)],
            }]
        )
        
        models.execute_kw(
            ODOO_DB, uid, ODOO_PASSWORD,
            'product.template.attribute.line', 'create',
            [{
                'product_tmpl_id': product_b7_id,
                'attribute_id': length_attr_id,
                'value_ids': [(6, 0, length_value_ids)],
            }]
        )
        
        print(f"✅ Đã tạo sản phẩm B7 với {len(diameters) * len(lengths)} variants")
        
        # 7. Tạo sản phẩm B8
        print("\n📦 Tạo sản phẩm: Bulong A193M B8")
        product_b8_id = models.execute_kw(
            ODOO_DB, uid, ODOO_PASSWORD,
            'product.template', 'create',
            [{
                'name': 'Bulong A193M B8',
                'default_code': 'HB A193M B8',
                'sale_ok': True,
                'purchase_ok': True,
                'type': 'product',
            }]
        )
        
        # Gán attributes
        models.execute_kw(
            ODOO_DB, uid, ODOO_PASSWORD,
            'product.template.attribute.line', 'create',
            [{
                'product_tmpl_id': product_b8_id,
                'attribute_id': diameter_attr_id,
                'value_ids': [(6, 0, diameter_value_ids)],
            }]
        )
        
        models.execute_kw(
            ODOO_DB, uid, ODOO_PASSWORD,
            'product.template.attribute.line', 'create',
            [{
                'product_tmpl_id': product_b8_id,
                'attribute_id': length_attr_id,
                'value_ids': [(6, 0, length_value_ids)],
            }]
        )
        
        print(f"✅ Đã tạo sản phẩm B8 với {len(diameters) * len(lengths)} variants")
        
        total_variants = len(diameters) * len(lengths) * 2
        print(f"\n🎉 Hoàn thành! Đã tạo 2 sản phẩm với tổng {total_variants} variants")
        print(f"   - Bulong A193M B7: {len(diameters) * len(lengths)} variants")
        print(f"   - Bulong A193M B8: {len(diameters) * len(lengths)} variants")
        
        return True
        
    except Exception as e:
        print(f"❌ Lỗi: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == '__main__':
    print("=" * 60)
    print("Tạo sản phẩm với Attributes & Variants")
    print("=" * 60)
    print(f"Database: {ODOO_DB}")
    print(f"URL: {ODOO_URL}")
    print()
    
    create_products_with_variants()
