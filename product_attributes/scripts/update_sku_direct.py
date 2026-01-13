#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script cập nhật SKU trực tiếp vào default_code (không dùng auto_sku field)
"""

import sys
odoo_path = '/Users/baonguyen/Desktop/app/odoo-source'
sys.path.insert(0, odoo_path)

import odoo
from odoo import api, SUPERUSER_ID

def update_sku_direct():
    db_name = sys.argv[1] if len(sys.argv) > 1 else 'odoo'
    
    print(f"🔌 Kết nối database: {db_name}")
    
    try:
        odoo.tools.config.parse_config(['-d', db_name])
        registry = odoo.registry(db_name)
        
        with registry.cursor() as cr:
            env = api.Environment(cr, SUPERUSER_ID, {})
            
            print("✅ Đã kết nối!\n")
            
            # Tìm variants của Bulong A193M B7 và B8
            products = env['product.template'].search([
                ('name', 'in', ['Bulong A193M B7', 'Bulong A193M B8'])
            ])
            
            if not products:
                print("⚠️  Không tìm thấy sản phẩm Bulong A193M B7/B8")
                return False
            
            total_updated = 0
            
            for product in products:
                print(f"\n📦 Cập nhật SKU cho: {product.name}")
                
                # Đặt template code nếu chưa có
                if not product.default_code:
                    if 'B7' in product.name:
                        product.default_code = 'HB A193M B7'
                    elif 'B8' in product.name:
                        product.default_code = 'HB A193M B8'
                    print(f"   ✅ Đã set Template Code: {product.default_code}")
                
                print(f"   Template Code: {product.default_code}")
                
                variants = product.product_variant_ids
                print(f"   Số variants: {len(variants)}")
                
                updated = 0
                for variant in variants:
                    try:
                        # Tính toán SKU
                        sku_parts = []
                        
                        # Đảm bảo template code có giá trị
                        template_code = product.default_code or ''
                        if template_code:
                            sku_parts.append(template_code)
                        
                        # Thêm attribute values
                        if variant.product_template_attribute_value_ids:
                            sorted_values = variant.product_template_attribute_value_ids.sorted(
                                lambda v: (v.attribute_id.sequence, v.attribute_id.id)
                            )
                            for attr_value in sorted_values:
                                value_name = attr_value.product_attribute_value_id.name
                                if value_name:
                                    sku_parts.append(value_name)
                        
                        # Tạo SKU
                        new_sku = ' '.join(sku_parts) if sku_parts else ''
                        
                        if new_sku:
                            # Force update default_code
                            cr.execute(
                                "UPDATE product_product SET default_code = %s WHERE id = %s",
                                (new_sku, variant.id)
                            )
                            updated += 1
                            
                    except Exception as e:
                        print(f"   ⚠️  Lỗi variant {variant.id}: {str(e)[:50]}")
                
                cr.commit()
                print(f"   ✅ Đã cập nhật {updated}/{len(variants)} variants")
                total_updated += updated
                
                # Hiển thị ví dụ
                if updated > 0:
                    print(f"\n   📋 Ví dụ SKU:")
                    for v in variants[:3]:
                        attrs = ', '.join([av.product_attribute_value_id.name for av in v.product_template_attribute_value_ids[:2]])
                        print(f"      - {attrs}: {v.default_code}")
            
            print(f"\n🎉 HOÀN THÀNH!")
            print(f"   ✅ Đã cập nhật SKU cho {total_updated} variants")
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
    print("CẬP NHẬT SKU TRỰC TIẾP VÀO DEFAULT_CODE")
    print("=" * 60)
    print()
    
    db_name = sys.argv[1] if len(sys.argv) > 1 else 'odoo'
    update_sku_direct()
