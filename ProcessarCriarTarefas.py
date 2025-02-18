import token
from turtle import pd

from CriarTarefas import criar_tarefa


def processar_planilha(token, plan_id, bucket_ids, arquivo="tarefas.xlsx"):
    df = pd.read_excel(arquivo)

    for _, linha in df.iterrows():
        titulo = f"{linha['JAVA']} / {linha['Codigo Histórico']} - {linha['Farmacia']}"
        descricao = f"{linha['Bandeira']}\n{linha['IP']}"
        prazo = linha["Data Coleta"]
        progresso = "Encerrado" if linha["Status Configuração"] == "OK" else "Em Progresso"
        bucket_id = bucket_ids.get(f"{prazo:%B %Y}", "ID_BUCKET_PADRAO")  # Bucket baseado no mês/ano
        etiquetas = [linha["Bandeira"], f"{prazo:%B}"]  # Bandeira e Mês

        criar_tarefa(token, plan_id, titulo, descricao, prazo, bucket_id, etiquetas, progresso)

# Mapeamento de Buckets
bucket_ids = {
    "Fevereiro 2025": "ID_DO_BUCKET_AQUI",
    "Março 2025": "ID_OUTRO_BUCKET",
    # Adicione mais conforme necessário
}

# Executar o processo
processar_planilha(token, "ID_DO_PLANO_AQUI", bucket_ids)
