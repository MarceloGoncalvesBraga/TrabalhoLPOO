
from datetime import date, datetime
from statistics import mode
import locale,application

try:
  locale.setlocale(locale.LC_TIME, locale.normalize('pt_BR.utf8'))
except locale.Error:
  print('Instale o módulo de linguagem adequado no seu Sistema Operacional.')

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

class Gerente:

  def Gerenciar():
    listamprestimos = EmprestimoDao.ListarEmprestimos()
    listaexemplares = ExemplarDao.ListarExemplares()
    listacategorias = CategoriaDao.ListarCategorias()
    listalivros = LivrosDao.ListarLivros()
    listausuarios = UsuarioDao.ListarUsuarios()
    while True:

      print("""\t 
        -----------------------------------------
              BIBLIOTECA       GERENCIA       
        ----------------------------------------- 
        1- Relatório de todos os livros e o número de exemplares cadastrados
        2- Relatório de todos os livros emprestados.
        3- Relatório de todos os livros reservados.
        4- Relatório de todos os usuários e seus respectivos dados cadastrais.
        5- Relatório de todos os livros em atraso a devolução.
        _________________________________________
        0- Sair 

        """)
      opcao = input("Digite uma opcao \n")
      if opcao == '1':
        print("\tLista de Livros Cadastrados")
        for lis in listalivros:
          print("\tTitulo:  ",lis.getTitulo())
          print("\tN° Isbn: ",lis.getIsbn())
          print("\tAutor: ",  lis.getAutor())
          print("\tEditora: ",lis.getEditora())
          print("\tAno:     ",lis.getAno())
          for ass in listacategorias:
            if ass.getId() == lis.getAssunto():
               print("\tAssunto: ",ass.getNome())
          
        print("\tLista de Exemplares Cadastrados")
        for lis in listaexemplares:
          print("\tNome::  ",lis.getNome())
          print("\tQuantidade: ",lis.getQuantidade())

      if opcao == '2':
        for listamprestimo in listamprestimos:
          for lis in listalivros:
           if lis.getId() == listamprestimo.getId() and listamprestimo.getDevolvido() == 'n':
              print("\tLista de Livros Emprestados")

              print("\tTitulo:  ",lis.getTitulo())
              print("\tN° Isbn: ",lis.getIsbn())
              print("\tAutor: ",  lis.getAutor())
              print("\tEditora: ",lis.getEditora())
              print("\tAno:     ",lis.getAno())
              for ass in listacategorias:
                if ass.getId() == lis.getAssunto():
                  print("\tAssunto: ",ass.getNome())

      if opcao == '3':
        for listamprestimo in listamprestimos:
          for lis in listalivros:
           if lis.getId() == listamprestimo.getId() and listamprestimo.getReservado() == 's':
              print("\tLista de Livros Emprestados")

              print("\tTitulo:  ",lis.getTitulo())
              print("\tN° Isbn: ",lis.getIsbn())
              print("\tAutor: ",  lis.getAutor())
              print("\tEditora: ",lis.getEditora())
              print("\tAno:     ",lis.getAno())
              for ass in listacategorias:
                if ass.getId() == lis.getAssunto():
                  print("\tAssunto: ",ass.getNome())

      if opcao == '4':
        for user in listausuarios:
          print("Nome: ",user.getNome())
          print("Matricula:", user.getMatricula())
      if opcao == '5':
        for listamprestimo in listamprestimos:
          for lis in listalivros:
      
            if lis.getId() == listamprestimo.getId() and listamprestimo.getDevolvido() == 'n':
              print("\tLista de Livros Emprestados e nao Devolvidos")

              print("\tTitulo:  ",lis.getTitulo())
              print("\tN° Isbn: ",lis.getIsbn())
              print("\tAutor: ",  lis.getAutor())
              print("\tEditora: ",lis.getEditora())
              print("\tAno:     ",lis.getAno())
              for ass in listacategorias:
                if ass.getId() == lis.getAssunto():
                  print("\tAssunto: ",ass.getNome())
          
      elif opcao == '0':
        application.Home()
      else:
        print("Opcao Invalida")
