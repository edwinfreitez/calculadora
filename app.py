import streamlit as st

st.set_page_config(page_title="Calculadora Blending", page_icon="🧪")

# Base de datos
PUNTOS = {75.0: 1.1420, 76.0: 1.1450, 77.0: 1.1490, 78.0: 1.1520, 79.0: 1.1560,
          80.0: 1.1600, 81.0: 1.1630, 82.0: 1.1670, 83.0: 1.1710, 84.0: 1.1750,
          85.0: 1.1790, 86.0: 1.1830, 87.0: 1.1870, 88.0: 1.1920, 89.0: 1.1960,
          90.0: 1.2010, 91.0: 1.2060, 92.0: 1.2110, 93.0: 1.2160, 94.0: 1.2220,
          95.0: 1.2280, 96.0: 1.2340, 97.0: 1.2400, 98.0: 1.2470, 99.0: 1.2540, 100.0: 1.2620}

def obtener_fp(grado):
    if grado in PUNTOS: return PUNTOS[grado]
    g_base = int(grado)
    if g_base in PUNTOS and (g_base + 1) in PUNTOS:
        return PUNTOS[g_base] + (grado - g_base) * (PUNTOS[g_base + 1] - PUNTOS[g_base])
    return None

st.title("🧪 Control de Blending")
grado = st.number_input("Grado Real (°GL):", 75.0, 100.0, 96.0, 0.1)
laa = st.number_input("LAA Solicitados:", 0.0, 1000000.0, 1000.0)

if st.button("CALCULAR"):
    fp = obtener_fp(grado)
    vol = (laa / grado) * 100
    peso = vol / fp
    st.success(f"**Volumen Real:** {vol:,.2f} Lts")
    st.success(f"**Pesar en Romana:** {peso:,.2f} Kg")
    st.caption(f"Factor utilizado: {fp:.4f}")
