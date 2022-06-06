
from application.model.entity.exemplar import Exemplar

class ExemplarDao:

    def ListarExemplares():

        cadastro_de_exemplares = [
          Exemplar(id=1, nome="O Amanhecer", quantidade=20),
          Exemplar(id=1, nome="Guerra Virtual", quantidade=12),
        ]

        return cadastro_de_exemplares

