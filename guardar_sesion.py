from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    navegador = p.chromium.launch(headless=False)
    contexto = navegador.new_context()
    pagina = contexto.new_page()
    pagina.goto("https://www.instagram.com/accounts/login/")
    input("Inicia sesión con la cuenta TEMPORAL y presiona ENTER aquí cuando veas el inicio de Instagram...")
    contexto.storage_state(path="sesion.json")
    navegador.close()