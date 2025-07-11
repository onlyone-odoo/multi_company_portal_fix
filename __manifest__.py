# pylint: disable=missing-module-docstring,pointless-statement
# License AGPL-3.0 or later[](https://www.gnu.org/licenses/agpl).
{
    "name": "Multi Company Portal Fix",
    "summary": """
        Corrige acceso 403 en portal multi-compañía para rutas /my/*""",
    "author": "Be OnlyOne",
    "maintainers": ["onlyone-odoo"],
    "website": "https://onlyone.odoo.com/",
    "license": "AGPL-3",
    "category": "Technical Settings",
    "version": "17.0.1.0.0",
    "development_status": "Production/Stable",
    "application": False,
    "installable": True,
    "external_dependencies": {
        "python": [],
        "bin": [],
    },
    "depends": ["website"],
}
