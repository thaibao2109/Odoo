# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrderLine(models.Model):
    _inherit = 'sale.order_line'

    # Checkboxes for category alignment
    need_purchasing = fields.Boolean(string='Mua', default=False, tracking=True)
    need_manufacturing = fields.Boolean(string='SX', default=False, tracking=True)
    from_inventory = fields.Boolean(string='KHO', default=False, tracking=True)

    # Manufacturing fields
    mfg_note = fields.Text(string='Ghi chú sx')
    surface_finish = fields.Char(string='Bề mặt')

    # Status field for detailed tracking
    line_status = fields.Selection([
        ('new', 'Mới'),
        ('in_production', 'Đang SX'),
        ('po_placed', 'Đã lên PÔ mua'),
        ('no_mold', 'Chưa có khuôn'),
        ('packaged', 'Đã đóng gói'),
        ('completed', 'Hoàn thành'),
        ('cancelled', 'Hủy'),
    ], string='Tình trạng', default='new', tracking=True)

    # Sequence number for display
    sequence_number = fields.Integer(string='STT', compute='_compute_sequence_number', store=True)

    @api.depends('order_id', 'order_id.order_line')
    def _compute_sequence_number(self):
        for line in self:
            lines = line.order_id.order_line.sorted('id')
            line.sequence_number = lines.ids.index(line.id) + 1

    @api.onchange('need_purchasing', 'need_manufacturing', 'from_inventory')
    def _onchange_category_checkboxes(self):
        """Auto-update status based on checkboxes"""
        if self.need_manufacturing and not self.line_status or self.line_status == 'new':
            self.line_status = 'in_production'
        elif self.need_purchasing and not self.line_status or self.line_status == 'new':
            self.line_status = 'po_placed'
