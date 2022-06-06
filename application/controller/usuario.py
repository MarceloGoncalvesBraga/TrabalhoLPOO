
from ast import Break
from tracemalloc import stop
from application.model.dao.livros_dao import LivrosDao
from application.model.dao.Categoria_dao import CategoriaDao
from application.model.entity.Livros import Livros

class Usuario:
  def consultarLivros():
    listalivros = LivrosDao.ListarLivros()
    listacategorias = CategoriaDao.ListarCategorias()
    while True:
      print("""\t   
      -------------------------------------
              BIBLIOTECA     USUARIO       
      ------------------------------------- 
        1- Pesquisar Por Titulo 
        2- Pesquisar Por Categoria  
        3- Pesquisar Por Autor  
        0- Sair
      _____________________________________
        """)

      opcao = input("\t  Digite uma opcao \n")
      if opcao == '1':
        tem = 0
        titulo = input("\t Digite um Titulo \n")

        if len(titulo)<2:
          titulo = input("\t Digite um titulo corretamente \n")

        for lis in LivrosDao.ListarLivros():
         
          if titulo == lis.getTitulo():
            print("\t Livro Encontrado \n")
            print("\t Titulo:  ",lis.getTitulo())
            print("\t N° Isbn: ",lis.getIsbn())
            print("\t Autor:   ",lis.getAutor())
            print("\t Editora: ",lis.getEditora())
            print("\t Ano:     ",lis.getAno())
            for cat in listacategorias:
              if cat.getId() == lis.getAssunto():

                print("\t Assunto: ",cat.getNome())
                tem = 1
            break

        if tem == 0:
            print("\t Nenhum Livro não encontrado")
         
      
      elif opcao == '2':
        tem = 0
        assunto = input("\t Digite um assunto \n")

        if len(assunto)<3:
          assunto = input("\t Digite um assunto corretamente \n")

      
        list = LivrosDao.ListarLivros()
        for cat in listacategorias:
          if cat.getNome() == assunto:
            for lis in listalivros:
             if lis.getAssunto() == cat.getId():
              print("\t Livro Encontrado \n")
              print("\t Titulo:  ",lis.getTitulo())
              print("\t N° Isbn: ",lis.getIsbn())
              print("\t Autor:   ",lis.getAutor())
              print("\t Editora: ",lis.getEditora())
              print("\t Ano:     ",lis.getAno())
              print("\t Assunto: ",cat.getNome())
        if tem == 0:
            print("\t Nenhum Livro não encontrado")
      
      elif opcao == '3':
        tem = 0
        autor = input("\t Digite um autor \n")

        if len(autor)<3:
         autor = input("\t Digite um autor corretamente \n")
          
        for lis in listalivros:
          if lis.getAutor() == autor:
              print("\t Livro Encontrado \n")
              print("\t Titulo:  ",lis.getTitulo())
              print("\t N° Isbn: ",lis.getIsbn())
              print("\t Autor:   ",lis.getAutor())
              print("\t Editora: ",lis.getEditora())
              print("\t Ano:     ",lis.getAno())
              for cat in listacategorias:
                if cat.getId() == lis.getAssunto():
                  print("\t Assunto: ",cat.getNome())
        if tem == 0:
            print("\t Nenhum Livro não encontrado")
      
      elif opcao == '0':
         break
      else:
        print("Opcao Invalida")
      