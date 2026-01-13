# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError


class ProductAutoCreateWizard(models.TransientModel):
    _name = 'product.auto.create.wizard'
    _description = 'Wizard tự động tạo sản phẩm với attributes'

    def action_create_products(self):
        """Tự động tạo sản phẩm Bulong A193M B7 và B8 với attributes"""
        
        # 1. Tạo hoặc tìm attribute "Đường kính"
        diameter_attr = self.env['product.attribute'].search([
            ('name', '=', 'Đường kính')
        ], limit=1)
        
        if not diameter_attr:
            diameter_attr = self.env['product.attribute'].create({
                'name': 'Đường kính',
                'display_type': 'radio',
                'create_variant': 'always',
            })
        
        # 2. Tạo hoặc tìm attribute "Chiều dài"
        length_attr = self.env['product.attribute'].search([
            ('name', '=', 'Chiều dài')
        ], limit=1)
        
        if not length_attr:
            length_attr = self.env['product.attribute'].create({
                'name': 'Chiều dài',
                'display_type': 'radio',
                'create_variant': 'always',
            })
        
        # 3. Tạo attribute values cho đường kính
        diameters = ['M12', 'M14', 'M16', 'M18', 'M20', 'M22', 'M24', 'M27', 'M30', 'M32', 'M36']
        diameter_values = []
        for dia in diameters:
            value = self.env['product.attribute.value'].search([
                ('name', '=', dia),
                ('attribute_id', '=', diameter_attr.id)
            ], limit=1)
            if not value:
                value = self.env['product.attribute.value'].create({
                    'name': dia,
                    'attribute_id': diameter_attr.id,
                })
            diameter_values.append(value)
        
        # 4. Tạo attribute values cho chiều dài
        lengths = ['100', '150', '200', '250', '300', '350', '400', '450', '500']
        length_values = []
        for len_val in lengths:
            value = self.env['product.attribute.value'].search([
                ('name', '=', len_val),
                ('attribute_id', '=', length_attr.id)
            ], limit=1)
            if not value:
                value = self.env['product.attribute.value'].create({
                    'name': len_val,
                    'attribute_id': length_attr.id,
                })
            length_values.append(value)
        
        # 5. Xóa sản phẩm cũ (nếu có)
        old_products = self.env['product.template'].search([
            ('name', 'ilike', 'Bulong A193')
        ])
        if old_products:
            old_products.unlink()
        
        # 6. Tạo sản phẩm B7
        product_b7 = self.env['product.template'].create({
            'name': 'Bulong A193M B7',
            'default_code': 'HB A193M B7',
            'sale_ok': True,
            'purchase_ok': True,
            'type': 'product',
        })
        
        self.env['product.template.attribute.line'].create({
            'product_tmpl_id': product_b7.id,
            'attribute_id': diameter_attr.id,
            'value_ids': [(6, 0, [v.id for v in diameter_values])],
        })
        
        self.env['product.template.attribute.line'].create({
            'product_tmpl_id': product_b7.id,
            'attribute_id': length_attr.id,
            'value_ids': [(6, 0, [v.id for v in length_values])],
        })
        
        # 7. Tạo sản phẩm B8
        product_b8 = self.env['product.template'].create({
            'name': 'Bulong A193M B8',
            'default_code': 'HB A193M B8',
            'sale_ok': True,
            'purchase_ok': True,
            'type': 'product',
        })
        
        self.env['product.template.attribute.line'].create({
            'product_tmpl_id': product_b8.id,
            'attribute_id': diameter_attr.id,
            'value_ids': [(6, 0, [v.id for v in diameter_values])],
        })
        
        self.env['product.template.attribute.line'].create({
            'product_tmpl_id': product_b8.id,
            'attribute_id': length_attr.id,
            'value_ids': [(6, 0, [v.id for v in length_values])],
        })
        
        # Mở danh sách sản phẩm
        return {
            'type': 'ir.actions.act_window',
            'name': 'Sản phẩm đã tạo',
            'res_model': 'product.template',
            'view_mode': 'tree,form',
            'domain': [('id', 'in', [product_b7.id, product_b8.id])],
            'target': 'current',
        }
