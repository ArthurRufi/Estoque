import psycopg2
from dbinfos import cod
import datetime

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


    def db_import(self, conn, *args, entradasaida):
        #aqui vai importar informações ao db
        cur = conn.cursor()
        
        if entradasaida == 1:
            #insere as informações na tabela entradas
            cur.execute(f"INSERT INTO entradas (codigo, preço, vendedor) VALUES({args[0]}, '{args[1]}', {int(args[2])});")
            #começar a tratar erros


        elif entradasaida == 2:
            #insere as informações na tabela saidas
            dataautal = datetime.datetime.now()
            dataformatada = dataautal.strftime("%Y-%m-%d | %H:%M:%S")
            cur.execute(f"INSERT INTO saidas (razao, valor, dataatual, idfuncionario) VALUES('{args[0]}', {args[1]}, '{dataformatada}', {int(args[2])});")
            #começar a tratar erros
            
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
                #adicionar isso em um dicionario para usar mais tarde
                print(f'id: {row[0]} | venda: {row[1]} | total: {row[2]} | vendedor: {row[3]}')
        
        elif codselect == 2 and conn != False:
            print('cod 2 ok!')
            cur = conn.cursor()
            cur.execute("SELECT * FROM saidas;")
            rows = cur.fetchall()
            a = []
            # Imprima os resultados
            for row in rows:
                print(row)

        elif codselect == 3 and conn !=False:
            cur = conn.cursor()
            cur.execute()
        
        else:
            cur = conn.cursor()
            cur.execute("SELECT * FROM entradas WHERE vendedor = 2132;")
            rows = cur.fetchall()
            a = []
            # Imprima os resultados
            for row in rows:
                print(f'id: {row[0]} | venda: {row[1]} | total: {row[2]} | vendedor: {row[3]}')
        
        cur.close()
        conn.close() 
            


    def db_delete(self, conn, codselect, delcod):
        #organizar opções
        if codselect == 1 and conn != False:
            #deletar com codigo de entrada
            #mudar essa opção para outra coisa como status da venda
            cur = conn.cursor()
            cur.execute (f"DELETE FROM entradas WHERE codigo = '{delcod}';")
            conn.commit()
            cur.close()
            conn.close()
        
        elif codselect == 2 and conn !=False:
            pass
        # adicionar tratamento de erros para conferir se o arquivo foi excluido



class DBnotas:
    def __init__(self) -> None:
        pass