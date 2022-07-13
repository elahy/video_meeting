from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class OlclassParticipant(models.Model):
    _name = "vidmeet.participant"
    _inherit = []
    _description = "Video Meeting Participant"
    _order = 'id'

    name = fields.Char(string='Name', default='New')
    participant_id = fields.Many2one('res.partner', string='Participant')
