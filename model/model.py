# <ZOPEDIR>Products/minimal/model/model.py

"""This is my script for sql."""

from Products.ZSQLMethods.SQL import SQL
from OFS import SimpleItem


class Query(SimpleItem.SimpleItem):
    """Modelos zsql."""

    meta_type = 'query'

    zope = '/home/aparicio/workspace/aplix-filmes/aplix-zope/Products/minimal/'

    def get_filmes(self):
        """SQL SELECT FILMES FOR FILTER."""
        return self.zsql_select_filmes()

    zsql_select_filmes = SQL(
        id='zsql_select_filmes',
        title='',
        connection_id='connection',
        arguments='nome',
        template=open(zope + 'model/zsql_select_filmes.sql').read()
    )
