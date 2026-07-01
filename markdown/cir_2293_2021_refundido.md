<!-- source: cir_2293_2021_refundido.pdf -->
<!-- language: es -->
<!-- note: Las fórmulas matemáticas extraídas de PDFs pueden ser incompletas.
     Los bloques marcados con ⚠️ deben verificarse contra el PDF original. -->

# CIRCULAR N° 2293

Manual del Sistema de Información
### ARCHIVOS MAGNÉTICOS
Catálogo de archivos hoja 3
### SISTEMA DEUDORES

| Código | NOMBRE | Periodicidad | Plazo (días hábiles) |
| --- | --- | --- | --- |
| D02 | Deudas Específicas | Mensual | 7 |
| D03 | Características de los deudores | Mensual | 7 |
| D04 | Captaciones | Mensual | 10 |
| D05 | Deudores de operaciones transfronterizas | Mensual | 10 |
| D10 | Información de deudores artículo 14 LGB | Semanal (10) Mensual | 3 |
| D22 | Bienes en leasing | Mensual | 7 |
| D24 | Operaciones de factoraje | Mensual | 10(7) |
| D25 | Créditos relacionados otorgados por filiales y sucursales en el exterior | Mensual | 12 |
| D26 | Créditos otorgados por sucursales en el exterior | Mensual | 15 |
| D27 | Obligaciones de los arrendatarios en operaciones de leasing | Semanal (10) Mensual | 3 |
| D32 | Tasas de interés diarias por operaciones | Diario | 1 |
| D33 | Tasas de interés de créditos concedidos mediante el uso de líneas de crédito o sobregiros | Diario | 1 |
| D34 | Tasas de interés diarias para operaciones activas y pasivas | Diario | 1 (1) |
| D35 | Tasas de interés diarias por operaciones (9) | Diario | 4 |
| D40 | Créditos para exportaciones exentos de impuesto | Mensual | 12 |
| D41 | Créditos adquiridos de ANAP (2) | Semestral | 15 |
| D42 | Créditos para la vivienda con subsidio (2) | S/P (3) | 15 |
| D43 | Remates o cesiones en pago de viviendas subsi- diadas (4) | S/P (3) | - |
| D50 | Acreedores financieros | Mensual | 10 |
| D51 | Créditos para el financiamiento de estudios supe- riores | Trimestral | 15 |
| D52 | Tasas de interés de operaciones realizadas en líneas de crédito | Vigencia TMC (5) | 5 |
| D53 | Tasas de interés de créditos | Semanal | 4 |
| D54 | Garantías y personas con operaciones garanti- zadas (6) | Mensual | 10(7) |
| D55 | Operaciones con personas relacionadas (8) | Mensual | 15 |
| D56 | Operaciones afectas a los límites individuales de crédito (8) | Mensual | 15 |
| D57 | Créditos y otras operaciones con bancos regidos por la LGB (8) | Mensual | 15 |
| D58 | Tasas de interés diarias operaciones FOGAPE- COVID19 | Semanal | 2 |
| D59 | Tasas de interés diarias operaciones garantizadas por el FOGAPE Reactivación y FOGAPE Postergación | Semanal | 2 |

(1) Entregar en el curso de la mañana del día hábil bancario siguiente.
(2) Estos archivo lo enviarán sólo los bancos que tengan los créditos que se exige informar.
(3) Sin periodicidad. Los archivos se enviarán sólo en la oportunidad en que se soliciten.
(4) El archivo D43 se enviará sólo si existieron los remates o daciones en pago que se deben informar, y el plazo para su envío será indicado en la respectiva solicitud.
(5) Período de vigencia de una Tasa Máxima Convencional (TMC) determinada, es decir, desde el día de su publicación y hasta el día anterior al de publicación de la TMC siguiente.
(6) Este archivo D54 se remitirá por primera vez con la información referida al 30 de junio de 2016. Antes de esa fecha, se seguirán remitiendo los archivos D16 y D17.
Circular N°2.293 / 02.09.2021 por Resolución N°4850

Manual del Sistema de Información
### ARCHIVOS MAGNÉTICOS
Catálogo de archivos hoja 4
(7) El plazo de envío de los archivos se mantendrá en 14 días hábiles durante el segundo semestre de 2019, pasando a ser de 10 días hábiles a partir de enero de 2020.
(8) Los archivos D55, D56 y D57 se remitirán por primera vez con la información referida al mes de septiembre de 2019.
(9) El archivo D35 comenzará a remitirse con la información correspondiente al 1° de octubre de 2019.
(10) Los archivos D10 y D27 se enviarán de manera semanal con información referida a los viernes de cada semana y, además, con la información referida al último día de cada mes (considerando los plazos de implementación indicados en las Circular N°2.293 y 2.294, según el tipo de institución de que se trate)..
Archivos no aplicables a bancos:

