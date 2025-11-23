# Flujo Lean del Sistema de Auditoría Inteligente

## 1. Entrada
- El usuario sube el documento al repositorio o bandeja de entrada.
- El sistema genera un log de entrada.

## 2. Inspección automática (Jidoka)
1. Leer nombre del archivo  
2. Extraer ID  
3. Leer contenido interno  
4. Buscar coincidencias con el ID del nombre  
5. Verificar que el texto no está vacío  
6. Validar integridad técnica (tamaño, corrupción)

## 3. Decisión automática
- Si todo coincide → APROBADO
- Si el texto está vacío → OCR / Revisión manual
- Si el ID no coincide → ERROR CRÍTICO → Auditoría
- Si el archivo está corrupto → Rechazo directo

## 4. Flujo continuo
- El documento pasa inmediatamente a la siguiente etapa, sin lotes.

## 5. Gestión de excepciones
- Los fallos se registran en auditorías/
- Se crea un caso de estudio si el error se repite
- El error desencadena análisis de causa raíz (RCA)

## 6. Cierre
- El documento aprobado se archiva
- Se actualizan métricas y dashboards
