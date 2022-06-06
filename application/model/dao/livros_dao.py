
from application.model.entity.Livros import Livros

class LivrosDao:

    def ListarLivros():
      
      cadastro_de_livros = [
          Livros(id=1, titulo="Grande", isbn="1254", autor="ane", editora="atlanta", ano="2027", assunto=1,status=0),
          Livros(id=2, titulo="Agua", isbn="1294", autor="ana", editora="NovaTec", ano="2012", assunto=2, status=1),
          Livros(id=3, titulo="Era do Gelo", isbn="1294", autor="jin", editora="NovaTec", ano="2013", assunto=7, status=1),
          Livros(id=4, titulo="Helboy", isbn="2323", autor="ana joa", editora="Disney", ano="2020", assunto=1,status=1),
          Livros(id=5, titulo="Vade Mecum", isbn="1478", autor="erik", editora="Imperios", ano="2012", assunto=2, status=1),
          Livros(id=6, titulo="Avatar", isbn="3434", autor="Huam", editora="Movida", ano="2022", assunto=3, status=1),
          Livros(id=7, titulo="pilatos", isbn="3434", autor="Aroldo", editora="Movida", ano="2022", assunto=1, status=1),
          Livros(id=8, titulo="Grilo", isbn="3485", autor="Ana", editora="Movida", ano="2000", assunto=4, status=1),
          Livros(id=9, titulo="Matto selvagem", isbn="4534", autor="pires", editora="Movida", ano="1946", assunto=4, status=0),
          Livros(id=10, titulo="Avatar", isbn="9878", autor="marcos", editora="Movida", ano="2016", assunto=7, status=1),
          Livros(id=11, titulo="joao e pe feijao", isbn="3434", autor="irinei", editora="humo", ano="2022", assunto=3, status=0),
          Livros(id=12, titulo="halo", isbn="4354", autor="jonas", editora="novatec", ano="2014", assunto=5, status=1),
          Livros(id=13, titulo="guerra", isbn="8678", autor="Huam", editora="seleniun", ano="2015", assunto=1, status=1),

        ]

      return cadastro_de_livros
