
### **Paso 1: Instalar Visual Studio Code**

1. **Descargar e instalar VS Code**:
   - Ve al sitio oficial de Visual Studio Code: [https://code.visualstudio.com/](https://code.visualstudio.com/).
   - Descarga la versión correspondiente para tu sistema operativo (Windows, macOS o Linux).
   - Instala VS Code siguiendo las instrucciones del instalador.

2. **Verificar la instalación**:
   - Abre VS Code después de la instalación. Verás la ventana principal del editor.

---

### **Paso 2: Instalar la extensión de Python**

1. **Abrir el gestor de extensiones en VS Code**:
   - Haz clic en el ícono de **Extensiones** en la barra lateral izquierda o usa el atajo de teclado **Ctrl+Shift+X** (Cmd+Shift+X en macOS).

2. **Buscar la extensión de Python**:
   - En la barra de búsqueda del gestor de extensiones, escribe `Python` y selecciona la extensión oficial de **Microsoft**.

3. **Instalar la extensión**:
   - Haz clic en el botón **Instalar** en la extensión de Python. Esta extensión proporciona soporte para características como la ejecución de código Python, depuración, autocompletado, linting (análisis de código), entre otros.

---

### **Paso 3: Configurar Python en VS Code**

1. **Seleccionar la versión de Python**:
   - Abre cualquier archivo de Python en VS Code o crea uno nuevo (por ejemplo, `hello.py`).
   - Una vez que tengas un archivo `.py` abierto, VS Code te pedirá que selecciones un **intérprete de Python** (la versión de Python que deseas usar).
   - Para cambiar el intérprete, haz clic en la esquina inferior izquierda donde dice `Python` o en la paleta de comandos usando **Ctrl+Shift+P** (Cmd+Shift+P en macOS) y busca `Python: Select Interpreter`.
   - Selecciona la versión de Python que acabas de instalar (por ejemplo, `Python 3.11`).

2. **Verificar el entorno de Python**:
   - Para asegurarte de que VS Code está utilizando el intérprete correcto, abre la terminal integrada de VS Code (**Ctrl+`** o Cmd+` en macOS) y escribe:
     ```bash
     python --version
     ```
   - Deberías ver la versión de Python que seleccionaste.

---

### **Paso 4: Ejecutar un programa Python en VS Code**

1. **Escribir un programa Python**:
   - En VS Code, crea un archivo llamado `hello.py` y escribe el siguiente código simple:
     ```python
     print("Hello, World!")
     ```

2. **Ejecutar el archivo**:
   - Para ejecutar el programa, haz clic derecho en el archivo `hello.py` y selecciona **Run Python File in Terminal** (Ejecutar archivo de Python en la terminal).
   - Alternativamente, puedes usar el atajo de teclado **F5** para ejecutar el archivo en modo de depuración.

3. **Ver el resultado**:
   - En la terminal de VS Code, deberías ver el siguiente resultado:
     ```bash
     Hello, World!
     ```

---

### **Paso 5: Configurar un entorno virtual en VS Code**

Es recomendable usar **entornos virtuales** para gestionar tus dependencias de Python en proyectos.

1. **Crear un entorno virtual**:
   - Abre la terminal en VS Code y navega a la carpeta de tu proyecto.
   - Crea un entorno virtual ejecutando:
     ```bash
     python -m venv venv
     ```

2. **Activar el entorno virtual**:
   - En Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - En macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

3. **Seleccionar el entorno virtual en VS Code**:
   - Abre la paleta de comandos con **Ctrl+Shift+P** (Cmd+Shift+P en macOS) y busca `Python: Select Interpreter`.
   - Selecciona el intérprete del entorno virtual que acabas de crear (debería aparecer en la lista).

---

### **Paso 6: Depurar código en VS Code**

VS Code tiene un excelente soporte para **depuración** de código Python. Para iniciar una sesión de depuración:

1. **Añadir puntos de interrupción**:
   - Haz clic en el margen izquierdo de una línea de código para añadir un punto de interrupción (se verá como un círculo rojo). Esto detendrá la ejecución del programa en esa línea.

2. **Iniciar la depuración**:
   - Haz clic en el botón de **depuración** en la barra lateral izquierda (icono de un insecto) o presiona **F5**.
   - VS Code ejecutará tu programa y se detendrá en los puntos de interrupción que hayas definido. Desde allí, puedes inspeccionar variables, ejecutar código paso a paso y más.

---

### **Paso 7: Otras configuraciones útiles**

1. **Formateo de código automático**:
   - Puedes configurar VS Code para que automáticamente formatee tu código al guardar. Para hacer esto, instala una extensión como **Black** o **autopep8**.
   - Para activar el formateo automático, abre la configuración de VS Code (**Ctrl+,**) y busca `format on save`. Marca esta opción para habilitarla.

2. **Linting y análisis de código**:
   - El **linting** te ayuda a identificar errores y malas prácticas en tu código. Puedes activar el linting en VS Code instalando un linter como **pylint**:
     ```bash
     pip install pylint
     ```
   - VS Code detectará automáticamente pylint y te mostrará advertencias en tu código si encuentra problemas.
