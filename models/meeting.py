from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class VideoMeeting(models.Model):
    _name = "video.meeting"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Video Meeting"
    _rec_name = 'name'
    _order = 'id'

    name = fields.Char(string='Meeting Title')
    meeting_details = fields.Text(string='Description')
    host = fields.Many2one('res.users', string='Host')
    tag_ids = fields.Many2many('course.tag', string='Tags')
    channel = fields.Many2one('mail.channel', string='Channel')
    channel_id = fields.Char(string="Channel Id", compute='_compute_channel_id')
    number_of_attendees = fields.Integer(string="Number Of Attendees", compute='_compute_number_of_attendees')

    state = fields.Selection([
        ('upcoming', 'Upcoming'),
        ('running', 'Running'),
        ('completed', 'Completed'),
    ], string="Status", default='upcoming', tracking=True, required=True)
    progress = fields.Integer(string="Progress", compute='_compute_progress')

    @api.depends('channel')
    def _compute_channel_id(self):
        for rec in self:
            rec.channel_id = rec.channel.id

    def _compute_number_of_attendees(self):
        for rec in self:
            rec.number_of_attendees = len(rec.channel.channel_last_seen_partner_ids)

    def action_whiteboard(self):
        print(self.channel_id)
        return {
            'type': 'ir.actions.act_url',
            'target': 'new',
            'url': 'https://webwhiteboard.com/'
        }

    def action_test(self):
        print(self.channel_id)
        return {
            'type': 'ir.actions.act_url',
            'target': 'new',
            # 'url': f'/web#cids=1&menu_id=84&default_active_id=mail.box_inbox&action=116&active_id=mail.channel_{self.channel_id}'
            'url': f'/web#cids=1&default_active_id=mail.box_inbox&action=104&menu_id=75&active_id=mail.channel_{self.channel_id}'
        }
