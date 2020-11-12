# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Costing(models.Model):
    _name = 'costing.costing'
    _description = 'costing.costing'
    _inherit = 'res.currency'

    customer = fields.Many2one('res.users',
                               ondelete='set null', string="Customer", index=True)
    season = fields.Char()
    #season = fields.Char(default='Winter Season 2020 - T24B11', required=True)
    style_ref_name = fields.Char(default='PANTALOON', string="Style/Ref Name")
    prod_concept = fields.Char(string='Product Concept')
    # type = fields.One2many('costing.costingtypes', 'costing_types')
    type = fields.Many2one('costing.costingtypes', string="Type")
    company = fields.Many2one('res.company', string='Company')
    pricelist = fields.Many2one('product.pricelist', string='Pricelist')
    currency = fields.Many2one(comodel_name='res.currency', string='Currency', required="True", store="True", default=0)
    # stage = fields.One2many('costing.costingstages', 'costing_stages')
    stage = fields.Many2one('costing.costingstages')
    # stage = fields.Many2many('costing.costingstages')
    board = fields.Char(string='Board')
    order_qty = fields.Integer(string='Order Quantity', default=0)
    size_range = fields.Char(string='Size/Range', default='OBA')
    sample_size = fields.Char(string='Sample Size', default='OBA')
    merch_div = fields.Char(string='Merch of Division')
    merch_fabric = fields.Char(string='Merch of Fabrication')
    merch_size = fields.Char(string='Merch Size Offerings')
    spec_pattern = fields.Char(string='Spec/Pattern')
    costsheetlines = fields.Many2many('costing.costsheetlines')

    class CostSheetLines(models.Model):
        _name = 'costing.costsheetlines'
        _description = 'Cost Sheet Lines'

        # particulars = fields.Char(string='Particulars')
        desc = fields.Char(string='Description')
        placement = fields.Char(string='Placement')
        supplier = fields.Char(string='Supplier')
        cut_width = fields.Float(string='Cuttable Width')
        consump = fields.Float(string='Consumption')
        uom = fields.Char(string='UOM')
        curr = fields.Many2one('res.currency', string='Currency')
        cost_item = fields.Float(string='Cost of Item(Ex-works/CIF/CFR)')
        costing_type = fields.Many2many('costing.costingtypes')
        # costing_type = fields.Many2one('costing.costingtypes')
        display_type = fields.Selection([
            ('line_section', "Section"),
            ('line_note', "Note")], default=False, help="Technical field for UX purpose.")
        name = fields.Char(string="Particulars", required=True)

        @api.onchange('costing_type')
        def _onchange_costingtype(self):
            return {'domain': {'costing_id': [('costing_type', '=', self.costing_type.id)]}}

    class CostingTypes(models.Model):
        _name = 'costing.costingtypes'
        _description = 'Costing Types'

        name = fields.Char()
        sequence = fields.Integer()
        costing_types = fields.Selection(
            [('prelimnary', 'Prelimnary Costing'), ('buyer_approved', 'Buyer Approved Costing'),
             ('factory_approved', 'Factory Approved Costing')])
        # costing_types = fields.One2many('costing.costing', 'type')
        # prelim_costing = fields.Float(string="Prelimnary Costing")
        # buyer_approved = fields.Float(string="Buyer Approved Costing")
        # factory_approved = fields.Float(string="Factory Approved Costing")

    class CostingStages(models.Model):
        _name = 'costing.costingstages'
        _description = 'Costing Stages'

        name = fields.Char()
        sequence = fields.Integer()
        #approvals = fields.One2many(default='Approvals')
        costing_stages = fields.Selection([('new', 'New'), ('progress', 'Progress'),
                                           ('approved', 'Approved'), ('effective', 'Effective')])
        # costing_stages = fields.Char()
        # costing_stages = fields.One2many('costing.costing', 'stage')
        folded_in_kanban = fields.Boolean('Folded in kanban view')
        allow_to_apply_changes = fields.Boolean('Allow to apply changes')
        final_stage = fields.Boolean('Final Stage')
        # types = fields.Many2many('costing.costingtypes')
        types = fields.Many2one('costing.costingtypes', string="Type")
        approvals = fields.Many2many('costingstages.approvals')

    class Approvals(models.Model):
        _name = 'costingstages.approvals'
        _description = 'Approvals'

        role = fields.Char(string="Role")
        users = fields.Many2many('res.users', string="Users")
        approval_type = fields.Char(string="Approval Type")
