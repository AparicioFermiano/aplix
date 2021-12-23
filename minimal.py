# <ZOPEDIR>Products/minimal/minimal.py

"""This is my First minimal Product."""

from OFS import SimpleItem
from Globals import DTMLFile
from controller.controller import Metodos
from model.model import Query


class minimal(SimpleItem.SimpleItem):
    """Minimal object."""

    meta_type = 'minimal'

    controller = Metodos()

    model = Query()

    manage_options = (
        {'label': 'Properties', 'action': 'manage_edit_form'},
        {'label': 'View', 'action': 'controller.index_html'},
    )

    def __init__(self, id, connection):
        """Initialize."""
        self.id = id
        self.connection = connection

    def index_html(self):
        """Index_html"""
        return self.controller.index_html()

        # Conection for Database.
    def get_database_connection(self):
        """Database Connection."""
        return getattr(self.connection, 'id')

    def manage_edit_action(self, title, content, RESPONSE=None):
        """Altera os valores do produto."""
        self.title = title
        self._p_changed = 1
        RESPONSE.redirect('controller.manage_edit_form')


def manage_add_minimal_action(self, connection, id='minimal',
                              RESPONSE=None):
    """Add a minimal to a folder."""
    conn = getattr(self, connection)
    self._setObject(id, minimal(id, conn))
    RESPONSE.redirect(id + '/controller.index_html')

manage_add_minimal_form = DTMLFile('controller/dtml/manage_add_minimal_form',
                                   globals())
