import pandas as pd

path= "C:\\araujo\\araujo.XLSX"
nomes_colunas = ['CHAPA', 'NOME', 'VALOR', 'NROVIAGENS', 'CODSITUACAO', 'DESCRICAO']
# contador_funcionario_limite = 0
# contador_funcionario_normal = 0
def ler_arquivo(path):
    df = pd.read_excel(path)
    return df
def busca_funcionario(matricula):
    df = ler_arquivo(path)
    funcionario_buscado = df.query(f'CHAPA=="{matricula}"')
    return funcionario_buscado

def consulta_df():
    contador_funcionario_limite = 0
    contador_funcionario_normal = 0
    df = ler_arquivo(path)

    # REMOVE DUPLICIDADE DE ACORDO COM PARAMETRO CHAPA
    df_nao_duplicada = df.drop_duplicates('CHAPA')
    tam_df = len(df_nao_duplicada)

    for j in range(tam_df):
        nr_viagens = 0
        total_passagem = 0.0
        if 0 <= j < len(df_nao_duplicada):
            chapa = df_nao_duplicada['CHAPA'].iloc[j]
            funcionario_buscado = df.query(f'CHAPA=="{chapa}"')

        tam = len(funcionario_buscado)

        # SOMA QUANTIDADE DE NUMERO DE VIAGENS DIARIA POR FUNCIONARIO
        for i in range(tam):
            casting = funcionario_buscado['NROVIAGENS'].iloc[i]
            nr_viagens = nr_viagens + casting
        nome_funcionario = funcionario_buscado['NOME'].iloc[0]


        # ITERA SOBRE O FUNCIONARIO BUSCADO E SOMA O VALOR DAS PASSAGENS DE ACORDO COM A QUANTIDADE QUE CONTEM NO DATA-FRAME(FUNCIONARIO BUSCADO)
        for x in range(tam):
            vlr_passagem = funcionario_buscado["VALOR"].iloc[x]
            total_passagem = total_passagem + vlr_passagem

        dias_trabalhados = 26
        total_num_viagem = nr_viagens * dias_trabalhados
        limite_valor_mes = 100.00
        total_gasto = total_num_viagem * total_passagem

        limite_extrapolado = total_gasto > limite_valor_mes
        if limite_extrapolado:
            print(f'VALOR LIMITE: R$ {limite_valor_mes}')
            print(f'VALOR GASTO POR FUNCIONÁRIO: R$ {format(total_gasto, ".2f")}')
            print(f'O limite do valor gasto por mês foi ultrapassado, portanto, funcionário(a) {nome_funcionario} é recomendando mudar de loja!')
            contador_funcionario_limite += 1
        else:
            print(f'O limite não foi ultrapassado, portanto, funcionário(a) {nome_funcionario} não precisará mudar de loja!')
            contador_funcionario_normal += 1

if __name__ == "__main__":
    ler_arquivo(path)
    consulta_df()
