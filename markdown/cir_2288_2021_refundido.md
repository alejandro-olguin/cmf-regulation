<!-- source: cir_2288_2021_refundido.pdf -->
<!-- language: es -->
<!-- note: Las fórmulas matemáticas extraídas de PDFs pueden ser incompletas.
     Los bloques marcados con ⚠️ deben verificarse contra el PDF original. -->

# CIRCULAR N° 2288

### SISTEMA DE RIESGOS
(Instrucciones generales)
## 1. ARCHIVOS DEL SISTEMA DE RIESGOS
Este sistema comprende los archivos signados con la letra “R”, indicados en el Catálogo de Archivos a excepción de los archivos R04 y R05 .
Estos archivos tienen por objetivo implementar los estándares de Basilea, los cuales están contenidos entre las normas 21-1 a 21-30 de la Recopilación Actualizada de Normas para bancos (RAN).
Esta Comisión mantiene los archivos en sus versiones actualizadas, incluyendo los códigos y conceptos que deben incluirse, información que puede ser modificada cada vez que se introduzca un cambio en los mencionados Capítulos de la RAN.
## 2. MONEDA
Todos los montos deberán ser informados en pesos, salvo que en las instrucciones del respectivo archivo se indique expresamente lo contrario.
Los saldos de operaciones pagaderas en monedas extranjeras deberán convertirse a pesos chilenos, de acuerdo con el tipo de cambio de representación contable utilizado por el banco.
Circular N°2.288 / 27.04.2021 por Resolución N°2256

Archivo R01 Hoja 1
CÓDIGO : R01
NOMBRE : LÍMITES DE SOLVENCIA Y PATRIMONIO EFECTIVO
SISTEMA : Riesgos PERIODICIDAD : Mensual PLAZO : 9 días hábiles.
En este archivo se informarán los datos utilizados para el cálculo de los límites legales entre capital básico y activos totales, capital básico y activos ponderados por riesgo, patrimonio efectivo y activos ponderados por riesgo, entre otros límites mencionados en el artículo 66 de la Ley General de Bancos (LGB). Adicionalmente, se deben informar los ajustes regulatorios prudenciales y exclusiones a las partidas de activos y pasivos que se aplicarán en el cómputo del patrimonio efectivo de un banco, de acuerdo con las disposiciones del Capítulo 21-1 de la Recopilación Actualizada de Normas (RAN).
Los datos que deben proporcionarse se refieren a la situación consolidada global, situación consolidada local y al banco sin consolidar (individual).
Primer registro
1. Código del banco ............................................................................................. 9(04)
2. Identificación del archivo ................................................................................. X(03)
3. Período ............................................................................................................. P(06)
4. Filler ................................................................................................................. X(119)
Largo del registro ............................... 132 bytes
## 1. CÓDIGO DEL BANCO
Corresponde al código que identifica al banco.
## 2. IDENTIFICACIÓN DEL ARCHIVO
Corresponde a la identificación del archivo. Debe ser "R01".
## 3. PERÍODO
Corresponde al mes (AAAAMM) al cual se refiere la información.
Registros siguientes Los registros siguientes contendrán información sobre el cálculo de los límites legales establecidos en el artículo 66 de la LGB y los ajustes regulatorios que se aplicarán en el cómputo del patrimonio efectivo, de acuerdo con las disposiciones establecidas en el Capítulo
21-1 de la RAN, correspondientes al periodo al que se refiere la información. Esta información se identificará en el primer campo de cada registro, según los códigos:
Código Tipo de registro
01 Límites de solvencia y componentes del patrimonio efectivo.
02 Ajustes regulatorios y exclusiones de partidas de activos o pasivos.
03 Filiales que dan origen a interés no controlador en la situación consolidada del
banco.
04 Exposición en inversiones significativas y no significativas
Circular N°2.288 / 27.04.2021 por Resolución N°2256

Archivo R01 Hoja 2 Registro para informar límites de solvencia y componentes del patrimonio efectivo
1. Tipo de registro ........................................................................................ 9(02)
2. Nivel de consolidación .............................................................................. 9(01)
3. Capital básico ............................................................................................ 9(14)
4. Capital nivel 1 ............................................................................................ 9(14)
5. Capital nivel 2 .......................................................................................... 9(14)
6. Patrimonio efectivo ................................................................................... 9(14)
7. Activos ponderados por riesgo .................................................................. 9(14)
8. Activos totales ........................................................................................... 9(14)
9. Índice de adecuación del capital (IAC) ..................................................... 9(02)V9(03)
10. Índice de apalancamiento ......................................................................... 9(02)V9(03)
11. Índice capital básico .................................................................................. 9(02)V9(03)
12. Índice de capital nivel 1 ............................................................................. 9(02)V9(03)
13. Cargo banco sistémico .............................................................................. 9(02)V9(03)
14. Cargo pilar 2 .............................................................................................. 9(02)V9(03)
15. CET1 adicional disponible ........................................................................ 9(02)V9(03)
16. Nivel requerido de colchones .................................................................... 9(02)V9(03)
17. Déficit colchones ...................................................................................... 9(02)V9(03)
Largo del registro ............... 132 bytes
## 1. TIPO DE REGISTRO
Corresponde al código que identifica el tipo de registro. Debe ser “01”.
## 2. NIVEL DE CONSOLIDACIÓN
Corresponde al código asociado al nivel de consolidación, el cual se deberá indicar según la Tabla 80 de este Manual.
## 3. CAPITAL BÁSICO
Corresponde al monto del capital básico definido en el Capítulo 21-1 de la RAN, identificado bajo la expresión CET1_6.
## 4. CAPITAL NIVEL 1
Corresponde al monto del capital nivel 1 definido en el Capítulo 21-1 de la RAN, identificado como la suma de CET1_6 y AT1_5.
## 5. CAPITAL NIVEL 2
Corresponde al monto del capital nivel 2 definido en el Capítulo 21-1 de la RAN, identificado bajo la expresión T2_5.
## 6. PATRIMONIO EFECTIVO
Corresponde al monto compuesto por la suma de los factores capital nivel 1 y capital nivel 2, luego de todos los ajustes establecidos en el Capítulo 21-1 de la RAN.
## 7. ACTIVOS PONDERADOS POR RIESGO
Corresponde al monto obtenido de la suma de los activos ponderados por riesgo de crédito, de mercado y operacional, de acuerdo con lo establecido en el Título 7 del Capítulo 21-6 de la RAN.
Circular N°2.288 / 27.04.2021 por Resolución N°2256

