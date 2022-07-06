from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class VidMeetChannel(models.Model):
    _name = "vidmeet.channel"
    _inherit = []
    _description = "Video Meeting Channel"
    _order = 'id'

    name = fields.Char(string='Name', default='New')
    participant_id = fields.Many2one('res.partner', string='Participant')
