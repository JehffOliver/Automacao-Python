import requests # type: ignore

def obter_planos(token):
    url = "https://graph.microsoft.com/v1.0/me/planner/plans"
    headers = {"Authorization": f"Bearer {token}"}

    resposta = requests.get(url, headers=headers)

    if resposta.status_code == 200:
        planos = resposta.json()["value"]
        for plano in planos:
            print(f"Nome: {plano['title']}, ID: {plano['id']}")
    else:
        print("Erro ao obter planos:", resposta.text)

# Chamar a função
token = "SEU_TOKEN_AQUI"
obter_planos(token)