Archivo R01 Hoja 3 Para el cálculo de este monto se deben utilizar los activos ponderados por riesgo bajo metodologías internas, si es que el banco cuenta con autorización de la Comisión, o en caso contrario, metodologías estándar. Adicionalmente, cuando se utilicen metodologías internas, se debe considerar el piso mínimo u output floor del 72,5% del total que se hubiese obtenido con las metodologías estándar, de acuerdo con la siguiente fórmula.
APR = max{APRC +APRM +APRO ; 72,5%
### MI ME ME ⋅[APRC +APRM +APRO ] } ME ME ME
## 8. ACTIVOS TOTALES
Corresponde al monto de los activos totales calculado según lo dispuesto en el numeral 3 del Título I del Capítulo 21-30 de la RAN.
## 9. ÍNDICE DE ADECUACIÓN DE CAPITAL
Corresponde a la razón entre el patrimonio efectivo (campo 6) y los activos ponderados por riesgo del banco (campo 7), multiplicado por 100.
## 10. ÍNDICE DE APALANCAMIENTO
Corresponde a la razón entre el capital básico (campo 3) y los activos totales del banco (campo 8), multiplicado por 100.
## 11. ÍNDICE DE CAPITAL BÁSICO
Corresponde a la razón entre el capital básico (campo 3) y los activos ponderados por riesgo del banco (campo 7), multiplicado por 100.
## 12. ÍNDICE DE CAPITAL NIVEL 1
Corresponde a la razón entre el capital nivel 1 (campo 4) y los activos ponderados por riesgo del banco (campo 7), multiplicado por 100.
## 13. CARGO BANCO SISTÉMICO
Corresponde al cargo de capital establecido en el Capítulo 21-11 de la RAN.
## 14. CARGO PILAR 2
Corresponde a los cargos de patrimonio efectivo establecidos en el Capítulo 21-13 de la RAN.
## 15. CET1 ADICIONAL DISPONIBLE
Corresponde al capital básico adicional disponible, señalado en el Título IV del Capítulo 21-12 de la RAN, como fracción de los activos ponderados por riesgo, multiplicado por 100.
## 16. NIVEL REQUERIDO DE COLCHONES
Corresponde al valor de los colchones que el banco debe de cumplir, definido como el “nivel requerido” en el Título IV del Capítulo 21-12 de la RAN.
## 17. DÉFICIT COLCHONES
Corresponde a la razón entre el CET1 adicional disponible (campo 15) y el requerimiento de los colchones de conservación y contra cíclico, multiplicado por
100, de acuerdo con lo señalado en el Título IV del Capítulo 21-12 de la RAN. En caso de no existir déficit de colchones se debe reportar cero.
Circular N°2.288 / 27.04.2021 por Resolución N°2256

Archivo R01 Hoja 4 Registro para informar ajustes regulatorios y exclusiones de partidas de activos o pasivos
1. Tipo de registro ......................................................................................... 9(02)
2. Nivel de consolidación ............................................................................... 9(01)
3. Nivel de ajuste ............................................................................................ 9(02)
4. Tipo de ajuste ............................................................................................. 9(02)
5. Monto ......................................................................................................... s9(14)
6. Filler ........................................................................................................... X(111)
Largo del registro ............... 132 bytes
## 1. TIPO DE REGISTRO
Corresponde al código que identifica el tipo de registro. Debe ser “02”.
## 2. NIVEL DE CONSOLIDACIÓN
Corresponde al código asociado al nivel de consolidación, el cual se deberá indicar según la Tabla 80 de este Manual.
## 3. NIVEL DE AJUSTE
Corresponde al código asociado al componente de patrimonio efectivo sobre el cual se realiza el ajuste regulatorio o la exclusión. Los códigos corresponden a:
01 Capital básico, CET1
02 Capital adicional nivel 1, AT1
03 Capital nivel 2, T2
## 4. TIPO DE AJUSTES
Corresponde al código asociado al capital base y a los tipos de ajustes regulatorios o exclusiones realizadas sobre este, de acuerdo con lo señalado en el Título II y III del Capítulo 21-1 de la RAN. Se deberá indicar según los códigos de la Tabla 107 de este Manual.
## 5. MONTO
Corresponde al monto por deducir o agregar a cada nivel de capital inicial (CET_1, AT_1 y T2_1) para cada tipo de ajuste del campo 5, de acuerdo con las instrucciones señaladas en el Capítulo 21-1 de la RAN.
Registro para informar filiales en la situación consolidada del banco.
Se deben informar todas las filiales directas sobre las cuales el banco tiene control, incluyéndose las filiales indirectas consolidadas con aquellas filiales directas, que han sido consideradas en la situación consolidada del banco, independiente del porcentaje de participación del banco sobre la filial directa.
1. Tipo de registro ........................................................................................ 9(02)
2. Código institución ..................................................................................... 9(04)
3. Domicilio de la filial ................................................................................. 9(02)
4. Actividad económica ................................................................................ 9(04)
5. Activos ....................................................................................................... 9(14)
6. Pasivos ...................................................................................................... 9(14)
7. Patrimonio ............................................................................................... s9(14)
8. Participación del banco ............................................................................ 9(02)V9(03)
Circular N°2.288 / 27.04.2021 por Resolución N°2256

Archivo R01 Hoja 5
9. Capital total ............................................................................................... 9(14)
10. Capital regulatorio requerido ................................................................... 9(14)
11. Filler .......................................................................................................... X(44)
Largo del registro ...................... 132 bytes
## 1. TIPO DE REGISTRO
Corresponde al código que identifica el tipo de registro. Debe ser “03”.
## 2. CÓDIGO INSTITUCIÓN
Corresponde al código de la institución filial reportada según la codificación dada por esta Comisión.
## 3. DOMICILIO DE LA FILIAL
Corresponde al código que indica si la filial tiene su domicilio legal en Chile o en el extranjero. Los códigos corresponden a:
01 Chile
02 Extranjero
## 4. ACTIVIDAD ECONÓMICA
Se refiere a la actividad económica de la filial consignada de acuerdo con las categorías del Clasificador Chileno de Actividades Económicas (CIIU.CL). Se deberá representar la actividad principal de la filial con una categoría de cuatro dígitos (nivel de clase), conforme a la versión oficial vigente del Clasificador Chileno de Actividades Económicas publicado por el Instituto Nacional de Estadísticas.
## 5. ACTIVOS
Corresponde al total de activos consolidado de la filial, según su último estado de situación financiera.
## 6. PASIVOS
Corresponde al total de pasivos con terceros consolidado de la filial, sin considerar patrimonio, según su último estado de situación financiera.
## 7. PATRIMONIO
Corresponde al total de patrimonio consolidado de la filial, según su último estado de situación financiera.
## 8. PARTICIPACIÓN DEL BANCO
Corresponde al porcentaje de participación del banco en la filial, multiplicado por
100.
## 9. CAPITAL TOTAL
Corresponde al capital disponible de la filial para dar cumplimiento a los requisitos legales establecidos por la autoridad respectiva, según la fórmula correspondiente del numeral 1 del Título II del Capítulo 21-1 de la RAN, utilizada para el cómputo del exceso de capital regulatorio.
Circular N°2.288 / 27.04.2021 por Resolución N°2256

Archivo R01 Hoja 6
## 10. CAPITAL REGULATORIO REQUERIDO
Corresponde al capital regulatorio que la filial debe mantener para dar cumplimiento a los requisitos establecidos por la autoridad respectiva, según la fórmula correspondiente del numeral 1 del Título III del Capítulo 21-1 de la RAN, utilizada para el cómputo del exceso de capital regulatorio.
Registro para informar exposición en inversiones significativas y no significativas Se debe informar la inversión que mantenga el banco en otras empresas financieras sobre las cuales el banco no tenga el control según la NIIF10, sean bancarias o no bancarias, y que no son consolidadas en los estados financieros del banco. Se exceptuarán de este registro aquellas inversiones en sociedades que presten, única y exclusivamente, servicios destinados a facilitar el cumplimiento de los fines de los bancos, y/o aquellas que el banco utiliza para efectuar determinadas operaciones de su giro, definidas como sociedades de apoyo al giro (SAG) según el Capítulo 11-6 de la RAN. Cuando se trate de inversiones en el extranjero, aplicará la misma excepción cuando las inversiones sean asimilables a las sociedades de apoyo al giro que indica el Capítulo 11-6 de la RAN.
1. Tipo de registro ........................................................................................ 9(02)
2. Código identificador único ........................................................................ X(12)
3. Identificador ............................................................................................. 9(02)
4. Descripción emisión.................................................................................. X(50)
5. Tenedor del instrumento .......................................................................... 9(02)
6. Tipo de exposición .................................................................................... 9(02)
7. Tipo de instrumento ................................................................................. 9(02)
8. Monto de la exposición ............................................................................. 9(14)
9. Filler .......................................................................................................... X(46)
Largo del registro ............... 132 bytes
## 1. TIPO DE REGISTRO
Corresponde al código que identifica el tipo de registro. Debe ser “04”.
## 2. CÓDIGO IDENTIFICADOR ÚNICO
Corresponde al código identificador de la emisión otorgado por alguna plataforma financiera. Se aceptan los códigos NEMO, ISIN, BBG, RIC, SEUDOL y CUSIP, consistente con lo reportado en el campo 4. En caso de que la emisión no esté listada en bolsa reportar 999.
## 3. IDENTIFICADOR
Corresponde al tipo de código identificador único reportado. Se deberá indicar según los códigos de la Tabla 108 de este Manual.
## 4. DESCRIPCIÓN EMISIÓN
Corresponde a la descripción de la emisión y su contraparte, principalmente, cuando se trate de emisores extranjeros que no posean Rut o vehículos legales en el exterior, y cuando la inversión no esté públicamente listada en Bolsa.
## 5. TENEDOR DEL INSTRUMENTO
Corresponde al código con el cual se identifica al tenedor del instrumento. Los
códigos corresponden a:
01 Banco matriz
02 Filial domiciliada en Chile
03 Filial domiciliada en el extranjero
Circular N°2.288 / 27.04.2021 por Resolución N°2256

Archivo R01 Hoja 7
## 6. TIPO DE EXPOSICIÓN
Corresponde al código con el cual se identifica el tipo de exposición, según si es significativa o no significativa, de acuerdo con el numeral 3 y 4 del Título III del Capítulo 21-1 de la RAN respectivamente. Los códigos corresponden a:
01 Inversión no significativa
02 Inversión significativa
## 7. TIPO DE INSTRUMENTO
Corresponde al código que clasifica la exposición según el tipo de capital regulatorio al cual debe ser asignado para su tratamiento, de acuerdo con el numeral 3 y 4 para exposiciones no significativas y significativas, respectivamente, del Título III del Capítulo 21-1 de la RAN. Los códigos corresponden a:
01 Exposición en capital ordinario de nivel 1
02 Exposición en instrumentos de capital adicional de nivel 1
03 Exposición en instrumentos de capital nivel 2
04 Exposición en instrumentos TLAC de bancos G-SIB
## 8. MONTO DE LA EXPOSICIÓN
Corresponde al monto de la exposición, estimada según el numeral 3 y 4 del Título III del Capítulo 21-1 de la RAN, para el caso de inversiones no significativas y significativas, respectivamente.
Carátula de cuadratura El archivo R01 debe entregarse con una carátula de cuadratura cuyo modelo se
especifica a continuación:
MODELO Institución: ________________________________ Código: _______ Información correspondiente al mes de: _________________ Archivo R01

| Número de registros |  |
| --- | --- |
| Número de registros con código 01 en el campo 1 |  |
| Número de registros con código 02 en el campo 1 |  |
| Número de registros con código 03 en el campo 1 |  |
| Número de registros con código 04 en el campo 1 |  |

Observaciones En los registros anteriores se incluirán solo las combinaciones que resulten atingentes al banco.
Los valores informados durante el 01 de diciembre de 2021 y el 01 de diciembre de
2025 considerarán las disposiciones transitorias graduales establecidas para los
componentes afectos a estas disposiciones.
Circular N°2.288 / 27.04.2021 por Resolución N°2256

Archivo R02 Hoja 1
CÓDIGO : R02
NOMBRE : INSTRUMENTOS DE CAPITAL REGULATORIO
SISTEMA : Riesgos PERIODICIDAD : Semestral PLAZO : 9 días hábiles.
En este archivo se informarán los instrumentos constitutivos de capital regulatorio:
acciones ordinarias, acciones preferentes, bonos sin plazo fijo de vencimiento y bonos subordinados, vigentes a la fecha de referencia de la información.
Este archivo también debe ser reportado por las filiales en Chile y en el extranjero.
Primer registro
1. Código del banco ......................................................................................... 9(04)
2. Identificación del archivo ............................................................................ X(03)
3. Período ......................................................................................................... P(06)
4. Filler ............................................................................................................. X(115)
Largo del registro ............................. 128 bytes
## 1. CÓDIGO DEL BANCO
Corresponde al código que identifica al banco.
## 2. IDENTIFICACIÓN DEL ARCHIVO
Corresponde a la identificación del archivo. Debe ser "R02".
## 3. PERÍODO
Corresponde al último mes del semestre al cual se refiere la información.
Registros siguientes Los registros siguientes contendrán información sobre las emisiones de instrumentos de capital correspondientes al periodo al que se refiere la información. Esta información se identificará en el primer campo de cada registro, según los códigos:
Código Tipo de registro
01 Emisiones de acciones ordinarias
02 Emisiones de acciones preferentes
03 Emisiones de bonos sin plazo fijo de vencimiento
04 Emisiones de bonos subordinados
Circular N°2.288 / 27.04.2021 por Resolución N°2256

Archivo R02 Hoja 2 Registro para informar emisiones de acciones ordinarias Se deben informar las emisiones de acciones ordinarias de pago y aquellas liberadas de pago que computan como patrimonio efectivo. Adicionalmente, si ha ocurrido una conversión en acciones de algún instrumento de capital, se deben registrar aquellas acciones correspondientes a la proporción en que se realizó la conversión.
1. Tipo de registro .................................................................................. 9(02)
2. Fecha de inscripción ........................................................................... F(08)
3. Código institución emisora ................................................................ 9(04)
4. Código identificador único ................................................................. X(12)
5. Identificador ....................................................................................... 9(02)
6. Número de inscripción ....................................................................... X(30)
7. Serie .................................................................................................... X(01)
8. Número acciones serie........................................................................ 9(14)
9. Monto total pagado ............................................................................ 9(14)
10. Capital regulatorio .............................................................................. 9(02)
11. Monto computable como capital regulatorio ..................................... 9(14)
12. Filler.................................................................................................... X(25)
Largo del registro ............... 128 bytes
## 1. TIPO DE REGISTRO
Corresponde al código que identifica el tipo de registro. Debe ser “01”.
## 2. FECHA DE INSCRIPCIÓN
Corresponde a la fecha en que se realiza la inscripción de las emisiones en el Registro de Valores de la Comisión.
## 3. CÓDIGO INSTITUCIÓN EMISORA
Corresponde al código de la institución emisora de las acciones ordinarias según la codificación dada por esta Comisión.
## 4. CÓDIGO IDENTIFICADOR ÚNICO
Corresponde al código identificador de la emisión otorgado por alguna plataforma financiera. Se aceptan los códigos NEMO, ISIN, BBG, RIC, SEUDOL y CUSIP, consistente con lo reportado en el campo 5. En caso de que la emisión no esté listada en bolsa reportar 999.
## 5. IDENTIFICADOR
Corresponde al tipo de código identificador único reportado. Se deberá indicar según los códigos de la Tabla 108 de este Manual.
## 6. NÚMERO DE INSCRIPCIÓN
Corresponde al número de inscripción de la emisión en el Registro de Valores de la Comisión.
## 7. SERIE
Corresponde al código que identifica la serie de acciones de acuerdo con la inscripción en el Registro de Valores. Se deberá indicar según los códigos de la Tabla 29 de este Manual.
## 8. NÚMERO ACCIONES SERIE
Corresponde al número total de acciones de la serie reportada en el campo 7, es decir, aquellas acciones que se encuentren suscritas y pagadas. No considera a las acciones adquiridas por el propio banco.
Circular N°2.288 / 27.04.2021 por Resolución N°2256

Archivo R02 Hoja 3
## 9. MONTO TOTAL PAGADO
Corresponde al capital total pagado por terceros respecto de la serie reportada en el campo 7, según lo registrado en los estados financieros del banco.
## 10. CAPITAL REGULATORIO
Corresponde al código asociado a si las acciones ordinarias reportadas reúnen las condiciones establecidas en el Capítulo 21-1 de la RAN para contabilizarse como patrimonio efectivo.
01 Sí
02 No
## 11. MONTO COMPUTABLE COMO CAPITAL REGULATORIO
Corresponde al monto ajustado por el no reconocimiento de emisiones que no cumplan con los requisitos establecidos en el Anexo 1 del Capítulo 21-1 de la RAN para acciones emitidas por filiales en el extranjero.
Registro para informar emisiones de acciones preferentes En este archivo se informarán las acciones preferentes constitutivas de capital regulatorio, solo en los casos en que el banco o filial tenga emisiones de este tipo. En caso contrario, no deberá informar el registro.
1. Tipo de registro ........................................................................................... 9(02)
2. Fecha de inscripción .................................................................................... F(08)
3. Código institución emisora ......................................................................... 9(04)
4. Código identificador único ......................................................................... X(12)
5. Identificador ................................................................................................ 9(02)
6. Número de inscripción ................................................................................ X(30)
7. Serie ............................................................................................................. X(01)
8. Número acciones serie................................................................................. 9(14)
9. Tipo de preferencias ................................................................................... 9(02)
10. Monto total pagado ..................................................................................... 9(14)
11. Capital regulatorio ....................................................................................... 9(02)
12. Monto computable como capital regulatorio .............................................. 9(14)
13. Mecanismo going concern de absorción de pérdidas ................................ 9(02)
14. Gatillo going concern consolidado local ..................................................... 9(01)V9(03)
15. Gatillo going concern consolidado global ................................................... 9(01)V9(03)
16. Precio de conversión ................................................................................... 9(02)
17. Tipo de adquisición ..................................................................................... 9(02)
18. Primera fecha de adquisición ...................................................................... F(08)
19. Filler............................................................................................................. X(01)
Largo del registro ............................. 128 bytes
## 1. TIPO DE REGISTRO
Corresponde al código que identifica el tipo de registro. Debe ser “02”.
## 2. FECHA DE INSCRIPCIÓN
Corresponde a la fecha en que se realiza la inscripción de las emisiones en el Registro de Valores de la Comisión.
Circular N°2.288 / 27.04.2021 por Resolución N°2256

Archivo R02 Hoja 4
## 3. CÓDIGO INSTITUCIÓN EMISORA
Corresponde al código de la institución emisora de las acciones preferentes según la codificación dada por esta Comisión.
## 4. CÓDIGO IDENTIFICADOR ÚNICO
Corresponde al código identificador de la emisión otorgado por alguna plataforma financiera. Se aceptan los códigos NEMO, ISIN, BBG, RIC, SEUDOL y CUSIP, consistente con lo reportado en el campo 5. En caso de que la emisión no esté listada en bolsa reportar 999.
## 5. IDENTIFICADOR
Corresponde al tipo de código identificador único reportado. Se deberá indicar según los códigos de la Tabla 108 de este Manual.
## 6. NÚMERO DE INSCRIPCIÓN
Corresponde al número de inscripción de la emisión en el Registro de Valores de la Comisión.
## 7. SERIE
Corresponde al código que identifica la serie de acciones preferentes de acuerdo con la inscripción en el Registro de Valores. Se deberá indicar según los códigos de la Tabla 29 de este Manual.
## 8. NÚMERO ACCIONES SERIE
Corresponde al número total de acciones de la serie reportada en el campo 7, es decir, aquellas acciones que se encuentren suscritas y pagadas. No considera a las acciones adquiridas por el propio banco.
## 9. TIPO DE PREFERENCIAS
Corresponde al código asociado al tipo de preferencias de orden patrimonial otorgadas a los titulares. Los códigos corresponden a:
01 Prioridad en el pago de dividendos con derecho a voto limitado
02 Prioridad en el pago de dividendos sin derecho a voto
03 Derecho a una proporción determinada o determinable de las utilidades
líquidas con derecho a voto limitado
04 Derecho a una proporción determinada o determinable de las utilidades
líquidas sin derecho a voto
## 10. MONTO TOTAL PAGADO
Corresponde al capital total pagado por terceros respecto de la serie reportada en el campo 7, según lo registrado en los estados financieros del banco.
## 11. CAPITAL REGULATORIO
Corresponde al código asociado a si las acciones preferentes reportadas reúnen las condiciones establecidas en el Capítulo 21-2 de la RAN para contabilizarse como patrimonio efectivo.
01 Sí
02 No
Circular N°2.288 / 27.04.2021 por Resolución N°2256

Archivo R02 Hoja 5
## 12. MONTO COMPUTABLE COMO CAPITAL REGULATORIO
Corresponde al monto ajustado por el no reconocimiento producido en el caso que las emisiones no cumplan con las condiciones establecidas en el Capítulo 212 de la RAN y en el caso de emisiones realizadas por filiales en el extranjero y que deben ser descontadas del monto computable como capital regulatorio de acuerdo con el Capítulo 21-1 de la RAN.
## 13. MECANISMO GOING CONCERN DE ABSORCIÓN DE PÉRDIDAS
Corresponde al código asociado al mecanismo de absorción de pérdida de los instrumentos en gatillos going concern. Los códigos corresponden a:
01 Conversión parcial a acciones ordinarias.
02 Conversión total a acciones ordinarias.
## 14. GATILLO GOING CONCERN CONSOLIDADO LOCAL
Corresponde al nivel del gatillo going concern estipulado en las condiciones contractuales para el nivel de consolidación local.
## 15. GATILLO GOING CONCERN CONSOLIDADO GLOBAL
Corresponde al nivel del gatillo going concern estipulado en las condiciones contractuales para el nivel de consolidación global.
## 16. PRECIO DE CONVERSIÓN
Corresponde al código asociado al tipo de precio con el cual se determinará el número de acciones a convertir, una vez que se activen los gatillos. Los códigos
corresponden a:
01 Valor de mercado
02 Valor libro
03 Valor mínimo preestablecido
09 Otro – No aplica
## 17. TIPO DE ADQUISICIÓN
Corresponde al código asociado al tipo de adquisición. Los códigos corresponden
a:
01 Total
02 Parcial
## 18. PRIMERA FECHA DE ADQUISICIÓN
Corresponde a la fecha en que está estipulada la primera adquisición del instrumento.
Registro para informar emisiones de bonos sin plazo fijo de vencimiento En este archivo se informarán los bonos sin plazo fijo de vencimiento constitutivas de capital regulatorio, solo en los casos en que el banco o filial tenga emisiones de este tipo. En caso contrario, no deberá informar el registro.
1. Tipo de registro .................................................................................. 9(02)
2. Fecha de inscripción ........................................................................... F(08)
3. Código institución emisora ................................................................ 9(04)
Circular N°2.288 / 27.04.2021 por Resolución N°2256

Archivo R02 Hoja 6
4. Código identificador único ................................................................. X(12)
5. Identificador ....................................................................................... 9(02)
6. Número de inscripción ....................................................................... X(30)
7. Serie .................................................................................................... X(15)
8. Monto total pagado ............................................................................ 9(14)
9. Capital regulatorio .............................................................................. 9(02)
10. Monto computable como capital regulatorio ..................................... 9(14)
11. Mecanismo going concern de absorción de pérdidas ........................ 9(02)
12. Mecanismo gone concern de absorción de pérdidas ......................... 9(02)
13. Gatillo going concern consolidado local ............................................ 9(01)V9(03)
14. Gatillo going concern consolidado global .......................................... 9(01)V9(03)
15. Precio de conversión .......................................................................... 9(02)
16. Tipo de rescate .................................................................................... 9(02)
17. Primera fecha de rescate .................................................................... F(08)
18. Filler.................................................................................................... X(01)
Largo del registro ............... 128 bytes
## 1. TIPO DE REGISTRO
Corresponde al código que identifica el tipo de registro. Debe ser “03”.
## 2. FECHA DE INSCRIPCIÓN
Corresponde a la fecha en que se realiza la inscripción de las emisiones en el Registro de Valores de la Comisión.
## 3. CÓDIGO INSTITUCIÓN EMISORA
Corresponde al código de la institución emisora de las acciones ordinarias según la codificación dada por esta Comisión.
## 4. CÓDIGO IDENTIFICADOR ÚNICO
Corresponde al código identificador de la emisión otorgado por alguna plataforma financiera. Se aceptan los códigos NEMO, ISIN, BBG, RIC, SEUDOL y CUSIP, consistente con lo reportado en el campo 5. En caso de que la emisión no esté listada en bolsa reportar 999.
## 5. IDENTIFICADOR
Corresponde al tipo de código identificador único reportado. Se deberá indicar según los códigos de la Tabla 108 de este Manual.
## 6. NÚMERO DE INSCRIPCIÓN
Corresponde al número de inscripción de la emisión en el Registro de Valores de la Comisión.
## 7. SERIE
Corresponde al código que identifica la serie del instrumento de acuerdo con la inscripción en el Registro de Valores.
## 8. MONTO TOTAL PAGADO
Corresponde al capital total pagado por terceros respecto de la serie reportada en el campo 7, según lo registrado en los estados financieros del banco.
Circular N°2.288 / 27.04.2021 por Resolución N°2256

Archivo R02 Hoja 7
## 9. CAPITAL REGULATORIO
Corresponde al código asociado a si los bonos sin plazo fijo de vencimiento reportados reúnen las condiciones establecidas en el Capítulo 21-2 de la RAN para contabilizarse como patrimonio efectivo.
01 Sí
02 No
## 10. MONTO COMPUTABLE COMO CAPITAL REGULATORIO
Corresponde al monto ajustado por el no reconocimiento producido en el caso que las emisiones no cumplan con las condiciones establecidas en el Capítulo
21-2 de la RAN y en el caso de emisiones realizadas por filiales en el extranjero y que deben ser descontadas del monto computable como capital regulatorio de acuerdo con el Capítulo 21-1 de la RAN.
## 11. MECANISMO GOING CONCERN DE ABSORCIÓN DE PÉRDIDAS
Corresponde al código asociado al mecanismo de absorción de pérdida de los instrumentos en gatillos going concern. Los códigos corresponden a:
01 Conversión parcial a acciones ordinarias
02 Conversión total a acciones ordinarias
03 Depreciación a $10 pesos
04 Caducidad
## 12. MECANISMO GONE CONCERN DE ABSORCIÓN DE PÉRDIDAS Corresponde
al código asociado al mecanismo de absorción de pérdida de los instrumentos en gatillos gone concern. Los códigos corresponden a:
01 Conversión a acciones ordinarias.
02 Caducidad
## 13. GATILLO GOING CONCERN CONSOLIDADO LOCAL
Corresponde al nivel del gatillo going concern estipulado en las condiciones contractuales para el nivel de consolidación local.
## 14. GATILLO GOING CONCERN CONSOLIDADO GLOBAL
Corresponde al nivel del gatillo going concern estipulado en las condiciones contractuales para el nivel de consolidación global.
## 15. PRECIO DE CONVERSIÓN
Corresponde al código asociado al tipo de precio con el cual se determinará el número de acciones a convertir, una vez que se activen los gatillos. Los códigos
corresponden a:
01 Valor de mercado
02 Valor libro
03 Valor mínimo preestablecido
09 Otro - No aplica
## 16. TIPO DE RESCATE
Corresponde al código asociado al tipo de rescate, Los códigos corresponden a:
01 Total
02 Parcial
Circular N°2.288 / 27.04.2021 por Resolución N°2256

Archivo R02 Hoja 8
## 17. PRIMERA FECHA DE RESCATE
Corresponde a la fecha en que está estipulado el primer rescate del instrumento.
Registro para informar emisiones de bonos subordinados
1. Tipo de registro .................................................................................. 9(02)
2. Fecha de inscripción ........................................................................... F(08)
3. Código institución emisora ................................................................ 9(04)
4. Código identificador único ................................................................. X(12)
5. Identificador ....................................................................................... 9(02)
6. Número de inscripción ....................................................................... X(30)
7. Serie .................................................................................................... X(15)
8. Monto total pagado ............................................................................ 9(14)
9. Capital regulatorio .............................................................................. 9(02)
10. Monto computable como capital regulatorio ..................................... 9(14)
11. Fecha vencimiento residual ................................................................ F(08)
12. Mecanismo gone concern de absorción de pérdida .......................... 9(02)
13. Filler.................................................................................................... X(15)
Largo del registro ............... 128 bytes
## 1. TIPO DE REGISTRO
Corresponde al código que identifica el tipo de registro. Debe ser “04”.
## 2. FECHA DE INSCRIPCIÓN
Corresponde a la fecha en que se realiza la inscripción de las emisiones en el Registro de Valores de la Comisión.
## 3. CÓDIGO INSTITUCIÓN EMISORA
Corresponde al código de la institución emisora de las acciones ordinarias según la codificación dada por esta Comisión.
## 4. CÓDIGO IDENTIFICADOR ÚNICO
Corresponde al código identificador de la emisión otorgado por alguna plataforma financiera. Se aceptan los códigos NEMO, ISIN, BBG, RIC, SEUDOL y CUSIP, consistente con lo reportado en el campo 5. En caso de que la emisión no esté listada en bolsa reportar 999.
## 5. IDENTIFICADOR
Corresponde al tipo de código identificador único reportado. Se deberá indicar según los códigos de la Tabla 108 de este Manual.
## 6. NÚMERO DE INSCRIPCIÓN
Corresponde al número de inscripción de la emisión en el Registro de Valores de la Comisión.
## 7. SERIE
Corresponde al código que identifica la serie del instrumento de acuerdo con la inscripción en el Registro de Valores
## 8. MONTO TOTAL PAGADO
Corresponde al capital total pagado por terceros respecto de la serie reportada en el campo 7, según lo registrado en los estados financieros del banco.
Circular N°2.288 / 27.04.2021 por Resolución N°2256

Archivo R02 Hoja 9
## 9. CAPITAL REGULATORIO
Corresponde al código asociado a si los bonos subordinados reportados reúnen las condiciones establecidas en el Capítulo 21-3 de la RAN para contabilizarse como patrimonio efectivo.
01 Sí
02 No
## 10. MONTO COMPUTABLE COMO CAPITAL REGULATORIO
Corresponde al monto ajustado por el porcentaje computable como capital por cada año que transcurra desde que falten seis años para la fecha de vencimiento residual de la emisión (campo 11), de acuerdo con lo establecido en el Título IV del Capítulo 21-3. Adicionalmente, se debe considerar el monto ajustado por la razón de reconocimiento producida en el caso que las emisiones no cumplan con las condiciones establecidas en el Capítulo 21-3 de la RAN y el monto ajustado por la razón de reconocimiento producida en el caso de emisiones realizadas por filiales en el extranjero y que deben ser descontadas del monto computable como capital regulatorio de acuerdo con el Capítulo 21-1 de la RAN.
## 11. FECHA VENCIMIENTO RESIDUAL
Corresponden a la fecha de vencimiento del bono subordinado reportado.
## 12. MECANISMO GONE CONCERN DE ABSORCIÓN DE PÉRDIDAS
Corresponde al código asociado al mecanismo de absorción de pérdida de los instrumentos en gatillos gone concern. Los códigos corresponden a:
01 Conversión a acciones ordinarias
02 Caducidad
Carátula de cuadratura El archivo R02 debe entregarse con una carátula de cuadratura cuyo modelo se
especifica a continuación:
MODELO Institución: ________________________________ Código: _______ Información correspondiente al semestre de: ______________Archivo R02

| Número de registros |  |
| --- | --- |
| Número de registros con código 01 en el campo 1 |  |
| Número de registros con código 02 en el campo 1 |  |
| Número de registros con código 03 en el campo 1 |  |
| Número de registros con código 04 en el campo 1 |  |

Observaciones En cada reporte del archivo se debe informar el stock total de instrumentos de capital regulatorio que tenga el banco en dicho periodo, considerando emisiones nuevas y cambios en las características de emisiones reportadas previamente En el caso en que el banco no tenga nuevas emisiones en el periodo, el banco deberá informar el mismo stock total de instrumentos que reportó en la última entrega de información a la Comisión.
Circular N°2.288 / 27.04.2021 por Resolución N°2256

Archivo R06 Hoja 1
CÓDIGO : R06
NOMBRE : ACTIVOS PONDERADOS POR RIESGO DE CRÉDITO
SISTEMA : Riesgos PERIODICIDAD : Mensual PLAZO : 9 días hábiles.
En este archivo se informarán las exposiciones activas de las entidades bancarias afectas a requerimiento de capital por riesgo de crédito, bajo método estándar (ME) y metodologías internas (MI), informando el tipo de contraparte y diferentes factores de riesgo utilizados en el cálculo de los activos ponderados por riesgo de crédito (APRC), así como los mitigadores de riesgo utilizados, de acuerdo con los lineamientos establecidos en el Capítulo
21-6 de la RAN. Las exposiciones anteriormente mencionadas corresponden a activos en el libro de banca, fondos de inversión en el libro de banca, equivalentes de créditos y exposiciones contingentes, de acuerdo con el numeral 2 del mismo Capítulo.
Adicionalmente, se deben informar los requisitos de información utilizados en el cálculo del requerimiento contra cíclico internacional, según los cargos fijados por la autoridad extranjera respectiva con la que el banco mantiene una exposición, de acuerdo con lo señalado en el Capítulo 21-12 de la RAN.
Los datos que deben proporcionarse se refieren a la situación consolidada global, consolidada local y al banco sin consolidar (individual).
Primer registro
1. Código del banco ............................................................................................. 9(04)
2. Identificación del archivo ................................................................................. X(03)
3. Período ............................................................................................................. P(06)
4. Filler ................................................................................................................. X(169)
Largo del registro .............................. 182 bytes
## 1. CÓDIGO DEL BANCO
Corresponde al código que identifica al banco.
## 2. IDENTIFICACIÓN DEL ARCHIVO
Corresponde a la identificación del archivo. Debe ser "R06".
## 3. PERÍODO
Corresponde al mes (AAAAMM) al cual se refiere la información.
Registros siguientes Los registros siguientes contendrán información sobre las exposiciones afectas a requerimiento de capital por riesgo de crédito para determinar los APRC de un banco, a través de método estándar y metodologías internas, los mitigadores de riesgo utilizados y requisitos adicionales correspondientes al periodo al que se refiere la información. Esta información se identificará en el primer campo de cada registro, según los códigos:
Circular N°2.288 / 27.04.2021 por Resolución N°2256

Archivo R06 Hoja 2 Código Tipo de registro
01 Activos ponderados por riesgo de crédito y requerimiento contracíclico
internacional
02 Método estándar para cálculo de los APRC y técnicas de mitigación
03 Metodologías internas para cálculo de los APRC y técnicas de mitigación
Registro para informar activos ponderados por riego de crédito y requerimiento contra cíclico internacional
1. Tipo de registro ................................................................................. 9(02)
2. Nivel de consolidación ....................................................................... 9(01)
3. APRC ME ........................................................................................... 9(14)
4. APRC MI ............................................................................................ 9(14)
5. APRC ME ajustado por técnicas de mitigación ................................. 9(14)
6. APRC MI ajustado por técnicas de mitigación .................................. 9(14)
7. Requerimiento contra cíclico internacional ...................................... 9(02)V9(03)
8. Filler ................................................................................................... X(118)
Largo del registro ............... 182 bytes
## 1. TIPO DE REGISTRO
Corresponde al código que identifica el tipo de registro. Debe ser “01”.
## 2. NIVEL DE CONSOLIDACIÓN
Corresponde al código asociado al nivel de consolidación, el cual se deberá indicar según la Tabla 80 de este Manual.
## 3. APRC ME
Corresponde al monto de los activos ponderados por riesgo de crédito obtenidos a través del método estándar (ME), calculados de acuerdo con lo señalado en el numeral 3 del Capítulo 21-6 de la RAN.
## 4. APRC MI
Corresponde al monto de los activos ponderados por riesgo de crédito obtenidos a través de metodologías internas (MI), calculado de acuerdo con lo señalado en el numeral 4 del Capítulo 21-6 de la RAN, sujeto a la aprobación de esta Comisión.
En el caso de no ser permitido, reportar cero.
## 5. APRC ME AJUSTADO POR TÉCNICAS DE MITIGACIÓN
Corresponde al monto de los activos ponderados por riesgo de crédito obtenidos a través del método estándar (ME), ajustado por las técnicas de mitigación de riesgo de crédito establecidas en el numeral 5 del Capítulo 21-6 de la RAN. En caso de no registrar ajustes por técnicas de mitigación reportar el mismo valor que campo 3.
## 6. APRC MI AJUSTADO POR TÉCNICAS DE MITIGACIÓN
Corresponde al monto de los activos ponderados por riesgo de crédito obtenidos a través de metodologías internas (MI), si estuviesen aprobadas por esta Comisión, ajustado por alguna de las técnicas de mitigación de riesgo de crédito establecidas en el numeral 5 del Capítulo 21-6 de la RAN. En caso de no registrar ajustes por técnicas de mitigación reportar el mismo valor que campo 4.
Circular N°2.288 / 27.04.2021 por Resolución N°2256

Archivo R06 Hoja 3
## 7. REQUERIMIENTO CONTRA CÍCLICO INTERNACIONAL
Corresponde al requerimiento asociado al colchón contra cíclico internacional que el banco debe informar a la Comisión, según los cargos fijados por la autoridad extranjera respectiva con la que el banco mantiene una exposición, de acuerdo con la fórmula expresada en el Título V del Capítulo 21-12 de la RAN.
Para el cómputo se debe utilizar los APRC obtenidos desde el registro 2, en el caso de utilizar método estándar, o desde el registro 3, en el caso de utilizar metodologías internas autorizadas por la Comisión. En ambos casos, se deben utilizar los valores posteriores al ajuste de las técnicas de mitigación.
Registro para informar método estándar para cálculo de los APRC y técnicas de mitigación Todos los bancos deben reportar este registro y calcular los APRC ME, independiente de si el banco cuenta con la autorización de la Comisión para utilizar metodologías internas.
1. Tipo de registro ........................................................................................ 9(02)
2. Nivel de consolidación .............................................................................. 9(01)
3. Tipo de exposición .................................................................................... 9(02)
4. Contraparte ............................................................................................... 9(02)
5. Tipo de contraparte ................................................................................... 9(02)
6. Rubro ........................................................................................................ 9(05)
7. Técnica de mitigación ............................................................................... 9(02)
8. Clasificación de riesgo ............................................................................... 9(04)
9. Sujeto de clasificación ............................................................................... 9(02)
10. País de riesgo ............................................................................................ 9(03)
11. Cargo contra cíclico ................................................................................... 9(02)V9(03)
12. Monto ........................................................................................................ 9(14)
13. Monto exposición post factor de conversión de crédito ........................... 9(14)
14. APRC sin mitigación ................................................................................. 9(14)
15. Colateral .................................................................................................... 9(02)
16. Monto cubierto.......................................................................................... 9(14)
17. Monto no cubierto .................................................................................... 9(14)
18. APRC post mitigación ............................................................................... 9(14)
19. Filler .......................................................................................................... X(66)
Largo del registro ............... 182 bytes
## 1. TIPO DE REGISTRO
Corresponde al código que identifica el tipo de registro. Debe ser “02”.
## 2. NIVEL DE CONSOLIDACIÓN
Corresponde al código asociado al nivel de consolidación, el cual se deberá indicar según la Tabla 80 de este Manual.
## 3. TIPO DE EXPOSICIÓN
Corresponde al código asociado al tipo de exposición afecta a requerimientos de capital por riesgo de crédito. Se deberá indicar el tipo de exposición según los códigos de la Tabla 109 de este Manual.
Circular N°2.288 / 27.04.2021 por Resolución N°2256

Archivo R06 Hoja 4
## 4. CONTRAPARTE
Corresponde al código asociado a las exposiciones y contraparte sujetas a riesgo de crédito. Se deberá indicar la exposición según los códigos de la Tabla 110 de este Manual.
## 5. TIPO DE CONTRAPARTE
Corresponde al código que asigna características específicas con las que se materializan las exposiciones y sus contrapartes señaladas en los campos 3 y 4.
Se debe indicar el tipo de exposición según los códigos de la Tabla 111 de este Manual.
En los casos en que el tipo de contraparte no tenga características especificadas en la Tabla, reportar código 99.
## 6. RUBRO
Se debe informar el código que identifica el rubro correspondiente con la información reportada en los campos anteriores y según el Capítulo C-3 del Compendio de Normas Contables.
Cuando el campo “tipo de exposición” sea igual a 3 (campo 3), se debe asignar el rubro en donde se informe el contrato de derivado financiero. Cuando el campo
3 tome valor 4, se debe informar el rubro asociado a la Información
Complementaria del Capítulo C-3 señalado anteriormente. En caso de que la exposición contingente no tenga un rubro asociado se deberá informar el campo en ceros.
## 7. TÉCNICAS DE MITIGACIÓN
Corresponde al código asociado a las técnicas de mitigación aceptadas para mitigar el riesgo de crédito, de acuerdo con lo estipulado en el numeral 5 del Capítulo 21-6 de la RAN. En caso de coexistir 2 técnicas de mitigación, donde una de ellas sea una compensación (categorías 1, 2, 5 y 6) y la otra una cobertura
(categorías 3 y 4), se deberá reportar la técnica de mitigación asociada a la cobertura. En otro caso, se debe considerar la que genera un mayor efecto en el cálculo de los APRC. Se deberá indicar la técnica de mitigación según los códigos de la Tabla 112 de este Manual.
## 8. CLASIFICACIÓN DE RIESGO
Corresponde al código asociado a la clasificación de riesgo externa asignada a las contrapartes o emisión que lo requieran, y que estén en la cartera normal o subestándar, de acuerdo con los criterios establecidos en el Capítulo B-1 del CNC.
Se debe indicar la categoría de riesgo según los códigos de la Tabla 92 1) de este Manual.
Cuando no exista clasificación para alguna exposición y su contraparte, debe informarse el campo con 9999.
## 9. SUJETO DE CLASIFICACIÓN
Corresponde al código que indica si la clasificación crediticia (campo 7) fue realizada sobre la emisión o la contraparte. Los códigos corresponden a:
01 Emisión
02 Emisor o contraparte
09 Otro/ No aplica
Circular N°2.288 / 27.04.2021 por Resolución N°2256

