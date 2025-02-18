from urllib import request


def criar_tarefa(token, plan_id, titulo, descricao, prazo, bucket_id, etiquetas, progresso):
    url = "https://graph.microsoft.com/v1.0/planner/tasks"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    dados = {
        "planId": plan_id,
        "title": titulo,
        "dueDateTime": f"{prazo}T23:59:00Z",  # Formato ISO 8601
        "bucketId": bucket_id,
        "priority": "Medium",
        "percentComplete": 100 if progresso == "Encerrado" else 0,  # Define progresso
        "assignments": {
            "ID_JEFFERSON": {"@odata.type": "microsoft.graph.plannerAssignment"},
            "ID_ROGERIO": {"@odata.type": "microsoft.graph.plannerAssignment"}
        }
    }

    resposta = request.post(url, json=dados, headers=headers)

    if resposta.status_code == 201:
        print(f"Tarefa '{titulo}' criada com sucesso!")
    else:
        print("Erro ao criar tarefa:", resposta.text)
