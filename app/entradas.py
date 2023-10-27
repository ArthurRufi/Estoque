from funcionalidades import DBDiario

class Entradas:

    def __init__(self, entradas):
        self.entradas = entradas


    def entregarvenda(self):
        p = DBDiario()
        vendedor = int(input('Insira o codigo do vendedor: '))
        valor = str(input('Insira o valor da venda: '))
        codven = int(input('Insira o codigo da venda:'))
        p.db_import(p.db_conect(), vendedor, valor, codven)
        #aqui deve entregar as informações ao banco de dados para conectar inserir no DB
                

    def get_infos(self, codigo):
        #retorna informações
        p = DBDiario()
        if p.db_export(p.db_conect(), codigo) == False:
            print('tabaco')


    def set_infos(self):
        p = DBDiario()
        p.db_import(p.db_conect())
        print ('ok')


    def conect_db():
        pass