Archivo R06 Hoja 5
## 10. PAÍS DE RIESGO
Corresponde al código que identifica el país, territorio o jurisdicción de la contraparte de la exposición, donde la persona natural o jurídica tiene su domicilio u oficina registrada de acuerdo con lo señalado por el Título V del Capítulo 21-12 de la RAN. Se debe indicar el país según los códigos de la Tabla 45 de este Manual.
## 11. CARGO CONTRA CÍCLICO
Corresponde al cargo contra cíclico aplicado a las exposiciones del país de riesgo
(campo 9), vigentes a la fecha de la estimación. En el caso de Chile, el cargo corresponde al valor definido por el Banco Central de Chile, mientras que, en jurisdicciones extranjeras corresponderá a aquellos publicados por el Comité de Supervisión de Bancaria de Basilea. El valor debe estar multiplicado por 100.
## 12. MONTO
Corresponde al monto de cada exposición valorada de acuerdo con lo señalado en numeral 2 del Capítulo 21-6 de la RAN, sin compensaciones de ningún tipo.
En el caso de los fondos de inversión se deben utilizar los métodos de valorización autorizados, mientras que los equivalentes de crédito deben reportase como la suma del valor razonable y el nocional con su respectivo factor. Se consideran valores netos de provisiones específicas para los activos en el libro de banca y para los créditos contingentes. Dichos créditos contingentes no deben considerar la aplicación de los factores de conversión de crédito (FCC) señalados en el Capítulo
21-6 de la RAN.
## 13. MONTO EXPOSICIÓN POST FACTOR DE CONVERSIÓN DE CRÉDITO
Corresponde al monto de cada exposición contingente reportada después de haber aplicado los factores de conversión de crédito (FCC) señalados en el Capítulo 21-6 de la RAN. Si el tipo de exposición (campo 3) no corresponde a créditos contingentes se debe informar el monto del campo 12.
## 14. APRC SIN MITIGACIÓN
Corresponde al monto de los activos ponderados por riesgo de crédito, aplicando el Ponderador por Riesgo de Crédito (PRC) correspondiente al monto exposición post factor de conversión de crédito (campo 13).
## 15. COLATERAL
Corresponde al código asociado al tipo de deudor indirecto o al tipo de garantía financiera calificada utilizada en las técnicas de mitigación “avales y fianzas” y
“garantías financieras” (campo 7) que mitigan el riesgo de la exposición. Se debe indicar el colateral según los códigos de la Tabla 113 de este Manual.
## 16. MONTO CUBIERTO
Corresponde al monto de la exposición garantizada del campo 13, cuando se utilizan las técnicas de mitigación “avales y fianzas” y “garantías financieras”
(campo 7), de acuerdo con lo señalado en el numeral 5 del Capítulo 21-6 de la RAN.
Circular N°2.288 / 27.04.2021 por Resolución N°2256

