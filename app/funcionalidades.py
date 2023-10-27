import psycopg2
from dbinfos import cod
class DBDiario:
    def __init__(self):
        pass

    
    def db_create(self):
        #NUNCA DEVE SER CHAMADO FORA DESSE MODULO
        pass


    def db_conect(self):
        # Parâmetros de conexão
        dbname = cod(1)
        user = cod(2)
        password = cod(3)
        host = cod(4)  # ou o host do seu banco de dados
        port = cod(5)       # ou a porta do seu banco de dados

        # Conecte-se ao PostgreSQL
        try:
            conn = psycopg2.connect(dbname= dbname, user=user, password=password, host=host, port=port)
            return conn
        except:
            return False


    def db_import(self, conn, codigo, valor, vendedor):
        #aqui vai importar informações ao db
        cur = conn.cursor()
        cur.execute(f"INSERT INTO entradas (codigo, preço, vendedor) VALUES({codigo}, {valor}, {vendedor});")
        conn.commit()
        # Feche o cursor e a conexão quando terminar
        cur.close()
        conn.close()


    def db_export(self, conn, codselect):
        #codselect Recebe um codigo retornado que vai definir que tipo de exportação tratada vai receber
        #aqui vai exportar as informações do db
        cur = conn.cursor()
        if conn == False:
            print('fudeu')
        elif codselect == 1234 and conn != False:
            print('cod 1234 ok!')
            cur = conn.cursor()
            cur.execute("SELECT * FROM entradas;")
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


    def db_delete(self, conn, codselect):
        
        if codselect == 1 and conn != False:
            pass
        elif codselect == 2 and conn !=False:
            pass

class DBnotas:
    def __init__(self) -> None:
        pass