# <ZOPEDIR>Products/minimal/controller/controller.py

"""This is my script for controller."""


from Products.PageTemplates.PageTemplateFile import PageTemplateFile
from OFS import SimpleItem
from ..model.model import Query


class Metodos(SimpleItem.SimpleItem):
    """Metodos dinamicos."""

    meta_type = 'controller'

    query = Query()

    def index_html(self):
        """Pagina principal."""
        return self.index(macro_page=self.slot,
                          select_filmes=self.query.zsql_select_filmes())

    def macros(self):
        """Slot de Macros."""
        return self.slot()

    # Used to view content of the object.

    index = PageTemplateFile('zpt/index_html', globals())

    manage_edit_form = PageTemplateFile('zpt/manage_edit_form',
                                        globals())

    slot = PageTemplateFile('zpt/slot.zpt', globals())

    manage_edit_form = PageTemplateFile('zpt/manage_edit_form', globals())
