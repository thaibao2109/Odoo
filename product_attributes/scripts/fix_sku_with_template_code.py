#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script để cập nhật lại SKU cho tất cả variants, đảm bảo có template code
Sử dụng: python3 fix_sku_with_template_code.py [database_name]
"""

import sys
import os

# Thêm path để import odoo
sys.path.insert(0, '/Users/baonguyen/Desktop/app/odoo-source')

import odoo
from odoo import api, SUPERUSER_ID

def fix_sku_with_template_code(db_name='odoo'):
    """Cập nhật lại SKU cho tất cả variants, đảm bảo có template code"""
    
    # Kết nối Odoo
    odoo.tools.config.parse_config(['-c', '/Users/baonguyen/Desktop/app/Odoo/odoo.conf'])
    registry = odoo.registry(db_name)
    
    with registry.cursor() as cr:
        env = api.Environment(cr, SUPERUSER_ID, {})
        
        # Tìm tất cả product templates có default_code
        templates = env['product.template'].search([
            ('default_code', '!=', False),
            ('default_code', '!=', '')
        ])
        
        print(f"📦 Tìm thấy {len(templates)} product templates có template code\n")
        
        updated_count = 0
        skipped_count = 0
        
        for template in templates:
            template_code = template.default_code
            variants = template.product_variant_ids
            
            print(f"🔧 Template: {template.name} (Code: {template_code})")
            print(f"   Variants: {len(variants)}")
            
            for variant in variants:
                # Tính toán SKU mới với template code
                sku_parts = []
                
                # Thêm template code
                if template_code:
                    sku_parts.append(template_code)
                
                # Thêm các attribute values
                if variant.product_template_attribute_value_ids:
                    sorted_values = variant.product_template_attribute_value_ids.sorted(
                        lambda v: (v.attribute_id.sequence, v.attribute_id.id)
                    )
                    for attr_value in sorted_values:
                        value_name = attr_value.product_attribute_value_id.name
                        if value_name:
                            sku_parts.append(value_name)
                
                new_sku = ' '.join(sku_parts) if sku_parts else ''
                
                # Chỉ cập nhật nếu SKU mới khác với SKU hiện tại
                if new_sku and new_sku != variant.default_code:
                    try:
                        # Cập nhật bằng SQL để tránh trigger constraint
                        cr.execute(
                            "UPDATE product_product SET default_code = %s WHERE id = %s",
                            (new_sku, variant.id)
                        )
                        # Cập nhật auto_sku
                        cr.execute(
                            "UPDATE product_product SET auto_sku = %s WHERE id = %s",
                            (new_sku, variant.id)
                        )
                        updated_count += 1
                        print(f"   ✅ Variant {variant.id}: '{variant.default_code}' → '{new_sku}'")
                    except Exception as e:
                        print(f"   ⚠️  Lỗi variant {variant.id}: {str(e)[:50]}")
                        skipped_count += 1
                else:
                    skipped_count += 1
            
            cr.commit()
            print()
        
        print(f"\n✅ Hoàn thành!")
        print(f"   📊 Đã cập nhật: {updated_count} variants")
        print(f"   ⏭️  Đã bỏ qua: {skipped_count} variants")

if __name__ == '__main__':
    db_name = sys.argv[1] if len(sys.argv) > 1 else 'odoo'
    print(f"🚀 Bắt đầu cập nhật SKU cho database: {db_name}\n")
    fix_sku_with_template_code(db_name)