Archivo R06 Hoja 6 En el caso que la técnica de mitigación corresponda a acuerdos de compensación bilateral, acuerdos mediante una Entidad de Contraparte Central (ECC), garantía constituida a favor de terceros bajo el amparo de un contrato de marco o compensación en el balance y cambie el valor de la exposición, reportar cero. Si la exposición no ha sido mitigada por ninguna técnica, también, reportar cero.
En el caso de que coexistan 2 técnicas de mitigación, donde una de ellas sea una compensación (categorías 1, 2, 5 y 6 del campo 7) y la otra una cobertura (categorías
3 y 4 del campo 7), reportar el monto garantizado asociado al monto de la
exposición ya compensado.
## 17. MONTO NO CUBIERTO
Corresponde al monto de la exposición no garantizada del campo 13, cuando se utilizan las técnicas de mitigación “avales y fianzas” y “garantías financieras”
(campo 7), de acuerdo con lo señalado en el numeral 5 del Capítulo 21-6 de la RAN.
En el caso que la técnica de mitigación corresponda a acuerdos de compensación bilateral, acuerdos mediante una Entidad de Contraparte Central (ECC), garantía constituida a favor de terceros bajo el amparo de un contrato de marco o compensación en el balance y cambie el valor de la exposición, reportar el nuevo monto. Si la exposición no ha sido mitigada por ninguna técnica reportar el valor del campo monto post factor de conversión de crédito (campo 13).
En el caso de que coexistan 2 técnicas de mitigación, donde una de ellas sea una compensación (categorías 1, 2, 5 y 6 del campo 7) y la otra una cobertura (categorías
3 y 4 del campo 7), reportar el monto no garantizado asociado al monto de la
exposición ya compensado.
## 18. APRC POST MITIGACIÓN
Corresponde al monto de los activos ponderados por riesgo de crédito, aplicando el Ponderador por Riesgo de Crédito (PRC) correspondiente a los montos cubiertos y no cubiertos (campos 16 y 17).
Registro para informar metodologías internas para cálculo de los APRC y técnicas de mitigación Este registro debe ser reportado solo por aquellos bancos que se encuentren autorizados, por la Comisión, a utilizar metodologías internas. El reporte debe contener todas las exposiciones afectas a riesgo de crédito, incluso de aquellas en las que solo se permite la utilización de ME, de acuerdo con la agrupación de carteras y una misma técnica de mitigación, que el banco estime conveniente.
1. Tipo de registro ...................................................................................... 9(02)
2. Nivel de consolidación ............................................................................ 9(01)
3. Tipo de exposición .................................................................................. 9(02)
4. Identificador de la cartera ...................................................................... 9(02)
5. Descripción de la cartera ........................................................................ X(50)
6. Rubro ...................................................................................................... 9(05)
7. Técnicas de mitigación ............................................................................ 9(02)
8. Método ................................................................................................... 9(02)
Circular N°2.288 / 27.04.2021 por Resolución N°2256

Archivo R06 Hoja 7
9. Clasificación de la contraparte ................................................................ X(02)
10. País de riesgo .......................................................................................... 9(03)
11. Cargo contra cíclico ................................................................................. 9(02)V9(03)
12. Madurez promedio ................................................................................. 9(02)V9(03)
13. Probabilidad de incumplimiento (PI) promedio .................................... 9(02)V9(03)
14. Pérdida dado el incumplimiento (PDI) promedio .................................. 9(02)V9(03)
15. Exposición al incumplimiento (EAI) ...................................................... 9(14)
16. Monto exposición post factor de conversión de crédito ......................... 9(14)
17. Cargo por riesgo de crédito promedio .................................................... 9(02)V9(03)
18. APRC sin mitigación ............................................................................... 9(14)
19. Colateral .................................................................................................. 9(02)
20. Monto cubierto ....................................................................................... 9(14)
21. Monto no cubierto .................................................................................. 9(14)
22. APRC post mitigación ............................................................................. 9(14)
Largo del registro ............. 182 bytes
## 1. TIPO DE REGISTRO
Corresponde al código que identifica el tipo de registro. Debe ser “03”.
## 2. NIVEL DE CONSOLIDACIÓN
Corresponde al código asociado al nivel de consolidación, el cual se deberá indicar según la Tabla 80 de este Manual.
## 3. TIPO DE EXPOSICIÓN
Corresponde al código asociado al tipo de exposición afecta a requerimientos de capital por riesgo de crédito. Se deberá indicar el tipo de exposición según los códigos de la Tabla 109 de este Manual.
## 4. IDENTIFICADOR DE LA CARTERA
Corresponde al número correlativo iniciado en 1, asignado por el banco a la cartera sujeta a riesgo de crédito compuesta por exposiciones de características homogéneas en cuanto a tipo de deudores y condiciones pactadas, a fin de establecer, mediante estimaciones técnicamente fundamentadas y siguiendo criterios prudenciales, el comportamiento de pago de la cartera.
## 5. DESCRIPCIÓN DE LA CARTERA
Corresponde al nombre de la cartera asociado al identificador reportado en el campo 4, mencionando las principales exposiciones contenidas y sus contrapartes.
## 6. RUBRO
Se debe informar el código que identifica el rubro correspondiente con la información reportada en los campos anteriores y según el Capítulo C-3 del Compendio de Normas Contables.
Cuando el campo “tipo de exposición” sea igual a 3 (campo 3), se debe asignar el rubro en donde se informe el contrato de derivado financiero. Cuando el campo
3 tome valor 4, se debe informar el rubro asociado a la Información
Complementaria del Capítulo C-3 señalado anteriormente. En caso de que la exposición contingente no tenga un rubro asociado se deberá informar el campo en ceros.
Circular N°2.288 / 27.04.2021 por Resolución N°2256

Archivo R06 Hoja 8
## 7. TÉCNICAS DE MITIGACIÓN
Corresponde al código asociado a las técnicas de mitigación aceptadas para mitigar el riesgo de crédito, de acuerdo con lo estipulado en el numeral 5 del Capítulo 21-6 de la RAN. En caso de existir más de una técnica de mitigación, se debe considerar la que genera un mayor efecto en el cálculo de los APRC. Se deberá indicar la técnica de mitigación según los códigos de la Tabla 112 de este Manual.
## 8. MÉTODO
Corresponde al código asociado al método utilizado para obtener el APRC de la exposición. Los códigos corresponden a:
01 Método estándar (ME)
02 Metodologías internas (MI)
## 9. CLASIFICACIÓN DE LA CONTRAPARTE
Se debe indicar la clasificación de la contraparte de cada tipo de exposición, cartera y técnica de mitigación reportada en los campos anteriores, de acuerdo con lo señalado en el Capítulo B-1 del CNC y según los códigos de la Tabla 13 del MSI.
## 10. PAÍS DE RIESGO
Corresponde al código que identifica el país, territorio o jurisdicción de la contraparte de la exposición, donde la persona natural o jurídica tiene su domicilio u oficina registrada de acuerdo con lo señalado por el Título V del Capítulo 21-12 de la RAN. Se debe indicar el país según los códigos de la Tabla 45 de este Manual.
## 11. CARGO CONTRA CÍCLICO
Corresponde al cargo contra cíclico aplicado a las exposiciones del país de riesgo
(campo 9), vigentes a la fecha de la estimación. En el caso de Chile, el cargo corresponde al valor definido por el Banco Central de Chile, y en los otros casos, corresponderá a aquellos publicados por el Comité de Supervisión de Bancaria de Basilea. El valor debe estar multiplicado por 100.
## 12. MADUREZ PROMEDIO
Corresponde al promedio ponderado por exposición del número de años calculados de acuerdo con lo señalado en el numeral 4.2 del Capítulo 21-6 de la RAN.
## 13. PROBABILIDAD DE INCUMPLIMIENTO (PI) PROMEDIO
Corresponde al promedio ponderado por exposición de la probabilidad de incumplimiento de la cartera, de acuerdo con lo establecido en el numeral 4.1 del Capítulo 21-6 de la RAN.
## 14. PÉRDIDA DADO EL INCUMPLIMIENTO (PDI) PROMEDIO
Corresponde al promedio ponderado por exposición de la PDI calculada para la cartera, de acuerdo con lo establecido en el numeral 4.3 del Capítulo 21-6 de la RAN.
Circular N°2.288 / 27.04.2021 por Resolución N°2256

