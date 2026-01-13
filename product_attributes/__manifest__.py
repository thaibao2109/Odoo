# -*- coding: utf-8 -*-
{
    'name': 'Product Attributes & SKU Generator',
    'version': '1.0',
    'category': 'Sales',
    'summary': 'Quản lý thuộc tính sản phẩm và tự động tạo mã SKU',
    'description': """
        Module quản lý thuộc tính sản phẩm và tự động tạo mã SKU
        =========================================================
        
        * Quản lý các thuộc tính: Loại sản phẩm, Tiêu chuẩn, Cấp bền, Kích thước, Bề mặt, Đặc biệt
        * Tự động tạo mã SKU theo công thức: Loại + Tiêu chuẩn + Cấp bền + Kích thước + Bề mặt + Đặc biệt
        * Quản lý từ điển thuộc tính với mã viết tắt và giải thích
        * Validation và đảm bảo SKU unique
        * Giao diện nhập liệu thân thiện với dropdown
    """,
    'author': 'Odoo',
    'depends': ['product', 'sale'],
    'data': [
        'security/ir.model.access.csv',
        'data/product_attribute_data.xml',
        'data/product_sample_data.xml',  # Phải load trước product_sample_products.xml
        'data/product_sample_products.xml',
        'data/auto_create_action.xml',
        'views/product_attribute_views.xml',
        'views/product_template_views.xml',
        'views/product_product_views.xml',
        'views/product_attribute_menus.xml',
        'views/product_wizard_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