| Código | NOMBRE | Periodicidad | Plazo (días hábiles) |
| --- | --- | --- | --- |
| D16 | Garantías constituidas | Trimestral | 10 |
| D17 | Personas con garantías constituidas | Trimestral | 10 |

Se mantienen en este Manual las instrucciones de estos archivos para información para las cooperativas de ahorro y crédito que deben seguir utilizándolos.
Circular N°2.293 / 02.09.2021 por Resolución N°4850

### ARCHIVO D10
CODIGO : D10
NOMBRE : INFORMACION DE DEUDORES ARTICULO 14 LGB
SISTEMA : Deudores PERIODICIDAD : Semanal y al cierre de cada mes PLAZO : 3 días hábiles En este archivo deben incluirse todos los créditos efectivos y contingentes que son objeto de refundición por esta Comisión, según lo indicado en el Capítulo 18-5 de la Recopilación Actualizada de Normas.
La información debe estar referida a los viernes de cada semana y al último día de cada mes.
Primer registro
## 1. Código de la institución financiera .... 9(04)
## 2. Identificación del archivo ............. X(03)
## 3. Fecha ................................ F(08)
4 Filler ................................. X(63)
_____ Largo del registro 78 bytes
## 1. CODIGO DE LA IF.
Corresponde a la identificación de la institución financiera según la codificación dada por esta Comisión.
## 2. IDENTIFICACION DEL ARCHIVO.
Corresponde a la identificación del archivo. Debe ser
"D10".
## 3. FECHA.
Corresponde a la fecha del viernes (aaaammdd) de la semana a la que se refiere la información y/o a la fecha
(aaaammdd) del último día de cada mes, cuando sea el caso.
Estructura de los registros
## 1. RUT del deudor ......................... R(09) VX(01)
## 2. Nombre o razón social del deudor ....... X(50)
## 3. Tipo de deudor ...................... 9(01)
## 4. Tipo de créditos u operaciones ......... 9(02)
5 Morosidad ................. 9(01)
6 Monto 9(14)
_____ Largo del registro 78 bytes Circular N°2.293 / 02.09.2021 por Resolución N° 4850

Archivo D10 / hoja 5 En general, de acuerdo con lo indicado en el Capítulo 18-5 de la Recopilación Actualizada de Normas, los valores que deben informarse en este archivo son aquellos que se obtienen de acuerdo con las condiciones convenidas para los créditos otorgados, sin considerar los intereses penales pactados para el período de mora transcurrido ni gastos de cobranza.
En el caso de operaciones contingentes, corresponderá al monto que podría traducirse en un crédito efectivo.
Los créditos u operaciones pagaderas en moneda extranjera se expresarán en pesos según el tipo de cambio de representación contable utilizado por el banco.
Las operaciones reajustables deberán estar calculadas según el valor del factor o unidad de cuenta pactado (UF, tipo de cambio, etc.) correspondiente al día a que se refiere la información.
El devengo de reajustes e intereses deberá ser reconocido en la semana que la entidad lo compute, o en su defecto a fin de mes.
Carátula de cuadratura El archivo D10 debe entregarse con una carátula de cuadratura cuyo modelo se especifica a continuación.
MODELO Institución: __________________________________ Código: ________ Información correspondiente a la semana de: ____________ Archivo D10

| Número de registros informados |  |
| --- | --- |
| Número de deudores directos informados |  |
| Número de deudores indirectos informados |  |
| Total deudas directas al día y operaciones contingentes |  |
| Total deudas indirectas al día |  |
| Total deudas directas con morosidad menor a 30 días |  |
| Total deudas directas con morosidad desde 30 a menos de 60 días |  |
| Total deudas directas con morosidad desde 60 a menos de 90 días |  |
| Total deudas directas con morosidad desde 90 a menos de 180 días |  |
| Total deudas directas con morosidad desde 180 días a menos de un año |  |
| Total deudas directas con morosidad desde un año a menos de dos años |  |
| Total deudas directas con morosidad desde dos años a menos de tres años |  |
| Total deudas directas con morosidad desde tres años a menos de cuatro años |  |
| Total deudas directas con morosidad desde cuatro años |  |
| Total deudas indirectas morosas |  |
| Total líneas de crédito de libre disposición |  |