Archivo R06 Hoja 9
## 15. EXPOSICIÓN AL INCUMPLIMIENTO (EAI)
Corresponde a la suma de los montos de cada exposición valorada de acuerdo con lo señalado en numeral 2 del Capítulo 21-6 de la RAN.
Se consideran valores netos de provisiones específicas para los activos en el libro de banca y para las exposiciones contingentes. En el caso de los fondos de inversión se deben utilizar los métodos de valorización autorizados, mientras que los equivalentes de crédito deben reportase como el total del valor razonable y el nocional con su respectivo factor.
## 16. MONTO EXPOSICIÓN POST FACTOR DE CONVERSIÓN DE CRÉDITO
Corresponde al monto de cada exposición contingente reportada después de haber aplicado los factores de conversión de crédito (FCC) señalados en el Capítulo 21-6 de la RAN. Si algún tipo de exposición de la cartera (campo 3) no corresponde a créditos contingentes se debe informar el monto del campo 15.
## 17. CARGO POR RIESGO DE CRÉDITO PROMEDIO
Corresponde al cálculo del promedio ponderado por exposición de los cargos por riesgo de crédito para la cartera, de acuerdo con las especificaciones señaladas en el numeral 4.4 del Capítulo 21-6 de la RAN.
## 18. APRC SIN MITIGACIÓN
Corresponde al monto de los activos ponderados por riesgo de crédito, aplicando el cargo por riesgo de crédito promedio (campo 17) correspondiente al monto exposición post factor de conversión de crédito (campo 16) y multiplicado por
12,5, de acuerdo con lo señalado en el numeral 4.4.1 del Capítulo 21-6 de la RAN.
## 19. COLATERAL
Corresponde al código asociado al tipo de deudor indirecto o al tipo de garantía financiera calificada utilizada en las técnicas de mitigación “avales y fianzas” y
“garantías financieras” (campo 7) que mitigan el riesgo de la exposición. Se debe indicar el colateral según los códigos de la Tabla 113 de este Manual.
## 19. MONTO CUBIERTO
Corresponde al monto de la exposición garantizada del campo 13, cuando se utilizan las técnicas de mitigación “avales y fianzas” y “garantías financieras”
(campo 7), de acuerdo con lo señalado en el numeral 5 del Capítulo 21-6 de la RAN.
En el caso que la técnica de mitigación corresponda a acuerdos de compensación bilateral, acuerdos mediante una Entidad de Contraparte Central (ECC), garantía constituida a favor de terceros bajo el amparo de un contrato de marco o compensación en el balance y cambie el valor de la exposición, reportar cero. Si la exposición no ha sido mitigada por ninguna técnica, también, reportar cero.
En el caso de que coexistan 2 técnicas de mitigación, donde una de ellas sea una compensación (categorías 1, 2, 5 y 6 del campo 7) y la otra una cobertura (categorías
3 y 4 del campo 7), reportar el monto garantizado asociado al monto de la
exposición ya compensado.
Circular N°2.288 / 27.04.2021 por Resolución N°2256

Archivo R06 Hoja 10
## 20. MONTO NO CUBIERTO
Corresponde al monto de la exposición no garantizada del campo 13, cuando se utilizan las técnicas de mitigación “avales y fianzas” y “garantías financieras”
(campo 7), de acuerdo con lo señalado en el numeral 5 del Capítulo 21-6 de la RAN.
En el caso que la técnica de mitigación corresponda a acuerdos de compensación bilateral, acuerdos mediante una Entidad de Contraparte Central (ECC), garantía constituida a favor de terceros bajo el amparo de un contrato de marco o compensación en el balance y cambie el valor de la exposición, reportar el nuevo monto. Si la exposición no ha sido mitigada por ninguna técnica reportar el valor del campo monto post factor de conversión de crédito (campo 13).
En el caso de que coexistan 2 técnicas de mitigación, donde una de ellas sea una compensación (categorías 1, 2, 5 y 6 del campo 7) y la otra una cobertura (categorías
3 y 4 del campo 7), reportar el monto no garantizado asociado al monto de la
exposición ya compensado.
## 20. APRC POST MITIGACIÓN
Corresponde al monto de los activos ponderados por riesgo de crédito, aplicando el cargo por riesgo de crédito promedio (campo 17) correspondiente al monto no cubierto (campo 21) y multiplicado por 12,5, de acuerdo con lo señalado en el numeral 4.4.1 del Capítulo 21-6 de la RAN.
Carátula de cuadratura El archivo R06 debe entregarse con una carátula de cuadratura cuyo modelo se
especifica a continuación:
MODELO Institución: ________________________________ Código: _______ Información correspondiente al mes de: _________________ Archivo R06

| Número de registros |  |
| --- | --- |
| Número de registros con código 01 en el campo 1 |  |
| Número de registros con código 02 en el campo 1 |  |
| Número de registros con código 03 en el campo 1 |  |

Observaciones En los registros anteriores se incluirán solo las combinaciones que resulten atingentes al banco.
Circular N°2.288 / 27.04.2021 por Resolución N°2256

Archivo R07 Hoja 1
CÓDIGO : R07
NOMBRE : ACTIVOS PONDERADOS POR RIESGO DE MERCADO
SISTEMA : Riesgos PERIODICIDAD : Semanal: sólo para la información a nivel individual y consolidada local. Debe estar referida a cada uno de los días hábiles bancarios de la semana anterior a la fecha de envío, con excepción de los registros 7 y 8, cuya fecha se referirá solo al último día hábil de la semana anterior a la fecha de envío.
Mensual: sólo para la información a nivel consolidada global; y cada banco establecido en el exterior, filial de un banco establecido en Chile, en forma consolidada. Debe estar referida al último día de cada mes.
PLAZO : 3 días hábiles desde la fecha a la que se refiere la información, para la información con periodicidad semanal.
9 días hábiles desde el último día del mes, para la información con
periodicidad mensual.
En este archivo se informarán las exposiciones de las entidades bancarias afectas a requerimiento de capital por riesgo de mercado, bajo modelo estándar simplificado, informando movimientos de tasas de interés de referencia, monedas extranjeras, materias primas y cotizaciones bursátiles utilizados en el cálculo de los activos ponderados por riesgo de mercado (APRM). Las exposiciones anteriormente mencionadas corresponden a instrumentos financieros clasificados en el libro de negociación considerando, además, el riesgo de moneda extranjera y materias primas para las posiciones del libro de banca.
Los datos que deben proporcionarse se refieren a la situación consolidada global, situación consolidada local y al banco sin consolidar (individual).
Los registros del 02 al 08 sólo deberán ser reportados en los casos en que el banco tenga exposiciones asociadas a esos factores de riesgo o aplique el método solicitado.
Primer registro
1. Código del banco ................................................................................................ 9(04)
2. Identificación del archivo ................................................................................... X(03)
3. Fecha ................................................................................................................... F(08)
4. Filler .................................................................................................................... X(179)
Largo del registro ........................... 194 bytes
## 1. CÓDIGO DEL BANCO
Corresponde al código que identifica al banco.
## 2. IDENTIFICACIÓN DEL ARCHIVO
Corresponde a la identificación del archivo. Debe ser "R07".
Circular N°2.288 / 27.04.2021 por Resolución N°2256

Archivo R07 Hoja 2
## 3. FECHA
Corresponde a la fecha del último día hábil de la semana a la que se refiere la información, en el caso de los archivos semanales. Para el reporte mensual, y solo para efectos de su identificación, corresponderá al primer día del mes siguiente al de la fecha de reporte.
Registros siguientes Los registros siguientes contendrán información sobre las exposiciones afectas a requerimiento de capital por riesgo de mercado para determinar los APRM de un banco, a través de modelo estándar simplificado, correspondientes al periodo al que se refiere la información. Esta información se identificará en el primer campo de cada registro, según los
códigos:
Código Tipo de registro
01 Activos ponderados por riesgo de mercado por modelo estándar
simplificado
02 Riesgo general y específico de tasas de interés
03 Riesgo general y específico de cotizaciones bursátiles
04 Riesgo de materias primas
05 Riesgo de moneda extranjera
06 Riesgo de opciones
07 Detalle de riesgo de opciones a través de método de escenarios
08 Posiciones excluidas del marco de riesgo general de tasa de interés
09 Detalle de securitizaciones
Registro para informar activos ponderados por riesgo de mercado por modelo estándar simplificado
1. Tipo de registro ........................................................................................ 9(02)
2. Fecha ......................................................................................................... F(08)
3. Nivel de consolidación .............................................................................. 9(01)
4. APRM ........................................................................................................ 9(14)
5. Riesgo específico de tasa de interés .......................................................... 9(14)
6. Riesgo general de tasa de interés .............................................................. 9(14)
7. Riesgo de moneda extranjera .................................................................... 9(14)
8. Riesgo de materias primas ........................................................................ 9(14)
9. Riesgo específico de cotizaciones bursátiles ............................................. 9(14)
10. Riesgo general de cotizaciones bursátiles ................................................. 9(14)
11. Riesgo de opciones sobre tasa de interés .................................................. 9(14)
12. Riesgo de opciones sobre monedas .......................................................... 9(14)
13. Riesgo de opciones sobre cotizaciones bursátiles ..................................... 9(14)
14. Riesgo de opciones sobre materias primas .............................................. 9(14)
15. Cargo por traspaso de instrumentos entre libros .................................... 9(14)
16. Securitizaciones......................................................................................... 9(14)
17. Filler .......................................................................................................... X(01)
Largo del registro ............... 194 bytes
## 1. TIPO DE REGISTRO
Corresponde al código que identifica el tipo de registro. Debe ser “01”.
## 2. FECHA
Corresponde a la fecha a la cual se refiere la información.
Circular N°2.288 / 27.04.2021 por Resolución N°2256

Archivo R07 Hoja 3
## 3. NIVEL DE CONSOLIDACIÓN
Corresponde al código asociado al nivel de consolidación, el cual se deberá indicar según la Tabla 80 de este Manual.
## 4. APRM
Corresponde al monto de los activos ponderados por riesgo de mercado obtenidos a través del modelo estándar simplificado, calculados de acuerdo con lo señalado en el numeral 3 del Capítulo 21-7 de la RAN, considerando los montos reportados entre los campos 5 a 16.
## 5. RIESGO ESPECÍFICO DE TASA DE INTERÉS
Corresponde al monto del cargo por exposiciones calificadas en el libro de negociación cuyo valor se vea afectado por la variación de las tasas de interés del mercado, considerando el riesgo específico de tasa de interés de acuerdo con lo señalado en el numeral 3.1.1 del Capítulo 21-7 de la RAN.
## 6. RIESGO GENERAL DE TASA DE INTERÉS
Corresponde al monto del cargo por exposiciones calificadas en el libro de negociación cuyo valor se vea afectado por la variación de las tasas de interés del mercado, considerando el riesgo general de tasa de interés de acuerdo con lo señalado en el numeral 3.1.2 del Capítulo 21-7 de la RAN. Este cálculo debe considerar la posición neta ponderada, el resultado del ajuste vertical y los ajustes horizontales.
Adicionalmente, se deben considerar las posiciones delta ponderadas de las opciones sobre tasas de interés, cuando corresponda.
## 7. RIESGO DE MONEDA EXTRANJERA
Corresponde al monto del cargo por exposiciones en moneda extranjera en todo el balance, incluyendo el oro, de acuerdo con lo instruido en el numeral 3.2 del Capítulo 21-7 de la RAN.
Adicionalmente, se debe agregar el cargo determinado para la posición delta ponderada en opciones en monedas extranjeras, cuando corresponda.
## 8. RIESGO DE MATERIAS PRIMAS
Corresponde al monto del cargo por exposiciones en materias primas en todo el balance, de acuerdo con lo establecido en el numeral 3.3 del Capítulo 21-7 de la RAN.
Adicionalmente, se debe incluir las posiciones delta ponderadas netas para las opciones sobre materias primas, cuando corresponda.
## 9. RIESGO ESPECÍFICO DE COTIZACIONES BURSÁTILES
Corresponde al monto del cargo de riesgo específico de cotizaciones bursátiles calificadas en el libro de negociación, de acuerdo con lo señalado por el numeral
3.4 del Capítulo 21-7 de la RAN.
## 10. RIESGO GENERAL DE COTIZACIONES BURSÁTILES
Corresponde al monto del cargo de riesgo general de cotizaciones bursátiles calificadas en el libro de negociación, de acuerdo con lo señalado por el numeral
3.4 del Capítulo 21-7 de la RAN.
Circular N°2.288 / 27.04.2021 por Resolución N°2256

Archivo R07 Hoja 4 Adicionalmente, se debe incluir las posiciones delta ponderadas netas para las opciones sobre cotizaciones bursátiles, cuando corresponda.
## 11. RIESGO DE OPCIONES SOBRE TASA DE INTERÉS
Corresponde al monto del cargo por exposiciones en opciones sobre tasas de interés, calificadas en el libro de negociación, resultante de la aplicación del método simplificado o el método de escenarios, de acuerdo con lo señalado por el numeral 3.5 del Capítulo 21-7 de la RAN.
Adicionalmente, se debe incluir las exposiciones a los riesgos gamma y vega resultante de la aplicación del método delta plus.
## 12. RIESGO DE OPCIONES SOBRE MONEDAS
Corresponde al monto del cargo por exposiciones en opciones sobre moneda extranjera, en todo el balance, resultante de la aplicación del método simplificado o el método de escenarios, de acuerdo con lo señalado por el numeral 3.5 del Capítulo 21-7 de la RAN.
Adicionalmente, se debe incluir las exposiciones a los riesgos gamma y vega resultante de la aplicación del método delta plus.
## 13. RIESGO DE OPCIONES SOBRE COTIZACIONES BURSÁTILES
Corresponde al monto del cargo por exposiciones en opciones sobre acciones e índices accionarios, calificados en el libro de negociación, resultante de la aplicación del método simplificado o el método de escenarios, de acuerdo con lo señalado por el numeral 3.5 del Capítulo 21-7 de la RAN.
Adicionalmente, se debe incluir las exposiciones a los riesgos gamma y vega resultante de la aplicación del método delta plus.
## 14. RIESGO DE OPCIONES SOBRE MATERIAS PRIMAS
Corresponde al monto del cargo pors exposiciones en opciones sobre materias primas, en todo el balance, resultante de la aplicación del método simplificado o el método de escenarios, de acuerdo con lo señalado por el numeral 3.5 del Capítulo 21-7 de la RAN.
Adicionalmente, se debe incluir las exposiciones a los riesgos gamma y vega resultante de la aplicación del método delta plus.
## 15. CARGO POR TRASPASO DE INSTRUMENTOS ENTRE LIBROS
Corresponde al monto de la reducción en el cargo de capital total como resultado del traspaso de instrumentos entre libros, de acuerdo con lo estipulado en el numeral 2.3 del Capítulo 21-7 de la RAN. En caso de no existir este cargo, reportar el campo en cero.
## 16. SECURITIZACIONES
Corresponde al monto del cargo de capital por riesgo específico de tasa de interés para securitizaciones que son mantenidas en el libro de negociación, las que se calculan de acuerdo con lo estipulado en el numeral 3.13 del Capítulo 216 de la RAN. Para dicho cómputo, se debe considerar la clasificación de riesgo, madurez, grado de preferencia de la serie o tramo y el cumplimiento de los criterios para la distinción de securitizaciones menos complejas estipuladas en dicho Capítulo.
Circular N°2.288 / 27.04.2021 por Resolución N°2256

