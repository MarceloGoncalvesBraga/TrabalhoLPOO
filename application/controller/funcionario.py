
import datetime
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
    listaemprestimos = EmprestimoDao.ListarEmprestimos()
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

      opcao = input("\t Digite uma opcao \t")
      if opcao == '1':
        titulo = input("\t Titulo do Livro \t")
  
        for lis in listalivros:
          if lis.getTitulo() == titulo:
              if lis.getStatus() == 1:
                print("\t Livro Indisponivel \t ")
                break
              for listaemprestimo in listaemprestimos:
                if lis.getId() == listaemprestimo.getId() and listaemprestimo.getDevolvido == 'n':
                  print("\t Livro Indisponivel \t ")
                  break 
              print("\tTitulo:  ",lis.getTitulo())
              print("\tN° Isbn: ",lis.getIsbn())
              print("\tAutor: ",  lis.getAutor())
              print("\tEditora: ",lis.getEditora())
              print("\tAno:     ",lis.getAno())
              for ass in listacategorias:
                if ass.getId() == lis.getAssunto():
                  print("\tAssunto: ",ass.getNome())
                  
              lis.setStatus(1)
              ide = int(input("\t Digite id  \t"))
              idliv = int(input("\t Digite id do livro \t"))
              idusuario = int(input("\t Digite seu id de usuario \t"))
              datadevo = input("\t Digite a data de devolucao 00/00/0000 \t")
              #for l in listaemprestimos:
              #listaemprestimos.append(Emprestimo(id=ids, idLivro=lis.getId(),idUsuario=idusuario,datainit=dat, datadev=datadevo, devolvido='n',reservado='s', encerrado='n'))
              #listaemprestimos.append((Emprestimo(id=5, idLivro=6, idUsuario=2, datainit='17/03/2022', datadev='25/07/2022', devolvido='n', reservado='s',encerrado='n')))
              listaemprestimos.append(Emprestimo(id=4, idLivro=6, idUsuario=2, datainit='17/03/2022', datadev='25/07/2022', devolvido='n', reservado='s',encerrado='n'),)
              listaemprestimos.append(Emprestimo(id=11, idLivro=idliv, idUsuario=idusuario, datainit='17/03/2022', datadev='25/07/2022', devolvido='n', reservado='s',encerrado='n'))

              print("\t ------------------------------")
              print("\t\t Livro Reservado")
              print("\t ------------------------------")
              for listaemprestimo in listaemprestimos:
                for lis in listalivros:
                  if lis.getId() == listaemprestimo.getidLivro() and lis.getStatus() == 0 and listaemprestimo.getDevolvido() == 'n':
                    print("\t--------------------------")
                    print("\tId:      ",lis.getId())
                    print("\tTitulo:  ",lis.getTitulo())
                    print("\tN° Isbn: ",lis.getIsbn())
                    print("\tAutor:   ",  lis.getAutor())
                    print("\tEditora: ",lis.getEditora())
                    print("\tAno:     ",lis.getAno())
                    for ass in listacategorias:
                      if ass.getId() == lis.getAssunto():
                        print("\tAssunto: ",ass.getNome())
              break
     
      elif opcao == '2':
              print("\t Lista de Livros Emprestados ")
              for listaemprestimo in listaemprestimos:
                for lis in listalivros:
                  if lis.getId() == listaemprestimo.getidLivro() and lis.getStatus() == 0 and listaemprestimo.getDevolvido() == 'n':
                    print("\t--------------------------")
                    print("\tId:      ",lis.getId())
                    print("\tTitulo:  ",lis.getTitulo())
                    print("\tN° Isbn: ",lis.getIsbn())
                    print("\tAutor:   ",  lis.getAutor())
                    print("\tEditora: ",lis.getEditora())
                    print("\tAno:     ",lis.getAno())
                    for ass in listacategorias:
                      if ass.getId() == lis.getAssunto():
                        print("\tAssunto: ",ass.getNome())
      
      elif opcao == '3':
        
        id = int(input("\t id da Reserva do Livro \t"))
        for lis in listaemprestimos:
           if lis.getId() == id:
              lis.setDevolvido('s')
              print("\t Devolucao Feita \n")
              
        
      elif opcao == '4':
        for lis in listausuarios:
          print("\t Nome:  ",lis.getNome())
          print("\tN° Matricula: ",lis.getMatricula())
          print('\t-------------------------------')
          
      elif opcao == '5':
          id = input("\tdigite um id \t ")
          nome = input("\tdigite um Nome \t")
          matricula = input("\tdigite uma Matricula \t")

          listausuarios.append((Usuario(id=id, nome=nome, matricula=matricula)))
          print("\tCadastro Realizado \n")
          
      elif opcao == '6': 
        for lis in listaprofessores:
          print("\t Nome:  ",lis.getNome())
          print("\tN° Matricula: ",lis.getMatricula())
          print('\t-------------------------------')

      elif opcao == '7':
          id = input("\tdigite um id \t")
          nome = input("\tdigite um Nome \t")
          matricula = input("\tdigite uma Matricula \t")

          listaprofessores.append((Professor(id=id, nome=nome, matricula=matricula)))
          print("\tCadastro Realizado")
      
      elif opcao == '0':
        application.Home()
      else:
        print("\t Opcao Invalida ")

