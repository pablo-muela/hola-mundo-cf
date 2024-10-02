### Tutorial: Cómo instalar Python y configurar un entorno de programación en Windows 10/11

### Requisitos previos
- **Sistema operativo**: Windows 10 o Windows 11.
- **Permisos de administrador** para instalar software.

### Paso 1: Descargar e instalar Python 3
1. **Descarga Python**:
   - Ve a la página oficial de descargas de Python: [https://www.python.org/downloads/](https://www.python.org/downloads/).
   - Descarga la versión más reciente de Python 3 (actualmente Python 3.11 en octubre de 2024).

2. **Instalar Python**:
   - Ejecuta el archivo descargado (`python-3.x.x.exe`).
   - **Importante**: Asegúrate de marcar la opción **"Add Python to PATH"** (Agregar Python al PATH). Esto te permitirá ejecutar Python desde cualquier directorio en la línea de comandos.
   - Haz clic en **Install Now** (Instalar ahora).

3. **Verificar la instalación**:
   - Abre la terminal de Windows (puedes usar la terminal de PowerShell o el CMD).
   - Ejecuta el siguiente comando para verificar la instalación:
     ```bash
     python --version
     ```
   - Deberías ver algo como `Python 3.x.x`, confirmando que Python está instalado correctamente.

4. **Instalar pip (si es necesario)**:
   - Pip es la herramienta de gestión de paquetes para Python. En las últimas versiones de Python, pip ya está incluido por defecto. Para verificar que pip está instalado, ejecuta:
     ```bash
     pip --version
     ```

### Paso 2: Configurar un entorno virtual
Python permite crear **entornos virtuales** donde puedes aislar las dependencias y bibliotecas necesarias para cada proyecto, evitando conflictos con otros proyectos o con el sistema.

1. **Instalar `venv`**:
   - El módulo `venv` ya viene integrado con las versiones más recientes de Python. No necesitas instalar nada adicional. Para crear un entorno virtual en tu proyecto, navega al directorio donde deseas crear tu entorno.
   - Usa el siguiente comando para crear un entorno virtual:
     ```bash
     python -m venv nombre_entorno
     ```

2. **Activar el entorno virtual**:
   - Una vez que hayas creado el entorno virtual, debes activarlo. Para activarlo en Windows, usa:
     ```bash
     .\nombre_entorno\Scripts\activate
     ```
   - Si la activación fue exitosa, verás el nombre del entorno en el prompt de tu terminal (por ejemplo, `(nombre_entorno)`).

3. **Instalar paquetes en el entorno**:
   - Ahora que el entorno está activado, puedes instalar paquetes utilizando pip. Por ejemplo, para instalar **Django** o **NumPy**, usa los siguientes comandos:
     ```bash
     pip install django
     pip install numpy
     ```

### Paso 3: Crear un programa "Hello, World"
Para verificar que el entorno está funcionando correctamente, crearemos un programa básico de **"Hello, World"**.

1. **Crear el archivo del programa**:
   - Abre tu editor de texto favorito (puedes usar Notepad o cualquier editor de código como Visual Studio Code o Sublime Text).
   - Escribe el siguiente código en un nuevo archivo:
     ```python
     print("Hello, World!")
     ```
   - Guarda el archivo como `hello.py`.

2. **Ejecutar el programa**:
   - En la terminal, asegúrate de estar dentro del entorno virtual y ejecuta el archivo:
     ```bash
     python hello.py
     ```
   - Deberías ver el mensaje `Hello, World!` impreso en la terminal.

### Paso 4: Desactivar el entorno virtual
Para salir del entorno virtual, simplemente ejecuta:
```bash
deactivate
```
Esto desactivará el entorno y volverás al shell normal de Windows.

### Paso 5: Gestionar bibliotecas con pip
Recuerda que dentro de tu entorno virtual puedes instalar y gestionar bibliotecas utilizando pip, lo cual es fundamental para proyectos de Python que dependen de varias bibliotecas. Puedes listar las bibliotecas instaladas con:
```bash
pip list
```

### Conclusión

Si te interesa seguir aprendiendo más sobre Python, puedes consultar más tutoriales o leer la documentación oficial en [https://docs.python.org/3/](https://docs.python.org/3/).