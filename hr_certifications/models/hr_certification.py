from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
from datetime import date

class HrCertification(models.Model):
    """Model to manage employee certifications with expiration tracking."""
    _name = 'hr.certification'
    _description = 'Employee Certification'

    name = fields.Char(string='Certification Name', required=True)
    employee_id = fields.Many2one('hr.employee', string='Employee', required=True,
                                  track=True)
    expiry_date = fields.Date(string='Expiry Date', required=True)
    is_expired = fields.Boolean(string='Is Expired', store=True, readonly=True, default=False)

    @api.model
    def check_hr_certificate_expiration(self):
        """Scheduled action to check and update expired certifications."""
        today = date.today()
        expired_certs = self.search([('expiry_date', '<', today), ('is_expired', '=', False)])
        for cert in expired_certs:
            cert.is_expired = True
            # send notification to employee or HR
            self.env['mail.message'].create({
                'subject': _('Certification Expired'),
                'body': _('The certification %s has expired.') % cert.name,
                'model': 'hr.employee',
                'res_id': cert.employee_id.id,
                'message_type': 'notification',
            })
        return True

    @api.constrains('expiry_date')
    def _check_expiry_date(self):
        """Ensure expiry date is not set in the past."""
        for record in self:
            if record.expiry_date and record.expiry_date < date.today():
                raise ValidationError(_("Expiry date cannot be in the past!"))
