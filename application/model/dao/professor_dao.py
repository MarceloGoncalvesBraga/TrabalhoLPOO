
from application.model.entity.professor import Professor

class Professor_Dao:

    def ListarProfessores():

        CadastroProfessores= [
          Professor(id=1, nome="Erika", matricula=20211054),
          Professor(id=2, nome="Joana", matricula=201810547),
          Professor(id=3, nome="Patricia", matricula=201910249),
          Professor(id=4, nome="Ana elisa", matricula=20211054),
          Professor(id=5, nome="Kamila Evelin", matricula=201810547),
          Professor(id=6, nome="Samira Avelar", matricula=201656569),
          Professor(id=7, nome="Jussara", matricula=201587894),
          Professor(id=8, nome="Suelen", matricula=2018565),
          Professor(id=9, nome="Renata", matricula=20139595)
        ]

        return CadastroProfessores

