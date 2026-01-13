# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    def action_setup_attributes_variants(self):
        """Thiết lập attributes và tạo variants cho bulong A193 B7/B8"""
        
        # Tìm hoặc tạo attributes
        diameter_attr = self.env['product.attribute'].search([
            ('name', '=', 'Đường kính')
        ], limit=1)
        
        if not diameter_attr:
            diameter_attr = self.env['product.attribute'].create({
                'name': 'Đường kính',
                'display_type': 'radio',
                'create_variant': 'always',
            })
        
        length_attr = self.env['product.attribute'].search([
            ('name', '=', 'Chiều dài')
        ], limit=1)
        
        if not length_attr:
            length_attr = self.env['product.attribute'].create({
                'name': 'Chiều dài',
                'display_type': 'radio',
                'create_variant': 'always',
            })
        
        # Tạo attribute values cho đường kính (M12-M36)
        diameters = ['M12', 'M14', 'M16', 'M18', 'M20', 'M22', 'M24', 'M27', 'M30', 'M32', 'M36']
        diameter_values = []
        for dia in diameters:
            value = self.env['product.attribute.value'].search([
                ('attribute_id', '=', diameter_attr.id),
                ('name', '=', dia)
            ], limit=1)
            if not value:
                value = self.env['product.attribute.value'].create({
                    'name': dia,
                    'attribute_id': diameter_attr.id,
                })
            diameter_values.append(value)
        
        # Tạo attribute values cho chiều dài (100-500)
        lengths = ['100', '150', '200', '250', '300', '350', '400', '450', '500']
        length_values = []
        for len_val in lengths:
            value = self.env['product.attribute.value'].search([
                ('attribute_id', '=', length_attr.id),
                ('name', '=', len_val)
            ], limit=1)
            if not value:
                value = self.env['product.attribute.value'].create({
                    'name': len_val,
                    'attribute_id': length_attr.id,
                })
            length_values.append(value)
        
        # Gán attributes vào product template
        self.attribute_line_ids = [(5, 0, 0)]  # Xóa attributes cũ
        
        # Thêm đường kính
        self.attribute_line_ids = [(0, 0, {
            'product_tmpl_id': self.id,
            'attribute_id': diameter_attr.id,
            'value_ids': [(6, 0, [v.id for v in diameter_values])],
        })]
        
        # Thêm chiều dài
        self.attribute_line_ids = [(0, 0, {
            'product_tmpl_id': self.id,
            'attribute_id': length_attr.id,
            'value_ids': [(6, 0, [v.id for v in length_values])],
        })]
        
        # Reload form để hiển thị tab "Thuộc tính & biến thể"
        return {
            'type': 'ir.actions.client',
            'tag': 'reload',
        }
