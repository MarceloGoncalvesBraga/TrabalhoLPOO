
from application.model.entity.usuario import Usuario

class UsuarioDao:

    def ListarUsuarios():

        CadastroUsuarios= [
          Usuario(id=1, nome="Erika", matricula=20211054),
          Usuario(id=2, nome="Joana", matricula=201810547),
          Usuario(id=3, nome="Patricia", matricula=201910249),
          Usuario(id=4, nome="Marcelo", matricula=20218954),
          Usuario(id=5, nome="Pedro", matricula=201810477),
          Usuario(id=6, nome="Leticia", matricula=201915249)
        ]

        return CadastroUsuarios

