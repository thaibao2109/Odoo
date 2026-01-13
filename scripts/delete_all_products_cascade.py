#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script để xóa toàn bộ sản phẩm trong Odoo sử dụng CASCADE DELETE
"""

import sys
import os

# Thêm đường dẫn Odoo vào sys.path
odoo_path = '/Users/baonguyen/Desktop/app/odoo-source'
sys.path.insert(0, odoo_path)

import odoo
from odoo import api, SUPERUSER_ID

def delete_all_products_cascade(db_name='odoo'):
    """Xóa toàn bộ sản phẩm sử dụng CASCADE DELETE"""
    
    # Kết nối database
    odoo.tools.config.parse_config(['-c', '/Users/baonguyen/Desktop/app/Odoo/odoo.conf'])
    registry = odoo.registry(db_name)
    
    with registry.cursor() as cr:
        env = api.Environment(cr, SUPERUSER_ID, {})
        
        # Đếm số lượng sản phẩm trước khi xóa
        ProductTemplate = env['product.template']
        ProductProduct = env['product.product']
        
        template_count = ProductTemplate.search_count([])
        product_count = ProductProduct.search_count([])
        
        print(f"Tìm thấy {template_count} product templates và {product_count} product variants")
        
        if template_count == 0:
            print("Không có sản phẩm nào để xóa!")
            return
        
        auto_confirm = '--yes' in sys.argv or '-y' in sys.argv
        if not auto_confirm:
            confirm = input(f"Bạn có chắc chắn muốn xóa {template_count} templates và {product_count} variants? (yes/no): ")
            if confirm.lower() != 'yes':
                print("Đã hủy!")
                return
        else:
            print(f"Tự động xác nhận: Xóa {template_count} templates và {product_count} variants...")
        
        # Tắt foreign key constraints tạm thời
        print("Đang tắt foreign key constraints tạm thời...")
        cr.execute("SET session_replication_role = 'replica';")
        
        # Xóa tất cả products
        print("Đang xóa product variants...")
        cr.execute("DELETE FROM product_product;")
        variant_deleted = cr.rowcount
        print(f"Đã xóa {variant_deleted} product variants")
        
        print("Đang xóa product templates...")
        cr.execute("DELETE FROM product_template;")
        template_deleted = cr.rowcount
        print(f"Đã xóa {template_deleted} product templates")
        
        # Bật lại foreign key constraints
        print("Đang bật lại foreign key constraints...")
        cr.execute("SET session_replication_role = 'origin';")
        
        # Commit transaction
        cr.commit()
        print("✅ Đã xóa toàn bộ sản phẩm thành công!")
        
        # Đếm lại để xác nhận
        remaining_templates = ProductTemplate.search_count([])
        remaining_products = ProductProduct.search_count([])
        print(f"Số sản phẩm còn lại: {remaining_templates} templates, {remaining_products} variants")

if __name__ == '__main__':
    db_name = sys.argv[1] if len(sys.argv) > 1 and sys.argv[1] not in ['--yes', '-y'] else 'odoo'
    delete_all_products_cascade(db_name)
