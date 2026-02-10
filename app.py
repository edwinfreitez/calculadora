import streamlit as st

# 1. CONFIGURACIÓN ULTRA COMPACTA
st.set_page_config(page_title="Blending DUSA", page_icon="🧪", layout="centered")

# CSS para forzar que NADA se corte y todo suba al máximo
st.markdown("""
    <style>
    .block-container {padding-top: 0.5rem; padding-bottom: 0rem;}
    [data-testid="stMetricValue"] {font-size: 1.8rem; font-weight: bold;}
    div[data-testid="stMetric"]:nth-child(1) [data-testid="stMetricValue"] {color: #D35400;}
    /* Evitar cualquier recorte en imágenes */
    [data-testid="stImage"] img {
        object-fit: contain !important;
    }
    </style>
    """, unsafe_allow_html=True)

def obtener_fp(grado):
    puntos = {
        75.0: 1.1420, 76.0: 1.1450, 77.0: 1.1490, 78.0: 1.1520, 79.0: 1.1560,
        80.0: 1.1600, 81.0: 1.1630, 82.0: 1.1670, 83.0: 1.1710, 84.0: 1.1750,
        85.0: 1.1790, 86.0: 1.1830, 87.0: 1.1870, 88.0: 1.1920, 89.0: 1.1960,
        90.0: 1.2010, 91.0: 1.2160, 92.0: 1.2110, 93.0: 1.2160, 94.0: 1.2220,
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

# LOGO REDUCIDO AL 50% (Tamaño pequeño para asegurar visibilidad total)
URL_LOGO = "https://media.licdn.com/dms/image/v2/C4E0BAQGROeCPt2-5rQ/company-logo_200_200/company-logo_200_200/0/1630651014568/destileras_unidas_s_a_logo?e=2147483647&v=beta&t=4KCIm7iySF8w6uXTN9ISvF6zPFRGhe8L3MTN2oGJh34"

st.image(URL_LOGO, width=50) 
st.subheader("Pase de Alcohol")
st.caption("By Edwin Freitez")

# ENTRADA DE DATOS
c1, c2 = st.columns(2)
with c1:
    entrada_g = st.number_input("Grado Real (°GL):", 75.0, 100.0, 96.0, 0.1, format="%.1f")
with c2:
    laa = st.number_input("LAA Solicitado:", min_value=0, value=1000, step=1)

if st.button("CALCULAR", use_container_width=True):
    fp = obtener_fp(entrada_g)
    
    if fp:
        vol_bruto = (laa / entrada_g) * 100
        peso_bruto = vol_bruto / fp
        
        v_fmt = "{:,}".format(round(vol_bruto)).replace(',', '.')
        p_fmt = "{:,}".format(round(peso_bruto)).replace(',', '.')
        
        st.divider()
        st.write(f"Resultados para **{entrada_g}°GL**:")
        
        st.metric(label="⚖️ PESAR EN ROMANA", value=f"{p_fmt} Kg")
        st.metric(label="Volumen Real", value=f"{v_fmt} Lts")
        
        st.caption(f"F.P.: {fp:.4f}")
    else:
        st.error("Error en rango de grado.")
