

from application.controller.bibliotecario import Biblioteca
from application.controller.gerente import Gerente
from application.controller.menu import Menus
from application.controller.usuario import Usuario
from application.controller.funcionario import Funcionario

def Home():

  while True:
      
    M = Menus
    M.Menu()
    opcao = input("Digite uma opcao \n")
    if opcao == '1':
        Usuario.consultarLivros()
        
    elif opcao == '2':
      Biblioteca.Bibliotecario()

    elif opcao == '3':
        Gerente.Gerenciar()

    elif opcao == '4':
      Funcionario.Administrar()

    elif opcao == '0':
      break
    else: 
      M.Menu()
      print("Digite uma opcao válida !")
    break
Home()