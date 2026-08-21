# 🚀 Guía de Despliegue Online Gratuito (24/7) en Streamlit Community Cloud

Esta guía explica paso a paso cómo poner tu **FC Barcelona Match Analytics Hub** online en la nube de forma **100% gratuita y activa 24/7**, sin necesidad de tener tu computadora encendida.

---

## 🎯 1. Filosofía de Acceso Zero-Friction (Sin Fricción)

La aplicación entra **directamente en Modo Visualización** para cualquier visitante que abra la URL:
- **👥 Modo Visualización (Público/Invitados)**:
  - Sin contraseñas ni pantallas de bloqueo al entrar.
  - Acceso inmediato y fluido a todas las estadísticas, filtros, gráficas de Match Center, Momentum & Progresión, Perfil Táctico e Historial.
- **🔐 Modo Administrador (Tú - Control Total)**:
  - Desplegable rápido en la barra lateral izquierda: **"🔐 Iniciar Sesión como Admin"**.
  - **Usuario**: `admin` | **Contraseña**: `barca2026` *(configurable en `.streamlit/secrets.toml`)*.
  - Desbloquea la pestaña de **Sincronización Automática con Agente** para sincronizar nuevas jornadas y auditar datos.

---

## 📦 2. Pasos para Publicar la App Gratis

### Paso 1: Subir el proyecto a GitHub
1. Crea una cuenta gratuita en [GitHub.com](https://github.com/) (si aún no tienes una).
2. Crea un **nuevo repositorio** (puedes marcarlo como **Público** o **Privado**).
3. En la carpeta de la aplicación (`c:\Users\IT\Documents\Barca app`), abre una terminal y ejecuta:
   ```bash
   git init
   git add .
   git commit -m "FC Barcelona Analytics Hub con Modo Visualización Directo y Admin Auth"
   git branch -M main
   git remote add origin https://github.com/TU_USUARIO/TU_REPOSITORIO.git
   git push -u origin main
   ```

### Paso 2: Desplegar en Streamlit Community Cloud
1. Entra a [share.streamlit.io](https://share.streamlit.io/) e inicia sesión con tu cuenta de GitHub.
2. Haz clic en el botón azul **"New app"** (Nueva aplicación).
3. Configura los siguientes campos:
   - **Repository**: Selecciona tu repositorio de GitHub.
   - **Branch**: `main`
   - **Main file path**: `app.py`
4. Despliega la sección **"Advanced settings" -> "Secrets"** y personaliza tus credenciales de admin:
   ```toml
   [auth]
   admin_user = "admin"
   admin_pass = "barca2026"
   ```
5. Haz clic en **"Deploy!"** (Desplegar).

---

## 🎉 ¡Listo!
En menos de 2 minutos tu aplicación tendrá una URL pública (ejemplo: `https://barca-analytics-hub.streamlit.app`) activa **24/7 sin costo alguno**. Cualquier persona podrá consultar las estadísticas sin fricción, y solo tú podrás autenticarte como Administrador para sincronizar nuevos partidos.
