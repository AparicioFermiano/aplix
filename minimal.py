# <ZOPEDIR>Products/minimal/minimal.py

"""This is my First minimal Product."""

from OFS import SimpleItem
from Globals import DTMLFile
from controller.controller import Metodos


class minimal(SimpleItem.SimpleItem):
    """Minimal object."""

    meta_type = 'minimal'

    metodos = Metodos()

    def __init__(self, id, connection):
        """Initialize."""
        self.id = id
        self.connection = connection

        # Conection for Database.
    def get_database_connection(self):
        """Database Connection."""
        return getattr(self.connection, 'id')

    def manage_edit_action(self, title, content, RESPONSE=None):
        """Altera os valores do produto."""
        self.title = title
        self._p_changed = 1
        RESPONSE.redirect('manage_editForm')


def manage_add_minimal_action(self, connection, id='minimal',
                              RESPONSE=None):
    """Add a minimal to a folder."""
    conn = getattr(self, connection)
    self._setObject(id, minimal(id, conn))
    RESPONSE.redirect(id + '/index_html')

manage_add_minimal_form = DTMLFile('controller/dtml/manage_add_minimal_form',
                                   globals())
