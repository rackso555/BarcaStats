# 🔵🔴 FC Barcelona Match Analytics Hub (2024/25, 2025/26 & 2026/27)

Una aplicación analítica local interactiva para estudiar, comparar y proyectar el rendimiento del **FC Barcelona** a través de todas sus competiciones oficiales: **LaLiga**, **UEFA Champions League**, **Copa del Rey** y **Supercopa de España**.

---

## ⚡ Filosofía: 100% Local & Cero Consumo de Tokens

- **Base de Datos Local (SQLite)**: 154 partidos registrados y estructurados con métricas oficiales completas.
- **Motor Estadístico Determinista (Python / Pandas / NumPy)**: Los cálculos de *Momentum Index*, xG diferencial acumulado ($\sum(xG - xGA)$), historial Head-to-Head y perfiles radar se ejecutan localmente en milisegundos.
- **Visualización Interactiva (Plotly)**: Gráficos de alta fidelidad, interactivos y con la identidad visual del Barça (Blaugrana, Dark Mode).

---

## 🚀 Cómo Iniciar la Aplicación

### Opción 1: Con el ejecutable por lotes (Doble clic)
Haz doble clic en `run_app.bat`.

### Opción 2: Desde la terminal
```bash
.\venv\Scripts\streamlit.exe run app.py
```
La aplicación se abrirá automáticamente en tu navegador en `http://localhost:8501`.

---

## 📊 Módulos Principales

1. **🏟️ Match Center & Previa**:
   - Selector de partido/jornada actual (2026/27) o histórico (24/25, 25/26).
   - Previa táctica con barras comparativas vs el rival (xG, Posesión, Tiros, Córners, Faltas).
   - Historial directo Cara a Cara (H2H) en 24/25 y 25/26 contra ese rival con desglose de goles y métricas medias.

2. **📈 Momentum & Progresión de Temporadas**:
   - Curvas de puntos acumulados por jornada comparando 2024/25, 2025/26 y 2026/27.
   - Curva de $\Delta xG$ acumulado (dominio real de ocasiones).
   - Gráfico de *Momentum Score* (media móvil ponderada de 3 partidos).
   - Comparador en una jornada específica (ej. "¿Cómo iba el Barça en la Jornada 10 en 24/25 vs 25/26?").

3. **🎯 Perfil Táctico & Radar 360°**:
   - Radar polar multivariante comparando los pilares de juego (Ataque, Control, Solidez Defensiva, Balón Parado, Intensidad).

4. **📋 Historial de Partidos Completo**:
   - Tabla interactiva con filtros por temporada, torneo, resultado (W, D, L) y rival.
   - Botón para exportar todos los datos a CSV con un solo clic.

5. **✍️ Gestor & Actualizador 2026/27**:
   - Formulario para registrar fácilmente los resultados y estadísticas a medida que se disputen los encuentros de la temporada 2026/27.
