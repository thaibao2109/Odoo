# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    # Status field for progress tracking
    progress_status = fields.Selection([
        ('new', 'MỚI'),
        ('in_production', 'ĐANG SX'),
        ('external_purchase', 'MUA NGOÀI'),
        ('not_delivered', 'CHƯA GIAO'),
        ('delivered', 'ĐÃ GIAO'),
        ('completed', 'HOÀN THÀNH'),
        ('cancelled', 'HỦY'),
    ], string='Trạng thái tiến độ', default='new', tracking=True)

    # Người phụ trách section
    execution_date = fields.Date(string='Ngày thực hiện')
    quotation_staff_id = fields.Many2one('res.users', string='Nhân viên báo giá')
    sales_staff_id = fields.Many2one('res.users', string='Nhân viên kinh doanh')
    estimated_delivery_date_mfg = fields.Datetime(string='Ngày giao hàng dự kiến (SX)')
    internal_mfg_note = fields.Text(string='Ghi chú nội bộ SX')

    # BÁO GIÁ section
    quotation_note = fields.Text(string='Ghi chú báo giá')
    quotation_attachment_ids = fields.Many2many('ir.attachment', string='Tài liệu đính kèm')

    # MUA HÀNG section
    purchasing_note = fields.Text(string='Ghi chú mua hàng')
    purchase_request_id = fields.Many2one('purchase.order', string='Yêu cầu mua hàng')
    purchase_deadline = fields.Date(string='Ngày deadline')
    purchase_completion_date = fields.Date(string='Ngày hoàn thành')
    purchase_note = fields.Text(string='Ghi chú')

    # MẪU IN CHỨNG NHẬN XUẤT XƯỞNG
    project_name = fields.Char(string='Dự án')
    customer_name_english = fields.Char(string='Tên KH tiếng anh')

    # Order details
    customer_pays_shipping = fields.Boolean(string='Khách chịu phí vận chuyển', default=False)

    # KHO section
    inventory_note = fields.Text(string='Ghi chú kho')

    # SẢN XUẤT section
    production_request_id = fields.Many2one('mrp.production', string='Yêu cầu sản xuất')
    warehouse_entry_date = fields.Datetime(string='Ngày nhập kho')
    production_note = fields.Text(string='Ghi chú sản xuất')

    # Computed fields for statistics
    total_quantity = fields.Float(string='Tổng số lượng', compute='_compute_order_statistics', store=False)
    manufacturing_count = fields.Integer(string='Số lượng sản xuất', compute='_compute_order_statistics', store=False)
    purchasing_count = fields.Integer(string='Số lượng mua hàng', compute='_compute_order_statistics', store=False)
    inventory_count = fields.Integer(string='Số lượng tồn kho', compute='_compute_order_statistics', store=False)

    @api.depends('order_line')
    def _compute_order_statistics(self):
        for order in self:
            order.total_quantity = sum(order.order_line.mapped('product_uom_qty'))
            order.manufacturing_count = len(order.order_line.filtered(lambda l: l.need_manufacturing))
            order.purchasing_count = len(order.order_line.filtered(lambda l: l.need_purchasing))
            order.inventory_count = len(order.order_line.filtered(lambda l: l.from_inventory))

    def action_sync_order(self):
        """Đồng bộ lại đơn hàng"""
        # Logic để đồng bộ lại đơn hàng
        return True

    def action_create_purchase_request(self):
        """Tạo yêu cầu mua hàng"""
        # Logic để tạo purchase request
        return {
            'type': 'ir.actions.act_window',
            'name': 'Tạo yêu cầu mua hàng',
            'res_model': 'purchase.order',
            'view_mode': 'form',
            'target': 'new',
            'context': {'default_origin': self.name},
        }

    def set_status_new(self):
        self.progress_status = 'new'
        return True

    def set_status_in_production(self):
        self.progress_status = 'in_production'
        return True

    def set_status_external_purchase(self):
        self.progress_status = 'external_purchase'
        return True

    def set_status_not_delivered(self):
        self.progress_status = 'not_delivered'
        return True

    def set_status_delivered(self):
        self.progress_status = 'delivered'
        return True

    def set_status_completed(self):
        self.progress_status = 'completed'
        return True

    def set_status_cancelled(self):
        self.progress_status = 'cancelled'
        return True