Archivo R07 Hoja 5 Registro para informar riesgo general y específico de tasas de interés En este registro se deben reportar todas las exposiciones del banco afectas a riesgo de tasas de interés, tanto para su riesgo específico como general. Adicionalmente, en el caso de opciones cuyo subyacente sea un instrumento de deuda o tasas de interés, se debe computar una entrada en el momento en que el contrato subyacente tiene efecto y una segunda entrada en el momento en que el contrato subyacente vence.
En el caso de los instrumentos securitizados, el riesgo específico de tasas de interés debe reportarse en este registro 9, para lo cual se deberá completar el campo 6 “Riesgo específico de tasa de interés” con el valor 99. El mismo tratamiento debe realizarse en las posiciones en derivados cuyo subyacente no tenga un emisor, dado que quedan exentas de cargo por riesgo específico.
1. Tipo de registro ........................................................................................ 9(02)
2. Fecha ......................................................................................................... F(08)
3. Nivel de consolidación .............................................................................. 9(01)
4. Fondos ....................................................................................................... 9(02)
5. Exposiciones ............................................................................................. 9(02)
6. Tipo de tasa de interés .............................................................................. 9(01)
7. Riesgo específico de tasa de interés .......................................................... 9(02)
8. Moneda ..................................................................................................... 9(02)
9. Banda temporal ......................................................................................... 9(02)
10. Monto posición riesgo específico .............................................................. 9(14)
11. Monto posición riesgo general .................................................................. 9(14)
12. Monto posiciones perfectamente compensadas ....................................... 9(14)
13. Filler .......................................................................................................... X(130)
Largo del registro ............... 194 bytes
## 1. TIPO DE REGISTRO
Corresponde al código que identifica el tipo de registro. Debe ser “02”.
## 2. FECHA
Corresponde la fecha a la cual se refiere la información.
## 3. NIVEL DE CONSOLIDACIÓN
Corresponde al código asociado al nivel de consolidación, el cual se deberá indicar según la Tabla 80 de este Manual.
## 4. FONDOS
Corresponde al código asociado al método utilizado para reportar las exposiciones mantenidas en fondos de inversión y fondos mutuos de acuerdo con lo estipulado en el numeral 3.6.1 del Capítulo 21-7 de la RAN. Los códigos
corresponden a:
01 Enfoque del constituyente
02 Enfoque reglamento interno
09 Inversión directa
En caso de que el reporte no corresponda a inversiones en fondos sino a otros tipos de instrumentos del libro de negociación, se debe informar el código 09.
Circular N°2.288 / 27.04.2021 por Resolución N°2256

Archivo R07 Hoja 6
## 5. EXPOSICIONES
Corresponde al código asociado al tipo de exposición sujetas a riesgos de tasa de interés. Se deben indicar las exposiciones según los códigos de la Tabla 114 de este Manual.
Los instrumentos financieros no derivados corresponden sólo a aquellas posiciones en instrumentos registrados en el activo por su valor de mercado que no presenten restricciones de ninguna naturaleza que puedan impedir que sean negociados y que: (i) se mantengan en cartera para negociarlos en el corto plazo con el propósito de obtener ganancias provenientes del arbitraje o de fluctuaciones esperadas en los precios o tasas de mercado; o que (ii) formen parte de una cartera de instrumentos que se negocian activa y frecuentemente por la institución.
Los derivados deben ser descompuestos en los subyacentes respectivos y éstos computados a valor de mercado en cada clase de riesgo y banda temporal correspondiente
## 6. TIPO DE TASA DE INTERÉS
Corresponde al código que asigna el tipo de tasa de interés. Los códigos
corresponden a:
01 Operaciones con tasas fijas y saldos no sujetos a interés
02 Operaciones con tasa flotante
## 7. RIESGO ESPECÍFICO DE TASA DE INTERÉS
Corresponde al código que asigna características de las exposiciones (campo 4) sujetas a riesgo específico de tasa de interés. Se debe indicar el tipo de exposición según los códigos de la Tabla 115 de este Manual.
## 8. MONEDA
Corresponde al código que identifica la moneda en la que se materializarán las exposiciones o tipo de reajustabilidad. Se debe indicar la moneda según los códigos de la Tabla 1 de este Manual.
Para operaciones pagaderas en pesos reajustables en moneda extranjera
(incluidas las expresadas en moneda extranjera y pagaderas en pesos), se utilizará el código correspondiente a la moneda extranjera de que se trate y no el código que identifica el tipo de reajustabilidad.
## 9. BANDA TEMPORAL
Corresponde al código asociado a las bandas temporales de los instrumentos según su vencimiento para instrumentos a tasa fija, mientras que en instrumentos a tasa flotante corresponde al período de recálculo de la tasa. Se debe indicar la banda temporal según los códigos de la Tabla 116 de este Manual.
Los instrumentos a tasa fija se asignan a las bandas en función de su vencimiento residual, mientras que los instrumentos a tasa flotante en función del siguiente período de recálculo de la tasa.
Los instrumentos derivados, exceptuando las opciones, deben ser descompuestos según sus subyacentes y asignados a las bandas temporales que correspondan.
Circular N°2.288 / 27.04.2021 por Resolución N°2256

Archivo R07 Hoja 7
## 10. MONTO POSICIÓN RIESGO ESPECÍFICO
Corresponde al monto de la posición neta activa o pasiva de las exposiciones
(campo 4) afectas a riesgo específico, permitiendo la compensación en instrumentos que correspondan a una misma serie de emisión, de acuerdo con lo estipulado en el Capítulo 21-7 de la RAN.
## 11. MONTO POSICIÓN RIESGO GENERAL
Corresponde al monto de la posición activa o pasiva de las exposiciones (campo
4) afectas a riesgo general, de acuerdo con lo estipulado en el Capítulo 21-7 de la RAN.
Se deben considerar las posiciones perfectamente compensadas en derivados.
## 12. MONTO POSICIONES PERFECTAMENTE COMPENSADAS
Corresponde al monto de la exposición que calificaría para ser excluida del riesgo general de tasa de interés por encontrarse perfectamente compensada, correspondiente a la posición activa o pasiva, de acuerdo con lo estipulado en el Capítulo 21-7 de la RAN. Si no hay posiciones perfectamente compensadas reportar cero.
Registro para informar riesgo general y específico de cotizaciones bursátiles En este registro se deben reportar todas las exposiciones del banco afectas a riesgo de cotizaciones bursátiles, tanto para su riesgo específico como general, considerando todos los mercados bursátiles, solo en los casos en que el banco tenga exposiciones asociadas a este tipo de riesgo. En caso contrario, no deberá informar el registro.
1. Tipo de registro ........................................................................................ 9(02)
2. Fecha ......................................................................................................... F(08)
3. Nivel de consolidación .............................................................................. 9(01)
4. Fondos ....................................................................................................... 9(02)
5. Exposiciones ............................................................................................. 9(02)
6. Moneda ..................................................................................................... 9(02)
7. Jurisdicción mercado bursátil .................................................................. 9(03)
8. Monto posición ......................................................................................... 9(14)
9. Filler .......................................................................................................... X(160)
Largo del registro ............... 194 bytes
## 1. TIPO DE REGISTRO
Corresponde al código que identifica el tipo de registro. Debe ser “03”.
## 2. FECHA
Corresponde la fecha a la cual se refiere la información.
## 3. NIVEL DE CONSOLIDACIÓN
Corresponde al código asociado al nivel de consolidación, el cual se deberá indicar según la Tabla 80 de este Manual.
Circular N°2.288 / 27.04.2021 por Resolución N°2256

Archivo R07 Hoja 8
## 4. FONDOS
Corresponde al código asociado al método utilizado para reportar las exposiciones mantenidas en fondos de inversión y fondos mutuos de acuerdo con lo estipulado en el numeral 3.6.1 del Capítulo 21-7 de la RAN. Los códigos
corresponden a:
01 Enfoque del constituyente
02 Enfoque reglamento interno
09 Inversión directa
En caso de que el reporte no corresponda a inversiones en fondos sino a otros tipos de instrumentos del libro de negociación, se debe informar el código 09.
## 5. EXPOSICIONES
Corresponde al código asociado al tipo de exposición sujetas a riesgo de cotizaciones bursátiles. Se deben indicar las exposiciones según los códigos de la Tabla 117 de este Manual.
Los instrumentos financieros no derivados corresponden sólo a aquellas posiciones en instrumentos registrados en el activo por su valor de mercado que no presenten restricciones de ninguna naturaleza que puedan impedir que sean negociados y que: (i) se mantengan en cartera para negociarlos en el corto plazo con el propósito de obtener ganancias provenientes del arbitraje o de fluctuaciones esperadas en los precios o tasas de mercado; o que (ii) formen parte de una cartera de instrumentos que se negocian activa y frecuentemente por la institución.
## 6. MONEDA
Corresponde al código que identifica la moneda en la que se materializarán las exposiciones o tipo de reajustabilidad. Se debe indicar la moneda según los códigos de la Tabla 1 de este Manual.
Para operaciones pagaderas en pesos reajustables en moneda extranjera
(incluidas las expresadas en moneda extranjera y pagaderas en pesos), se utilizará el código correspondiente a la moneda extranjera de que se trate y no el código que identifica el tipo de reajustabilidad.
## 7. JURISDICCIÓN MERCADO BURSÁTIL
Corresponde al código asociado a la identificación de cada mercado bursátil, los que se relacionan a la jurisdicción donde operan. Se debe indicar el país según los códigos de la Tabla 45 de este Manual.
## 8. MONTO POSICIÓN
Corresponde al monto de la posición activa o pasiva de las exposiciones (campo
4) afectas a cada uno de los riesgos generales y/o específicos, de acuerdo con lo estipulado en el Capítulo 21-7 de la RAN.
Circular N°2.288 / 27.04.2021 por Resolución N°2256

Archivo R07 Hoja 9 Registro para informar riesgo de materias primas En este registro se deben reportar todas las exposiciones del banco afectas a riesgo de materias primas en los casos en que el banco tenga exposiciones asociadas a este tipo de riesgo. En caso contrario, no deberá informar el registro.
1. Tipo de registro ........................................................................................ 9(02)
2. Fecha ......................................................................................................... F(08)
3. Nivel de consolidación .............................................................................. 9(01)
4. Fondos ....................................................................................................... 9(02)
5. Exposiciones ............................................................................................. 9(02)
6. Materia prima ........................................................................................... 9(02)
7. Monto posición ......................................................................................... 9(14)
8. Filler .......................................................................................................... X(163)
Largo del registro ............... 194 bytes
## 1. TIPO DE REGISTRO
Corresponde al código que identifica el tipo de registro. Debe ser “04”.
## 2. FECHA
Corresponde la fecha a la cual se refiere la información.
## 3. NIVEL DE CONSOLIDACIÓN
Corresponde al código asociado al nivel de consolidación, el cual se deberá indicar según la Tabla 80 de este Manual.
## 4. FONDOS
Corresponde al código asociado al método utilizado para reportar las exposiciones mantenidas en fondos de inversión y fondos mutuos de acuerdo con lo estipulado en el numeral 3.6.1 del Capítulo 21-7 de la RAN. Los códigos
corresponden a:
01 Enfoque del constituyente
02 Enfoque reglamento interno
09 Inversión directa
En caso de que el reporte no corresponda a inversiones en fondos sino a otros tipos de instrumentos del libro de negociación, se debe informar el código 09.
## 5. EXPOSICIONES
Corresponde al código asociado al tipo de exposición sujetas a riesgo de materias primas. Se deben indicar las exposiciones según los códigos de la Tabla
118 de este Manual.
Los derivados deben ser descompuestos en los subyacentes respectivos y éstos computados a valor de mercado en cada clase de riesgo y banda temporal correspondiente.
## 6. MATERIA PRIMA
Corresponde al código de las categorías de materias primas, las cuales se agrupan de acuerdo con sus características comunes. Se deben indicar las exposiciones según los códigos de la Tabla 119 de este Manual.
Circular N°2.288 / 27.04.2021 por Resolución N°2256

Archivo R07 Hoja 10 Si una categoría tiene “n” materias primas y éstas no son sustitutas, de acuerdo con la definición establecida en el numeral 3.3 del Capítulo 21-7 de la RAN, entonces se tendrá que informar tantas posiciones como materias primas haya dentro de cada categoría de este campo.
## 7. MONTO POSICIÓN
Corresponde al monto de la posición activa o pasiva de las exposiciones afectas a riesgo de materias primas (campo 4), de acuerdo con lo estipulado en el Capítulo 21-7 de la RAN.
Registro para informar riesgo de moneda extranjera En este registro se deben reportar todas las exposiciones del banco afectas a riesgo de moneda extranjera, considerando todas las posiciones netas en monedas en todo el balance, incluyendo el oro.
1. Tipo de registro ........................................................................................ 9(02)
2. Fecha ......................................................................................................... F(08)
3. Nivel de consolidación .............................................................................. 9(01)
4. Fondos ....................................................................................................... 9(02)
5. Exposiciones ............................................................................................. 9(02)
6. Moneda ..................................................................................................... 9(03)
7. Monto posición ......................................................................................... 9(14)
8. Filler .......................................................................................................... X(162)
Largo del registro ............... 194 bytes
## 1. TIPO DE REGISTRO
Corresponde al código que identifica el tipo de registro. Debe ser “05”.
## 2. FECHA
Corresponde a la fecha a la cual se refiere la información.
## 3. NIVEL DE CONSOLIDACIÓN
Corresponde al código asociado al nivel de consolidación, el cual se deberá indicar según la Tabla 80 de este Manual.
## 4. FONDOS
Corresponde al código asociado al método utilizado para reportar las exposiciones mantenidas en fondos de inversión y fondos mutuos de acuerdo con lo estipulado en el numeral 3.6.1 del Capítulo 21-7 de la RAN. Los códigos
corresponden a:
01 Enfoque del constituyente
02 Enfoque reglamento interno
09 Inversión directa
En caso de que el reporte no corresponda a inversiones en fondos sino a otros tipos de instrumentos del libro de negociación, se debe informar el código 09.
Circular N°2.288 / 27.04.2021 por Resolución N°2256

Archivo R07 Hoja 11
## 5. EXPOSICIONES
Corresponde al código asociado al tipo de exposición sujetas a riesgo de moneda extrajera en el libro de banca y de negociación. Se deben indicar las exposiciones según los códigos de la Tabla 120 de este Manual.
Los códigos correspondientes a colocaciones incluyen tanto las vigentes como las vencidas. Los instrumentos financieros no derivados corresponden a la posición pagadera o reajustable en moneda extranjera en instrumentos financieros no derivados incluidos en el libro de negociación y en el libro de banca. Para las posiciones en derivados debe informarse el valor de mercado de las posiciones activas y/o pasivas.
Todas las exposiciones deben reportarse de acuerdo con lo estipulado en el Capítulo 21-7 de la RAN.
## 6. MONEDA
Corresponde al código que identifica la moneda en la que se materializarán las exposiciones. Se debe indicar la moneda según los códigos de la Tabla 1 de este Manual.
Para operaciones pagaderas en pesos reajustables en moneda extranjera
(incluidas las expresadas en moneda extranjera y pagaderas en pesos), se utilizará el código correspondiente a la moneda extranjera de que se trate y no el código que identifica el tipo de reajustabilidad.
## 7. MONTO POSICIÓN
Corresponde al monto de la posición activa o pasiva de las exposiciones afectas a riesgo de moneda extranjera, de acuerdo con lo estipulado en el Capítulo 21-7 de la RAN.
Se pueden excluir aquellas posiciones estructurales en el nivel de consolidación global, de acuerdo con las políticas internas de gestión de riesgo que tenga el banco y al cumplimiento de las condiciones establecidas en el numeral 3.2 del Capítulo 21-7 de la RAN.
Registro para informar riesgo de opciones En este registro se deben reportar todas las posiciones en opciones, ya sean estas adquiridas o vendidas, detallando el método de tratamiento.
Las compensaciones con spot o coberturas que se reporten en este registro no deben ser incluidas en los registros anteriores, a fin de no generar duplicidad de información.
1. Tipo de registro ........................................................................................ 9(02)
2. Fecha ......................................................................................................... F(08)
3. Nivel de consolidación .............................................................................. 9(01)
4. Id estrategia .............................................................................................. 9(02)
5. Moneda ..................................................................................................... 9(03)
6. Método ...................................................................................................... 9(02)
7. Valor posición ........................................................................................... 9(14)
8. Valor subyacente ....................................................................................... 9(14)
Circular N°2.288 / 27.04.2021 por Resolución N°2256

