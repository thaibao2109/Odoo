# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductAttributeType(models.Model):
    _name = 'product.attribute.type'
    _description = 'Product Attribute Type'
    _order = 'sequence, name'

    name = fields.Char(string='Tên loại thuộc tính', required=True, translate=True)
    code = fields.Char(string='Mã', required=True, help='Mã viết tắt để dùng trong SKU')
    sequence = fields.Integer(string='Thứ tự', default=10)
    description = fields.Text(string='Mô tả')
    active = fields.Boolean(string='Active', default=True)
    
    # Các loại thuộc tính chuẩn
    attribute_type = fields.Selection([
        ('product_type', 'Loại sản phẩm'),
        ('standard', 'Tiêu chuẩn'),
        ('grade', 'Cấp bền'),
        ('size', 'Kích thước'),
        ('surface', 'Bề mặt'),
        ('special', 'Đặc biệt'),
    ], string='Loại thuộc tính', required=True)
    
    value_ids = fields.One2many('product.attribute.value', 'attribute_type_id', string='Giá trị thuộc tính')
    value_count = fields.Integer(string='Số lượng giá trị', compute='_compute_value_count', store=False)

    @api.depends('value_ids')
    def _compute_value_count(self):
        for record in self:
            record.value_count = len(record.value_ids)

    _sql_constraints = [
        ('code_unique', 'unique(code)', 'Mã thuộc tính phải là duy nhất!'),
    ]
