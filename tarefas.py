import pandas as pd # type: ignore

def ler_planilha(arquivo="Testes Automação/Farmácias - Aberturas.xlsx"):
    df = pd.read_excel(arquivo)

    # Exibir os primeiros registros para verificar os dados
    print(df.head())

    return df

# Teste: Ler e exibir os dados
df_tarefas = ler_planilha()
