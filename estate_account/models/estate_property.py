from odoo import models,fields

from odoo17.odoo.fields import Command


class EstateProperty(models.Model):
    _inherit = "estate.property"

    def action_do_book(self):
        journal = self.env["account.journal"].search([("type","=","sale")], limit=1)

        for prop in self:
            self.env["account.move"].create(
                {
                    # "partner_id": self.env.user,
                    "move_type": "out_invoice",
                    "journal_id": journal.id,
                    "invoice_line_ids":[
                        Command.create({
                            "name": prop.fname,
                            "quantity": 1.0,
                            "price_unit": prop.total_price * 6.0 / 100.0,
                        }),
                        Command.create({
                            "name": "Administrative fees",
                            "quantity": 1.0,
                            "price_unit": 100.0,
                        }),
                    ]
                }
            )

        return super().action_do_book()
