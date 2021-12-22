# <ZOPEDIR>Products/minimal/minimal.py

"""This is my First minimal Product."""

from OFS import SimpleItem
from Globals import DTMLFile
from Products.PageTemplates.PageTemplateFile import PageTemplateFile
from Products.ZSQLMethods.SQL import SQL


class minimal(SimpleItem.SimpleItem):
    """Minimal object."""

    zope = '/home/aparicio/workspace/project-aplix/aplix-zope/Products/minimal'

    meta_type = 'minimal'

    manage_options = (
        {'label': 'Properties', 'action': 'manage_editForm'},
        {'label': 'View', 'action': 'index_html'},
    )

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

    def index_html(self):
        """Pagina principal."""
        return self.index(macro_page=self.slot,
                          select_filmes=self.zsql_select_filmes)

    def macros(self):
        """Slot de Macros."""
        return self.slot()

    def get_filmes(self):
        """SQL SELECT FILMES FOR FILTER."""
        return self.zsql_select_filmes()

    # Used to view content of the object.
    index = PageTemplateFile('zpt/index_html', globals())

    manage_edit_form = PageTemplateFile('zpt/manage_edit_form', globals())

    standard_html_header = DTMLFile('www/standard_html_header', globals())

    standard_html_footer = DTMLFile('www/standard_html_footer', globals())

    slot = PageTemplateFile('zpt/slot.zpt', globals())

    zsql_select_filmes = SQL(
        id='zsql_select_filmes',
        title='',
        connection_id='connection',
        arguments='nome',
        template=open(zope + '/sql/zsql_select_filmes.sql').read()
    )


def manage_add_minimal_action(self, connection, id='minimal',
                              RESPONSE=None):
    """Add a minimal to a folder."""
    conn = getattr(self, connection)
    self._setObject(id, minimal(id, conn))
    RESPONSE.redirect(id + '/index_html')

manage_add_minimal_form = DTMLFile('www/manage_addMinimalForm', globals())
