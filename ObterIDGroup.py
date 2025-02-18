import token
from urllib import request


def obter_membros_do_plano(token, plan_id):
    url = f"https://graph.microsoft.com/v1.0/planner/plans/{plan_id}/buckets"
    headers = {"Authorization": f"Bearer {token}"}

    resposta = request.get(url, headers=headers)

    if resposta.status_code == 200:
        grupos = resposta.json()["value"]
        for grupo in grupos:
            print(f"Nome do Grupo: {grupo['name']}, ID: {grupo['id']}")
    else:
        print("Erro ao obter membros:", resposta.text)

# Teste: Obter membros do plano
plan_id = "ID_DO_PLANO_AQUI"
obter_membros_do_plano(token, plan_id)
