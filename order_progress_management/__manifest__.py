# -*- coding: utf-8 -*-
{
    'name': 'Order Progress Management',
    'version': '1.0',
    'category': 'Sales',
    'summary': 'Quản lý tiến độ chi tiết đơn hàng cho sản xuất, mua hàng và tồn kho',
    'description': """
        Module quản lý tiến độ chi tiết đơn hàng
        ========================================
        
        * Theo dõi tiến độ đơn hàng theo 3 hạng mục: Sản xuất, Mua hàng, Tồn kho
        * Quản lý trạng thái chi tiết cho từng sản phẩm
        * Giao diện theo dõi trực quan với status bar
        * Activity feed để theo dõi lịch sử thay đổi
    """,
    'author': 'Odoo',
    'depends': ['sale', 'stock', 'mrp', 'purchase'],
    'data': [
        'security/ir.model.access.csv',
        'views/sale_order_views.xml',
        'views/order_progress_menus.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'order_progress_management/static/src/css/order_progress.css',
            'order_progress_management/static/src/js/order_progress.js',
        ],
    },
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
