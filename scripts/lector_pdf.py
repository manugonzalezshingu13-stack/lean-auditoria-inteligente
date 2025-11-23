import fitz  # PyMuPDF

def leer_pdf(pdf_path):
    """
    Función para leer el contenido de un archivo PDF y extraer sus metadatos.

    Parámetros:
    pdf_path (str): Ruta del archivo PDF a procesar

    Retorna:
    texto (str): El texto extraído del PDF
    metadatos (dict): Los metadatos del documento PDF
    """
    # Abrir el archivo PDF
    doc = fitz.open(pdf_path)

    # Extraer texto de cada página
    texto = ""
    for pagina in doc:
        texto += pagina.get_text()

    # Extraer metadatos
    metadatos = doc.metadata

    return texto, metadatos

# Ejemplo de uso:
if __name__ == "__main__":
    archivo_pdf = "documento.pdf"  # Cambia la ruta por la de tu archivo
    texto, metadatos = leer_pdf(archivo_pdf)
    
    print("Texto Extraído:")
    print(texto[:500])  # Muestra los primeros 500 caracteres
    print("\nMetadatos del Documento:")
    print(metadatos)
