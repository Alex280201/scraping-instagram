"""Utilidades compartidas para abrir Instagram con la sesión guardada."""
import os
import sys

ARCHIVO_SESION = "sesion.json"


def lanzar_navegador(p):
    """Usa Google Chrome real si está instalado (Instagram lo detecta menos
    como automatización); si no, usa el Chromium de Playwright."""
    opciones = dict(
        headless=False,
        ignore_default_args=["--enable-automation"],
        args=["--disable-blink-features=AutomationControlled"],
    )
    try:
        return p.chromium.launch(channel="chrome", **opciones)
    except Exception:
        return p.chromium.launch(**opciones)


def sesion_activa(contexto):
    """True si el contexto tiene una cookie de sesión de Instagram."""
    return any(c["name"] == "sessionid" and c["value"] for c in contexto.cookies())


def abrir_con_sesion(p):
    """Devuelve (navegador, contexto, pagina) ya logueado.
    Si la sesión no existe o caducó, avisa y termina el programa."""
    if not os.path.exists(ARCHIVO_SESION):
        sys.exit("No existe sesion.json. Ejecuta primero:  python guardar_sesion.py")

    navegador = lanzar_navegador(p)
    contexto = navegador.new_context(storage_state=ARCHIVO_SESION)
    pagina = contexto.new_page()
    pagina.goto("https://www.instagram.com/")
    pagina.wait_for_timeout(3000)

    if "/accounts/login" in pagina.url or not sesion_activa(contexto):
        navegador.close()
        sys.exit(
            "La sesión de Instagram caducó o fue cerrada.\n"
            "Vuelve a iniciar sesión con:  python guardar_sesion.py"
        )
    return navegador, contexto, pagina
