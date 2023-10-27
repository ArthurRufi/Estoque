from funcionalidades import DBDiario

class Saidas:
    
    def __init__(self) -> None:
        self.saida = float


    def consultar (self):
        f = DBDiario()
        f.db_export(f.db_conect(), 1234)


    def entregar(self):
        pass