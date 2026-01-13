# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductAttributeValue(models.Model):
    _inherit = 'product.attribute.value'
    _description = 'Product Attribute Value'
    _order = 'sequence, abbreviation'

    # Override name field để thêm translate
    name = fields.Char(translate=True)
    
    # Custom fields - thêm vào model mặc định của Odoo
    abbreviation = fields.Char(string='Từ viết tắt', 
                               help='Mã viết tắt dùng trong SKU (ví dụ: HHB, A193M, B7)')
    explanation_vi = fields.Text(string='Giải thích (Tiếng Việt)')
    explanation_en = fields.Char(string='Tiếng Anh')
    
    # Custom attribute type - không required để tương thích với Odoo native
    attribute_type_id = fields.Many2one('product.attribute.type', 
                                        string='Loại thuộc tính (Custom)', 
                                        required=False, 
                                        ondelete='cascade',
                                        help='Loại thuộc tính tùy chỉnh cho module này')
    attribute_type_code = fields.Char(related='attribute_type_id.code', store=True, string='Mã loại')
    
    # Thông tin bổ sung
    active = fields.Boolean(string='Active', default=True, help='Uncheck to archive this attribute value')
    color = fields.Integer(string='Color', help='Màu sắc để phân biệt trong giao diện')
    notes = fields.Text(string='Ghi chú')

    _sql_constraints = [
        ('abbreviation_unique_per_type', 'unique(attribute_type_id, abbreviation)', 
         'Từ viết tắt phải là duy nhất trong mỗi loại thuộc tính!'),
    ]
    
    # Override _order để ưu tiên abbreviation nếu có
    _order = 'sequence, abbreviation, name'

    @api.model
    def create(self, vals):
        # Tự động tạo màu nếu chưa có
        if 'color' not in vals or not vals.get('color'):
            vals['color'] = self._generate_color()
        
        # Tự động tạo attribute_id từ attribute_type_id nếu chưa có
        if 'attribute_id' not in vals or not vals.get('attribute_id'):
            # Lấy attribute_type_id từ vals hoặc từ record hiện tại (nếu đang write)
            attr_type_id = vals.get('attribute_type_id')
            if not attr_type_id and hasattr(self, '_origin') and self._origin:
                attr_type_id = self._origin.attribute_type_id.id
            
            if attr_type_id:
                attr_type = self.env['product.attribute.type'].browse(attr_type_id)
                if attr_type.exists():
                    # Tìm attribute có tên giống với attribute_type
                    attribute = self.env['product.attribute'].search([
                        ('name', '=', attr_type.name)
                    ], limit=1)
                    
                    if not attribute:
                        # Tạo attribute mới
                        attribute = self.env['product.attribute'].create({
                            'name': attr_type.name,
                            'display_type': 'radio',
                            'create_variant': 'always',
                        })
                    
                    vals['attribute_id'] = attribute.id
        
        return super(ProductAttributeValue, self).create(vals)

    def _generate_color(self):
        """Tạo màu ngẫu nhiên cho attribute value"""
        import random
        colors = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        return random.choice(colors)
