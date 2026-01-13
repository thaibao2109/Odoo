# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductTemplateAttributeLine(models.Model):
    _inherit = 'product.template.attribute.line'

    def write(self, vals):
        """Khi thay đổi attributes, tự động cập nhật SKU cho tất cả variants"""
        result = super(ProductTemplateAttributeLine, self).write(vals)
        
        # Cập nhật SKU cho tất cả variants khi attributes thay đổi
        # Odoo sẽ tự động tạo variants khi thêm attributes, không cần tạo product template mới
        if 'value_ids' in vals:
            for line in self:
                # Đợi Odoo tạo variants xong, sau đó cập nhật SKU
                line.product_tmpl_id.product_variant_ids._compute_auto_sku()
                # Cập nhật default_code cho variants bằng SQL
                for variant in line.product_tmpl_id.product_variant_ids:
                    if variant.auto_sku and variant.product_tmpl_id.default_code:
                        if not variant.default_code or variant.default_code != variant.auto_sku:
                            self.env.cr.execute(
                                "UPDATE product_product SET default_code = %s WHERE id = %s",
                                (variant.auto_sku, variant.id)
                            )
                            variant.invalidate_recordset(['default_code', 'auto_sku'])
        
        return result

    @api.model
    def create(self, vals):
        """Khi tạo attribute line mới, tự động cập nhật SKU cho variants"""
        result = super(ProductTemplateAttributeLine, self).create(vals)
        
        # Odoo sẽ tự động tạo variants khi thêm attribute line
        # Chỉ cập nhật SKU cho variants hiện có, không tạo product template mới
        if result.product_tmpl_id:
            # Đợi Odoo tạo variants xong
            result.product_tmpl_id.product_variant_ids._compute_auto_sku()
            # Cập nhật default_code cho variants bằng SQL
            for variant in result.product_tmpl_id.product_variant_ids:
                if variant.auto_sku and variant.product_tmpl_id.default_code:
                    if not variant.default_code or variant.default_code != variant.auto_sku:
                        self.env.cr.execute(
                            "UPDATE product_product SET default_code = %s WHERE id = %s",
                            (variant.auto_sku, variant.id)
                        )
                        variant.invalidate_recordset(['default_code', 'auto_sku'])
        
        return result
