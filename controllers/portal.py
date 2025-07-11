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
    def _invoice_get_page_view(self, page, filterby=None, **kw):
        response = super()._invoice_get_page_view(page, filterby, **kw)
        if filterby == "invoices":
            user = request.env.user
            response.qcontext.update(
                {
                    "allowed_company_ids": user.company_ids.ids,
                }
            )
        return response
