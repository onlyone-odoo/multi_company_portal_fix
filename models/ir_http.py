# custom_module/models/ir_http.py
from odoo import models
from odoo.http import request


class Http(models.AbstractModel):
    _inherit = "ir.http"

    @classmethod
    def _frontend_pre_dispatch(cls):
        super()._frontend_pre_dispatch()
        path = request.httprequest.path
        if path.startswith("/my/"):
            # Restaura allowed originales para portal
            user = request.env.user
            request.update_context(allowed_company_ids=user.company_ids.ids)
        else:
            # Para otras rutas website, ajusta company_id al forzado para consistencia
            allowed = request.context.get("allowed_company_ids")
            if allowed:
                request.update_context(company_id=allowed[0])
