# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class ProductProduct(models.Model):
    _inherit = 'product.product'

    # Computed field cho SKU tự động từ attributes
    auto_sku = fields.Char(
        string='Mã SKU tự động',
        compute='_compute_auto_sku',
        store=True,
        readonly=True,
        help='Mã SKU tự động tạo từ template code và attribute values'
    )
    
    # Template code để dùng trong SKU
    template_code_for_sku = fields.Char(
        related='product_tmpl_id.default_code',
        store=True,
        string='Mã template'
    )

    @api.depends('product_tmpl_id.default_code', 'product_template_attribute_value_ids')
    def _compute_auto_sku(self):
        """Tự động tạo SKU từ template default_code (SKU tổng) + attribute values"""
        for variant in self:
            sku_parts = []
            
            # Bước 1: Thêm SKU tổng từ template (default_code)
            if variant.product_tmpl_id.default_code:
                sku_parts.append(variant.product_tmpl_id.default_code)
            
            # Bước 2: Thêm các attribute values theo thứ tự
            if variant.product_template_attribute_value_ids:
                # Sắp xếp theo attribute sequence để đảm bảo thứ tự nhất quán
                sorted_values = variant.product_template_attribute_value_ids.sorted(
                    lambda v: (v.attribute_id.sequence, v.attribute_id.id)
                )
                for attr_value in sorted_values:
                    # Lấy tên của attribute value (ví dụ: M12, 100)
                    value_name = attr_value.product_attribute_value_id.name
                    if value_name:
                        sku_parts.append(value_name)
            
            # Bước 3: Kết hợp thành SKU
            variant.auto_sku = ' '.join(sku_parts) if sku_parts else ''
            
            # Bước 4: Tự động cập nhật default_code của variant = auto_sku
            # Chỉ cập nhật nếu có SKU tổng (template code) và không đang trong context skip
            if (variant.auto_sku and variant.product_tmpl_id.default_code and 
                not self.env.context.get('skip_auto_sku_update')):
                # Sử dụng SQL để tránh trigger write() loop
                if not variant.default_code or variant.default_code != variant.auto_sku:
                    self.env.cr.execute(
                        "UPDATE product_product SET default_code = %s WHERE id = %s",
                        (variant.auto_sku, variant.id)
                    )
                    # Invalidate cache để UI cập nhật
                    variant.invalidate_recordset(['default_code', 'auto_sku'])

    @api.model
    def create(self, vals):
        """Tự động set default_code từ auto_sku khi tạo variant mới"""
        variant = super(ProductProduct, self).create(vals)
        # Tính toán auto_sku sau khi tạo
        variant._compute_auto_sku()
        # Cập nhật default_code nếu có auto_sku
        if variant.auto_sku and variant.product_tmpl_id.default_code:
            if not variant.default_code or variant.default_code != variant.auto_sku:
                variant.with_context(skip_auto_sku_update=True).write({'default_code': variant.auto_sku})
        return variant

    def write(self, vals):
        """Cập nhật default_code khi auto_sku thay đổi"""
        result = super(ProductProduct, self).write(vals)
        # Chỉ cập nhật nếu không đang skip
        if not self.env.context.get('skip_auto_sku_update'):
            # Tự động cập nhật default_code = auto_sku cho tất cả variants
            for variant in self:
                if variant.auto_sku and variant.product_tmpl_id.default_code:
                    if variant.default_code != variant.auto_sku:
                        variant.with_context(skip_auto_sku_update=True).write({'default_code': variant.auto_sku})
        return result

    @api.constrains('auto_sku')
    def _check_sku_unique(self):
        """Đảm bảo SKU unique - chỉ kiểm tra nếu SKU đầy đủ (có template code)"""
        for variant in self:
            if variant.auto_sku:
                # Chỉ kiểm tra unique nếu SKU có template code (bắt đầu bằng template code)
                template_code = variant.product_tmpl_id.default_code or ''
                if template_code and variant.auto_sku.startswith(template_code):
                    duplicates = self.search([
                        ('auto_sku', '=', variant.auto_sku),
                        ('id', '!=', variant.id)
                    ])
                    if duplicates:
                        raise ValidationError(
                            f'Mã SKU "{variant.auto_sku}" đã tồn tại cho variant: {duplicates[0].display_name}'
                        )
                elif not template_code:
                    # Cảnh báo nếu thiếu template code nhưng không block
                    # Vì có thể đang trong quá trình cấu hình
                    pass
