# <ZOPEDIR>Products/minimal/controller/controller.py

"""This is my script for controller."""


from Products.PageTemplates.PageTemplateFile import PageTemplateFile
from OFS import SimpleItem
from ..model.model import Query


class Controller(SimpleItem.SimpleItem):
    """Metodos dinamicos."""

    manage_options = (
        {'label': 'Properties', 'action': 'manage_editForm'},
        {'label': 'View', 'action': 'index_html'},
    )

    meta_type = 'controller'

    query = Query()

    def index_html(self):
        """Pagina principal."""
        return self.index(
            macro_page=self.slot,
            select_filmes=self.query.get_filmes())

    def categoria_html(self, categoria_id=None):
        """Categoria de filmes."""
        return self.categoria(
            macro_page=self.slot,
            select_filmes_for_cat=self.query.get_filmes_for_cat(
                categoria_id=categoria_id),
            select_categoria=self.query.get_categoria())

    def cadastro_html(self):
        """Cadastro de filmes."""
        return self.cadastro(macro_page=self.slot)

    def action_insert(self, nome=None, elenco=None,
                      categoria_id=None, imgurl=None, sinopse=None):
        """Insert filmes."""
        self.query.insert_filme(
            nome=nome,
            elenco=elenco,
            categoria_id=categoria_id,
            imgurl=imgurl,
            sinopse=sinopse)
        return self.REQUEST.RESPONSE.redirect('cadastro_html')

    def lista_html(self):
        """Listando os filmes."""
        return self.lista(
            macro_page=self.slot,
            select_filmes=self.query.get_filmes())

    def editar_filme_html(self, cod_id):
        """Editar filmes."""
        return self.editar(
            macro_page=self.slot,
            select_filmes_for_id=self.query.get_filmes_for_id(cod_id=cod_id))

    def delete_filme_html(self, cod_id):
        """Editar filmes."""
        self.query.delete_filmes_for_id(cod_id=cod_id)
        return self.REQUEST.RESPONSE.redirect('lista_html')

    def infofilme_html(self, cod_id):
        """Editar filmes."""
        return self.infofilme(
            macro_page=self.slot,
            select_filmes_for_id=self.query.get_filmes_for_id(cod_id=cod_id))

    def action_update(self, cod_id=None, nome=None, elenco=None,
                      categoria_id=None, imgurl=None, sinopse=None):
        """Update filmes."""
        self.query.update_filme(
            cod_id=cod_id,
            nome=nome,
            elenco=elenco,
            categoria_id=categoria_id,
            imgurl=imgurl,
            sinopse=sinopse)
        return self.REQUEST.RESPONSE.redirect('editar_filme_html')

    # Used to view content of the object.

    index = PageTemplateFile('zpt/index_html', globals())

    categoria = PageTemplateFile('zpt/categoria_html', globals())

    cadastro = PageTemplateFile('zpt/cadastro_html', globals())

    lista = PageTemplateFile('zpt/lista_html', globals())

    editar = PageTemplateFile('zpt/editar_filme_html.zpt', globals())

    infofilme = PageTemplateFile('zpt/infofilme_html.zpt', globals())

    manage_edit_form = PageTemplateFile('zpt/manage_edit_form', globals())

    slot = PageTemplateFile('zpt/slot.zpt', globals())

    manage_edit_form = PageTemplateFile('zpt/manage_edit_form', globals())
