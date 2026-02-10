import streamlit as st

# Configuración de página
st.set_page_config(page_title="Calculadora Edwin Freitez", page_icon="🧪")

def obtener_fp(grado):
    puntos = {
        75.0: 1.1420, 76.0: 1.1450, 77.0: 1.1490, 78.0: 1.1520, 79.0: 1.1560,
        80.0: 1.1600, 81.0: 1.1630, 82.0: 1.1670, 83.0: 1.1710, 84.0: 1.1750,
        85.0: 1.1790, 86.0: 1.1830, 87.0: 1.1870, 88.0: 1.1920, 89.0: 1.1960,
        90.0: 1.2010, 91.0: 1.2060, 92.0: 1.2110, 93.0: 1.2160, 94.0: 1.2220,
        95.0: 1.2280, 96.0: 1.2340, 97.0: 1.2400, 98.0: 1.2470, 99.0: 1.2540,
        100.0: 1.2620
    }
    if grado in puntos: return puntos[grado]
    g_base = int(grado)
    g_next = g_base + 1
    if g_base in puntos and g_next in puntos:
        ratio = (grado - g_base)
        return puntos[g_base] + ratio * (puntos[g_next] - puntos[g_base])
    return None

# Interfaz Web
st.markdown("### CALCULADORA PESAJE DE ALCOHOL")
st.caption("By Edwin Freitez")
st.divider()

col1, col2 = st.columns(2)

with col1:
    entrada_g = st.number_input("1. Ingrese Grado Real (°GL):", min_value=75.0, max_value=100.0, value=96.0, step=0.1)

with col2:
    laa = st.number_input("2. Ingrese LAA solicitado:", min_value=0.0, value=1000.0, step=100.0)

if st.button("CALCULAR RESULTADOS"):
    fp = obtener_fp(entrada_g)
    
    if fp:
        # Fórmulas
        vol_mezcla_bruto = (laa / entrada_g) * 100
        peso_bruto = vol_mezcla_bruto / fp
        
        # Redondeo y Formateo (Punto para miles)
        vol_formateado = "{:,}".format(round(vol_mezcla_bruto)).replace(',', '.')
        peso_formateado = "{:,}".format(round(peso_bruto)).replace(',', '.')
        
        st.subheader(f"Resultados para {entrada_g}°GL:")
        
        st.success(f"**VOLUMEN REAL:** {vol_formateado} Lts")
        st.info(f"**PESAR EN ROMANA:** {peso_formateado} Kg")
        
        st.write(f"Factor F.P. utilizado: `{fp:.4f}`")
    else:
        st.error("Grado fuera de rango permitido (75-100).")
