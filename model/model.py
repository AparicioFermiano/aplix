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

    def get_filmes_for_cat(self, cod_categoria):
        """SQL SELECT FILMES FOR CATEGORIA."""
        return self.zsql_select_filmes_for_categoria(cod_categoria=cod_categoria)

    def get_categoria(self):
        """SQL SELECT CATEGORIA."""
        return self.zsql_select_categoria()

    def insert_filme(self, nome, elenco, cod_categoria, imgurl, sinopse):
        """INSERT FOR FILME."""
        return self.zsql_insert_filme(nome=nome,
                                      elenco=elenco,
                                      cod_categoria=cod_categoria,
                                      imgurl=imgurl,
                                      sinopse=sinopse)

    zsql_select_filmes = SQL(
        id='zsql_select_filmes',
        title='',
        connection_id='connection',
        arguments='nome',
        template=open(zope + 'model/zsql_select_filmes.sql').read()
    )

    zsql_select_filmes_for_categoria = SQL(
        id='zsql_select_filmes_for_categoria',
        title='',
        connection_id='connection',
        arguments='cod_categoria',
        template=open(zope + 'model/zsql_select_filmes_for_cat.sql').read()
    )
    zsql_select_categoria = SQL(
        id='zsql_categoria',
        title='',
        connection_id='connection',
        arguments='',
        template=open(zope + 'model/zsql_select_categoria.sql').read()
    )
    zsql_insert_filme = SQL(
        id='zsql_insert_filme',
        title='',
        connection_id='connection',
        arguments='nome\nelenco\ncod_categoria\nimgurl\nsinopse',
        template=open(zope + 'model/zsql_insert_filme.sql').read()
    )
