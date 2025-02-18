import msal # type: ignore
import webbrowser

CLIENT_ID = "339e52e5-92f4-470a-8568-daedfbfec205"  # ID público da Microsoft
TENANT_ID = "common"

AUTHORITY = f"https://login.microsoftonline.com/{TENANT_ID}"
SCOPE = ["https://graph.microsoft.com/.default"]

def obter_token():
    app = msal.PublicClientApplication(CLIENT_ID, authority=AUTHORITY)

    # Abre o navegador manualmente para o login
    token = app.acquire_token_interactive(scopes=SCOPE, open_browser=True)

    return token["access_token"]

# Teste de autenticação
token = obter_token()
print("Token obtido:", token[:50], "...")