Circular N° 2.293 / 02.09.2021 por Resolución N° 4850

### ARCHIVO D27
Hoja 1
CODIGO : D27
NOMBRE : OBLIGACIONES DE LOS ARRENDATARIOS EN OPERACIONES DE LEASING
SISTEMA : Deudores PERIODICIDAD : Semanal y al cierre de cada mes PLAZO : 3 días hábiles En este archivo debe entregarse información de las obligaciones que a la fecha de la información mantienen los arrendatarios que hayan pactado operaciones de leasing con el banco, siguiendo los criterios del archivo D10 como se indica.
Primer registro
1. Código del banco ................................................................................ 9(03)
2. Identificación del archivo ................................................................... X(03)
3. Fecha ................................................................................................... F(08)
4. Filler .................................................................................................... X(62)
Largo del registro .......... 76 bytes
## 1. CÓDIGO DEL BANCO
Corresponde al código que identifica al banco.
## 2. IDENTIFICACIÓN DEL ARCHIVO
Corresponde a la identificación del archivo. Debe ser "D27".
## 3. FECHA
Corresponde a la fecha del viernes (aaaammdd) de la semana a la que se refiere la información y/o a la fecha (aaaammdd) del último día de cada mes, cuando sea el caso.
Estructura de los registros
1. RUT del arrendatario ......................................................................... R(9)VX(01)
2. Nombre o razón social del arrendatario ............................................. X(50)
3. Tipo de arrendatario ........................................................................... 9(01)
4. Morosidad ........................................................................................... 9(01)
5. Monto .................................................................................................. 9(14)
Largo del registro .......... 76 bytes
## 1. RUT DEL ARRENDATARIO
Corresponde al RUT de la persona natural o jurídica que suscribe el contrato con la institución financiera.
## 2. NOMBRE O RAZÓN SOCIAL DEL ARRENDATARIO
Corresponde al nombre o razón social del arrendatario.
## 3. TIPO DE ARRENDATARIO
Código que identifica si se trata de arrendatarios relacionados con el banco de acuerdo al Capítulo 12-4 de la RAN, utilizando los siguientes:
8 Arrendatario relacionado
9 Arrendatario no relacionado
Circular N°2.293 / 02.09.2021 por Resolución N° 4850

### ARCHIVO D27
Hoja 2
## 4. MOROSIDAD
Debe incluirse un código para indicar la situación en que se encuentra el importe informado en relación con el cumplimiento oportuno de su pago, de acuerdo con los códigos utilizados para este efecto en archivo D10 referido a créditos, esto es:
Código Tiempo transcurrido desde el vencimiento
0 Crédito al día
1 Menos de 30 días
2 30 días o más, pero menos de 60 días
3 60 días o más, pero menos de 90 días
4 90 días o más, pero menos de 180 días
5 180 días o más, pero menos de un año
6 Un año o más, pero menos de dos años
7 Dos años o más, pero menos de 3 años
8 Tres años o más, pero menos de 4 años
9 Cuatro años o más
La información por morosidad debe tomar en cuenta las cláusulas contractuales y los eventuales convenios de pago posteriores, de modo que esa información refleje efectivamente lo que el deudor ha dejado de pagar según el calendario de pago vigente.
## 5. MONTO
Debe incluirse el monto que corresponda según lo definido en los campos anteriores.
Carátula de cuadratura El archivo D27 debe entregarse con una carátula de cuadratura cuyo modelo se
especifica a continuación:
MODELO Institución __________________________ Código: _______ Información correspondiente a la semana de: _____________________ Archivo D27

| Número de registros informados |  |
| --- | --- |
| Total montos al día |  |
| Total montos morosos |  |

Circular N°2.293 / 02.09.2021 por Resolución N° 4850

Texto actualizado: Circular N° 23 Sociedades de apoyo al giro Hoja 4
## ANEXO N° 1 INFORMACION QUE DEBEN ENVIAR LOS EMISORES DE TARJETAS DE CRÉDITO
Descrita en el Manual del Sistema de Información para bancos:

