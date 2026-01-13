#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script cập nhật SKU tự động cho tất cả variants hiện có
"""

import sys
odoo_path = '/Users/baonguyen/Desktop/app/odoo-source'
sys.path.insert(0, odoo_path)

import odoo
from odoo import api, SUPERUSER_ID

def update_variants_sku():
    db_name = sys.argv[1] if len(sys.argv) > 1 else 'odoo'
    
    print(f"🔌 Kết nối database: {db_name}")
    
    try:
        odoo.tools.config.parse_config(['-d', db_name])
        registry = odoo.registry(db_name)
        
        with registry.cursor() as cr:
            env = api.Environment(cr, SUPERUSER_ID, {})
            
            print("✅ Đã kết nối!\n")
            
            # Tìm tất cả variants
            all_variants = env['product.product'].search([])
            print(f"📦 Tìm thấy {len(all_variants)} variants")
            
            # Cập nhật SKU cho từng variant
            updated = 0
            for variant in all_variants:
                try:
                    # Tính toán lại auto_sku
                    variant._compute_auto_sku()
                    if variant.auto_sku:
                        variant.default_code = variant.auto_sku
                        updated += 1
                except Exception as e:
                    print(f"⚠️  Lỗi khi cập nhật variant {variant.id}: {e}")
            
            cr.commit()
            
            print(f"\n✅ Đã cập nhật SKU cho {updated}/{len(all_variants)} variants")
            
            # Hiển thị một số ví dụ
            print("\n📋 Ví dụ SKU đã được tạo:")
            sample_variants = env['product.product'].search([
                ('auto_sku', '!=', False)
            ], limit=5)
            for v in sample_variants:
                print(f"   - {v.name}: {v.auto_sku}")
            
            return True
            
    except Exception as e:
        print(f"❌ Lỗi: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == '__main__':
    print("=" * 60)
    print("CẬP NHẬT SKU TỰ ĐỘNG CHO VARIANTS")
    print("=" * 60)
    print()
    
    db_name = sys.argv[1] if len(sys.argv) > 1 else 'odoo'
    update_variants_sku()
