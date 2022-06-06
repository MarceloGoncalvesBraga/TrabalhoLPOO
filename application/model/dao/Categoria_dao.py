
from application.model.entity.Categoria import Categoria

class CategoriaDao:

    def ListarCategorias():

        cadastro_de_categoria = [
          Categoria(id=1, nome="Terror"),
          Categoria(id=2, nome="Romance"),
          Categoria(id=3, nome="Suspense"),
          Categoria(id=4, nome="Acao"),
          Categoria(id=5, nome="Comedia"),
          Categoria(id=6, nome="Politica"),
          Categoria(id=7, nome="Infantil"),
          Categoria(id=8, nome='Estudos')


        ]

        return cadastro_de_categoria

