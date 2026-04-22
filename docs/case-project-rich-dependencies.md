# Case Project (PR1): frontera de cleanup en dependencias internas más ricas

## Propósito del caso
Definir una base documental breve para explorar una posible frontera de cleanup entre `cli`, `core` y `utils`, antes de realizar cambios técnicos en el repositorio.

## Hipótesis del experimento
En un repositorio con dependencias internas más ricas, es posible tomar decisiones conservadoras y razonables, mantener PRs pequeñas y validar cada paso con criterios explícitos.

## Módulos bajo observación
- `src/har_sanitiser/cli.py`
- `src/har_sanitiser/core.py`
- `src/har_sanitiser/utils.py`

## Frontera o zona bajo observación
Como hipótesis de trabajo (no como defecto demostrado), revisar si la separación de responsabilidades puede aclararse entre:
- capa de interfaz de línea de comandos (`cli`),
- capa de lógica principal (`core`),
- utilidades compartidas (`utils`).

## Alternativas plausibles de cleanup
1. **Ajuste mínimo de límites actuales**: mantener estructura y mover solo responsabilidades claramente fuera de capa.
2. **Extracción puntual de funciones comunes**: centralizar en `utils` helpers reutilizados por `cli` y `core`.
3. **Orquestación más explícita en `core`**: dejar `cli` como capa delgada de entrada/salida y delegación.

## Criterio para elegir entre alternativas
- Menor tamaño y riesgo de la primera PR técnica.
- Claridad de intención (una sola intención por PR).
- Validación simple con pruebas existentes y comportamiento observable.

## Fuera de alcance (PR1)
- Cambios de implementación.
- Nuevas funcionalidades.
- Reestructuración amplia del paquete.
- Cambios en tests, setup, workflows o packaging.

## Secuencia prevista de PRs
- **PR1 (esta):** delimitación documental de hipótesis y frontera.
- **PR2 (técnica, pequeña):** primer ajuste mínimo con una sola intención, validado con checks existentes.
- **PR3+ (si aplica):** iteraciones incrementales según evidencia obtenida en PR2.
