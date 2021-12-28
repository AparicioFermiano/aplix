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
        return self.index(macro_page=self.slot,
                          select_filmes=self.query.get_filmes())

    def categoria_html(self, cod_categoria=None):
        """Categoria de filmes."""
        return self.categoria(macro_page=self.slot,
                              select_filmes_for_cat=self.query.get_filmes_for_cat(cod_categoria=cod_categoria),
                              select_categoria=self.query.get_categoria())

    def cadastro_html(self):
        """Cadastro de filmes."""
        return self.cadastro(macro_page=self.slot)

    def action_insert(self, nome=None, elenco=None,
                      cod_categoria=None, imgurl=None, sinopse=None):
        """Insert filmes."""
        return self.cadastro(macro_page=self.slot,
                             insert_filme=self.query.insert_filme(nome=nome,
                                                                  elenco=elenco,
                                                                  cod_categoria=cod_categoria,
                                                                  imgurl=imgurl,
                                                                  sinopse=sinopse))

    def lista_html(self):
        """Cadastro de filmes."""
        return self.lista(macro_page=self.slot)

    # Used to view content of the object.

    index = PageTemplateFile('zpt/index_html', globals())

    categoria = PageTemplateFile('zpt/categoria_html', globals())

    cadastro = PageTemplateFile('zpt/cadastro_html', globals())

    lista = PageTemplateFile('zpt/lista_html', globals())

    manage_edit_form = PageTemplateFile('zpt/manage_edit_form',
                                        globals())

    slot = PageTemplateFile('zpt/slot.zpt', globals())

    manage_edit_form = PageTemplateFile('zpt/manage_edit_form', globals())
