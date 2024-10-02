# Tutorial: Cómo instalar Python y configurar un entorno de programación en un servidor de Ubuntu 22.04


## Introducción

Python es un lenguaje de programación flexible y versátil, popular por su sencillez y potencia, ideal para múltiples casos de uso como automatización, análisis de datos, inteligencia artificial y desarrollo backend. Publicado inicialmente en 1991, Python ha evolucionado y, en su versión actual (Python 3), se ha consolidado como la opción preferida tanto para principiantes como para desarrolladores experimentados.

En este tutorial, aprenderás a configurar tu servidor Ubuntu 22.04 con un entorno de programación Python 3. Configurar Python en un servidor te permite desarrollar proyectos colaborativos y aprovechar los recursos del servidor para tareas computacionales. Aunque este tutorial se centra en Ubuntu 22.04, los principios se aplican a cualquier distribución basada en Debian.

---

## Requisitos previos

Para completar este tutorial, debes contar con:

1. Un servidor con **Ubuntu 22.04**.
2. Un usuario no root con privilegios **sudo**.
3. Familiaridad con el uso de la terminal. Si eres nuevo, te puede ayudar la guía [Introducción al terminal de Linux].

Una vez configurado tu servidor y usuario, estarás listo para comenzar.

---

## Paso 1: Actualizar el sistema y verificar Python 3

Ubuntu 22.04 incluye Python 3 preinstalado. Primero, asegurémonos de que nuestro sistema esté actualizado con los últimos parches de seguridad y mejoras de software. Ejecuta los siguientes comandos:

```bash
sudo apt update && sudo apt -y upgrade
```

Después, confirma la versión de Python 3 instalada:

```bash
python3 --version
```

Verás un resultado similar a este:

```bash
Python 3.10.x
```

Si Python no está instalado, puedes instalarlo ejecutando:

```bash
sudo apt install python3
```

---

## Paso 2: Instalar pip y herramientas esenciales

`pip` es el administrador de paquetes de Python que te permitirá instalar módulos y bibliotecas para tus proyectos. Para instalar `pip` junto con otras herramientas de desarrollo necesarias, ejecuta:

```bash
sudo apt install -y python3-pip build-essential libssl-dev libffi-dev python3-dev
```

Una vez que tengas `pip`, puedes instalar paquetes usando el comando:

```bash
pip3 install nombre_paquete
```

Por ejemplo, para instalar la popular biblioteca de ciencia de datos **NumPy**:

```bash
pip3 install numpy
```

---

## Paso 3: Crear un entorno virtual

Los entornos virtuales te permiten aislar los paquetes y dependencias de cada proyecto, evitando conflictos entre versiones. Python incluye la herramienta `venv` para crear estos entornos.

Instala el módulo `venv` si no está disponible:

```bash
sudo apt install python3-venv
```

Luego, crea un directorio para tus entornos virtuales y genera uno nuevo:

```bash
mkdir ~/python-environments
cd ~/python-environments
python3 -m venv mi_entorno
```

Esto creará un nuevo entorno virtual llamado `mi_entorno`. Para activarlo, ejecuta:

```bash
source mi_entorno/bin/activate
```

El prompt de tu terminal cambiará para reflejar que estás dentro del entorno virtual, mostrando algo como:

```bash
(mi_entorno) usuario@servidor:~$
```

---

## Paso 4: Crear y ejecutar un programa “Hello, World”

Ahora que tienes tu entorno configurado, es hora de probarlo con un simple programa de “Hello, World!”. Crea un archivo llamado `hello.py` con el siguiente comando:

```bash
nano hello.py
```

Escribe el siguiente código en el archivo:

```python
print("Hello, World!")
```

Guarda y cierra el editor (CTRL+X, luego 'y' y ENTER). Para ejecutar tu programa:

```bash
python hello.py
```

Verás la salida:

```bash
Hello, World!
```

Para salir del entorno virtual, simplemente ejecuta:

```bash
deactivate
```

---

## Paso 5: Automatización de tareas comunes (Opcional)

Para facilitar tu flujo de trabajo, puedes utilizar un archivo `requirements.txt` donde listarás las dependencias de tu proyecto. Crea un archivo y lista las bibliotecas que necesitas:

```bash
echo numpy > requirements.txt
```

Luego, instala todas las dependencias con:

```bash
pip install -r requirements.txt
```

Esto es especialmente útil para proyectos colaborativos o que requieran instalaciones repetitivas en diferentes entornos.

---

## Conclusión

Para seguir aprendiendo, consulta [más tutoriales de Python](https://docs.python.org/es/3/tutorial/) o explora cómo integrar Python en aplicaciones web, análisis de datos o automatización de tareas.

---

### Recursos adicionales
- [Documentación oficial de Python 3](https://docs.python.org/es/3/)
- [Cómo gestionar entornos virtuales en Python](https://virtualenv.pypa.io/en/latest/)
- [Guía completa de pip](https://pip.pypa.io/en/stable/)



