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

    def get_filmes_for_cat(self, categoria_id):
        """SQL SELECT FILMES FOR CATEGORIA."""
        return self.zsql_select_filmes_for_categoria(categoria_id=categoria_id)

    def get_categoria(self):
        """SQL SELECT CATEGORIA."""
        return self.zsql_select_categoria()

    def insert_filme(self, nome, elenco, categoria_id, imgurl, sinopse):
        """INSERT FOR FILME."""
        return self.zsql_insert_filme(nome=nome,
                                      elenco=elenco,
                                      categoria_id=categoria_id,
                                      imgurl=imgurl,
                                      sinopse=sinopse)

    def get_filmes_for_id(self, cod_id):
        """SELECT FILME FOR ID."""
        return self.zsql_select_filme_for_id(cod_id=cod_id)

    def delete_filmes_for_id(self, cod_id):
        """DELETE FILME FOR ID."""
        return self.zsql_delete_filme_for_id(cod_id=cod_id)

    def update_filme(self, cod_id, nome, elenco, categoria_id, imgurl, sinopse):
        """INSERT FOR FILME."""
        return self.zsql_update_filme(cod_id=cod_id,
                                      nome=nome,
                                      elenco=elenco,
                                      categoria_id=categoria_id,
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
        arguments='categoria_id',
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
        arguments='nome\nelenco\ncategoria_id\nimgurl\nsinopse',
        template=open(zope + 'model/zsql_insert_filme.sql').read()
    )
    zsql_select_filme_for_id = SQL(
        id='zsql_select_filme_for_id',
        title='',
        connection_id='connection',
        arguments='cod_id',
        template=open(zope + 'model/zsql_select_filme_for_id.sql').read()
    )
    zsql_delete_filme_for_id = SQL(
        id='zsql_delete_filme_for_id',
        title='',
        connection_id='connection',
        arguments='cod_id',
        template=open(zope + 'model/zsql_delete_filme_for_id.sql').read()
    )
    zsql_update_filme = SQL(
        id='zsql_update_filme',
        title='',
        connection_id='connection',
        arguments='cod_id\nnome\nelenco\ncategoria_id\nimgurl\nsinopse',
        template=open(zope + 'model/zsql_update_filme.sql').read()
    )
