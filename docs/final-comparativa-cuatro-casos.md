# Comparativa final — mi-primer-repo vs csvtools-case vs timesheet-case vs har-file-sanitiser-case

## Propósito
Comparar los cuatro casos realizados para identificar qué señal aporta cada uno, en qué condiciones Codex rinde mejor y qué hipótesis conviene probar a continuación.

## Caso 1 — mi-primer-repo
Repositorio sandbox inicial para validar el método de trabajo con Codex en condiciones controladas.

### Qué se probó
- PRs pequeñas y de una sola intención.
- Tests puntuales.
- Bugfixes pequeños.
- Mejoras de UX acotadas.
- Refactors pequeños, incluyendo un caso multiarchivo.
- Cambios mixtos de código, tests y documentación.

### Qué señal aportó
`mi-primer-repo` confirmó que el método base funciona bien cuando:
- el contexto es simple,
- el riesgo es bajo,
- la validación es barata,
- y el alcance está claramente delimitado.

También ayudó a fijar un patrón operativo:
- contrato de trabajo claro,
- PR pequeña,
- checks explícitos,
- microevaluación humana al cierre.

## Caso 2 — csvtools-case
Case Project de cleanup arquitectónico pequeño en un entorno más real que el sandbox inicial.

### Qué se probó
- PR1 documental para delimitar alcance y hotspots.
- Cleanup local mínimo.
- Cleanup multiarchivo real.
- Blindaje con tests de la frontera tratada.
- Estabilización del entorno mínimo de tests.
- Un segundo hotspot distinto, aunque de menor entidad estructural.
- Cierre documental y artefactos reutilizables del método.

### Qué señal aportó
`csvtools-case` confirmó que Codex puede trabajar con control en un repo más real cuando:
- el hotspot está bien delimitado,
- el cambio sigue siendo pequeño y reversible,
- la validación mínima del repo es suficiente,
- y la revisión humana mantiene disciplina de alcance.

Aprendizaje clave adicional: mejorar primero la infraestructura mínima de validación aumenta la calidad de todas las PRs posteriores.

## Caso 3 — timesheet-case
Caso orientado a medir una hipótesis distinta: elección entre varias alternativas plausibles de cleanup.

### Qué se probó
- PR1 de selección explícita entre alternativas.
- PR2 técnica sobre la opción más conservadora para la frontera CLI ↔ dominio.
- Revisión crítica de una primera dirección menos conservadora.
- PR3 de blindaje con tests unitarios.
- PR4 mínima de entorno para hacer ejecutable ese blindaje.
- PR5 de retrospectiva breve de cierre.

### Qué señal aportó
`timesheet-case` añadió una señal nueva respecto a los casos anteriores: no solo que Codex puede ejecutar cambios pequeños, sino que puede participar en una decisión local entre varias opciones plausibles, siempre que existan:
- alcance explícito,
- criterio conservador,
- revisión humana disciplinada,
- y validación mínima suficiente.

También mostró que la revisión humana no solo valida ejecución, sino calidad de decisión.

## Caso 4 — har-file-sanitiser-case
Caso para medir una hipótesis de dependencias internas más ricas entre módulos (`cli`, `core`, `utils`) sin abandonar el marco de PRs pequeñas.

### Qué se probó
- PR1 documental para delimitar la frontera bajo observación.
- PR2 técnica mínima sobre un ajuste conservador de límites entre CLI y core.
- PR3 de blindaje explícito de la delegación a streaming sin prelectura redundante.
- PR4 mínima de compatibilidad para hacer ejecutable el test objetivo en Python 3.10, sin abrir un frente amplio.

### Qué señal aportó
`har-file-sanitiser-case` aportó una señal útil en un contexto con dependencias internas más ricas:
- Codex puede mantener criterio conservador en una frontera más densa.
- Puede sostener el cambio con blindaje específico.
- Puede aceptar una corrección mínima de compatibilidad cuando esa corrección sigue siendo local, explícita y de una sola intención.

También confirmó que no toda fricción de entorno justifica abrir una reforma amplia: a veces existe una salida pequeña y suficiente.

## Diferencias clave entre los cuatro casos

### mi-primer-repo
- Mayor control.
- Menor complejidad.
- Señal rápida.
- Mejor para fijar el método base.

### csvtools-case
- Más real que el sandbox.
- Útil para medir cleanup multiarchivo pequeño.
- Mejor para probar disciplina de frontera y entorno de tests.
- Buena base para extraer método reusable.

### timesheet-case
- Mejor para medir juicio entre alternativas plausibles.
- Más dependiente de revisión humana para distinguir una solución válida de la opción más conservadora.
- Buena señal sobre decisión local y reformulación.

### har-file-sanitiser-case
- Mejor para medir ajustes pequeños en dependencias internas más ricas.
- Añade complejidad modular sin exigir todavía cambios amplios.
- Buena señal sobre cuándo merece la pena una corrección mínima de compatibilidad y cuándo no.

## Aprendizajes operativos comunes
En los cuatro casos, Codex rindió mejor cuando se mantuvieron estas condiciones:
- una sola intención por PR,
- cambios pequeños y revisables,
- restricciones explícitas,
- checks claros,
- separación entre fallo del entorno y efecto del cambio,
- microevaluación humana breve tras cada revisión.

## Qué parece funcionar mejor
Codex aporta más valor cuando trabaja como:
- operador técnico de ejecución,
- en repos con validación razonablemente barata,
- sobre hotspots acotados,
- con decisiones reversibles,
- y con revisión humana que disciplina alcance y criterio.

## Límites observados
- El valor cae cuando la PR aporta más higiene local que señal estructural.
- La señal empeora cuando el entorno de validación introduce demasiado ruido.
- Aún no se ha probado un caso con dependencias internas claramente más profundas y coordinación entre varias capas con mayor densidad.
- Tampoco se ha probado todavía una decisión local con trade-offs más fuertes y más de una solución conservadora seriamente competitiva.

## Conclusión
Los cuatro casos, en conjunto, sugieren que Codex funciona bien en cambios pequeños, acotados, reversibles y bien revisados.

La evidencia acumulada es especialmente sólida en cuatro planos:
1. ejecución disciplinada de PRs pequeñas,
2. cleanup multiarchivo pequeño con validación suficiente,
3. elección conservadora entre alternativas plausibles,
4. mantenimiento del criterio en una frontera con dependencias internas más ricas.

## Recomendación del siguiente experimento
No seguir por inercia en ninguno de estos cuatro repositorios.

El siguiente Case Project debería probar una hipótesis nueva y explícita, idealmente una de estas:
1. dependencias internas más profundas entre varias capas,
2. trade-offs locales más exigentes entre varias opciones razonables,
3. coordinación entre módulos con validación parcial pero todavía controlable.

Recomendación actual: pasar a un caso donde el reto principal ya no sea solo ejecutar bien ni elegir bien en una frontera local, sino sostener decisiones razonables en un sistema algo más denso sin perder disciplina de PR pequeña.
