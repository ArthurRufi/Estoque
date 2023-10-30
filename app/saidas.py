from funcionalidades import DBDiario

class Saidas:
    
    def __init__(self) -> None:
        self.saida = float


    def consultar_saidas(self):
        f = DBDiario()
        f.db_export(f.db_conect(), 2)


    def adicionar_saida(self, codvendedor, valortotal, razaodasaida):

        p = DBDiario()
        p.db_import(p.db_conect(), razaodasaida, valortotal, codvendedor, entradasaida=2)
        #aqui deve entregar as informações ao banco de dados para conectar inserir no DB