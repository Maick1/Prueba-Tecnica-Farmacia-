# 🧪 Automatización con WinAppDriver

Este proyecto contiene pruebas automatizadas para la calculadora de Windows utilizando **Python + Appium + WinAppDriver**.

---

## ⚙️ Requisitos

Antes de ejecutar el proyecto, asegúrate de tener instalado:

* Python 3.x
* WinAppDriver (incluido en el proyecto)

---

## 🚀 Pasos para ejecutar el proyecto

### 1. Instalar Python

Verifica que Python esté instalado:

```bash
python --version
```

---

### 2. Instalar WinAppDriver

Dentro del proyecto encontrarás el instalador.
Ejecuta el archivo y completa la instalación.

---

### 3. Levantar WinAppDriver

Abre una terminal (CMD) como administrador y navega a:

```bash
C:\Program Files (x86)\Windows Application Driver
```

Ejecuta:

```bash
WinAppDriver.exe
```

Si todo está correcto, verás:

```bash
Listening for requests at: http://127.0.0.1:4723/
```

---

### 4. Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/tu-repositorio.git
cd tu-repositorio
```

---

### 5. Crear y activar entorno virtual

```bash
python -m venv venv
venv\Scripts\activate
```

---

### 6. Instalar dependencias

Verifica o instala las librerías necesarias:

```bash
pip install selenium
pip install Appium-Python-Client
pip install urllib3
```

(O verificar instalación:)

```bash
pip show selenium
pip show Appium-Python-Client
pip show urllib3
```

---

### 7. Ejecutar el script

```bash
python script.py
```

---

## 📁 Estructura del proyecto

```
├── script.py
├── venv/
├── README.md
└── WinAppDriver.exe (instalador)
```

---

## 🧠 Notas

* Asegúrate de que WinAppDriver esté en ejecución antes de correr las pruebas.
* El proyecto automatiza la aplicación Calculadora de Windows.
* Se recomienda ejecutar la terminal como administrador para evitar problemas de permisos.

---
