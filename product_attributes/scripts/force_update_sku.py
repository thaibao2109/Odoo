#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script force update SKU cho tất cả variants hiện có
"""

import sys
odoo_path = '/Users/baonguyen/Desktop/app/odoo-source'
sys.path.insert(0, odoo_path)

import odoo
from odoo import api, SUPERUSER_ID

def force_update_sku():
    db_name = sys.argv[1] if len(sys.argv) > 1 else 'odoo'
    
    print(f"🔌 Kết nối database: {db_name}")
    
    try:
        odoo.tools.config.parse_config(['-d', db_name])
        registry = odoo.registry(db_name)
        
        with registry.cursor() as cr:
            env = api.Environment(cr, SUPERUSER_ID, {})
            
            print("✅ Đã kết nối!\n")
            
            # Tìm tất cả variants có attributes
            all_variants = env['product.product'].search([
                ('product_template_attribute_value_ids', '!=', False)
            ])
            
            print(f"📦 Tìm thấy {len(all_variants)} variants có attributes\n")
            
            if len(all_variants) == 0:
                print("⚠️  Không có variants nào có attributes!")
                return False
            
            # Cập nhật SKU cho từng variant
            updated = 0
            for variant in all_variants:
                try:
                    # Tính toán SKU thủ công
                    sku_parts = []
                    
                    # Thêm template code
                    if variant.product_tmpl_id.default_code:
                        sku_parts.append(variant.product_tmpl_id.default_code)
                    
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
                        # Cập nhật auto_sku và default_code
                        variant.write({
                            'auto_sku': new_sku,
                            'default_code': new_sku
                        })
                        updated += 1
                        
                except Exception as e:
                    print(f"⚠️  Lỗi variant {variant.id}: {str(e)[:50]}")
            
            cr.commit()
            
            print(f"\n✅ Đã cập nhật SKU cho {updated}/{len(all_variants)} variants")
            
            # Hiển thị ví dụ
            print("\n📋 Ví dụ SKU đã được tạo:")
            sample = env['product.product'].search([
                ('auto_sku', '!=', False)
            ], limit=10)
            for v in sample:
                attrs = ', '.join([av.product_attribute_value_id.name for av in v.product_template_attribute_value_ids[:2]])
                print(f"   - {v.name}: {v.auto_sku} (Attributes: {attrs})")
            
            return True
            
    except Exception as e:
        print(f"❌ Lỗi: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == '__main__':
    print("=" * 60)
    print("FORCE UPDATE SKU CHO TẤT CẢ VARIANTS")
    print("=" * 60)
    print()
    
    db_name = sys.argv[1] if len(sys.argv) > 1 else 'odoo'
    force_update_sku()
