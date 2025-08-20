from odoo import models, fields, api, _
class stock_move(models.Model):
    
    _inherit = 'stock.move'
    aval_qty = fields.Float(string="Available Quantity")
    
    @api.onchange('product_id','picking_id')
    def get_values_aval_qty(self):
        for line in self:
            qty = 0.00
            if line.product_id and line.picking_id.location_id.id:
                qty = self.env['stock.quant'].search([('location_id','=',line.picking_id.location_id.id),('product_id','=', line.product_id.id)])
                qty = sum(line.quantity for line in qty)
            line.aval_qty = qty
            
            
class stock_picking(models.Model):
    _inherit = 'stock.picking'

    def button_validate(self):
        for line in self.move_ids:
           line.get_values_aval_qty()
        res = super(stock_picking, self).button_validate()
        return res
    
 
      
