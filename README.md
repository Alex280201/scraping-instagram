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

Estructura del proyecto

scraping-instagram/
├── guardar_sesion.py
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

Los resultados se guardan localmente en archivos JSON o CSV, según el script ejecutado.

Seguridad y uso responsable

No subir cookies, contraseñas, archivos de sesión ni credenciales a GitHub.

No compartir el archivo sesion.json.

Respetar las condiciones de uso y los límites de acceso de Instagram.

Utilizar el proyecto únicamente con fines educativos y con autorización para acceder a la información.

Autor

Proyecto académico de scraping con Python.