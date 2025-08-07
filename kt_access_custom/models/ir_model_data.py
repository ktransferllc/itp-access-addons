from odoo import models, api


class IrModelData(models.Model):
    _inherit = "ir.model.data"

    @api.model
    def kt_xmlid_lookup(self, xmlid: str) -> tuple:
        """Return (id, res_model, res_id) or raise ValueError if not found"""
        model, res_id = self._xmlid_lookup(xmlid)
        return (0, model, res_id)
    
    @api.model
    def kt_xmlid_to_res_model_res_id(self, xmlid, raise_if_not_found=False):
        """ Return (res_model, res_id)"""
        return self._xmlid_to_res_model_res_id(xmlid, raise_if_not_found)
