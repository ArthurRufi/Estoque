from funcionalidades import DBDiario

class Saidas:
    
    def __init__(self) -> None:
        self.saida = float


    def consultar_saidas(self):
        f = DBDiario()
        f.db_export(f.db_conect(), 2)


    def adicionar_saida(self):

        p = DBDiario()
        vendedor = int(input('Insira o codigo do funcionario: '))
        valor = str(input('Insira o valor da saida: '))
        codven = str(input('Insira a razao da venda:'))
        p.db_import(p.db_conect(), codven, valor, vendedor, entradasaida=2)
        #aqui deve entregar as informações ao banco de dados para conectar inserir no DB