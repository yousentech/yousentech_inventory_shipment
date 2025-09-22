from odoo import models, fields, api, _
import logging

_logger = logging.getLogger(__name__)


class stock_picking(models.Model):
    _inherit = 'stock.picking'

    prevent_update_source_des_location = fields.Boolean(compute='_check_group_prevent_update_source_des_location',)
    location_domain = fields.Char()
   
    # @api.depends('picking_type_id')
    # def get_location_domain(self):
    #         for rec in self:
    #             if rec.picking_type_id and rec.picking_type_id.warehouse_id:
    #                 rec.location_domain = [('warehouse_id', '=', rec.picking_type_id.warehouse_id.id),('usage', 'in', ['internal'])]
    #             else:
    #                 rec.location_domain  = []
           

    def get_location_dest_domain(self):
        domain = []
        for rec in self:
            if rec.picking_type_id and rec.picking_type_id.warehouse_id:
                domain = [('warehouse_id', '=', rec.picking_type_id.warehouse_id.id),('usage', 'in', ['internal'])]
            else:
                domain = []
        return domain

    # @api.onchange('picking_type_id','location_id','location_dest_id')
    # def onchange_update_location_domain(self):
    #     for rec in self:
    #         rec._fields['location_id'].domain = rec._get_location_dest_domain()
    #         rec._fields['location_dest_id'].domain = rec._get_location_dest_domain()

    @api.depends('user_id')
    def check_group_prevent_update_source_des_location(self):
        for rec in self:
            try:
                is_user_has_group = self.user_has_groups(
                    "yousentech_inventory_shipment.group_prevent_update_source_des_location")
                if is_user_has_group:
                    rec.prevent_update_source_des_location = True
                else:
                    rec.prevent_update_source_des_location = False

            except Exception as e:
                _logger.warning("Error: %s", str(e))


    @api.onchange('picking_type_id','location_id','location_dest_id')
    def onchange_update_location_readonly(self):
        for rec in self:
            rec._fields['location_id'].readonly = rec.prevent_update_source_des_location
            rec._fields['location_dest_id'].readonly = rec.prevent_update_source_des_location        
        

    @api.onchange('picking_type_id', 'partner_id','company_id')
    def get_location_domain(self):
        
        return  {'domain': {'branch_id': [('warehouse_id', '=', self.picking_type_id.warehouse_id.id),('usage', 'in', ['internal']),('company_id','=',self.company_id.id)]}}
