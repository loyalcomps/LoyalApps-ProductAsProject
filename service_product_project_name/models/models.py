# -*- coding: utf-8 -*-

from odoo import models, fields, api



class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    def _timesheet_create_project_prepare_values(self):
        """Generate project values"""
        values = super()._timesheet_create_project_prepare_values()
        service_products = self.order_id.order_line.product_id.filtered(
            lambda p: p.service_tracking == 'task_in_project' or p.service_tracking == 'project_only')
        if len(service_products) == 1:
            for order_line in self.order_id.order_line:
                if order_line.product_id:
                    if order_line.product_id.service_tracking == 'task_in_project' or order_line.product_id.service_tracking == 'project_only':
                # lambda p: p.type == 'service' and (p.service_tracking == 'task_in_project' or p.service_tracking == 'project_only'))
                        default_name = order_line.name if len(service_products) == 1 else None
                        if service_products:
                            values['name'] = default_name
        return values



    def _timesheet_create_project(self):
        project = super()._timesheet_create_project()
        service_products = self.order_id.order_line.product_id.filtered(
            lambda p: p.service_tracking == 'task_in_project' or p.service_tracking == 'project_only')
        if len(service_products) == 1:
            for order_line in self.order_id.order_line:
                if order_line.product_id:
                    if order_line.product_id.service_tracking == 'task_in_project' or order_line.product_id.service_tracking == 'project_only':
                        # lambda p: p.type == 'service' and (p.service_tracking == 'task_in_project' or p.service_tracking == 'project_only'))
                        default_name = order_line.name if len(service_products) == 1 else None
                        if service_products:
                            project.write({'name':default_name})
        return project

