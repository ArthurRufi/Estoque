import psycopg2


class DBDiario:
    def __init__(self):
        pass

    
    def db_create(self):
        pass


    def db_conect(self):
        # Parâmetros de conexão
        dbname = "sistemagestao"
        user = "arthur"
        password = "86128931"
        host = "localhost"  # ou o host do seu banco de dados
        port = "5432"       # ou a porta do seu banco de dados

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


    def db_export(self, conn):
        #aqui vai exportar as informações do db
        if conn == False:
            print('fuder')
        else:
            cur = conn.cursor()
            cur.execute("SELECT * FROM entradas WHERE vendedor = 2132;")
            rows = cur.fetchall()
            a = []
            # Imprima os resultados
            for row in rows:
                print(f'id: {row[0]} | venda: {row[1]} | preço: {row[2]} | vendendor: {row[3]}')
        
            # Feche o cursor e a conexão quando terminar
            cur.close()
            conn.close()


class DBnotas:
    def __init__(self) -> None:
        pass