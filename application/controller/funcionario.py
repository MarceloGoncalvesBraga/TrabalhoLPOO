
from datetime import datetime,date
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
import application
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
        1- Novo Emprestimo

        2- Listar Emprestimo
        
        3- Devolucao Emprestimo 

        4- Listar Usuarios
        
        5- Cadastrar Novo Usuario
         
        6- Listar Professores

        7- Cadastrar Novo Professor 

        0- Sair
        _____________________________________

        """)

      opcao = input("\t tDigite uma opcao \n")
      if opcao == '1':
        
        titulo = input("\t Titulo do Livro \n")
        for lis in listalivros:
          if lis.getTitulo() == titulo:
              if lis.getStatus() == 1:
                print("\t Livro Indisponivel\n ")
                break
              print("Titulo:  ",lis.getTitulo())
              print("N° Isbn: ",lis.getIsbn())
              print("Autor: ",  lis.getAutor())
              print("Editora: ",lis.getEditora())
              print("Ano:     ",lis.getAno())
              for ass in listacategorias:
                if ass.getId() == lis.getAssunto():
                  print("\tAssunto: ",ass.getNome())
              idusuario = input("\t Digite seu id de usuario \t")
              datadevo = input("\t Digite a data de devolucao \t")

              for l in listamprestimos:
                  listamprestimos.append((Emprestimo(id=lis.getId()+1000, idLivro=lis.getId(),idUsuario=idusuario,datainit=datetime, datadev=datadevo, devolvido='n',reservado='s', encerrado='n')))
                  print("\t Livro Reservado")
     
      if opcao == '2':
              for listamprestimo in listamprestimos:
                for lis in listalivros:
                  if lis.getId() == listamprestimo.getId() and listamprestimo.getDevolvido() == 'n':
                    print("\t Lista de Livros Emprestados ")

                    print("\tTitulo:  ",lis.getTitulo())
                    print("\tN° Isbn: ",lis.getIsbn())
                    print("\tAutor: ",  lis.getAutor())
                    print("\tEditora: ",lis.getEditora())
                    print("\tAno:     ",lis.getAno())
                    for ass in listacategorias:
                      if ass.getId() == lis.getAssunto():
                        print("\tAssunto: ",ass.getNome())
      
      if opcao == '3':
        
        id = input("\t id da Reserva do Livro \t")
        for lis in listamprestimos:
           if lis.getId() == id:
              value = 's'
              lis.setDevolvido(value)
              print("\t Devolucao Feita \n")
              break
        
      if opcao == '4':
        for lis in listausuarios:
          print("\t Nome:  ",lis.getNome())
          print("\tN° Matricula: ",lis.getMatricula())
          print('-------------------------------')

      if opcao == '5':
          id = input("digite um id \t ")
          nome = input("digite um Nome \t")
          matricula = input("digite uma Matricula \t")

          listausuarios.append((Usuario(id=id, nome=nome, matricula=matricula)))
          print("Cadastro Realizado \n")

      if opcao == '6': 
        for lis in listaprofessores:
          print("\t Nome:  ",lis.getNome())
          print("\tN° Matricula: ",lis.getMatricula())
          print('-------------------------------')

      if opcao == '7':
          id = input("\tdigite um id \t")
          nome = input("\tdigite um Nome \t")
          matricula = input("\tdigite uma Matricula \t")

          listaprofessores.append((Professor(id=id, nome=nome, matricula=matricula)))
          print("\tCadastro Realizado")
      
      elif opcao == '0':
        application.Home()
      else:
        print("\t Opcao Invalida\t")

