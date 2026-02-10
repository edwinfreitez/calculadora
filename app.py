import streamlit as st

# 1. CONFIGURACIÓN
st.set_page_config(page_title="Pase de Alcohol DUSA", page_icon="🧪", layout="centered")

# CSS para ajustes definitivos
st.markdown("""
    <style>
    .block-container {padding-top: 2rem; padding-bottom: 2rem;}
    
    /* Resultados numéricos */
    [data-testid="stMetricValue"] {font-size: 1.8rem; font-weight: bold;}
    div[data-testid="stMetric"]:nth-child(1) [data-testid="stMetricValue"] {color: #D35400;}
    
    /* F.P. Súper pegado a los resultados con margen inferior */
    .fp-final {
        font-size: 1.05rem;
        color: #566573;
        margin-top: -10px;
        margin-bottom: 20px;
        font-weight: 500;
    }
    
    /* Alineación de logo y textos */
    .header-container {
        display: flex;
        align-items: center;
        gap: 15px;
        margin-bottom: 0.5rem;
    }
    
    /* AJUSTES DE TEXTO SOLICITADOS */
    .titulo-mini {
        font-size: 0.75rem; /* Significativamente reducido */
        margin: 0;
        text-transform: uppercase;
        font-weight: bold;
        color: #808B96;
    }
    .subtitulo-mini {
        font-size: 0.85rem; /* Mucho más reducido que antes */
        margin: 0;
        color: #2E4053;
        font-weight: bold;
    }
    .autor-text {
        margin: 0;
        font-size: 0.95rem; /* Aumentado para legibilidad */
        color: #21618C;
        font-weight: 500;
    }
    </style>
    """, unsafe_allow_html=True)

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

# ENCABEZADO
URL_LOGO = "https://media.licdn.com/dms/image/v2/C4E0BAQGROeCPt2-5rQ/company-logo_200_200/company-logo_200_200/0/1630651014568/destileras_unidas_s_a_logo?e=2147483647&v=beta&t=4KCIm7iySF8w6uXTN9ISvF6zPFRGhe8L3MTN2oGJh34"

st.markdown(f"""
    <div class="header-container">
        <img src="{URL_LOGO}" width="50">
        <div>
            <p class="titulo-