Archivo R07 Hoja 12
9. Valor o variación riesgo de tasa de interés ............................................... 9(14)
10. Valor o variación riesgo de moneda extranjera ........................................ 9(14)
11. Valor o variación riesgo de materias primas. ........................................... 9(14)
12. Valor o variación riesgo de cotizaciones bursátiles .................................. 9(14)
13. Filler .......................................................................................................... X(92)
Largo del registro ............... 194 bytes
## 1. TIPO DE REGISTRO
Corresponde al código que identifica el tipo de registro. Debe ser “06”.
## 2. FECHA
Corresponde a la fecha a la cual se refiere la información.
## 3. NIVEL DE CONSOLIDACIÓN
Corresponde al código asociado al nivel de consolidación, el cual se deberá indicar según la Tabla 80 de este Manual.
## 4. ID ESTRATEGIA
Corresponde al número identificador único correlativo iniciado en 1, denominado por el banco para identificar cada una de las estrategias de opciones de acuerdo con cada método utilizado y tipo de riesgo. Cabe señalar que un mismo id estrategia puede referirse a más de una clase de riesgo.
## 5. MONEDA
Corresponde al código que identifica la moneda en la que se materializarán las posiciones en opciones o su tipo de reajustabilidad. Se debe indicar la moneda según los códigos de la Tabla 1 de este Manual.
Para operaciones pagaderas en pesos reajustables en moneda extranjera
(incluidas las expresadas en moneda extranjera y pagaderas en pesos), se utilizará el código correspondiente a la moneda extranjera de que se trate y no el código que identifica el tipo de reajustabilidad.
## 6. MÉTODO
Corresponde al código que identifica el tipo de tratamiento de opciones utilizado. Los códigos corresponden a:
01 Método simplificado
02 Método de escenarios
03 Método delta plus - gamma
04 Método delta plus – vega
## 7. VALOR POSICIÓN
Corresponde al monto del valor de mercado de las posiciones en opciones.
## 8. VALOR SUBYACENTE
Corresponde al monto del valor nominal de mercado del subyacente.
Este campo debe reportarse cuando el campo método corresponda al método simplificado. En caso contrario, reportar cero.
Circular N°2.288 / 27.04.2021 por Resolución N°2256

Archivo R07 Hoja 13
## 9. VALOR O VARIACIÓN RIESGO DE TASA DE INTERÉS
Corresponde al valor del cargo por riesgo de tasa de interés cuando los métodos utilizados sean el simplificado o el delta-plus. Si el método utilizado es el simplificado, debe reportarse el riesgo específico y el riesgo general. En el caso que el método utilizado sea el método de escenarios, reportar la máxima pérdida respecto a su valor base en función de la volatilidad implícita y precio del subyacente para el riesgo de tasa de interés.
En caso de no tener posiciones afectas a riesgo de materias primas, reportar cero.
## 10. VALOR O VARIACIÓN RIESGO DE MONEDA EXTRANJERA
Corresponde al valor del cargo por riesgo de moneda extranjera cuando los métodos utilizados sean el simplificado o el delta-plus. En el caso que el método utilizado sea el de escenarios, reportar la máxima pérdida respecto a su valor base en función de la volatilidad implícita y precio del subyacente para el riesgo de moneda extranjera.
En caso de no tener posiciones afectas a riesgo de materias primas, reportar cero.
## 11. VALOR O VARIACIÓN RIESGO DE MATERIAS PRIMAS
Corresponde al valor del cargo por riesgo de materias primas cuando los métodos utilizados sean el simplificado o el delta-plus. En el caso que el método utilizado sea el de escenarios, reportar la máxima pérdida respecto a su valor base en función de la volatilidad implícita y precio del subyacente para el riesgo de tasa de materias primas.
En caso de no tener posiciones afectas a riesgo de materias primas, reportar cero.
## 12. VALOR O VARIACIÓN RIESGO DE COTIZACIONES BURSÁTILES
Corresponde al valor del cargo por riesgo de cotizaciones bursátiles cuando los métodos utilizados sean el simplificado o el delta-plus. Si el método utilizado es el simplificado, debe reportarse el riesgo específico y el riesgo general. En el caso que el método utilizado sea el de escenarios, reportar la máxima pérdida respecto a su valor base en función de la volatilidad implícita y precio del subyacente para el riesgo de tasa de cotizaciones bursátiles.
En caso de no tener posiciones afectas a riesgo de cotizaciones bursátiles, reportar cero.
Registro para informar detalle de riesgo de opciones a través de método de escenarios En este registro se deben reportar el detalle de todas las posiciones en opciones, a través del método de escenarios, expuestas en el registro anterior.
Circular N°2.288 / 27.04.2021 por Resolución N°2256

Archivo R07 Hoja 14 La matriz que evalúa los cambios en el valor de las opciones y sus posiciones de cobertura asociada debe aplicarse para clase y subclase de riesgo. Esto es, si el banco tiene opciones de tasas y de monedas, se requiere el reporte de todos los escenarios para cada tipo de riesgo, ocurriendo lo mismo, cuando el banco tenga opciones de moneda USD/CLP y EUR/USD, por ejemplo.
La información reportada deberá reflejar la metodología y cálculo de las matrices utilizadas para la obtención del valor o variación reportada en el registro anterior, a la última fecha de cada mes.
Este registro se informa sólo para el último día hábil de cada semana.
1. Tipo de registro ........................................................................................ 9(02)
2. Fecha ......................................................................................................... F(08)
3. Id estrategia .............................................................................................. 9(02)
4. Clase de riesgo ........................................................................................... 9(02)
5. Subclase de riesgo ..................................................................................... X(05)
6. Id escenario ............................................................................................... 9(02)
7. Valor posición ........................................................................................... 9(14)
8. Variación valor subyacente ....................................................................... 9(14)
9. Variación volatilidad ................................................................................. 9(14)
10. Ganancia o pérdida bruta ......................................................................... s9(14)
11. Ganancia o pérdida cubierta ..................................................................... s9(14)
12. Filler .......................................................................................................... X(101)
Largo del registro ............... 194 bytes
## 1. TIPO DE REGISTRO
Corresponde al código que identifica el tipo de registro. Debe ser “07”.
## 2. FECHA
Corresponde a la fecha a la cual se refiere la información.
## 3. ID ESTRATEGIA
Corresponde al número identificador único correlativo e iniciado en 1, denominado por el banco para identificar cada una de las estrategias de opciones de acuerdo con cada método utilizado y tipo de riesgo. Cabe señalar que un mismo id estrategia puede referirse a más de una clase de riesgo.
## 4. CLASE DE RIESGO
Corresponde al código asociado a cada clase de riesgo relevante, de acuerdo con el subyacente de la opción. Los códigos corresponden a:
01 Tasas de interés
02 Moneda extranjera
03 Materias primas
04 Cotizaciones bursátiles
## 5. SUBCLASE DE RIESGO
Corresponde a la descripción de los factores de riesgo asociado a cada clase de riesgo (campo 4), de acuerdo con el subyacente de la opción.
Circular N°2.288 / 27.04.2021 por Resolución N°2256

Archivo R07 Hoja 15 Se debe indicar la subclase de riesgo de acuerdo con lo siguiente:
i) cuando la clase de riesgo sea tasa de interés, las subclases de riesgo
corresponderán a la moneda y banda temporal, las que deberán expresarse como la unión del código de la Tabla 1 y el código de la Tabla
116 de este Manual (campo 7 “Banda temporal” del registro 2), por
ejemplo, 00102;
ii) cuando la clase de riesgo sea moneda extranjera, las subclases de riesgo
corresponderán a cada paridad de monedas y oro, las que deberán expresarse con los códigos de la Tabla 1;
iii) cuando la clase de riesgo sea materias primas, las subclases de riesgo
corresponderán a cada materia prima individual, las que deberán expresarse de acuerdo con la agrupación establecida en el campo 6 del registro 4 y;
iv) cuando la clase de riesgo sea cotizaciones bursátiles, las subclases de
riesgo corresponderán a cada mercado donde el banco opere, las que deberán expresarse de acuerdo con los códigos de la Tabla 45 del MSI.
## 6. ID ESCENARIOS
Corresponde al número de escenario de los N definidos como resultado de shocks en el precio/tasa del subyacente y en la volatilidad de éste para el cómputo del método de escenarios. Se deben informar al menos 9 escenarios (3 escenarios relativos al cambio en el precio del subyacente y 3 escenarios en función de la volatilidad), incluyendo el valor actual, el cual debe ser identificado como escenario número 1. Dentro de los escenarios reportados se deberá incluir aquel que genere la mayor pérdida utilizado para el cálculo del cargo de capital de la opción.
## 7. VALOR POSICIÓN
Corresponde al monto del valor de mercado de la posición en opciones que se está evaluando de acuerdo con el escenario definido.
## 8. VARIACIÓN PRECIO SUBYACENTE
Corresponde al monto del cambio aplicado al activo subyacente, dependiendo de la clase de riesgo, de acuerdo con lo definido en el Capítulo 21-7 de la RAN.
## 9. VARIACIÓN VOLATILIDAD
Corresponde al monto del cambio aplicado a la volatilidad implícita, de acuerdo con lo definido en el Capítulo 21-7 de la RAN.
## 10. GANANCIA O PÉRDIDA BRUTA
Corresponde al monto del valor obtenido como ganancia o pérdida generado a partir de la revalorización de las opciones con los distintos escenarios respecto al escenario base para cada opción y subyacente, sin considerar las posiciones de coberturas asociadas.
## 11. GANANCIA O PÉRDIDA CUBIERTA
Corresponde al monto del valor obtenido como ganancia o pérdida generado a partir de la revalorización de las opciones con los distintos escenarios respecto al escenario base para cada opción y subyacente, considerando las posiciones de coberturas asociadas. En caso de no existir posiciones cubiertas reportar repetir el valor del campo 10.
Circular N°2.288 / 27.04.2021 por Resolución N°2256

Archivo R07 Hoja 16 Registro para informar posiciones excluidas del marco de riesgo general de tasa de interés En este registro se deben reportar todas las posiciones excluidas del marco de riesgo de tasa de interés por encontrase perfectamente compensadas, ya sea para las posiciones activas o pasivas. Dichas posiciones deben ser consistentes con aquellas reportadas, de forma agregada, en el campo “Monto posiciones perfectamente compensadas” del registro
2.
Este registro se informa sólo para el último día hábil de cada semana.
1. Tipo de registro ........................................................................................ 9(02)
2. Fecha ......................................................................................................... F(08)
3. Nivel de consolidación .............................................................................. 9(01)
4. Sistema ...................................................................................................... 9(02)
5. Identificador del contrato SIID................................................................. X(52)
6. Identificador del contrato no reportado al SIID ....................................... X(30)
7. Filler .......................................................................................................... X(99)
Largo del registro ............... 194 bytes
## 1. TIPO DE REGISTRO
Corresponde al código que identifica el tipo de registro. Debe ser “08”.
## 2. FECHA
Corresponde al último día hábil a la cual se refiere la información.
## 3. NIVEL DE CONSOLIDACIÓN
Corresponde al código asociado al nivel de consolidación, el cual se deberá indicar según la Tabla 80 de este Manual.
## 4. SISTEMA
Corresponde al código asociado al sistema en el que fueron reportadas las especificaciones de información de los derivados excluidos del marco de riesgo de tasa de interés, en el Sistema Integrado de Información sobre transacciones de derivados (SIID) del Banco Central de Chile, de acuerdo con cada activo subyacente. Los códigos corresponden a:
01 Sistema N°1 – Operaciones con instrumentos derivados sobre monedas
02 Sistema N°2 – Operaciones con instrumentos derivados sobre tasa de
interés
03 Sistema N°3 – Operaciones con instrumentos derivados sobre renta fija
## 5. IDENTIFICADOR DEL CONTRATO SIID
Corresponde al código único asignado por el participante a cada contrato suscrito, el cual debe coincidir con el campo 18 “Identificador del Contrato” reportado en la sección 1 de los sistemas 1, 2 o 3, según corresponda a lo informado en el campo 4, del Sistema Integrado de Información sobre transacciones de derivados (SIID) del Banco Central de Chile.
En caso de que la operación sea realizada por una filial en el exterior, se debe informar el campo con ceros.
Circular N°2.288 / 27.04.2021 por Resolución N°2256

Archivo R07 Hoja 17
## 6. IDENTIFICADOR DEL CONTRATO NO REPORTADO AL SIID
Corresponde al código interno de identificación asignado en forma única por el banco para identificar cada una de las operaciones realizadas por filiales en el exterior.
En caso de que el registro tenga un identificador del contrato SIID asignado en el campo anterior, se debe informar el campo con ceros.
Registro para informar detalle de securitizaciones En este registro se deben reportar todas las exposiciones a instrumentos securitizados clasificados en el libro de negociación, en las que sus subyacentes sean identificables y exista un mercado líquido secundario, solo en los casos en que el banco tenga exposiciones de este tipo. En caso contrario, no deberá informar el registro.
Este registro se informa el último día hábil de cada semana para cada uno de los días hábiles de la semana reportada.
1. Tipo de registro ............................................................................... 9(02)
2. Fecha ................................................................................................ F(08)
3. Nivel de consolidación ..................................................................... 9(01)
4. Clasificación de riesgo ...................................................................... 9(02)
5. País ................................................................................................... 9(03)
6. Tipo de activo ................................................................................... 9(02)
7. Tipo de tramo ................................................................................... 9(02)
8. Madurez ........................................................................................... 9(02)
9. Cumplimiento de criterios ............................................................... 9(02)
10. PRM utilizado................................................................................... 9(03)V9(01)
11. Monto posición ................................................................................ 9(14)
12. Filler ................................................................................................. X(152)
Largo del registro ............... 194 bytes
## 1. TIPO DE REGISTRO
Corresponde al código que identifica el tipo de registro. Debe ser “09”.
## 2. FECHA
Corresponde a la fecha a la cual se refiere la información.
## 3. NIVEL DE CONSOLIDACIÓN
Corresponde al código asociado al nivel de consolidación, el cual se deberá indicar según la Tabla 80 de este Manual.
## 4. CLASIFICACIÓN DE RIESGO
Corresponde al código asociado a la clasificación de riesgo externa asignada a las contrapartes. Se debe indicar la categoría de riesgo según los códigos de la Tabla 92 1) de este Manual.
## 5. PAÍS
Corresponde al código que identifica el país de emisión de la securitización. Se debe indicar según los códigos de la Tabla 45 de este Manual.
Circular N°2.288 / 27.04.2021 por Resolución N°2256

