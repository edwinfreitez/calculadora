import streamlit as st

# 1. CONFIGURACIÓN DE PÁGINA Y LOGO
st.set_page_config(page_title="Calculadora Edwin Freitez", page_icon="🧪")

# --- AQUÍ PUEDES PONER EL LOGO ---
# Si tienes una URL de imagen, reemplaza este link. Si no, quita estas dos líneas.
URL_LOGO = "https://media.licdn.com/dms/image/v2/C4E0BAQGROeCPt2-5rQ/company-logo_200_200/company-logo_200_200/0/1630651014568/destileras_unidas_s_a_logo?e=2147483647&v=beta&t=4KCIm7iySF8w6uXTN9ISvF6zPFRGhe8L3MTN2oGJh34" # Ejemplo: un icono de química
st.image(URL_LOGO, width=100) 

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

# INTERFAZ
st.title("Calculadora de Pesaje de Alcohol")
st.markdown("### Pase de Alcohol")
st.caption("Desarrollado por: **Edwin Freitez**")
st.divider()

col1, col2 = st.columns(2)

with col1:
    # Grado con 1 decimal
    entrada_g = st.number_input("1. Grado Real (°GL):", min_value=75.0, max_value=100.0, value=96.0, step=0.1, format="%.1f")

with col2:
    # LAA como número entero (sin decimales)
    laa = st.number_input("2. LAA solicitado (Entero):", min_value=0, value=1000, step=1)

if st.button("CALCULAR AHORA"):
    fp = obtener_fp(entrada_g)
    
    if fp:
        # Fórmulas
        vol_mezcla_bruto = (laa / entrada_g) * 100
        peso_bruto = vol_mezcla_bruto / fp
        
        # Formateo con punto para miles y redondeo a entero
        vol_formateado = "{:,}".format(round(vol_mezcla_bruto)).replace(',', '.')
        peso_formateado = "{:,}".format(round(peso_bruto)).replace(',', '.')
        
        st.success(f"### RESULTADOS PARA {entrada_g}°GL:")
        
        # Mostramos los resultados grandes y claros
        st.metric(label="VOLUMEN REAL", value=f"{vol_formateado} Lts")
        st.metric(label="PESAR EN ROMANA", value=f"{peso_formateado} Kg")
        
        st.info(f"Factor de corrección (F.P.) aplicado: **{fp:.4f}**")
    else:
        st.error("Error: Grado fuera de rango.")
