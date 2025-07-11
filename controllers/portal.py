# custom_module/controllers/portal.py
from odoo import http
from odoo.addons.account.controllers import portal


class CustomerPortal(portal.CustomerPortal):
    @http.route(
        ["/my/invoices", "/my/invoices/<int:page>"],
        type="http",
        auth="user",
        website=True,
    )
    def portal_my_invoices(self, page=1, filterby=None, **kw):
        user = request.env.user
        request.update_context(allowed_company_ids=user.company_ids.ids)
        response = super().portal_my_invoices(page, filterby, **kw)
        if filterby == "invoices":
            response.qcontext.update(
                {
                    "allowed_company_ids": user.company_ids.ids,
                }
            )
        return response
