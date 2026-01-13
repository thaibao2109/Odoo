#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script để xóa tất cả sản phẩm trong Odoo
Chạy qua Odoo shell
"""

import xmlrpc.client
import sys

# Cấu hình
ODOO_URL = 'http://localhost:8069'
ODOO_DB = 'odoo_db'  # Thay đổi theo database của bạn
ODOO_USERNAME = 'admin'  # Thay đổi theo username của bạn
ODOO_PASSWORD = 'admin'  # Thay đổi theo password của bạn

def delete_all_products():
    """Xóa tất cả sản phẩm"""
    
    try:
        # Kết nối
        common = xmlrpc.client.ServerProxy(f'{ODOO_URL}/xmlrpc/2/common')
        uid = common.authenticate(ODOO_DB, ODOO_USERNAME, ODOO_PASSWORD, {})
        
        if not uid:
            print("❌ Lỗi xác thực! Kiểm tra username và password.")
            return False
        
        models = xmlrpc.client.ServerProxy(f'{ODOO_URL}/xmlrpc/2/object')
        
        # Tìm tất cả sản phẩm
        product_ids = models.execute_kw(
            ODOO_DB, uid, ODOO_PASSWORD,
            'product.template', 'search',
            [[]]
        )
        
        if not product_ids:
            print("✅ Không có sản phẩm nào để xóa.")
            return True
        
        print(f"📦 Tìm thấy {len(product_ids)} sản phẩm.")
        print("⚠️  Bạn có chắc muốn xóa TẤT CẢ sản phẩm? (yes/no): ", end='')
        
        confirm = input().strip().lower()
        if confirm != 'yes':
            print("❌ Đã hủy.")
            return False
        
        # Xóa sản phẩm
        models.execute_kw(
            ODOO_DB, uid, ODOO_PASSWORD,
            'product.template', 'unlink',
            [product_ids]
        )
        
        print(f"✅ Đã xóa {len(product_ids)} sản phẩm thành công!")
        return True
        
    except Exception as e:
        print(f"❌ Lỗi: {e}")
        return False

if __name__ == '__main__':
    print("=" * 50)
    print("Script xóa tất cả sản phẩm")
    print("=" * 50)
    print(f"Database: {ODOO_DB}")
    print(f"URL: {ODOO_URL}")
    print()
    
    delete_all_products()
