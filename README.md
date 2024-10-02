# Proyecto de Ejemplo en Python

Este es un proyecto de ejemplo en Python que muestra cómo crear una lista de personas y sus perfiles de LinkedIn.

## Descripción

El proyecto consiste en una aplicación web simple que muestra una lista de personas y sus perfiles de LinkedIn. Utiliza Flask como framework web y HTML/CSS para la interfaz de usuario.

## Requisitos

- Python 3.x
- pip
- venv

## Instalación en Ubuntu

### Actualizar el sistema

```bash
sudo apt update
```

### Instalar Python

```bash
sudo apt install python3
```

### Instalar pip

```bash
sudo apt install python3-pip
```

### Instalar venv

```bash
sudo apt install python3-venv
```

### Crear un entorno virtual

```bash
python3 -m venv venv
```

### Activar el entorno virtual

```bash
source venv/bin/activate    
```

### Instalar dependencias

```bash
pip install -r requirements.txt
```

## Uso

1. Clona este repositorio:

```bash
git clone https://gitlab.com/training-devops-cf/hola-mundo-cf.git
```

2. Navega al directorio del proyecto:

```bash
cd hola-mundo-cf
```

3. Activa el entorno virtual:

```bash
source nombre_del_entorno/bin/activate 
```

4. Ejecuta la aplicación:

```bash
python app.py
```

5. Abre tu navegador web y ve a `http://localhost:5000` para ver la aplicación en funcionamiento.


## Estructura del Proyecto

```plaintext
.
app
├── app.py
├── data.json
├── requirements.txt
├── static
│   └── styles.css
├── templates
│   └── index.html
└── tests
    └── test_app.py
```

6. correr los test

```bash
PYTHONPATH=. pytest tests/test_app.py
``
