import re

class DocumentoSimulado:
    def __init__(self, nombre, contenido):
        self.nombre = nombre
        self.contenido = contenido

def validar_documento(doc):
    reporte = {"archivo": doc.nombre}

    # Validar formato del nombre
    match = re.search(r"(\d+)", doc.nombre)
    if not match:
        reporte["estado"] = "RECHAZADO"
        reporte["motivo"] = "Nombre de archivo inválido"
        return reporte

    id_nombre = match.group(1)

    # Validar contenido
    if not doc.contenido.strip():
        reporte["estado"] = "REVISIÓN MANUAL"
        reporte["motivo"] = "Contenido vacío o ilegible"
        return reporte

    # Validar coherencia ID
    if id_nombre not in doc.contenido:
        reporte["estado"] = "ERROR CRÍTICO"
        reporte["motivo"] = "ID no coincide con contenido"
        return reporte

    # Si todo pasa
    reporte["estado"] = "APROBADO"
    reporte["motivo"] = "Documento coherente y válido"
    return reporte
