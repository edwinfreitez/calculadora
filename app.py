import streamlit as st

# 1. CONFIGURACIÓN
st.set_page_config(page_title="Blending DUSA", page_icon="🧪", layout="centered")

# CSS para ajustes de precisión
st.markdown("""
    <style>
    .block-container {padding-top: 2rem; padding-bottom: 0rem;}
    
    /* Resultados numéricos */
    [data-testid="stMetricValue"] {font-size: 1.8rem; font-weight: bold;}
    div[data-testid="stMetric"]:nth-child(1) [data-testid="stMetricValue"] {color: #D35400;}
    
    /* F.P. Súper pegado a los resultados */
    .fp-final {
        font-size: 1.05rem;
        color: #566573;
        margin-top: -10px; /* Margen negativo para subirlo */
        font-weight: 500;
    }
    
    /* Alineación de logo y textos */
    .header-container {
        display: flex;
        align-items: center;
        gap: 15px;
        margin-bottom: 0.5rem;
    }
    
    /* Ajuste de tamaños de título y subtítulo */
    .titulo-principal {
        font-size: 1.6rem; /* Un poco más pequeño */
        margin: 0;
        line-height: 1.1;
    }
    .subtitulo {
        font-size: 1rem; /* Más pequeño */
        margin: 0;
        color: #5D6D7E;
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

# ENCABEZADO OPTIMIZADO
URL_LOGO = "https://media
