import psycopg2
from ocultados.dbinfos import dbnames,users,passwords,hosts,ports

class DBDiario:
    def __init__(self):
        pass

    
    def db_create(self):
        #NUNCA DEVE SER CHAMADO FORA DESSE MODULO
        pass


    def db_conect(self):
        # Parâmetros de conexão
        dbname = dbnames
        user = users
        password = passwords
        host = hosts  # ou o host do seu banco de dados
        port = ports       # ou a porta do seu banco de dados

        # Conecte-se ao PostgreSQL
        try:
            conn = psycopg2.connect(dbname= dbname, user=user, password=password, host=host, port=port)
            return conn
        except:
            return False


    def db_import(self, venda):
        #aqui vai importar informações ao db
        for chave, valor in venda.items():
            print (f'{chave} adicionado ao DB com valor {valor}')
            #adicionar interação com DB


    def db_export(self, conn, codselect):
        #codselect Recebe um codigo retornado que vai definir que tipo de exportação tratada vai receber
        #aqui vai exportar as informações do db
        cur = conn.cursor()
        if conn == False:
            print('fuder')
        elif codselect == 1234 and conn != False:
            print('cod 1234 ok!')
            cur = conn.cursor()
            cur.execute("SELECT * FROM entradas WHERE vendedor = 2134;")
            rows = cur.fetchall()
            a = []
            # Imprima os resultados
            for row in rows:
                print(f'id: {row[0]} | venda: {row[1]} | total: {row[2]} | vendedor: {row[3]}')
        
            # Feche o cursor e a conexão quando terminar
            cur.close()
            conn.close()

        else:
            cur = conn.cursor()
            cur.execute("SELECT * FROM entradas WHERE vendedor = 2132;")
            rows = cur.fetchall()
            a = []
            # Imprima os resultados
            for row in rows:
                print(f'id: {row[0]} | venda: {row[1]} | total: {row[2]} | vendedor: {row[3]}')
        
            # Feche o cursor e a conexão quando terminar
            cur.close()
            conn.close()


class DBnotas:
    def __init__(self) -> None:
        pass