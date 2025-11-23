Lean Auditoría Inteligente

Sistema de Validación, Control de Calidad y Auditoría Lean-Driven

1. Propósito del Proyecto

Este repositorio implementa un sistema Lean para auditoría inteligente de documentos y flujos de información. Aplica principios de Jidoka, Poka-Yoke, Estandarización, Flujo Continuo y validaciones automáticas mediante GitHub Actions.

El objetivo es lograr auditorías más rápidas, sin errores humanos y con trazabilidad completa.

## 2. Estructura del Repositorio `lean-auditoria-inteligente`

```
lean-auditoria-inteligente/
│
├── 0_metodologia/
│   ├── diseño_investigacion.md
│   ├── enfoque_lean.md
│   ├── referencias_formales.md
│   ├── 1_estado_del_arte.md
│   ├── data_quality.md
│   ├── information_lifecycle.md
│   ├── kaizen_tic.md
│   ├── 2_marco_teorico.md
│   ├── lean_it.md
│   ├── transformacion_digital.md
│
├── 3_desarrollo/
│   ├── procesos.md
│   ├── analisis.md
│
├── 4_validaciones/
│   ├── checklist_lean.md
│   ├── checklist_estructura.md
│
├── reportes/
│   ├── informe_general.md
│   ├── hallazgos.md
│
├── diagramas/
│   ├── arquitectura_auditoria.png
│   ├── flujos.png
│
├── .github/
│   └── workflows/
│       └── validador.yml
│
└── README.md
```

## 3. Flujo Conceptual (Diagrama ASCII)

```
────────────────────────────────────────────────────────────────────────
                     FLUJO GENERAL DE AUDITORÍA LEAN
────────────────────────────────────────────────────────────────────────

Entrada del Proyecto
   ▼ (Datos / Documentos)
────────────────────────────────────────────────────────────────────────

1. Metodología y Marco Formal
   • Definición Lean
   • ILM (Information Lifecycle Management)
   • Data Quality
   • Kaizen TIC
   ▼
   Evidencia estructurada

────────────────────────────────────────────────────────────────────────

2. Desarrollo y Análisis
   • Procesos
   • Diagramas
   • Modelado
   ▼
   Evidencia analizada

────────────────────────────────────────────────────────────────────────

3. Validación Automática
   • GitHub Actions ejecuta validador.yml
   ▼
   Evidencia validada + trazabilidad automática

────────────────────────────────────────────────────────────────────────

4. Reporte Final y Auditoría
   • Evidencia completa
   • Conclusiones técnicas
   • Matriz de cumplimiento
────────────────────────────────────────────────────────────────────────
```

4. Automatización con GitHub Actions

Tu archivo .github/workflows/validador.yml ejecuta:

Validación de estructura

Verificación de carpetas clave

Chequeo rápido tipo Poka-Yoke

Reporte automático en cada commit

Workflow activo en tu repositorio.

5. Tecnologías Utilizadas

GitHub Actions (CI/CD)

Markdown estructurado

Auditorías Lean

Validadores automatizados

Simuladores en Python para procesos Lean (opcionales)

6. Cómo usar este proyecto

Sube cualquier documento o análisis dentro de su carpeta correcta.

GitHub Actions ejecutará automáticamente el validador.

Si hay errores, verás un mensaje rojo indicando qué falta.

Si todo está en orden, el commit queda aprobado con validación verde.

7. Logotipo del Proyecto


<img width="1024" height="1024" alt="image" src="https://github.com/user-attachments/assets/c58c9143-d135-4690-8ee2-1a8999aa6acc" />


8. Autor

Manuel González Shingu
Sistema Lean de Auditoría Inteligente
2025
