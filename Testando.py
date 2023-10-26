import pandas as pd

path= "C:\\araujo\\araujo_csv.csv"
nomes_colunas = ['CHAPA', 'NOME', 'VALOR', 'NROVIAGENS', 'CODSITUACAO', 'DESCRICAO']

def ler_arquivo(path):
    df = pd.read_csv(path, sep=";")
    return df

def busca_funcionario(matricula):
    df = ler_arquivo(path)
    funcionario_buscado = df.query(f'CHAPA=="{matricula}"')
    return funcionario_buscado

def valida_funcionario_limite():
    contador_funcionario_limite = 0

    df = ler_arquivo(path)
    df_nao_duplicada = df.drop_duplicates('CHAPA')
    tam_df = len(df_nao_duplicada)

    for i in range(tam_df):
        qtde = 0
        if 0 <= i < len(df_nao_duplicada):
            chapa = df_nao_duplicada['CHAPA'].iloc[i]
        funcionario_buscado = df.query(f'CHAPA=="{chapa}"')

        tam = len(funcionario_buscado)

        for i in range(tam):
            casting = funcionario_buscado.query('NROVIAGENS!="0"')["NROVIAGENS"].mean()
            qtde = qtde + casting
        nome_funcionario = funcionario_buscado['NOME'].iloc[0]

        nmr_viagens_diaria = funcionario_buscado['NROVIAGENS'].iloc[0]
        preco_passagem = funcionario_buscado['VALOR'].iloc[0]
        preco_passagem = preco_passagem.replace(',', '.')
        preco = float(preco_passagem)
        dias_trabalhados = 26
        total_num_viagem = qtde * dias_trabalhados
        limite_valor_mes = 350.00
        total_gasto_mes = total_num_viagem * preco
        if total_gasto_mes > limite_valor_mes:
            contador_funcionario_limite += 1

    return contador_funcionario_limite

def valida_funcionario_normal():
    contador_funcionario_normal = 0

    df = ler_arquivo(path)
    df_nao_duplicada = df.drop_duplicates('CHAPA')
    tam_df = len(df_nao_duplicada)

    for i in range(tam_df):
        qtde = 0
        if 0 <= i < len(df_nao_duplicada):
            chapa = df_nao_duplicada['CHAPA'].iloc[i]
        funcionario_buscado = df.query(f'CHAPA=="{chapa}"')

        tam = len(funcionario_buscado)

        for i in range(tam):
            casting = funcionario_buscado.query('NROVIAGENS!="0"')["NROVIAGENS"].mean()
            qtde = qtde + casting
        nome_funcionario = funcionario_buscado['NOME'].iloc[0]

        nmr_viagens_diaria = funcionario_buscado['NROVIAGENS'].iloc[0]
        preco_passagem = funcionario_buscado['VALOR'].iloc[0]
        preco_passagem = preco_passagem.replace(',', '.')
        preco = float(preco_passagem)
        dias_trabalhados = 26
        total_num_viagem = qtde * dias_trabalhados
        limite_valor_mes = 350.00
        total_gasto_mes = total_num_viagem * preco
        if total_gasto_mes < limite_valor_mes:
            contador_funcionario_normal += 1
    return contador_funcionario_normal

if __name__ == "__main__":
    print(valida_funcionario_limite())
    print(valida_funcionario_normal())