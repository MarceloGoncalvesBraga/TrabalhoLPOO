
from datetime import datetime
from statistics import mode
from unittest import mock

from click import DateTime
from psycopg2 import Date
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

from application.model.dao.professor_dao import Professor_Dao
from application.model.entity.professor import Professor

class Funcionario:

  def Administrar():
    listamprestimos = EmprestimoDao.ListarEmprestimos()
    listaexemplares = ExemplarDao.ListarExemplares()
    listacategorias = CategoriaDao.ListarCategorias()
    listalivros = LivrosDao.ListarLivros()
    listausuarios = UsuarioDao.ListarUsuarios()
    listaprofessores = Professor_Dao.ListarProfessores()
    while True:
      print("""\t 
        -------------------------------------
              BIBLIOTECA     FUNCIONARIO       
        ------------------------------------- 
        1- Controlar Novo Emprestimo

        2- Controlar Devolucao Emprestimo 

        3- Listar Usuarios

        4- Cadastrar Novo Professor 

        0- Sair
        _____________________________________

        """)

      opcao = input("\tDigite uma opcao \n")
      if opcao == '1':
        
        titulo = input("Titulo do Livro")
        for lis in listalivros:
          if lis.getTitulo() == titulo:
              if lis.getStatus() == 1:
                print("Livro Indisponivel")
                break
              print("Titulo:  ",lis.getTitulo())
              print("N° Isbn: ",lis.getIsbn())
              print("Autor: ",  lis.getAutor())
              print("Editora: ",lis.getEditora())
              print("Ano:     ",lis.getAno())
              for ass in listacategorias:
                if ass.getId() == lis.getAssunto():
                  print("\tAssunto: ",ass.getNome())
              idusuario = input("Digite seu id de usuario")
              datadevo = input("Digite a data de devolucao")

              for l in listamprestimos:
                  listamprestimos.append((Emprestimo(id=lis.getId()+1000, idLivro=lis.getId(),idUsuario=idusuario,datainit=datetime, datadev=datadevo, devolvido='n',reservado='s', encerrado='n')))
                  print("Livro Reservado")

      if opcao == '2':
        
        id = input("id da Reserva do Livro")
        for lis in listamprestimos:
           if lis.getId() == id:
              value = 's'
              lis.setDevolvido(value)
              print("Devolucao Feita")
              break
        
      if opcao == '3':
        for lis in listausuarios:
          print("\t Nome:  ",lis.getNome())
          print("\tN° Matricula: ",lis.getMatricula())
          print('-------------------------------')

      if opcao == '4':
          id = input("digite um id ")
          nome = input("digite um Nome ")
          matricula = input("digite uma Matricula ")

          listausuarios.append((Usuario(id=id, nome=nome, matricula=matricula)))
          print("Cadastro Realizado")

      if opcao == '5': 
        for lis in listaprofessores:
          print("\t Nome:  ",lis.getNome())
          print("\tN° Matricula: ",lis.getMatricula())
          print('-------------------------------')

      if opcao == '6':
          id = input("digite um id ")
          nome = input("digite um Nome ")
          matricula = input("digite uma Matricula ")

          listaprofessores.append((Professor(id=id, nome=nome, matricula=matricula)))
          print("Cadastro Realizado")
      
      elif opcao == '0':
        break
      else:
        print("Opcao Invalida")

