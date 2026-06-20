# Copyright 2018 Ivan Yelizariev <https://github.com/yelizariev>
# License MIT (https://opensource.org/licenses/MIT).
import logging

from odoo import fields, models
from odoo.exceptions import AccessDenied

_logger = logging.getLogger(__name__)


class ResUsers(models.Model):
    _inherit = "res.users"

    auth_quick_token = fields.Char()

    def _check_credentials(self, credential, env):
        try:
            return super(ResUsers, self)._check_credentials(credential, env)
        except AccessDenied:
            if not (credential['type'] == 'auth_quick_token' and credential.get('token')):
                raise
            res = self.sudo().search(
                [("id", "=", credential['uid']), ("auth_quick_token", "=", credential['token'])]
            )
            if not res:
                raise
            return {
            'uid': self.env.user.id,
            'auth_method': 'auth_quick_token',
            'mfa': 'default',
        }