| Código | Nombre | Periodicidad | Plazo días hábiles bancarios |
| --- | --- | --- | --- |
| Archivo MB2 | Balance individual* | Mensual | 7 |
| Archivo MR2 | Estado de resultados individual* | Mensual | 7 |
| Archivo MC2 | Información complementaria individual* | Mensual | 7 |
| Archivo P38 | Tarjetas de crédito | Mensual | 9 |
| Archivo P39 | Tarjetas de crédito y débito. Utilización como medios de pago | Mensual | 9 |
| Archivo D03 | Características de los deudores | Mensual | 7 |
| Archivo D10 | Información de deudores artículo 14 LGB*** | Semanal Mensual | 3 |
| Archivo C11 | Colocaciones, créditos contingentes, provisiones y castigos | Mensual | 14 |
| Archivo C12 | Activos y provisiones de colocaciones de consumo y vivienda | Mensual | 14 |
| Archivo D33 | Tasas de interés de créditos concedidos mediante el uso de líneas de crédito o sobregiros | Diario | 1 |
| Archivo D35 | Tasas de interés diarias por operaciones | Diario | 1 |
| Archivo D52 | Tasas de interés de operaciones realizadas en líneas de crédito | Vigencia TMC** | 5 |
| Archivo D53 | Tasas de interés de créditos | Semanal | 4 |
| Archivo E04 | Reclamos de usuarios | Mensual | 7 |
| Archivo I12 | Incidentes de Ciberseguridad | Mensual | 10 |
| Formulario M2 | Resultado de evaluaciones y provisiones sobre colocaciones y créditos contingentes | Mensual | 9 |

* Esta información sustituye la indicada en la Circular N° 3 para Sociedades de Apoyo al Giro.
** Período de vigencia de una Tasa Máxima Convencional (TMC) determinada, es decir, desde el día
de su publicación y hasta el día anterior al de publicación de la TMC siguiente.
*** El archivo D10 se enviará de manera semanal con información referida a los viernes de cada semana y, además,
con la información referida al último día de cada mes (a partir de la fecha indicada en la Circular N°2.293 de esta Comisión).
Para la información básica, entrega de estados financieros u otras materias que no estén mencionadas en el presente Anexo, las emisoras se atendrán a lo dispuesto en la Circular
N° 3.
Circular N° 2.293 / 02.09.2021 por Resolución N°4850

Texto actualizado: Circular N° 108 COOPERATIVAS Hoja 9

| D04 | Depósitos a plazo (6) | Mensual | 10 | MSI bancos |
| --- | --- | --- | --- | --- |
| D03 | Características de los deudores(3) | Mensual | 7 | MSI bancos |
| D10 | Información de deudas artículo 14 LGB (7) | Semanal Mensual | 3 | MSI bancos |
| D16 | Garantías Constituidas | Trimestral | 10 | MSI bancos |
| D17 | Personas con garantías cons- tituidas | Trimestral | 10 | MSI bancos |
| D50 | Acreedores financieros | Mensual | 10 | MSI bancos |
| P10 | Cuentas de depósito a la vista y a plazo. | Mensual | 9 | MSI bancos |
| E04 | Reclamos de usuarios | Mensual | 7 | MSI bancos |
| Formulario M6 | Resultado de evaluaciones y pro- visiones por riesgo de crédito (4) | Mensual | 9 | ANEXO N° 14 adjunto |
| D01 | Deudas Generales (5) | Mensual | 7 | M SI bancos |
| Formulario M1 | Resultado de evaluaciones y pro- visiones sobre colocaciones y ope- raciones contingentes (5) | Mensual | 7 | MSI bancos |

(1): Estos archivos se enviarán a partir de la fecha indicada en el Compendio de Normas Contables.
(2): Estos archivos se enviarán por primera vez en el curso 2017, de acuerdo con lo siguiente:
El archivo C60 correspondiente al mes de enero de 2017 se enviará en el mes de marzo, dentro del mismo plazo en que debe entregarse el archivo de febrero.
Los archivos C61 de los meses de enero a junio de 2017, se remitirán en cualquier día hábil bancario del mes de julio.
(3): El archivo D03 se enviará por primera vez con la información referida al 30 de junio de 2017.
En ese primer archivo, como asimismo en los demás archivos D03 anteriores al del 31 diciembre de 2017, se podrá omitir la información de los deudores provenientes del año
2016.
(4): El Formulario M6 se remitirá por primera vez con la información correspondiente al mes de enero de 2017, dentro del plazo normal indicado en la tabla.
(5): Estos archivos se enviarán mientras no rijan las disposiciones del Compendio de Normas Contables. Por lo tanto, su último envío corresponderá a la información al 31 de diciembre de
2016.
(6): Estos archivos se enviarán por primera vez a partir del mes de febrero de 2020, con la información referida al mes de enero de dicho año.
(7): El archivo D10 se enviará de manera semanal con información referida a los viernes de cada semana y, además, con la información referida al último día de cada mes (a partir de la fecha indicada en la Circular N°2.293 de esta Comisión).
Circular N° 2.293 / 02.09.2021 por Resolución N°4850