Archivo R07 Hoja 18
## 6. TIPO DE ACTIVO
Corresponde al código que indica el tipo de activo que respalda la emisión. Los
códigos corresponden a:
01 Instrumentos financieros
02 Créditos hipotecarios
03 Créditos de consumo
04 Otras colocaciones
05 Tarjetas de crédito
09 Otros activos
## 7. TIPO DE TRAMO
Corresponde al código asociado al grado de preferencia de la serie o tramo. Los
códigos corresponden a:
01 Tramo preferente
02 Tramo subordinado
09 No aplica
## 8. MADUREZ
Corresponde al vencimiento efectivo residual del tramo, en años, calculada como la madurez promedio ponderada de los flujos de caja, de acuerdo con lo estipulado en el numeral 3.13 del Capítulo 21-6 de la RAN.
## 9. CUMPLIMIENTO DE CRITERIOS
Corresponde al código asociado al cumplimiento de los criterios para la distinción de securitizaciones menos complejas, que hacen alusión a su simplicidad, transparencia y comparabilidad (STC) descritos en el Anexo N°2 del Capítulo 21-6 de la RAN. Los códigos corresponden a:
01 Cumple STC.
02 No cumple STC.
## 10. PRM UTILIZADO
Corresponde al ponderador por riesgo de mercado utilizado en las securitizaciones multiplicado por 100, el cual depende de los campos descritos previamente. Puede corresponder a alguno de los valores de las tablas descritas en el numeral 3.13 del Capítulo 21-6 de la RAN o, en los casos en que la madurez de las exposiciones no esté dentro de las tablas mencionadas, los ponderadores pueden ser calculados acorde a lo señalado en el mismo numeral.
## 11. MONTO POSICIÓN
Corresponde al monto de la exposición a instrumentos securitizados afectas a riesgo específico de tasa de interés, de acuerdo con lo estipulado en el Capítulo
21-6 de la RAN.
Circular N°2.288 / 27.04.2021 por Resolución N°2256

Archivo R07 Hoja 19 Carátula de cuadratura El archivo R07 debe entregarse con una carátula de cuadratura cuyo modelo se
especifica a continuación:
MODELO Institución: ________________________________ Código: _______ Información correspondiente al mes de: _________________ Archivo R07

| Número de registros |  |
| --- | --- |
| Número de registros con código 01 en el campo 1 |  |
| Número de registros con código 02 en el campo 1 |  |
| Número de registros con código 03 en el campo 1 |  |
| Número de registros con código 04 en el campo 1 |  |
| Número de registros con código 05 en el campo 1 |  |
| Número de registros con código 06 en el campo 1 |  |
| Número de registros con código 07 en el campo 1 |  |
| Número de registros con código 08 en el campo 1 |  |
| Número de registros con código 09 en el campo 1 |  |

Observaciones En los registros anteriores se incluirán solo las combinaciones que resulten atingentes al banco.
Circular N°2.288 / 27.04.2021 por Resolución N°2256

Archivo R08 Hoja 1
CÓDIGO : R08
NOMBRE : ACTIVOS PONDERADOS POR RIESGO OPERACIONAL
SISTEMA : Riesgos PERIODICIDAD : Mensual PLAZO : 9 días hábiles.
En este archivo se informarán los elementos que componen los principales indicadores para el cálculo de los activos ponderados por riesgo operacional (APRO) a fin de determinar el requerimiento de capital por este tipo de riesgo, bajo método estándar.
Los datos que deben proporcionarse se refieren a la situación consolidada global, situación consolidada local y al banco sin consolidar (individual).
Todos los valores monetarios deben reflejarse en pesos, considerando el valor de la UF de la última fecha disponible del mes de referencia del archivo, en los casos que sea requerido.
Primer registro
1. Código del banco ............................................................................................... 9(04)
2. Identificación del archivo ................................................................................... X(03)
3. Período ............................................................................................................... P(06)
4. Filler ................................................................................................................... X(77)
Largo del registro ..................................... 90 bytes
## 1. CÓDIGO DEL BANCO
Corresponde al código que identifica al banco.
## 2. IDENTIFICACIÓN DEL ARCHIVO
Corresponde a la identificación del archivo. Debe ser "R08".
## 3. PERÍODO
Corresponde al mes (AAAAMM) al cual se refiere la información.
Registros siguientes Los registros siguientes contendrán información sobre los elementos que componen los indicadores utilizados para el cálculo de los APRO, a través de método estándar, correspondientes al periodo al que se refiere la información. Esta información se identificará en el primer campo de cada registro, según los códigos:
Código Tipo de registro
01 Activos ponderados por riesgo operacional
02 Componente del indicador de negocios (BIC)
03 Base de pérdidas operacionales
Registro para informar activos ponderados por riesgo operacional
1. Tipo de registro ........................................................................................ 9(02)
2. Nivel de consolidación .............................................................................. 9(01)
3. Indicador de negocio (BI) ......................................................................... 9(14)V9(03)
4. Componente del indicador de negocio (BIC) ............................................ 9(14)V9(03)
5. Componente de pérdida (LC) .................................................................... 9(14)V9(03)
6. Multiplicador interno de pérdidas operacionales (ILM) .......................... 9(14)V9(03)
Circular N°2.288 / 27.04.2021 por Resolución N°2256

Archivo R08 Hoja 2
7. Utilización cálculo ILM ............................................................................. 9(02)
8. APRO ......................................................................................................... 9(14)V9(03)
Largo del registro ............... 90 bytes
## 1. TIPO DE REGISTRO
Corresponde al código que identifica el tipo de registro. Debe ser “01”.
## 2. NIVEL DE CONSOLIDACIÓN
Corresponde al código asociado al nivel de consolidación, el cual se deberá indicar según la Tabla 80 de este Manual.
## 3. INDICADOR DE NEGOCIO (BI)
Corresponde al valor del indicador de negocios, calculado de acuerdo con lo señalado en el numeral 2 del Capítulo 21-8 de la RAN.
## 4. COMPONENTE DEL INDICADOR DE NEGOCIO (BIC)
Corresponde al valor de la componente del indicador de negocios, igual a la suma ponderada de los montos del BI en función de dos tramos, calculados de acuerdo con lo señalado en el numeral 2 del Capítulo 21-8 de la RAN.
## 5. COMPONENTE DE PÉRDIDA (LC)
Corresponde al valor de la componente de pérdida, calculada de acuerdo con lo señalado en el numeral 2 del Capítulo 21-8 de la RAN, para aquellos bancos que optaron por utilizar LC. Si el banco no utiliza el LC para el cálculo del cargo por riesgo operacional, reportar el valor del BIC.
## 6. MULTIPLICADOR INTERNO DE PÉRDIDAS OPERACIONALES (ILM)
Corresponde al valor del multiplicador interno de pérdidas operacionales de un banco, calculados de acuerdo con lo señalado en el numeral 2 del Capítulo 21-8 de la RAN, independientemente de si se utiliza el ILM para el cómputo de los APRO.
## 7. UTILIZACIÓN CÁLCULO ILM
Corresponde al código que identifica si las pérdidas reportadas son utilizadas en el cálculo del ILM (campo 6). Los códigos corresponden a:
01 Si (BI en tramo 1 opcional y BI en tramo 2).
02 No (BI en tramo 1).
Aquellos bancos que reporten “Si” deben ser aquellos que se encuentren con un BI (campo 3) en el tramo 2 y aquellos bancos que se encuentran con un BI en tramo 1 y optan por utilizar información de sus pérdidas operaciones para el cómputo de los APRO.
## 8. APRO
Corresponde al monto de los activos ponderados por riesgo operacional, obtenidos a través de método estándar, calculados de acuerdo con lo señalado en el numeral 2 del Capítulo 21-8 de la RAN.
Registro para informar componentes del indicador de negocios.
1. Tipo de registro ........................................................................................ 9(02)
2. Nivel de consolidación .............................................................................. 9(01)
3. Tipo de componente .................................................................................. 9(02)
4. Monto ........................................................................................................ 9(14)V9(03)
5. Filler .......................................................................................................... X(68)
Largo del registro ............... 90 bytes Circular N°2.288 / 27.04.2021 por Resolución N°2256

Archivo R08 Hoja 3
## 1. TIPO DE REGISTRO
Corresponde al código que identifica el tipo de registro. Debe ser “02”.
## 2. NIVEL DE CONSOLIDACIÓN
Corresponde al código asociado al nivel de consolidación, el cual se deberá indicar según la Tabla 80 de este Manual.
## 3. TIPO DE COMPONENTE
Corresponde al código que identifica al tipo de componente utilizado en el cómputo de los componentes ILDC, FC y SC. Los códigos corresponden a:
01 Ingresos por intereses (II)
02 Gastos por intereses (IE)
03 Activos que generan intereses (IEA)
04 Ingresos por dividendos (DI)
05 Ingresos netos del libro de negociación (TB)
06 Ingresos netos del libro de banca (BB)
07 Otros ingresos operativos (OOI)
08 Otros gastos operativos (OOE)
09 Ingresos por comisiones (FI)
10 Gastos por comisiones (FE)
Todos los códigos anteriores deben reportarse en cada periodo, reportando valor cero cuando corresponda.
## 4. MONTO
Corresponde al monto de cada tipo componente.
Registro para informar base de pérdidas operacionales.
En este registro se deben reportar el detalle de todos los eventos que materialicen pérdidas operacionales en el mes. Además, se deberán reportar los montos de gastos y recuperaciones asociados a pérdidas operacionales asociados a un mismo evento.
Los bancos deberán utilizar la fecha de contabilización del evento para construir el conjunto de registros sobre pérdidas. En el caso de contingencias legales, la fecha de contabilización será aquella en la que se constituye una provisión para esta contingencia legal en el estado de situación financiera, con su reflejo correspondiente en el estado de resultados.
1. Tipo de registro ........................................................................................ 9(02)
2. Código institución afectada ....................................................................... 9(03)
3. Fecha de ocurrencia .................................................................................. F(08)
4. Fecha de descubrimiento .......................................................................... F(08)
5. Fecha de contabilización ........................................................................... F(08)
6. Número interno de identificación del incidente ....................................... X(30)
7. Nivel categoría de Basilea y tipo de evento operacional ........................... 9(02)
8. Procesos afectados .................................................................................... 9(02)
9. Tipo de monto ........................................................................................... 9(02)
10. Monto ........................................................................................................ 9(14)V9(03)
11. Tipo de gasto ............................................................................................. 9(02)
12. Tipo de recuperación ................................................................................. 9(02)
13. Exclusión por reconocimiento de pérdidas en riesgo de crédito .............. 9(02)
14. Filler .......................................................................................................... X(02)
Largo del registro ............... 90 bytes Circular N°2.288 / 27.04.2021 por Resolución N°2256

Archivo R08 Hoja 4
## 1. TIPO DE REGISTRO
Corresponde al código que identifica el tipo de registro. Debe ser “03”.
## 2. CÓDIGO INSTITUCIÓN AFECTADA
Corresponde al código a la institución en la que ocurrió el evento de pérdida operacional o aquella que fue afectada, según la codificación dada por esta Comisión.
Cuando se reporten recuperaciones, deben excluirse aquellas que provengan de aseguradoras que sean filiales dentro del perímetro de consolidación.
## 3. FECHA DE OCURRENCIA
Corresponde a la fecha de ocurrencia cuando se produjo el evento operacional reportado.
## 4. FECHA DE DESCUBRIMIENTO
Corresponde a la fecha en la que se identifica el evento de pérdida.
## 5. FECHA DE CONTABILIZACIÓN
Corresponde a la fecha en la que se imputa contablemente la pérdida y/o recupero en los estados financieros.
## 6. NÚMERO INTERNO DE IDENTIFICACIÓN DEL INCIDENTE
Corresponde al código que identifica en forma unívoca el incidente reportado, asignado por el banco dentro de su registro interno. Este código servirá para otras pérdidas o recuperaciones asociadas al mismo incidente, enviados en archivos futuros.
Además de los incidentes reportados, se deben indicar códigos asociados al reporte de gastos y provisiones que no puedan ser asignados a eventos de pérdidas particulares, como es el caso de los servicios legales.
## 7. NIVEL CATEGORÍA DE BASILEA Y TIPO DE EVENTO OPERACIONAL
Corresponde al código que identifica la clasificación que tiene el banco respecto de los eventos de pérdidas operacionales (nivel 1 o 2), de acuerdo con lo establecido por el Comité de Supervisión Bancaria de Basilea. Se debe indicar el nivel de categoría según los códigos de la Tabla 121 de este Manual.
El nivel de categoría de Basilea informado debe considerar la máxima desagregación de información para la determinación del tipo de evento operacional.
Cuando se informen gastos y provisiones que no pueden ser asignados a eventos de pérdidas particulares, se debe informar el campo con el código 9900.
## 8. PROCESOS AFECTADOS
Corresponde al código asociado al tipo de canal, producto o servicio prestado por la institución que fueron afectados o puesto en riesgo por la ocurrencia del evento, ya sea en su disponibilidad o funcionamiento. Se debe indicar el nivel de categoría según los códigos de la Tabla 98 de este Manual.
En el caso en que se vean afectados dos canales, productos o procesos simultáneamente, se deberá considerar el código que mejor represente el incidente de acuerdo con los criterios internos del banco (mayor materialidad).
Circular N°2.288 / 27.04.2021 por Resolución N°2256

Archivo R08 Hoja 5
## 9. TIPO DE MONTO
Corresponde al código asociado al tipo de monto a reportar en el campo 11. Los
códigos corresponden a:
01 Pérdida (cargos directos en los estados de resultados)
02 Gastos y provisiones (costos incurridos internos o externos con relación directa
al evento operacional, provisiones o reservas contabilizadas contra el impacto potencial de pérdidas por riesgo operacional, otros)
03 Recuperación
## 10. MONTO
Corresponde al monto de las pérdidas que deben reportarse en la fecha en la que se contabilicen de acuerdo con el tipo de monto reportado (campo 10) y lo establecido en el numeral 3.2 del Capítulo 21-8 de la RAN.
## 11. TIPO DE GASTO
Corresponde al código que identifica el principal tipo de gasto asociado al evento de pérdida, ya sea interno o externo directamente atribuible al evento operacional. Los
códigos corresponden a:
01 Legales (gastos de servicios permanentes y adicionales en los que incurra el
banco)
02 Proveedores
03 Asesorías
04 Internos
09 Otros
10 No aplica (debe reportarse cuando el campo 9 toma valores 1 o 3)
## 12. TIPO DE RECUPERACIÓN
Corresponde al código asociado a las causas de la recuperación. Los códigos
corresponden a:
01 Compañías de seguros
02 Acciones judiciales
03 Otros (liberación de provisión)
09 No aplica
## 13. EXCLUSION POR RECONOCIMIENTO DE PÉRDIDAS EN RIESGO DE CRÉDITO
Corresponde al código que identifica si la exclusión reportada se debe a que estas pérdidas están reconocidas en riesgo de crédito, y por ello, no se utilizan para el cálculo del ILM. Los códigos corresponden a:
01 Sí
02 No
Carátula de cuadratura El archivo R08 debe entregarse con una carátula de cuadratura cuyo modelo se
especifica a continuación:
MODELO Institución: ________________________________ Código: _______ Información correspondiente al mes de: _________________ Archivo R08 Circular N°2.288 / 27.04.2021 por Resolución N°2256

Archivo R08 Hoja 6

| Número de registros |  |
| --- | --- |
| Número de registros con código 01 en el campo 1 |  |
| Número de registros con código 02 en el campo 1 |  |
| Número de registros con código 03 en el campo 1 |  |

Observaciones En los registros anteriores se incluirán solo las combinaciones que resulten atingentes al banco.
Circular N°2.288 / 27.04.2021 por Resolución N°2256