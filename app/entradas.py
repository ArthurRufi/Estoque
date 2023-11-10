from funcionalidades import DBDiario

class Entradas:

    def __init__(self, entradas):
        self.entradas = entradas


    def entregarvenda(self, codvendedor, valorvenda, codigodavenda):
        p = DBDiario()
        p.db_import(p.db_conect(), codvendedor, valorvenda, codigodavenda, entradasaida=1)
        #aqui deve entregar as informações ao banco de dados para conectar inserir no DB
        #!!!INSERIR TIPO DO PAGAMENTO
                

    def get_infos(self, codigo):
        #retorna informações
        p = DBDiario()
        if p.db_export(p.db_conect(), codigo) == False:
            #adicionar logs para registro de atividades
            print('tabaco')
            return False
        

    def set_infos(self):
        p = DBDiario()
        p.db_import(p.db_conect())
        print ('ok')


    def delete_venda(self, cod, codvenda):
        #trocar para status de venda

        p = DBDiario()
        p.db_delete(p.db_conect(), cod, codvenda)