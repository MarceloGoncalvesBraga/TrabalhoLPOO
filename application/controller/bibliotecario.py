
from application.model.dao.livros_dao import LivrosDao
from application.model.entity.Livros import Livros

from application.model.dao.usuario_dao import UsuarioDao
from application.model.entity.usuario import Usuario

from application.model.dao.emprestimo_dao import EmprestimoDao
from application.model.entity.emprestimo import Emprestimo

from application.model.dao.Exemplar_dao import ExemplarDao
from application.model.entity.exemplar import Exemplar

from application.model.dao.Categoria_dao import CategoriaDao
from application.model.entity.Categoria import Categoria
import application

class Biblioteca():

  def Bibliotecario():
  
    cadastro_de_livros = [
          Livros(id=1, titulo="Grande", isbn="1254", autor="ane", editora="atlanta", ano="2027", assunto=1,status=0),
        ]
    listamprestimos = EmprestimoDao.ListarEmprestimos()
    listaexemplares = ExemplarDao.ListarExemplares()
    listacategorias = CategoriaDao.ListarCategorias()
    listalivros = LivrosDao.ListarLivros()
    listausuarios = UsuarioDao.ListarUsuarios()
    while True:
      print("""\t
      -------------------------------------
                  BIBLIOTECARIO          
      ------------------------------------- 
        1- Listar Livros
        2- Cadastrar Livro 
        3- Editar Livro 
        4- Excluir Livro 
        ___________________________
        5- Listar Exemplares
        6- Cadastrar Exemplar 
        7- Editar Exemplar 
        8- Excluir Exemplar 
       _____________________________
        9- Listar Assuntos 
        10- Cadastrar Assunto 
        11- Editar Assunto 
        12- Excluir Assunto 
       _____________________________

        0- Sair
        """)
      
      opcao = input("Digite uma opcao \n")
      if opcao == '1':

        print("\tLista de Livros Cadastrados")
        for lis in listalivros:
          print("\tId: ",lis.getId())
          print("\tTitulo:  ",lis.getTitulo())
          print("\tN° Isbn: ",lis.getIsbn())
          print("\tAutor: ",  lis.getAutor())
          print("\tEditora: ",lis.getEditora())
          print("\tAno:     ",lis.getAno())
          for ass in listacategorias:
            if ass.getId() == lis.getAssunto():
               print("\tAssunto: ",ass.getNome())

      elif opcao == '2':
            id =  input("digite um id ")
            titulo =  input("digite um titulo ")
            isbn =    input("digite o isbn")
            autor =   input("digite o autor")
            editora = input("digite a editora") 
            ano =     input("digite o ano"),
            assunto = input("digite o id do  assunto")
            status =  input("digite o status 0 Indisponivel ou 1 Disponivel")

            listalivros.append((Livros(
              id=id, 
              titulo= titulo, 
              isbn= isbn,
              autor=autor,
              editora=editora,
              ano= ano,
              assunto= assunto,
              status= status)))
            print(listalivros)
      elif opcao == '3':
        alt = 0
        id = int(input("Digite um id \n"))

        for lis in listalivros:
          if lis.getId() == id:
            titulo =  input("digite um titulo ")
            isbn =    input("digite o isbn")
            autor =   input("digite o autor")
            editora = input("digite a editora") 
            ano =     input("digite o ano"),
            assunto = input("digite o id do  assunto")
            status =  input("digite o status 0 Indisponivel ou 1 Disponivel")

            lis.setTitulo(titulo) 
            lis.setIsbn(isbn)
            lis.setAutor(autor)
            lis.setEditora(editora)
            lis.setAno(ano)
            lis.setAssunto(assunto)
            lis.setStatus(status)

            alt = 1
        if alt == 1:
          print("Alterado com Sucesso")
    
      elif opcao == '4':
            id = int(input("Digite um id \n"))
            for lis in listalivros:
              if lis.getId() == id:
                listalivros.remove(lis) 
                print("\t Realizado com Sucesso !")
                
      elif opcao == '5':
        print("\tLista de Exemplares Cadastrados")
        for lis in listaexemplares:
          print("\tId: ",lis.getId())
          print("\tNome::  ",lis.getNome())
          print("\tQuantidade: ",lis.getQuantidade())

      elif opcao == '6':
          id = int(input("digite um id "))
          nome = input("digite um nome ")
          quantidade = input("digite a quantidade")

          listaexemplares.append((Exemplar(id, nome, quantidade)))
          print("Cadastro Realizado com Sucesso !")
         
      elif opcao == '7':
        id = input("Digite um id \n")
        for lis in listaexemplares:
            if lis.getId() == id:
              nome = input("digite um nome ")
              quantidade = input("digite a quantidade")

              lis.setNome(nome)
              lis.setQuantidade(quantidade)
              print("Alterado com sucesso")

      elif opcao == '8':
          id = int(input("Digite um id \n"))
          
          for lis in listaexemplares:
              if lis.getId() == id:
                listaexemplares.remove(lis)
                print("\t Realizado com Sucesso !")

      elif opcao == '9':
        print("\tLista de Assuntos Cadastrados")
        for lis in listacategorias:
          print("\tId: ",lis.getId())
          print("\tNome: ",lis.getNome())
          print('\t')

      elif opcao == '10':
          id = int(input("digite um id "))
          nome = input("digite um nome ")

          listacategorias.append((Categoria(id, nome)))
          print("Cadastro Realizado com Sucesso !")

      elif opcao == '11':
        id = int(input("Digite um id \n"))
        for lis in listacategorias:
            if lis.getId == id:
              nome = input("digite um nome ")
              lis.setNome(nome)

      elif opcao == '12':
          id = int(input("Digite um id \n"))
      
          for lis in listacategorias:
              if lis.getId == id:
                listacategorias.remove(lis) 
                print("\t Realizado com Sucesso !")
 
      elif opcao == '0':
        application.Home()
      else:
        print("Opcao Invalida")
 