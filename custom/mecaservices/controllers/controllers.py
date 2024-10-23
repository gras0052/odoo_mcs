# -*- coding: utf-8 -*-
from odoo import http


class Mecaservices(http.Controller):
    @http.route("/mecaservices/mecaservices", auth="public")
    def index(self, **kw):
        return "Hello, world"

    @http.route("/mecaservices/mecaservices/objects", auth="public")
    def list(self, **kw):
        return http.request.render(
            "mecaservices.listing",
            {
                "root": "/mecaservices/mecaservices",
                "objects": http.request.env["mecaservices.mecaservices"].search([]),
            },
        )

    @http.route(
        '/mecaservices/mecaservices/objects/<model("mecaservices.mecaservices"):obj>',
        auth="public",
    )
    def object(self, obj, **kw):
        return http.request.render("mecaservices.object", {"object": obj})
