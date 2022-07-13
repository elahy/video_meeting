# from odoo import api, fields, models, _
#
#
# class VidMeetSchedule(models.Model):
#     _name = "vidmeet.schedule"
#     _inherit = ['mail.thread', 'mail.activity.mixin']
#     _description = "Video Meeting Schedule"
#     _order = 'id desc'
#
#     name = fields.Char(string='Topic', required=True)
#     appointment_time = fields.Datetime(string='Schedule Time', tracking=True, required=True,
#                                        default=fields.Datetime.now)
#     host_id = fields.Many2one('res.users', string='Host')
#     duration = fields.Float(string="Duration")
#     channel_id = fields.Char(string="Channel Id", related='course_id.channel_id')
#
#     def action_test(self):
#         print(self.channel_id)
#         return {
#             'type': 'ir.actions.act_url',
#             'target': 'new',
#             'url': f'/web#cids=1&menu_id=84&default_active_id=mail.box_inbox&action=116&active_id=mail.channel_{self.channel_id}'
#         }
