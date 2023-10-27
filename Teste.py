import pandas as pd

path= "C:\\araujo\\araujo.XLSX"
nomes_colunas = ['CHAPA', 'NOME', 'VALOR', 'NROVIAGENS', 'CODSITUACAO', 'DESCRICAO']
# contador_funcionario_limite = 0
# contador_funcionario_normal = 0
def ler_arquivo(path):
    df = pd.read_excel(path)
    return df
def menu():
    caminho = input('Digite o caminho do arquivo: [C:\\pasta_exemplo\\arquivo_exemplo.xlsm]\n')
    opc = input(
                '\nDigite sua opção:'
                '\n1-CALCULAR PASSAGEM'
                '\n2-CALCULA QUANTIDADE FUNCIONÁRIO COM LIMITE EXCEDIDO OU NORMAL'
                '\n3-CALCULA N° VIAGEM'
                '\n4-CALCULA VALOR GASTO'
                '\n5-SAIR\n'
                )
def busca_funcionario(matricula):
    df = ler_arquivo(path)
    funcionario_buscado = df.query(f'CHAPA=="{matricula}"')
    return funcionario_buscado

def consulta_df():
    contador_funcionario_limite = 0
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
        # preco_passagem = preco_passagem.replace(',', '.')
        preco = float(preco_passagem)
        dias_trabalhados = 26
        total_num_viagem = qtde * dias_trabalhados
        limite_valor_mes = 100.00
        total_gasto_mes = total_num_viagem * preco_passagem
        if total_gasto_mes > limite_valor_mes:
            # print(f'VALOR LIMITE: R$ {limite_valor_mes}')
            # print(f'VALOR GASTO POR FUNCIONÁRIO: R$ {format(total_gasto_mes, ".2f")}')
            # print(f'O limite do valor gasto por mês foi ultrapassado, portanto, funcionário(a) {nome_funcionario} é recomendando mudar de loja!')
            contador_funcionario_limite += 1
        else:
            # print(f'O limite não foi ultrapassado, portanto, funcionário(a) {nome_funcionario} não precisará mudar de loja!')
            contador_funcionario_normal += 1

if __name__ == "__main__":
    menu()
