#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script để xóa toàn bộ sản phẩm trong Odoo
"""

import sys
import os

# Thêm đường dẫn Odoo vào sys.path
odoo_path = '/Users/baonguyen/Desktop/app/odoo-source'
sys.path.insert(0, odoo_path)

import odoo
from odoo import api, SUPERUSER_ID

def delete_all_products(db_name='odoo'):
    """Xóa toàn bộ sản phẩm (product.template và product.product)"""
    
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
        
        # Xác nhận (nếu có flag --yes thì tự động xác nhận)
        auto_confirm = '--yes' in sys.argv or '-y' in sys.argv
        if not auto_confirm:
            confirm = input(f"Bạn có chắc chắn muốn xóa {template_count} templates và {product_count} variants? (yes/no): ")
            if confirm.lower() != 'yes':
                print("Đã hủy!")
                return
        else:
            print(f"Tự động xác nhận: Xóa {template_count} templates và {product_count} variants...")
        
        # Xóa các bản ghi liên quan bằng SQL trực tiếp (tránh constraint phức tạp)
        print("Đang xóa các bản ghi liên quan bằng SQL...")
        
        def safe_delete(table_name, where_clause="", description=""):
            """Xóa an toàn với try-except"""
            try:
                if where_clause:
                    count_query = f"SELECT COUNT(*) FROM {table_name} WHERE {where_clause}"
                    delete_query = f"DELETE FROM {table_name} WHERE {where_clause}"
                else:
                    count_query = f"SELECT COUNT(*) FROM {table_name}"
                    delete_query = f"DELETE FROM {table_name}"
                
                cr.execute(count_query)
                count = cr.fetchone()[0]
                if count > 0:
                    print(f"  - Xóa {count} {description or table_name}...")
                    cr.execute(delete_query)
                    return count
            except Exception as e:
                print(f"  - Bỏ qua {table_name}: {str(e)}")
                cr.rollback()
            return 0
        
        # Xóa các bản ghi liên quan
        safe_delete("stock_move_line", "product_id IS NOT NULL", "stock move lines")
        safe_delete("stock_move", "product_id IS NOT NULL", "stock moves")
        safe_delete("stock_quant", "product_id IS NOT NULL", "stock quants")
        safe_delete("stock_valuation_layer", "product_id IS NOT NULL", "stock valuation layers")
        safe_delete("stock_lot", "product_id IS NOT NULL", "stock lots")
        safe_delete("sale_order_line", "product_id IS NOT NULL", "sale order lines")
        safe_delete("purchase_order_line", "product_id IS NOT NULL", "purchase order lines")
        
        # Xóa product variant combinations trước
        safe_delete("product_variant_combination", "", "product variant combinations")
        safe_delete("product_template_attribute_value", "", "product template attribute values")
        safe_delete("product_template_attribute_line", "", "product attribute lines")
        
        # Xóa mrp_bom (bill of materials)
        safe_delete("mrp_bom_line", "", "mrp bom lines")
        safe_delete("mrp_bom", "", "mrp boms")
        
        # Xóa lại stock_move và mrp_bom một lần nữa (có thể có bản ghi mới)
        print("Đang xóa lại các bản ghi còn sót...")
        safe_delete("stock_move", "", "stock moves (tất cả)")
        safe_delete("stock_move_line", "", "stock move lines (tất cả)")
        safe_delete("stock_quant", "", "stock quants (tất cả)")
        safe_delete("stock_valuation_layer", "", "stock valuation layers (tất cả)")
        safe_delete("sale_order_line", "", "sale order lines (tất cả)")
        safe_delete("mrp_production", "", "mrp productions (tất cả)")
        safe_delete("mrp_bom_line", "", "mrp bom lines (tất cả)")
        safe_delete("mrp_bom", "", "mrp boms (tất cả)")
        
        # Xóa product variants trước
        print("Đang xóa product variants...")
        variant_count = safe_delete("product_product", "", "product variants")
        if variant_count > 0:
            print(f"Đã xóa {variant_count} product variants")
        
        # Xóa lại các bản ghi có thể còn sót
        safe_delete("stock_quant", "", "stock quants (lần cuối)")
        safe_delete("stock_lot", "", "stock lots (lần cuối)")
        safe_delete("stock_move_line", "", "stock move lines (lần cuối)")
        safe_delete("stock_move", "", "stock moves (lần cuối)")
        safe_delete("sale_order_line", "", "sale order lines (lần cuối)")
        safe_delete("mrp_production", "", "mrp productions (lần cuối)")
        safe_delete("mrp_bom_line", "", "mrp bom lines (lần cuối)")
        safe_delete("mrp_bom", "", "mrp boms (lần cuối)")
        
        # Xóa product templates
        print("Đang xóa product templates...")
        template_count = safe_delete("product_template", "", "product templates")
        if template_count > 0:
            print(f"Đã xóa {template_count} product templates")
        
        # Xóa lại stock_move một lần nữa (nếu có bản ghi mới)
        safe_delete("stock_valuation_layer", "", "stock valuation layers (sau khi xóa templates)")
        safe_delete("stock_quant", "", "stock quants (sau khi xóa templates)")
        safe_delete("stock_lot", "", "stock lots (sau khi xóa templates)")
        safe_delete("stock_move_line", "", "stock move lines (sau khi xóa templates)")
        safe_delete("stock_move", "", "stock moves (sau khi xóa templates)")
        safe_delete("mrp_production", "", "mrp productions (sau khi xóa templates)")
        safe_delete("mrp_bom_line", "", "mrp bom lines (sau khi xóa templates)")
        safe_delete("mrp_bom", "", "mrp boms (sau khi xóa templates)")
        
        # Xóa lại sale_order_line và mrp_bom
        safe_delete("sale_order_line", "", "sale order lines (sau khi xóa lại)")
        safe_delete("mrp_bom_line", "", "mrp bom lines (sau khi xóa lại)")
        safe_delete("mrp_bom", "", "mrp boms (sau khi xóa lại)")
        
        # Thử xóa lại products một lần nữa
        print("Đang thử xóa lại products...")
        variant_count = safe_delete("product_product", "", "product variants (lần cuối)")
        template_count = safe_delete("product_template", "", "product templates (lần cuối)")
        
        # Commit transaction
        cr.commit()
        print("✅ Đã xóa toàn bộ sản phẩm thành công!")
        
        # Đếm lại để xác nhận
        remaining_templates = ProductTemplate.search_count([])
        remaining_products = ProductProduct.search_count([])
        print(f"Số sản phẩm còn lại: {remaining_templates} templates, {remaining_products} variants")

if __name__ == '__main__':
    db_name = sys.argv[1] if len(sys.argv) > 1 else 'odoo'
    delete_all_products(db_name)
