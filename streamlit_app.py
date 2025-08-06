import streamlit as st
from fpdf import FPDF
from datetime import datetime
from io import BytesIO

# Título
st.title("Generador de Plantillas - Pulso Perfecto")

# Inputs del usuario
nombre_cliente = st.text_input("Nombre del cliente")
nombre_playlist = st.text_input("Nombre de la playlist")
descripcion = st.text_area("Descripción de la playlist")
link_playlist = st.text_input("Link de la playlist")
fecha_entrega = st.date_input("Fecha de entrega", value=datetime.today())

# Botón para generar
if st.button("Generar PDF"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, 'Pulso Perfecto - Acceso Premium', ln=True, align='C')
    pdf.set_font("Arial", '', 12)
    pdf.ln(10)
    pdf.cell(200, 10, f'Fecha de entrega: {fecha_entrega.strftime("%d/%m/%Y")}', ln=True)
    pdf.cell(200, 10, f'Cliente: {nombre_cliente}', ln=True)
    pdf.ln(10)

    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 10, 'Playlist:', ln=True)
    pdf.set_font("Arial", '', 12)
    pdf.cell(200, 10, f'Nombre: {nombre_playlist}', ln=True)
    pdf.multi_cell(0, 10, f'Descripción:\n{descripcion}')
    pdf.cell(200, 10, f'Enlace: {link_playlist}', ln=True)
    pdf.ln(5)
    pdf.set_text_color(220, 50, 50)
    pdf.cell(200, 10, 'Este enlace es exclusivo para tu uso personal. No compartir.', ln=True)

    # Convertir a BytesIO para descarga
    buffer = BytesIO()
    pdf.output(buffer)
    buffer.seek(0)

    # Descargar
    st.download_button(
        label="Descargar plantilla PDF",
        data=buffer,
        file_name=f"PulsoPerfecto_{nombre_cliente}.pdf",
        mime="application/pdf"
    )
