
from application.model.entity.emprestimo import Emprestimo

class EmprestimoDao:

    def ListarEmprestimos():

        CadastroEmprestimos= [
          Emprestimo(id=1, idLivro=1, idUsuario=1, datainit='27/03/2022', datadev='25/04/2022', devolvido='s',reservado='s', encerrado='s'),
          Emprestimo(id=2, idLivro=2, idUsuario=1, datainit='27/03/2022', datadev='25/04/2022', devolvido='n', reservado='n',encerrado='n'),
          Emprestimo(id=3, idLivro=3, idUsuario=1, datainit='17/03/2022', datadev='25/04/2022', devolvido='s', reservado='s',encerrado='s'),

        ]

        return CadastroEmprestimos

