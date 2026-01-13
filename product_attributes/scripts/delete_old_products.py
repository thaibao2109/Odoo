#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script xóa tất cả sản phẩm cũ (trừ Bulong A193M B7 và B8)
"""

import sys
odoo_path = '/Users/baonguyen/Desktop/app/odoo-source'
sys.path.insert(0, odoo_path)

import odoo
from odoo import api, SUPERUSER_ID

def delete_old_products():
    db_name = sys.argv[1] if len(sys.argv) > 1 else 'odoo'
    
    print(f"🔌 Kết nối database: {db_name}")
    
    try:
        odoo.tools.config.parse_config(['-d', db_name])
        registry = odoo.registry(db_name)
        
        with registry.cursor() as cr:
            env = api.Environment(cr, SUPERUSER_ID, {})
            
            print("✅ Đã kết nối!\n")
            
            # Tìm sản phẩm cần giữ lại
            keep_products = env['product.template'].search([
                ('name', 'in', ['Bulong A193M B7', 'Bulong A193M B8'])
            ])
            keep_ids = keep_products.ids if keep_products else []
            
            print(f"📦 Giữ lại {len(keep_ids)} sản phẩm: Bulong A193M B7, B8")
            
            # Xóa tất cả sản phẩm khác
            all_products = env['product.template'].search([])
            old_products = all_products.filtered(lambda p: p.id not in keep_ids)
            
            if old_products:
                print(f"\n🗑️  Đang xóa {len(old_products)} sản phẩm cũ...")
                deleted = 0
                for product in old_products:
                    try:
                        product.unlink()
                        deleted += 1
                    except Exception as e:
                        print(f"⚠️  Không thể xóa {product.name}: {str(e)[:50]}")
                
                cr.commit()
                print(f"✅ Đã xóa {deleted}/{len(old_products)} sản phẩm")
            else:
                print("\nℹ️  Không có sản phẩm cũ để xóa")
            
            # Kiểm tra kết quả
            remaining = env['product.template'].search([])
            print(f"\n📊 Kết quả:")
            print(f"   - Tổng số sản phẩm còn lại: {len(remaining)}")
            for p in remaining:
                print(f"   - {p.name} (ID: {p.id})")
            
            return True
            
    except Exception as e:
        print(f"❌ Lỗi: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == '__main__':
    print("=" * 60)
    print("XÓA SẢN PHẨM CŨ (Giữ lại Bulong A193M B7/B8)")
    print("=" * 60)
    print()
    
    db_name = sys.argv[1] if len(sys.argv) > 1 else 'odoo'
    delete_old_products()
