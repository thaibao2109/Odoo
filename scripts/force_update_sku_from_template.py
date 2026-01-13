#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script để force update SKU cho tất cả variants từ template default_code
"""

import sys
import os

# Thêm đường dẫn Odoo vào sys.path
odoo_path = '/Users/baonguyen/Desktop/app/odoo-source'
sys.path.insert(0, odoo_path)

import odoo
from odoo import api, SUPERUSER_ID

def force_update_sku_from_template(db_name='odoo'):
    """Force update SKU cho tất cả variants từ template default_code"""
    
    # Kết nối database
    odoo.tools.config.parse_config(['-c', '/Users/baonguyen/Desktop/app/Odoo/odoo.conf'])
    registry = odoo.registry(db_name)
    
    with registry.cursor() as cr:
        env = api.Environment(cr, SUPERUSER_ID, {})
        
        ProductTemplate = env['product.template']
        ProductProduct = env['product.product']
        
        # Lấy tất cả templates có default_code
        templates = ProductTemplate.search([('default_code', '!=', False)])
        
        print(f"Tìm thấy {len(templates)} product templates có default_code")
        
        total_updated = 0
        
        for template in templates:
            template_code = template.default_code
            variants = template.product_variant_ids
            
            if not variants:
                continue
            
            print(f"\n📦 Template: {template.name} (Code: {template_code})")
            print(f"   Có {len(variants)} variants")
            
            updated = 0
            for variant in variants:
                try:
                    # Tính toán SKU
                    sku_parts = []
                    
                    # Thêm template code
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
                    
                    if new_sku and new_sku != variant.default_code:
                        # Update bằng SQL
                        cr.execute(
                            "UPDATE product_product SET default_code = %s WHERE id = %s",
                            (new_sku, variant.id)
                        )
                        # Update auto_sku
                        cr.execute(
                            "UPDATE product_product SET auto_sku = %s WHERE id = %s",
                            (new_sku, variant.id)
                        )
                        updated += 1
                        print(f"   ✅ Variant {variant.id}: {variant.default_code} → {new_sku}")
                        
                except Exception as e:
                    print(f"   ⚠️  Lỗi variant {variant.id}: {str(e)[:50]}")
            
            if updated > 0:
                cr.commit()
                print(f"   ✅ Đã cập nhật {updated}/{len(variants)} variants")
                total_updated += updated
        
        print(f"\n✅ Tổng cộng đã cập nhật {total_updated} variants")

if __name__ == '__main__':
    db_name = sys.argv[1] if len(sys.argv) > 1 else 'odoo'
    force_update_sku_from_template(db_name)
