# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    # Các thuộc tính sản phẩm
    product_type_attr = fields.Many2one('product.attribute.value',
                                       string='Loại sản phẩm',
                                       domain="[('attribute_type_id.attribute_type', '=', 'product_type')]")
    
    standard_attr = fields.Many2one('product.attribute.value',
                                    string='Tiêu chuẩn',
                                    domain="[('attribute_type_id.attribute_type', '=', 'standard')]")
    
    grade_attr = fields.Many2one('product.attribute.value',
                                string='Cấp bền',
                                domain="[('attribute_type_id.attribute_type', '=', 'grade')]")
    
    diameter_attr = fields.Many2one('product.attribute.value',
                                   string='Đường kính',
                                   domain="[('attribute_type_id.attribute_type', '=', 'size'), ('abbreviation', 'like', 'M%')]")
    
    length_attr = fields.Many2one('product.attribute.value',
                                 string='Chiều dài',
                                 domain="[('attribute_type_id.attribute_type', '=', 'size'), ('abbreviation', 'like', 'L%')]")
    
    size_attr = fields.Many2one('product.attribute.value',
                               string='Kích thước (cũ)',
                               domain="[('attribute_type_id.attribute_type', '=', 'size')]")
    
    surface_attr = fields.Many2one('product.attribute.value',
                                  string='Bề mặt',
                                  domain="[('attribute_type_id.attribute_type', '=', 'surface')]")
    
    special_attr = fields.Many2one('product.attribute.value',
                                  string='Đặc biệt',
                                  domain="[('attribute_type_id.attribute_type', '=', 'special')]")
    
    # Tự động generate SKU
    auto_generate_sku = fields.Boolean(string='Tự động tạo mã SKU', default=True)
    custom_sku = fields.Char(string='Mã SKU tùy chỉnh', 
                            help='Nếu để trống, sẽ tự động tạo từ các thuộc tính')
    
    # Computed field cho SKU
    generated_sku = fields.Char(string='Mã SKU được tạo', 
                               compute='_compute_sku', 
                               store=True,
                               readonly=True)
    
    # Hiển thị công thức SKU
    sku_formula_display = fields.Text(string='Công thức SKU', 
                                      compute='_compute_sku_formula',
                                      readonly=True)

    @api.depends('product_type_attr', 'standard_attr', 'grade_attr', 
                 'diameter_attr', 'length_attr', 'size_attr', 'surface_attr', 'special_attr', 
                 'auto_generate_sku', 'custom_sku')
    def _compute_sku(self):
        for record in self:
            if record.custom_sku:
                record.generated_sku = record.custom_sku
            elif record.auto_generate_sku:
                sku_parts = []
                
                if record.product_type_attr:
                    sku_parts.append(record.product_type_attr.abbreviation)
                if record.standard_attr:
                    sku_parts.append(record.standard_attr.abbreviation)
                if record.grade_attr:
                    sku_parts.append(record.grade_attr.abbreviation)
                # Ưu tiên diameter và length, nếu không có thì dùng size_attr
                if record.diameter_attr:
                    sku_parts.append(record.diameter_attr.abbreviation)
                if record.length_attr:
                    sku_parts.append(record.length_attr.abbreviation)
                elif record.size_attr:
                    sku_parts.append(record.size_attr.abbreviation)
                if record.surface_attr:
                    sku_parts.append(record.surface_attr.abbreviation)
                if record.special_attr:
                    sku_parts.append(record.special_attr.abbreviation)
                
                record.generated_sku = ' '.join(sku_parts) if sku_parts else ''
            else:
                record.generated_sku = ''

    @api.depends('product_type_attr', 'standard_attr', 'grade_attr', 
                 'diameter_attr', 'length_attr', 'size_attr', 'surface_attr', 'special_attr')
    def _compute_sku_formula(self):
        for record in self:
            formula_parts = []
            if record.product_type_attr:
                formula_parts.append(f"Loại: {record.product_type_attr.abbreviation}")
            if record.standard_attr:
                formula_parts.append(f"Tiêu chuẩn: {record.standard_attr.abbreviation}")
            if record.grade_attr:
                formula_parts.append(f"Cấp bền: {record.grade_attr.abbreviation}")
            if record.diameter_attr:
                formula_parts.append(f"Đường kính: {record.diameter_attr.abbreviation}")
            if record.length_attr:
                formula_parts.append(f"Chiều dài: {record.length_attr.abbreviation}")
            elif record.size_attr:
                formula_parts.append(f"Kích thước: {record.size_attr.abbreviation}")
            if record.surface_attr:
                formula_parts.append(f"Bề mặt: {record.surface_attr.abbreviation}")
            if record.special_attr:
                formula_parts.append(f"Đặc biệt: {record.special_attr.abbreviation}")
            
            record.sku_formula_display = ' + '.join(formula_parts) if formula_parts else 'Chưa chọn thuộc tính'

    def write(self, vals):
        result = super(ProductTemplate, self).write(vals)
        # Khi thay đổi default_code (SKU tổng) trên template, tự động cập nhật SKU cho tất cả variants
        # Đảm bảo default_code được lưu đúng cách và hiển thị lại
        if 'default_code' in vals:
            for record in self:
                # Đảm bảo giá trị được lưu vào database bằng SQL (force update)
                new_code = vals.get('default_code', '') or ''
                if new_code:
                    # Force update bằng SQL để đảm bảo lưu được
                    self.env.cr.execute(
                        "UPDATE product_template SET default_code = %s WHERE id = %s",
                        (new_code, record.id)
                    )
                    # Refresh record để đảm bảo giá trị được load lại
                    record.refresh()
                    # Invalidate cache để UI hiển thị lại giá trị
                    record.invalidate_recordset(['default_code'])
                
                # Force recompute auto_sku cho tất cả variants
                record.product_variant_ids._compute_auto_sku()
                # Cập nhật default_code của variants bằng SQL để tránh loop
                for variant in record.product_variant_ids:
                    if variant.auto_sku and variant.product_tmpl_id.default_code:
                        if not variant.default_code or variant.default_code != variant.auto_sku:
                            self.env.cr.execute(
                                "UPDATE product_product SET default_code = %s WHERE id = %s",
                                (variant.auto_sku, variant.id)
                            )
                            # Invalidate cache
                            variant.invalidate_recordset(['default_code', 'auto_sku'])
        return result

    @api.constrains('generated_sku')
    def _check_sku_unique(self):
        for record in self:
            if record.generated_sku:
                duplicates = self.search([
                    ('generated_sku', '=', record.generated_sku),
                    ('id', '!=', record.id)
                ])
                if duplicates:
                    raise ValidationError(
                        f'Mã SKU "{record.generated_sku}" đã tồn tại cho sản phẩm: {duplicates[0].name}'
                    )

    def action_generate_sku(self):
        """Action để tạo lại SKU"""
        for record in self:
            record._compute_sku()
            if record.generated_sku:
                record.default_code = record.generated_sku
        return True
