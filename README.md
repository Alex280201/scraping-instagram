Scraping de Instagram con Python

Descripción

Proyecto académico desarrollado en Python para recopilar y organizar información visible de perfiles y publicaciones de Instagram mediante automatización del navegador.

Tecnologías utilizadas

Python 3.11
Playwright
BeautifulSoup4
lxml
Git y GitHub

Funcionalidades

Guardar el estado de una sesión de navegador.
Consultar información de un perfil de Instagram.
Recopilar enlaces de publicaciones.
Extraer información disponible de publicaciones.
Exportar los resultados a archivos JSON y CSV.
Extraer la lista de seguidores y de seguidos, limpiarla y cruzarla (mutuos, quién no te sigue de vuelta).

Estructura del proyecto

scraping-instagram/
├── scraper.py
├── conexiones.py
├── sesion_util.py
├── guardar_sesion.py
├── depurar_datos.py
├── perfil.py
├── scrape_perfil.py
├── scrape_publicaciones.py
├── prueba.py
├── README.md
├── .gitignore
└── venv/

Los archivos generados durante la ejecución, como los JSON y CSV, se conservan localmente y están excluidos del repositorio mediante .gitignore.

Instalación

Clonar el repositorio:

git clone https://github.com/Alex280201/scraping-instagram.git
cd scraping-instagram

Crear un entorno virtual:

python -m venv venv

Activar el entorno virtual en Windows PowerShell:

.\venv\Scripts\Activate.ps1

Instalar las dependencias:

pip install playwright beautifulsoup4 lxml

Instalar Chromium para Playwright:

playwright install chromium

Uso

Ejecutar los scripts desde la terminal con el entorno virtual activado. Antes de ejecutar los scripts que requieren una sesión, debe configurarse el acceso de forma segura.

Flujo de uso:

1. python guardar_sesion.py   (inicia sesión una vez y crea sesion.json)
2. python scraper.py          (todo en uno: extrae, limpia y exporta)

Salida: instagram_publicaciones.xlsx (hojas Perfil y Publicaciones),
instagram_datos.json (perfil + resumen + publicaciones) e instagram_publicaciones.csv.

Además, scraper.py extrae seguidores y seguidos (EXTRAER_CONEXIONES = True) y genera un
documento aparte: instagram_conexiones.xlsx (hojas Resumen, Seguidores, Seguidos y
"No me siguen de vuelta"), instagram_conexiones.json, instagram_seguidores.csv e
instagram_seguidos.csv. También puede ejecutarse solo con:  python conexiones.py
Si una lista queda incompleta, la hoja Resumen lo indica y marca el cruce como no confiable.

Los scripts anteriores (scrape_perfil.py, scrape_publicaciones.py, depurar_datos.py)
siguen disponibles si se quiere ejecutar cada etapa por separado.

Si Instagram cierra la sesión, los scripts avisan y basta con repetir el paso 1.

Los resultados se guardan localmente en archivos JSON o CSV, según el script ejecutado.

Seguridad y uso responsable

No subir cookies, contraseñas, archivos de sesión ni credenciales a GitHub.

No compartir el archivo sesion.json.

Respetar las condiciones de uso y los límites de acceso de Instagram.

Utilizar el proyecto únicamente con fines educativos y con autorización para acceder a la información.

Autor

Proyecto académico de scraping con Python.