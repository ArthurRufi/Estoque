from funcionalidades import DBDiario

class Entradas:

    def __init__(self, entradas):
        self.entradas = entradas


    def entregarvenda(self, venda, total):
        p = DBDiario()
        # dic = dict(zip(venda, total))
        dic = {}
        for x in range (len(venda)):
            vendas = venda[x]
            totais = total[x]
            dic[vendas] = totais
        print (dic)
        p.db_import(dic)
        #aqui deve entregar as informações ao banco de dados para conectar inserir no DB
                

    def get_infos(self, codigo):
        #retorna informações
        p = DBDiario()
        if p.db_export(p.db_conect(), codigo) == False:
            print('tabaco')


    def set_infos():
        #altera informaçoes ou adiciona
        pass


    def conect_db():
        pass