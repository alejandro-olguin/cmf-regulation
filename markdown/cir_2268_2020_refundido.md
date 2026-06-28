<!-- source: cir_2268_2020_refundido.pdf -->
<!-- language: es -->
<!-- note: Las fórmulas matemáticas extraídas de PDFs pueden ser incompletas.
     Los bloques marcados con ⚠️ deben verificarse contra el PDF original. -->

### SISTEMA CONTABLE
(Instrucciones generales)
## 1. ARCHIVOS DEL SISTEMA CONTABLE
Este sistema comprende los archivos signados con la letra “M” y “C”, indicados en el Catálogo de Archivos.
## 2. MONEDAS
Todos los montos deberán ser informados en pesos, salvo que en las instrucciones del respectivo archivo se indique expresamente otra cosa.
Los saldos de operaciones pagaderas en monedas extranjeras deberán expresarse en pesos chilenos, de acuerdo con el tipo de cambio de representación contable utilizado por el banco.
## 3. ARCHIVOS SIGNADOS CON LA LETRA “M”
Los archivos signados con la letra “M” corresponden a la información mensual para la SBIF de que trata el Capítulo C-3 del Compendio de Normas Contables.
Los conceptos codificados que deben incluirse en esos archivos, como asimismo las instrucciones para la separación por monedas, se encuentran contenidos en ese Compendio.
Esta Comisión mantiene archivos con las versiones actualizadas de los códigos y conceptos que debe incluirse, la cual puede ser solicitada cada vez que se introduzca un cambio en el mencionado Capítulo C-3.
Circular N°2.268 / 28.08.2020 por Resolución N° 3870

### ARCHIVO MB1
Hoja 1
CODIGO : MB1
NOMBRE : BALANCE CONSOLIDADO
SISTEMA : Contable PERIODICIDAD : Mensual PLAZO : 7 días hábiles Primer registro
1. Código del banco ................................................................................ 9(04)
2. Identificación del archivo ................................................................... X(03)
3. Período ................................................................................................ P(06)
4. Filler .................................................................................................... X(69)
Largo del registro ............ 82 bytes
## 1. CÓDIGO DE LA IF
Corresponde al código que identifica al banco.
## 2. IDENTIFICACION DEL ARCHIVO
Corresponde a la identificación del archivo. Debe ser "MB1".
## 3. PERÍODO
Corresponde al mes (AAAAMM) al cual se refiere la información.
Estructura de los registros
1. Código contable .................................................................................. 9(07)
2. Monto total ......................................................................................... s9(14)
3. Monto moneda chilena no reajustable ............................................... s9(14)
4. Monto moneda reajustable por factores de IPC ................................ s9(14)
5. Monto moneda reajustable por tipos de cambio ............................... s9(14)
7. Monto moneda extranjera .................................................................. s9(14)
Largo del registro ............ 82 bytes Definición de términos
## 1. CÓDIGO CONTABLE:
Corresponde al código que identifica el rubro, línea o ítem a que corresponde la información del registro según el Capítulo C-3 del Compendio de Normas Contables. El archivo debe incluir todos los códigos, aun cuando los conceptos informados no sean aplicables en el caso del banco o por tratarse de balance consolidado.
Circular N°2.268 / 28.08.2020 por Resolución N° 3870

### ARCHIVO MR1
Hoja 1
CODIGO : MR1
NOMBRE : ESTADO DE RESULTADOS CONSOLIDADO
SISTEMA : Contable PERIODICIDAD : Mensual PLAZO : 7 días hábiles Primer registro
1. Código del banco ................................................................................ 9(04)
2. Identificación del archivo ................................................................... X(03)
3. Período ................................................................................................ P(06)
4. Filler .................................................................................................... X(69)
Largo del registro ............ 82 bytes
## 1. CÓDIGO DE LA IF
Corresponde al código que identifica al banco.
## 2. IDENTIFICACION DEL ARCHIVO
Corresponde a la identificación del archivo. Debe ser "MR1".
## 3. PERÍODO
Corresponde al mes (AAAAMM) al cual se refiere la información.
Estructura de los registros
1. Código contable .................................................................................. 9(07)
2. Monto total ......................................................................................... s9(14)
3. Monto moneda chilena no reajustable ............................................... s9(14)
4. Monto moneda reajustable por factores de IPC ................................ s9(14)
5. Monto moneda reajustable por tipos de cambio ............................... s9(14)
7. Monto moneda extranjera .................................................................. s9(14)
Largo del registro ............ 82 bytes Definición de términos
## 1. CÓDIGO CONTABLE:
Corresponde al código que identifica el rubro, línea o ítem a que corresponde la información del registro según el Capítulo C-3 del Compendio de Normas Contables. El archivo debe incluir todos los códigos, aun cuando los conceptos informados no sean aplicables en el caso del banco.
Circular N°2.268 / 28.08.2020 por Resolución N° 3870

### ARCHIVO MC1
Hoja 1
CODIGO : MC1
NOMBRE : INFORMACION COMPLEMENTARIA CONSOLIDADA
SISTEMA : Contable PERIODICIDAD : Mensual PLAZO : 7 días hábiles Primer registro
1. Código del banco ................................................................................ 9(04)
2. Identificación del archivo ................................................................... X(03)
3. Período ................................................................................................ P(06)
4. Filler .................................................................................................... X(09)
Largo del registro ............ 22 bytes
## 1. CÓDIGO DE LA IF
Corresponde al código que identifica al banco.
## 2. IDENTIFICACION DEL ARCHIVO
Corresponde a la identificación del archivo. Debe ser "MC1".
## 3. PERÍODO
Corresponde al mes (AAAAMM) al cual se refiere la información.
Estructura de los registros
1. Código contable .................................................................................. 9(07)
2. Monto .................................................................................................. 9(14)
3. Filler .................................................................................................... X(01)
Largo del registro .................... 22 bytes Definición de términos
## 1. CÓDIGO CONTABLE:
Corresponde al código que identifica el rubro o línea que corresponde la información del registro según el Capítulo C-3 del Compendio de Normas Contables. El archivo debe incluir todos los códigos, aun cuando los conceptos informados no sean aplicables en el caso del banco.
## 2. MONTO:
Todas las cifras deben incluirse en millones de pesos sin decimales, incluido los montos cero. La expresión en millones debe ser ajustada de manera que las sumas no arrojen diferencias.
Circular N°2.268 / 28.08.2020 por Resolución N° 3870

### ARCHIVO MB2
Hoja 1
CODIGO : MB2
NOMBRE : BALANCE INDIVIDUAL
SISTEMA : Contable PERIODICIDAD : Mensual PLAZO : 7 días hábiles Primer registro
1. Código del banco ................................................................................ 9(04)
2. Identificación del archivo ................................................................... X(03)
3. Período ................................................................................................ P(06)
4. Filler .................................................................................................... X(69)
Largo del registro ............ 82 bytes
## 1. CÓDIGO DE LA IF
Corresponde al código que identifica al banco.
## 2. IDENTIFICACION DEL ARCHIVO
Corresponde a la identificación del archivo. Debe ser "MB2".
## 3. PERÍODO
Corresponde al mes (AAAAMM) al cual se refiere la información.
Estructura de los registros
1. Código contable .................................................................................. 9(07)
2. Monto total ......................................................................................... s9(14)
3. Monto moneda chilena no reajustable ............................................... s9(14)
4. Monto moneda reajustable por factores de IPC ................................ s9(14)
5. Monto moneda reajustable por tipos de cambio ............................... s9(14)
7. Monto moneda extranjera .................................................................. s9(14)
Largo del registro ............ 82 bytes Definición de términos
## 1. CÓDIGO CONTABLE:
Corresponde al código que identifica el rubro, línea o ítem a que corresponde la información del registro según el Capítulo C-3 del Compendio de Normas Contables. El archivo debe incluir todos los códigos, aun cuando los conceptos informados no sean aplicables en el caso del banco o por tratarse de balance individual.
Circular N°2.268 / 28.08.2020 por Resolución N° 3870

### ARCHIVO MR2
Hoja 1
CODIGO : MR2
NOMBRE : ESTADO DE RESULTADOS INDIVIDUAL
SISTEMA : Contable PERIODICIDAD : Mensual PLAZO : 7 días hábiles Primer registro
1. Código del banco ................................................................................ 9(04)
2. Identificación del archivo ................................................................... X(03)
3. Período ................................................................................................ P(06)
4. Filler .................................................................................................... X(69)
Largo del registro ............ 82 bytes
## 1. CÓDIGO DE LA IF
Corresponde al código que identifica al banco.
## 2. IDENTIFICACION DEL ARCHIVO
Corresponde a la identificación del archivo. Debe ser "MR2".
## 3. PERÍODO
Corresponde al mes (AAAAMM) al cual se refiere la información.
Estructura de los registros
1. Código contable .................................................................................. 9(07)
2. Monto total ......................................................................................... s9(14)
3. Monto moneda chilena no reajustable ............................................... s9(14)
4. Monto moneda reajustable por factores de IPC ................................ s9(14)
5. Monto moneda reajustable por tipos de cambio ............................... s9(14)
7. Monto moneda extranjera .................................................................. s9(14)
Largo del registro ............ 82 bytes Definición de términos
## 1. CÓDIGO CONTABLE:
Corresponde al código que identifica el rubro, línea o ítem a que corresponde la información del registro según el Capítulo C-3 del Compendio de Normas Contables. El archivo debe incluir todos los códigos, aun cuando los conceptos informados no sean aplicables en el caso del banco o por tratarse de un estado individual.
Circular N°2.268 / 28.08.2020 por Resolución N° 3870

### ARCHIVO MC2
Hoja 1
CODIGO : MC2
NOMBRE : INFORMACION COMPLEMENTARIA INDIVIDUAL
SISTEMA : Contable PERIODICIDAD : Mensual PLAZO : 7 días hábiles Primer registro
1. Código del banco ................................................................................ 9(04)
2. Identificación del archivo ................................................................... X(03)
3. Período ................................................................................................ P(06)
4. Filler .................................................................................................... X(09)
Largo del registro ............ 22 bytes
## 1. CÓDIGO DE LA IF
Corresponde al código que identifica al banco.
## 2. IDENTIFICACION DEL ARCHIVO
Corresponde a la identificación del archivo. Debe ser "MC2".
## 3. PERÍODO
Corresponde al mes (AAAAMM) al cual se refiere la información.
Estructura de los registros
1. Código contable .................................................................................. 9(07)
2. Monto .................................................................................................. 9(14)
3. Filler .................................................................................................... X(01)
Largo del registro ............ 22 bytes Definición de términos
## 1. CÓDIGO CONTABLE:
Corresponde al código que identifica el rubro o línea que corresponde la información del registro según el Capítulo C-3 del Compendio de Normas Contables. El archivo debe incluir todos los códigos, aun cuando los conceptos informados no sean aplicables en el caso del banco.
## 2. MONTO:
Todas las cifras deben incluirse en pesos, incluido los montos cero.
Circular N°2.268 / 28.08.2020 por Resolución N° 3870

### ARCHIVO MB3
Hoja 1
CODIGO : MB3
NOMBRE : BALANCE SUCURSAL EN EL EXTERIOR
SISTEMA : Contable PERIODICIDAD : Mensual PLAZO : 7 días hábiles Primer registro
1. Código del banco ................................................................................ 9(04)
2. Identificación del archivo ................................................................... X(03)
3. Período ................................................................................................ P(06)
4. Filler .................................................................................................... X(13)
Largo del registro ............ 26 bytes
## 1. CÓDIGO DEL BANCO
Corresponde al código que identifica al banco.
## 2. IDENTIFICACION DEL ARCHIVO
Corresponde a la identificación del archivo. Debe ser "MB3".
## 3. PERÍODO
Corresponde al mes (AAAAMM) al cual se refiere la información.
Estructura de los registros
1. Código de la sucursal en el exterior ................................................... .9(03)
2. Código contable .................................................................................. .9(07)
3. Monto total ........................................................................................ s9(14)
4. Filler .................................................................................................... X(01)
Largo del registro ............ 26 bytes Definición de términos
## 1. CÓDIGO DE LA SUCURSAL EN EL EXTERIOR
Corresponde al código que identifica a cada sucursal del banco en el exterior.
## 2. CÓDIGO CONTABLE:
Corresponde al código que identifica el rubro, línea o ítem a que atañe la información del registro según el Capítulo C-3 del Compendio de Normas Contables. El archivo debe incluir todos los códigos, aun cuando los conceptos informados no sean aplicables en el caso de la sucursal.
Circular N°2.268 / 28.08.2020 por Resolución N° 3870

### ARCHIVO MR3
Hoja 1
CODIGO : MR3
NOMBRE : ESTADO DE RESULTADOS SUCURSAL EN EL
EXTERIOR SISTEMA : Contable PERIODICIDAD : Mensual PLAZO : 7 días hábiles Primer registro
1. Código del banco ................................................................................ 9(04)
2. Identificación del archivo ................................................................... X(03)
3. Período ................................................................................................ P(06)
4. Filler .................................................................................................... X(13)
Largo del registro ............ 26 bytes
## 1. CÓDIGO DEL BANCO
Corresponde al código que identifica al banco.
## 2. IDENTIFICACION DEL ARCHIVO
Corresponde a la identificación del archivo. Debe ser "MR3".
## 3. PERÍODO
Corresponde al mes (AAAAMM) al cual se refiere la información.
Estructura de los registros
1. Código de la sucursal en el exterior ................................................... .9(03)
2. Código contable .................................................................................. .9(07)
3. Monto total ........................................................................................ s9(14)
4. Filler .................................................................................................... X(01)
Largo del registro ............ 26 bytes Definición de términos
## 1. CÓDIGO DE LA SUCURSAL EN EL EXTERIOR
Corresponde al código que identifica a cada sucursal del banco en el exterior.
## 2. CÓDIGO CONTABLE:
Corresponde al código que identifica el rubro, línea o ítem a que atañe la información del registro según el Capítulo C-3 del Compendio de Normas Contables. El archivo debe incluir todos los códigos, aun cuando los conceptos informados no sean aplicables en el caso de la sucursal.
Circular N°2.268 / 28.08.2020 por Resolución N° 3870

### ARCHIVO MC3
Hoja 1
CODIGO : MC3
NOMBRE : INFORMACION COMPLEMENTARIA SUCURSAL EN EL
EXTERIOR SISTEMA : Contable PERIODICIDAD : Mensual PLAZO : 7 días hábiles Primer registro
1. Código del banco ................................................................................ 9(04)
2. Identificación del archivo ................................................................... X(03)
3. Período ................................................................................................ P(06)
4. Filler .................................................................................................... X(11)
Largo del registro ............ 24 bytes
## 1. CÓDIGO DEL BANCO
Corresponde al código que identifica al banco.
## 2. IDENTIFICACION DEL ARCHIVO
Corresponde a la identificación del archivo. Debe ser "MC3".
## 3. PERÍODO
Corresponde al mes (AAAAMM) al cual se refiere la información.
Estructura de los registros
1. Código de la sucursal en el exterior ................................................... .9(03)
2. Código contable .................................................................................. .9(07)
3. Monto total ........................................................................................ .9(14)
Largo del registro ............ 24 bytes Definición de términos
## 1. CÓDIGO DE LA SUCURSAL EN EL EXTERIOR
Corresponde al código que identifica a cada sucursal del banco en el exterior.
## 2. CÓDIGO CONTABLE:
Corresponde al código que identifica el rubro o línea que atañe la información del registro según el Capítulo C-3 del Compendio de Normas Contables. El archivo debe incluir todos los códigos, aun cuando los conceptos informados no sean aplicables en el caso de la sucursal.
Circular N°2.268 / 28.08.2020 por Resolución N° 3870

### ARCHIVO C16
CODIGO : C16
NOMBRE : INGRESOS Y GASTOS POR SERVICIOS CON EL
EXTERIOR SISTEMA : Contable PERIODICIDAD : Trimestral: Marzo, Junio, Septiembre y Diciembre PLAZO : 9 días hábiles En el presente archivo se informarán de manera agregada los saldos contables a la fecha a que se refiere el archivo, correspondientes a gastos e ingresos derivados por servicios contratados con no residentes, asociados a: comisiones, seguros, regalías y derechos de licencias, servicios de informática e información, y otros servicios bancarios. Se tratará de medir el intercambio con el exterior de servicios, por lo que no se consideran ingresos ni egresos por concepto de renta, tales como intereses, dividendos, ganancias de capital u otras remuneraciones a la provisión de capital. Todo ello a solicitud del Banco Central de Chile, como parte de la compilación de los servicios financieros en la Balanza de Pagos que ese organismo efectúa.
Primer registro
## 1. CODIGO DE LA IF.
Corresponde a la identificación de la institución financiera según la codificación dada por esta Comisión.
## 2. IDENTIFICACION DEL ARCHIVO.
Corresponde a la identificación del archivo. Debe ser
"C16".
## 3. PERIODO.
Corresponde al mes al que se refiere la información
(aaaamm).
Estructura de los registros
1 Gastos por comisiones ....................... 9(14)
2 Ingresos por comisiones ..................... 9(14)
3 Gastos por primas de seguros ................ 9(14)
4 Ingresos por indemnizaciones de seguros ..... 9(14)
5 Gastos por regalías y derechos de licencias . 9(14)
6 Ingresos por regalías y derechos de licencias ........................................ 9(14)
7 Gastos por servicios de informática e información ...................................... 9(14)
8 Ingresos por servicios de informática e
información ................................. 9(14)
9 Gastos por servicios empresariales y profesionales (Honorarios) ....................... 9(14)
10 Ingresos por otros servicios bancarios
(Honorarios) ................................ 9(14) Largo del registro 140 bytes Circular N°2.268 / 28.08.2020 por Resolución N° 3870

### ARCHIVO C17
CODIGO : C17
NOMBRE : ACTIVOS, PASIVOS Y CRÉDITOS CONTINGENTES
### CON EL EXTERIOR
SISTEMA : Contable PERIODICIDAD : Trimestral: Marzo, Junio, Septiembre y Diciembre PLAZO : 15 días hábiles En este archivo las instituciones financieras deben informar de las posiciones activas, pasivas y de créditos contingentes que al cierre de cada trimestre calendario mantienen con no residentes. Las instituciones que tengan sucursales o filiales en el exterior, deben informar además las posiciones activas, pasivas y de créditos contingentes que estas últimas mantengan con no residentes. La calidad de residente o no residente se refiere siempre a la residencia en Chile y no a la del país anfitrión en que se pudiese radicar una sucursal o filial.
Primer registro
## 1. CODIGO DE LA IF.
Corresponde a la identificación de la institución financiera según la codificación dada por esta Comisión.
## 2. IDENTIFICACION DEL ARCHIVO.
Corresponde a la identificación del archivo. Debe ser
"C17".
## 3. PERIODO.
Corresponde al mes al que se refiere la información
(aaaamm).
Estructura de los registros
1 Tipo de oficina informante .................. 9(01)
2 País u organismo ............................ 9(03)
3 Tipo de oficina de la contraparte ........... 9(01)
4 Clasificación de la contraparte ............. 9(02)
5 Tipo de posición ............................ 9(07)
6 Plazo de madurez residual ................... 9(01)
7 País del garante ............................ 9(03)
8 País de la matriz de la contraparte ......... 9(03)
9 Moneda o unidad de cuenta ................... 9(03)
10 Monto ....................................... 9(14)
Largo del registro 38 bytes Definición de términos
## 1. TIPO DE OFICINA DEL INFORMANTE
Corresponde al tipo de oficina a la que corresponde informar en relación a la operación, de acuerdo a los códigos de la tabla 53 “Tipo de oficina del informante o de la contraparte”.
Circular N°2.268 / 28.08.2020 por Resolución N° 3870

### ARCHIVO C40
CODIGO : C40
NOMBRE : FLUJOS ASOCIADOS A LOS RIESGOS DE TASA DE
### INTERES Y DE REAJUSTABILIDAD EN EL LIBRO DE
BANCA SISTEMA : Contable PERIODICIDAD : Mensual PLAZO : 9 días hábiles En este archivo se informarán los flujos calculados al último día de cada mes, para el cómputo de la relación de operaciones activas y pasivas, según la metodología de que trata el Capítulo III.B.2.2 del Compendio de Normas Financieras del Banco Central de Chile y el Capítulo 12-21 de la Recopilación Actualizada de Normas.
### PRIMER REGISTRO
## 1. Código de la institución financiera ........ 9(03)
## 2. Identificación del archivo .................. X(03)
## 3. Período ..................................... P(06)
## 4. Filler ...................................... X(14)
Largo del registro 26 bytes
## 1. CODIGO DE LA IF.
Corresponde a la identificación de la institución financiera según la codificación dada por esta Comisión.
## 2. IDENTIFICACION DEL ARCHIVO.
Corresponde a la identificación del archivo. Debe ser
"C40".
## 3. PERIODO.
Corresponde al mes (AAAAMM) a que se refiere la información.
### REGISTROS SIGUIENTES
Los registros siguientes contendrán información de distinta índole, por lo cual en el primer campo de cada registro se identificará de qué información se trata, según los siguientes códigos:
Código Tipo de registro (contenido)
01 Patrimonio efectivo.
02 Margen.
Circular N°2.268 / 28.08.2020 por Resolución N° 3870

Archivo C40 / hoja 5 Registro para indicar la exposición de opciones sobre tasas de interés en el Libro de Banca:
## 1. Tipo de registro ............................ 9(02)
## 2. Exposición al riesgo de opciones sobre tasas
de interés en el Libro de Banca ............. 9(14)
## 3. Filler ...................................... X(10)
Largo del registro 26 bytes
## 1. TIPO DE REGISTRO.
Corresponde al código que identifica el tipo de registro. Debe ser “07”.
## 2. EXPOSICION AL RIESGO DE OPCIONES SOBRE TASAS DE INTERES EN EL LIBRO DE BANCA.
Corresponde a la exposición al riesgo de mercado de las posiciones en opciones sobre tasas de interés en el Libro de Banca, calculada según lo dispuesto en el numeral 4.1 ó 4.2 del Anexo 1 del Capítulo III.B.2.2 del Compendio de Normas Financieras del Banco Central, según corresponda, considerando lo indicado en el numeral 3 de dicho anexo.
Registro para indicar los límites a las exposiciones de
corto y largo plazo:
## 1. Tipo de registro ............................ 9(02)
## 2. Límite a la exposición de corto plazo a los
riesgos de tasas de interés y de reajustabilidad en el Libro de Banca .................. 9(04)V9(01)
## 3. Límite a la exposición de largo plazo al
riesgo de tasas de interés en el Libro de Banca ....................................... 9(04)V9(01)
## 4. Filler ...................................... X(14)
Largo del registro 26 bytes
## 1. TIPO DE REGISTRO.
Corresponde al código que identifica el tipo de registro. Debe ser “08”.
## 2. LIMITE A LA EXPOSICION DE CORTO PLAZO A LOS RIESGOS DE TASAS DE INTERES Y DE REAJUSTABILIDAD EN EL LIBRO DE
BANCA.
La exposición de corto plazo a los riesgos de tasas de interés y de reajustabilidad en el Libro de Banca debe medirse conforme lo indicado en la primera ecuación del numeral 1.2 del Anexo 1 del Capítulo III.B.2.2 del Compendio de Normas Financieras del Banco Central de Chile. El límite que haya sido fijado para dicha exposición debe informarse como un porcentaje de la diferencia entre los ingresos y gastos por intereses y reajustes acumulados más los ingresos netos por comisiones sensibles a la tasa de interés a que se refiere dicho anexo, acumulados en los últimos doce meses.
Circular N°2.268 / 28.08.2020 por Resolución N° 3870

### ARCHIVO C41
CODIGO : C41
NOMBRE : INFORMACION SEMANAL SOBRE RIESGOS DE MERCADO SEGUN METODOLOGIA ESTANDARIZADA.
SISTEMA : Contable.
PERIODICIDAD : Semanal, referida a cada uno de los días hábiles bancarios de la semana anterior a la fecha de envío.
PLAZO : 3 días hábiles (tercer día hábil de la semana siguiente).
En este archivo se informarán los flujos para el cómputo de la relación de operaciones activas y pasivas, según medición estándar, de que trata el Capítulo III.B.2.2 del Compendio de Normas Financieras del Banco Central de Chile y el Capítulo 12-21 de la Recopilación Actualizada de Normas.
El archivo deben enviarlo solamente los bancos que no utilizan modelos propios para fines de determinar el límite normativo de que trata el numeral 1.6 del Capítulo III.B.2.2 antes mencionado, incluyendo la información diaria de lunes a viernes, con excepción de los feriados.
### PRIMER REGISTRO
## 1. Código de la institución financiera ........ 9(03)
## 2. Identificación del archivo .................. X(03)
## 3. Fecha para identificación del archivo ....... F(08)
## 4. Filler ...................................... X(20)
Largo del registro 34 bytes
## 1. CODIGO DE LA IF.
Corresponde a la identificación de la institución financiera según la codificación dada por esta Comisión.
## 2. IDENTIFICACION DEL ARCHIVO.
Corresponde a la identificación del archivo. Debe ser
"C41".
## 3. FECHA DE IDENTIFICACION DEL ARCHIVO.
Corresponde a la fecha del último día hábil de la semana cuya información diaria se informa (última fecha a la que se refiere la información).
Circular N°2.268 / 28.08.2020 por Resolución N° 3870

### ARCHIVO C42
CODIGO : C42
NOMBRE : INFORMACION MENSUAL SOBRE RIESGOS DE MERCADO SEGUN METODOLOGIA ESTANDARIZADA.
SISTEMA : Contable.
PERIODICIDAD : Mensual.
PLAZO : 9 días hábiles.
En este archivo se informarán los flujos para el cómputo de la relación de operaciones activas y pasivas, según medición estándar, de que trata el Capítulo III.B.2.2 del Compendio de Normas Financieras del Banco Central de Chile y el Capítulo 12-21 de la Recopilación Actualizada de Normas.
Este archivo deben enviarlo solamente los bancos que no utilizan la metodología estandarizada para la determinación del límite normativo, a fin de mostrar la situación sobre la base de esa metodología, referida al último día de cada mes.
### PRIMER REGISTRO
## 1. Código de la institución financiera ........ 9(03)
## 2. Identificación del archivo .................. X(03)
## 3. Período ..................................... P(06)
## 4. Filler ...................................... X(22)
Largo del registro 34 bytes
## 1. CODIGO DE LA IF.
Corresponde a la identificación de la institución financiera según la codificación dada por esta Comisión.
## 2. IDENTIFICACION DEL ARCHIVO.
Corresponde a la identificación del archivo. Debe ser
"C42".
## 3. PERIODO.
Corresponde al mes (AAAAMM) al cual se refiere la información.
### REGISTROS SIGUIENTES
Los registros siguientes corresponden a los instruidos para el archivo C41. En este caso la fecha incluida en el segundo campo de cada registro corresponderá a la del último día del mes que se informa.
Circular N°2.268 / 28.08.2020 por Resolución N° 3870

### ARCHIVO C43
CODIGO : C43
NOMBRE : INFORMACION CONSOLIDADA SOBRE RIESGOS DE
### MERCADO SEGUN METODOLOGIA ESTANDARIZADA.
SISTEMA : Contable.
PERIODICIDAD : Mensual.
PLAZO : 9 días hábiles.
En este archivo se informarán los flujos consolidados del banco con sus subsidiarias, referidos al último día de cada mes, para el cómputo de la relación de operaciones activas y pasivas, según medición estándar, de que trata el Capítulo III.B.2.2 del Compendio de Normas Financieras del Banco Central de Chile y el Capítulo 12-21 de la Recopilación Actualizada de Normas.
### PRIMER REGISTRO
## 1. Código de la institución financiera ........ 9(03)
## 2. Identificación del archivo .................. X(03)
## 3. Período ..................................... P(06)
## 4. Filler ...................................... X(22)
Largo del registro 34 bytes
## 1. CODIGO DE LA IF.
Corresponde a la identificación de la institución financiera según la codificación dada por esta Comisión.
## 2. IDENTIFICACION DEL ARCHIVO.
Corresponde a la identificación del archivo. Debe ser
"C43".
## 3. PERIODO.
Corresponde al mes (AAAAMM) al cual se refiere la información.
### REGISTROS SIGUIENTES
Los registros siguientes corresponden a los instruidos para el archivo C41. En este caso la fecha incluida en el segundo campo de cada registro corresponderá a la del último día del mes que se informa.
Circular N°2.268 / 28.08.2020 por Resolución N° 3870

### ARCHIVO C45
Hoja 1
CODIGO : C45
NOMBRE : CASTIGOS, RECUPERACIONES Y OTORGAMIENTO DE
### CRÉDITOS DE CONSUMO
SISTEMA : Contable PERIODICIDAD : Trimestral PLAZO : 15 días hábiles.
En este archivo se deberán informar los castigos, recuperaciones y resumen de los montos otorgados de los créditos de consumo para el trimestre calendario correspondiente.
Primer registro
1. Código del banco ............................................................................9(03)
2. Identificación del archivo ...............................................................X(03)
3. Período ............................................................................................F(06)
## 4. Filler……………………………………………………………………………………X(84)
Largo del registro ..........96 bytes
## 1. CÓDIGO DEL BANCO
Corresponde a la identificación de la institución según la codificación dada por esta Comisión.
## 2. IDENTIFICACIÓN DEL ARCHIVO.
Corresponde a la identificación del archivo. Debe ser "C45".
## 3. PERÍODO.
Corresponde al año-mes (AAAAMM) del último mes del trimestre calendario al que se refiere la información.
### REGISTROS SIGUIENTES
Los registros siguientes contendrán información de distinta índole, por lo cual en el primer campo de cada registro se identificará de qué información se trata, según los
siguientes códigos:
Código Tipo de registro (contenido) _____________________________
1 Información de operaciones castigadas
2 Información de recuperaciones de operaciones castigadas
3 Información resumen de otorgamiento de operaciones de consumo
Circular N°2.268 / 28.08.2020 por Resolución N° 3870

### ARCHIVO C46
Hoja 1
CODIGO : C46
NOMBRE : SITUACION DE LIQUIDEZ
SISTEMA : Contable PERIODICIDAD : Semanal: para información individual y consolidada local, a la que se refieren los numerales 7.1.i y 7.1.ii del Capítulo III.B.2.1 del Compendio de Normas Financieras del Banco Central, respectivamente. Debe estar referida a los días 4,
8, 12, 16, 20, 24, 28 y último día de cada mes.
Mensual: para información consolidada global a la que se refiere el numeral 7.1.iii del Capítulo III.B.2.1 del Compendio de Normas Financieras del Banco Central; y para cada banco establecido en el exterior, filial de un banco establecido en Chile, en forma consolidada. Debe estar referida al último día de cada mes.
PLAZO : 3 días hábiles: desde la fecha a que se refiere la información, para la información con periodicidad semanal.
9 días hábiles: desde el último día del mes, para la
información con periodicidad mensual.
Este archivo incluirá información periódica sobre el cómputo para los límites que tratan las Normas sobre la Gestión y Posición de Liquidez contenidas en el Capítulo 12-20 de la Recopilación Actualizada de Normas (RAN).
En el caso de la información mensual, sólo se informarán los flujos contractuales
(códigos 1 y 3 del campo tipo monto base).
Estas instrucciones también serán aplicables a aquella información que la Comisión pudiera requerir a los bancos de manera especial, o cuando se requiera una periodicidad distinta.
Primer registro
1. Código de la IF ................................................................................9(04)
2. Identificación del archivo ...............................................................X(03)
3. Fecha ...............................................................................................F(08)
## 4. Filler…..…………………………………………………………………………………X(11)
Largo del registro ..........26 bytes
## 1. CÓDIGO DE LA IF
Corresponde a la identificación de la institución financiera o filial en el exterior, según la codificación dada por esta Comisión.
## 2. IDENTIFICACIÓN DEL ARCHIVO.
Corresponde a la identificación del archivo. Debe ser "C46".
Circular N°2.268 / 28.08.2020 por Resolución N° 3870

### ARCHIVO C47
Hoja 1
CODIGO : C47
NOMBRE : ÍNDICES DE CONCENTRACIÓN
SISTEMA : Contable PERIODICIDAD : Semanal: para información individual y consolidada local, a la que se refieren los numerales 7.1.i y 7.1.ii del Capítulo III.B.2.1 del Compendio de Normas Financieras del Banco Central, respectivamente. Debe estar referida a los días 4,
8, 12, 16, 20, 24, 28 y último día de cada mes.
Mensual: para información consolidada global a la que se refiere el numeral 7.1.iii del Capítulo III.B.2.1 del Compendio de Normas Financieras del Banco Central; y para cada banco establecido en el exterior, filial de un banco establecido en Chile, en forma consolidada. Debe estar referida al último día de cada mes.
PLAZO : 3 día hábiles: desde la fecha a que se refiere la información, para la información con periodicidad semanal.
9 días hábiles: desde el último día del mes, para la
información con periodicidad mensual.
Este archivo incluirá información periódica sobre el cómputo de los Índices de Concentración que tratan las Normas sobre la Gestión y Posición de Liquidez contenidas en el Capítulo 12-20 de la Recopilación Actualizada de Normas (RAN).
Estas instrucciones también serán aplicables a aquella información que la Comisión pudiera requerir a los bancos de manera especial, o cuando se requiera una periodicidad distinta.
Primer registro
1. Código de la IF ................................................................................9(04)
2. Identificación del archivo ...............................................................X(03)
3. Fecha ...............................................................................................F(08)
## 4. Filler…..………………………………………………………………………………..X(37)
Largo del registro ..........52 bytes
## 1. CÓDIGO DE LA IF
Corresponde a la identificación de la institución financiera o filial en el exterior, según la codificación dada por esta Comisión.
## 2. IDENTIFICACIÓN DEL ARCHIVO.
Corresponde a la identificación del archivo. Debe ser "C47".
## 3. FECHA.
En el caso de los archivos semanales, corresponde a la fecha del día a que se refiere cada reporte (4, 8, 12, 16, 20, 24, 28 y último día de cada mes), en formato AAAAMMDD. Para el archivo mensual, y solo para efectos de su identificación, corresponderá al primer día del mes siguiente al de la fecha de reporte.
Circular N°2.268 / 28.08.2020 por Resolución N° 3870

### ARCHIVO C48
Hoja 1
CODIGO : C48
NOMBRE : RAZONES DE LIQUIDEZ
SISTEMA : Contable PERIODICIDAD : Semanal: para información individual y consolidada local, a la que se refieren los numerales 7.1.i y 7.1.ii del Capítulo III.B.2.1 del Compendio de Normas Financieras del Banco Central, respectivamente. Debe estar referida a los días 4,
8, 12, 16, 20, 24, 28 y último día de cada mes.
Mensual: para información consolidada global a la que se refiere el numeral 7.1.iii del Capítulo III.B.2.1 del Compendio de Normas Financieras del Banco Central; y para cada banco establecido en el exterior, filial de un banco establecido en Chile, en forma consolidada. Debe estar referida al último día de cada mes.
PLAZO : 3 día hábiles: desde la fecha a que se refiere la información, para la información con periodicidad semanal.
9 días hábiles: desde el último día del mes, para la
información con periodicidad mensual.
Este archivo incluirá información periódica sobre el cómputo de los indicadores Razón de Cobertura de Liquidez y Razón de Financiamiento Neto Estable que tratan las Normas sobre la Gestión y Posición de Liquidez contenidas en el Capítulo 12-20 de la Recopilación Actualizada de Normas (RAN).
Estas instrucciones también serán aplicables a aquella información que la Comisión pudiera requerir a los bancos de manera especial, o cuando se requiera una periodicidad distinta.
Primer registro
1. Código de la IF ................................................................................9(04)
2. Identificación del archivo ...............................................................X(03)
3. Fecha ...............................................................................................F(08)
## 4. Filler…..…………………………………………………………………………….…..X(55)
Largo del registro ..........70 bytes
## 1. CÓDIGO DE LA IF
Corresponde a la identificación de la institución financiera o filial en el exterior, según la codificación dada por esta Comisión.
## 2. IDENTIFICACIÓN DEL ARCHIVO.
Corresponde a la identificación del archivo. Debe ser "C48".
## 3. FECHA.
En el caso de los archivos semanales, corresponde a la fecha del día a que se refiere cada reporte (4, 8, 12, 16, 20, 24, 28 y último día de cada mes), en formato AAAAMMDD. Para el archivo mensual, y solo para efectos de su identificación, corresponderá al primer día del mes siguiente al de la fecha de reporte.
Circular N°2.268 / 28.08.2020 por Resolución N° 3870

CODIGO : C49
NOMBRE : RAZONES DE LIQUIDEZ
SISTEMA : Contable PERIODICIDAD : Semanal: para información individual y consolidada local, a la que se refieren los numerales 7.1.i y 7.1.ii del Título V del Capítulo III.B.2.1 del Compendio de Normas Financieras del Banco Central, respectivamente. Debe estar referida a los días 4, 8, 12, 16, 20, 24, 28 y último día de cada mes.
Mensual: para información consolidada global a la que se refiere el numeral 7.1.iii del Capítulo III.B.2.1 del Compendio de Normas Financieras del Banco Central; y para cada banco establecido en el exterior, filial de un banco establecido en Chile, en forma consolidada. Debe estar referida al último día de cada mes.
PLAZO : 3 día hábiles: desde la fecha a que se refiere la información, para la información con periodicidad semanal.
9 días hábiles: desde el último día del mes, para la
información con periodicidad mensual.
Este archivo incluirá información periódica sobre el cómputo de los indicadores Razón de Cobertura de Liquidez y Razón de Financiamiento Neto Estable que tratan las Normas sobre la Gestión y Posición de Liquidez contenidas en el Capítulo 12-20 de la Recopilación Actualizada de Normas (RAN).
Estas instrucciones también serán aplicables a aquella información que la Comisión pudiera requerir a los bancos de manera especial, o cuando se requiera una periodicidad distinta.
Primer registro
1. Código de la IF ................................................................................9(04)
2. Identificación del archivo ...............................................................X(03)
3. Fecha ...............................................................................................F(08)
## 4. Filler…..…………………………………………………………………………….…..X(55)
Largo del registro ..........70 bytes
## 1. CÓDIGO DE LA IF
Corresponde a la identificación de la institución financiera o filial en el exterior, según la codificación dada por esta Comisión.
## 2. IDENTIFICACIÓN DEL ARCHIVO.
Corresponde a la identificación del archivo. Debe ser "C49".
## 3. FECHA.
En el caso de los archivos semanales, corresponde a la fecha del día a que se refiere cada reporte (4, 8, 12, 16, 20, 24, 28 y último día de cada mes), en formato AAAAMMDD. Para el archivo mensual, y solo para efectos de su identificación, corresponderá al primer día del mes siguiente al de la fecha de reporte.
Circular N°2.268 / 28.08.2020 por Resolución N° 3870

### ARCHIVO D03
Hoja 1
CODIGO : D03
NOMBRE : CARACTERÍSTICAS DE LOS DEUDORES
SISTEMA : Deudores PERIODICIDAD : Mensual PLAZO : 7 días hábiles En este archivo debe entregarse información acerca de las personas naturales o jurídicas que se identifican en la información exigida por esta Comisión en otros archivos referidos a las operaciones del banco o de sus filiales o sucursales en el exterior.
El archivo se enviará incluyendo los datos de todas las personas cuyas operaciones están siendo informadas a esta Comisión.
Primer registro
1. Código del banco ................................................................................ 9(04)
2. Identificación del archivo ................................................................... X(03)
3. Período ................................................................................................ P(06)
4. Filler .................................................................................................... X(189)
Largo del registro ............ 202 bytes
## 1. CÓDIGO DEL BANCO
Corresponde al código que identifica al banco.
## 2. IDENTIFICACION DEL ARCHIVO
Corresponde a la identificación del archivo. Debe ser "D03".
## 3. PERÍODO
Corresponde al mes (AAAAMM) a que se refiere la información.
Estructura de los registros
## 1. Rut………………………………………………………………………………..R(09)VX(01)
2. Nombre ............................................................................................... X(50)
3. Categoría del deudor .......................................................................... 9(01)
4. Fecha de constitución ........................................................................ F(08)
5. Comuna o país .................................................................................... 9(06)
6. Actividad económica .......................................................................... 9(04)
7. Composición institucional .................................................................. 9(03)
8. Fecha de antecedentes financieros ..................................................... F(08)
9. Total de activos ................................................................................... 9(20)
10. Total de pasivos exigibles ................................................................... 9(20)
11 Patrimonio .......................................................................................... s9(20)
12 Resultado del ejercicio ........................................................................ s9(20)
Circular N°2.268 / 28.08.2020 por Resolución N° 3870

### ARCHIVO D04
CODIGO : D04
NOMBRE : DEPÓSITOS A PLAZO
SISTEMA : Deudores PERIODICIDAD : Mensual PLAZO : 10 días hábiles En este archivo se informarán a todas aquellas personas que hayan mantenido depósitos a plazo durante el mes al que se refiere la información, aun cuando no estén vigentes al término del periodo.
Primer registro
## 01. Código de la Institución Financiera ......... 9(03)
## 02. Identificación del archivo .................. X(03)
## 03. Periodo ..................................... P(06)
## 04. Filler ...................................... X(202)
Largo del registro 214 bytes
## 1. CODIGO DE LA IF
Corresponde a la identificación de la institución financiera según los códigos dados por esta Comisión.
## 2. IDENTIFICACION DEL ARCHIVO
Corresponde a la identificación del archivo. Debe ser
"D04".
## 3. PERIODO
Corresponde al mes al que se refiere la información, según lo solicitado.
Estructura de los registros
## 1. Tipo de depósito ............................ 9(02)
## 2. Moneda y reajustabilidad del depósito ....... 9(03)
## 3. Rut del cliente ............................. R(09)VX(01)
## 4. Nombre o razón del cliente .................. X(50)
## 5. Número interno de identificación del
depósito .................................... X(30)
## 6. Comuna origen del depósito .................. 9(06)
## 7. Monto original del depósito ................ 9(14)
## 8. Fecha de origen del depósito ................ F(08)
## 9. Fecha de extinción del depósito ............. F(08)
## 10. Saldo insoluto del depósito ................. 9(14)
Circular N°2.268 / 28.08.2020 por Resolución N° 3870

### ARCHIVO D09
CODIGO : D09
NOMBRE : CARTAS DE GARANTIA INTERBANCARIAS
SISTEMA : Deudores PERIODICIDAD : Mensual PLAZO : 7 días hábiles En este archivo se debe entregar información de las cartas de garantía interbancarias emitidas por la institución financiera que se encuentren vigentes a la fecha de la información y que garantizan a otro banco la obligación de un cliente que le ha otorgado garantías reales, según lo previsto en el Capítulo 8-12 de la Recopilación Actualizada de Normas.
Primer registro
## 1. CODIGO DE LA IF.
Corresponde a la identificación de la institución financiera según la codificación dada por esta Comisión.
## 2. IDENTIFICACION DEL ARCHIVO.
Corresponde a la identificación del archivo. Debe ser
"D09".
## 3. PERIODO.
Corresponde al año-mes al que se refiere la información
(aaaamm).
Estructura de los registros
## 01. RUT de la persona garantizada ................... R(09)VX(01)
## 02. Nombre o razón social de la persona garantizada . X(50)
## 03. Código Institución Financiera receptora ......... 9(03)
## 04. Identificación interna de la carta .............. X(10)
## 05. Fecha de emisión de la carta .................... F(08)
## 06. Monto garantizado en la carta ................... 9(14)
## 07. Fecha de vencimiento de la carta ................ F(08)
## 08. Identificación interna de la garantía ........... X(30)
## 09. Valor tasación comercial ........................ 9(14)
## 10. Filler .......................................... X(01)
Largo del registro .... 148 bytes Circular N°2.268 / 28.08.2020 por Resolución N° 3870

### ARCHIVO D10
CODIGO : D10
NOMBRE : INFORMACION DE DEUDORES ARTICULO 14 LGB
SISTEMA : Deudores PERIODICIDAD : Mensual PLAZO : 7 días hábiles En este archivo deben incluirse todos los créditos efectivos y contingentes que son objeto de refundición por esta Comisión, según lo indicado en el Capítulo 18-5 de la Recopilación Actualizada de Normas.
Primer registro
## 1. Código de la institución financiera .... 9(04)
## 2. Identificación del archivo ............. X(03)
## 3. Período ................................ 9(06)
4 Filler ................................. X(65)
_____ Largo del registro 78 bytes
## 1. CODIGO DE LA IF.
Corresponde a la identificación de la institución financiera según la codificación dada por esta Comisión.
## 2. IDENTIFICACION DEL ARCHIVO.
Corresponde a la identificación del archivo. Debe ser
"D10".
## 3. PERIODO.
Corresponde al mes (aaaamm) al que se refiere la información.
Estructura de los registros
## 1. RUT del deudor ......................... R(09) VX(01)
## 2. Nombre o razón social del deudor ....... X(50)
## 3. Tipo de deudor ...................... 9(01)
## 4. Tipo de créditos u operaciones ......... 9(02)
5 Morosidad ................. 9(01)
6 Monto 9(14)
_____ Largo del registro 78 bytes Circular N°2.268 / 28.08.2020 por Resolución N° 3870

### ARCHIVO D16
CODIGO : D16
NOMBRE : GARANTIAS CONSTITUIDAS
SISTEMA : Deudores PERIODICIDAD : Trimestral PLAZO : 10 días hábiles En este archivo deberán informarse todas las garantías constituidas a favor del banco.
Primer registro
## 1. CODIGO DE LA IF.
Corresponde a la identificación de la institución financiera según la codificación dada por esta Comisión.
## 2. IDENTIFICACION DEL ARCHIVO.
Corresponde a la identificación del archivo. Debe ser
"D16".
## 3. PERIODO.
Corresponde al mes (aaaamm) al que se refiere la información.
Estructura de los registros
1. RUT del dueño del bien o garante......... R(09)VX(1)
## 2. Nombre o razón social del dueño del bien
o garante ............................... X(50)
## 3. Número interno de identificación de la
garantía constituida .................... X(30)
## 4. Tipo de garantía ........................ 9(04)
## 5. Fecha de tasación ....................... F(08)
## 6. Valor tasación comercial ................ 9(14)
## 7. Monto del seguro vigente ................ 9(14)
## 8. Fecha de vencimiento del seguro ......... F(08)
Largo del registro 138 bytes Circular N°2.268 / 28.08.2020 por Resolución N° 3870

### ARCHIVO D17
CODIGO : D17
NOMBRE : PERSONAS CON GARANTIAS CONSTITUIDAS
SISTEMA : Deudores PERIODICIDAD : Trimestral PLAZO : 10 días hábiles En este archivo deben incluirse todas las personas cuyas operaciones actuales o futuras se encuentran caucionadas con las garantías informadas en el archivo D16.
Primer registro
## 1. CODIGO DE LA IF.
Corresponde a la identificación de la institución financiera según la codificación dada por esta Comisión.
## 2. IDENTIFICACION DEL ARCHIVO.
Corresponde a la identificación del archivo. Debe ser
"D17".
## 3. PERIODO.
Corresponde al mes (aaaamm) al que se refiere la información.
Estructura de los registros
1. RUT de la persona garantizada............ R(09)VX(1)
## 2. Nombre o razón social de la persona
garantizada ............................. X(50)
## 3. Número interno de identificación de la
garantía constituida .................... X(30)
## 4. Fecha de constitución de la garantía...... F(08)
## 5. Tipo de garantía..........................9(04)
## 6. Número interno de identificación de la
operación con garantía específica........ X(30)
## 7. Cláusula de cobertura ................... 9(04)
## 8. Valor aplicado por la institución........ 9(14)
Largo del registro 150 bytes Circular N°2.268 / 28.08.2020 por Resolución N° 3870

### ARCHIVO D32
Hoja 1
CODIGO : D32
NOMBRE : TASAS DE INTERÉS DIARIAS POR OPERACIONES.
SISTEMA : Deudores.
PERIODICIDAD : Diaria.
PLAZO : Un día hábil.
En este archivo se entregará información acerca de cada una de las operaciones que se indican, cursadas el o los días anteriores a su envío. Este archivo se utilizará tanto para la determinación de la tasa de interés corriente como para otros fines.
### OPERACIONES QUE DEBEN INFORMARSE EN ESTE ARCHIVO
Este archivo contendrá información individual de los créditos correspondientes a colocaciones (incluidas las operaciones de factoraje) y las compras de documentos con pacto, cursadas por el banco en todas las oficinas del país, incluyendo las operaciones con tasa de interés cero, con excepción de:
a) Los créditos que deben informarse en el archivo D33 y que corresponden a los
originados por el uso de líneas de crédito asociadas a cuentas corrientes o los sobregiros pactados en cuenta corriente, los correspondientes a tarjetas de crédito y otros que se puedan tomar automáticamente mediante el uso de líneas de crédito de disponibilidad inmediata. También se excluirán de este archivo D32 los sobregiros no pactados en cuentas corrientes.
b) Las operaciones asociadas a la compra de portafolios de créditos.
Los créditos deben incluirse en el respectivo archivo considerando el “momento de la convención”, en concordancia con lo indicado en el inciso cuarto del artículo 6° de la Ley N° 18.010.
Por tratarse de un archivo que persigue obtener información de operaciones de crédito de dinero concretadas, no se incluyen las operaciones de leasing ni los créditos contingentes.
### DESCRIPCIÓN DEL ARCHIVO
Primer registro
1. Código de la institución financiera .................................................. 9(04)
2. Identificación del archivo .................................................................. X(03)
3. Fecha.................................................................................................. F(08)
4. Filler .................................................................................................. X(79)
Largo del registro 94 bytes Circular N°2.268 / 28.08.2020 por Resolución N° 3870

### ARCHIVO D33
Hoja 2
## 1. CÓDIGO DE LA INSTITUCION FINANCIERA.
Corresponde a la identificación de la institución financiera según la codificación dada por esta Comisión.
## 2. IDENTIFICACIÓN DEL ARCHIVO.
Corresponde a la identificación del archivo. Debe ser "D33".
## 3. FECHA.
Corresponde al día (aaaammdd) a que se refiere la información.
Estructura de los registros
1. Fecha de la operación ........................................................................ F(08)
2. Tipo de operación .............................................................................. 9(03)
3. Destino del Producto Asociado a la operación ................................. 9(02)
4. Moneda .............................................................................................. 9(03)
5. Tipo de tasa de interés ...................................................................... 9(03)
6. Plazo contractual ............................................................................... 9(02)
7. Filler .................................................................................................. 9(01)
8. Tasa mínima ...................................................................................... 9(03)V9(04)
9. Tasa máxima ..................................................................................... 9(03)V9(04)
10. Tasa promedio ................................................................................... 9(03)V9(04)
11. Tramos de montos ............................................................................. 9(03)
12. Monto de operaciones ....................................................................... 9(14)
13. Número de operaciones .................................................................... 9(08)
Largo del registro .......................... 68 bytes Definición de términos
## 1. FECHA DE LA OPERACIÓN:
Se informará la fecha (aaaammdd) en que se efectuó la operación. Las operaciones efectuadas en días inhábiles se informan con su respectiva fecha de origen, en el archivo del día hábil bancario siguiente.
## 2. TIPO DE OPERACIÓN:
Identifica el tipo de las operaciones diarias, con el respectivo código de la Tabla 61 “Tipo de Operaciones Activas”.
## 3. DESTINO DEL PRODUCTO ASOCIADO A LA OPERACIÓN:
Debe incluirse el código que corresponda, según la Tabla 60 “Destino del Producto”.
## 4. MONEDA:
Se indicará el tipo de moneda de las operaciones de acuerdo a los códigos definidos en la Tabla 1 “Monedas y unidades de cuenta”.
Circular N°2.268 / 28.08.2020 por Resolución N° 3870

### ARCHIVO D34
Hoja 1
CÓDIGO : D34
NOMBRE : TASAS DE INTERÉS DIARIAS DE OPERACIONES
### ACTIVAS Y PASIVAS.
SISTEMA : Deudores.
PERIODICIDAD : Diario.
PLAZO : Un día hábil. Entregada en el curso de la mañana del día hábil bancario siguiente.
Este archivo contendrá información de las tasas de interés diarias contratadas en las operaciones activas y pasivas, desagregadas por tipo de operación, plazo, tipo de tasa y moneda. En este archivo se entregará información acerca de cada una de las operaciones que se indican, cursadas por el banco en todas las oficinas del país en el o los días anteriores a su envío.
### OPERACIONES QUE DEBEN INFORMARSE EN ESTE ARCHIVO
Este archivo deberá contener la información individual de las operaciones, activas y pasivas sujetas al pago de intereses, incluyendo también las operaciones de crédito con tasa cero, con excepción de:
a) las operaciones que correspondan a la compra de portafolios de créditos y,
b) las operaciones de leasing.
Como es natural, en este archivo no se informan los créditos contingentes.
### DESCRIPCIÓN DEL ARCHIVO
Primer registro
1. Código de la institución financiera .................................................. 9(04)
2. Identificación del archivo .................................................................. X(03)
3. Fecha.................................................................................................. F(08)
4. Filler .................................................................................................. X(59)
Largo del registro 74 bytes
## 1. CÓDIGO DE LA INSTITUCIÓN FINANCIERA.
Corresponde a la identificación de la institución financiera según la codificación dada por esta Comisión.
## 2. IDENTIFICACIÓN DEL ARCHIVO.
Corresponde a la identificación del archivo. Debe ser "D34".
## 3. FECHA.
Corresponde al día a que se refiere la información.
Circular N°2.268 / 28.08.2020 por Resolución N° 3870

### ARCHIVO D40
CODIGO : D40
NOMBRE : CREDITOS PARA EXPORTACIONES EXENTOS DE
IMPUESTO.
SISTEMA : Deudores PERIODICIDAD : Mensual.
PLAZO : 12 días hábiles Este archivo debe ser entregado por las empresas bancarias con la información de todos los créditos otorgados o recibidos durante el mes, cuyos documentos se encuentran exentos del impuesto de timbres y estampillas de acuerdo con lo previsto en el Nº 11 del artículo 24 del Decreto Ley Nº 3.475 y en el título I del Capítulo 14-8 de la Recopilación Actualizada de Normas.
### DESCRIPCION DEL ARCHIVO
Primer registro
## 1. Código de la institución financiera ............ 9(03)
## 2. Identificación del archivo ...................... X(03)
## 3. Período ......................................... F(06)
## 4. Filler .......................................... X(134)
Largo del registro 146 bytes
## 1. CODIGO DE LA IF.
Corresponde a la identificación de la institución financiera según la codificación dada por esta Comisión.
## 2. IDENTIFICACION DEL ARCHIVO.
Corresponde a la identificación del archivo. Debe ser
"D40".
## 3. PERIODO.
Corresponde al mes (aaaamm) a que se refiere la información .
Circular N°2.268 / 28.08.2020 por Resolución N° 3870

### ARCHIVO D42
CODIGO :D42
NOMBRE :CREDITOS PARA LA VIVIENDA CON SUBSIDIO.
SISTEMA :Deudores.
PERIODICIDAD :A pedido.
PLAZO :15 días hábiles.
En este archivo las instituciones financieras deben dar cuenta de aquellos créditos hipotecarios para viviendas asociadas a programas habitacionales y de subsidio.
Deben entregar datos respecto al valor de la vivienda y a las características del crédito, en cuanto a montos, tasas y plazos, y a la situación actual del préstamo, indicando la existencia de morosidad y castigos.
En caso de que se mantengan operaciones de leasing con subsidio, se incluirán también en este archivo siguiendo los mismos criterios que se indican para los préstamos hipotecarios.
### DESCRIPCION DEL ARCHIVO
Primer registro
## 1. Código de la institución financiera ............ 9(03)
## 2. Identificación del archivo ...................... X(03)
## 3. Fecha ........................................... F(08)
## 4. Filler .......................................... X(82)
Largo del registro 96 bytes
## 1. CODIGO DE LA IF.
Corresponde a la identificación del banco según la codificación dada por esta Comisión.
## 2. IDENTIFICACION DEL ARCHIVO.
Corresponde a la identificación del archivo. Debe ser
"D42".
## 3. FECHA.
Corresponde a la fecha (aaaammdd) a que se refiere la información.
Estructura de los registros
## 01. Rut del deudor .................................. R(09)VX(01)
## 02. Número interno de identificación de la
operación ....................................... X(30)
## 03. Valor de la vivienda en UF ...................... 9(04)
## 04. Tipo de vivienda ................................ 9(02)
## 05. Programa habitacional y de subsidio ............. 9(02)
06 Tipo de crédito ................................. 9(02)
## 07. Número de reprogramaciones efectuadas ........... 9(02)
## 08. Fecha del crédito ............................... F(08)
## 09. Moneda y reajustabilidad del contrato ........... 9(03)
Circular N°2.268 / 28.08.2020 por Resolución N° 3870

### ARCHIVO D43
CODIGO :D43
NOMBRE :REMATES Y CESIONES EN PAGO DE VIVIENDAS
SUBSIDIADAS.
SISTEMA :Deudores.
PERIODICIDAD :A pedido.
PLAZO :Según lo solicitado en cada oportunidad.
El objetivo de este archivo es que las instituciones financieras entreguen información acerca de remates o cesiones en pago de las viviendas adquiridas con subsidio y cuyo valor no supere las 2.000 UF. Para esto deben consignar el valor de la vivienda en el crédito original, los saldos de deuda antes de la operación, los niveles de morosidad a partir de los dividendos impagos y el valor para la vivienda al que se realizó la transferencia a terceros o al banco.
### DESCRIPCION DEL ARCHIVO
Primer registro
## 1. Código de la institución financiera ............ 9(03)
## 2. Identificación del archivo ...................... X(03)
## 3. Fecha ........................................... F(08)
## 4. Filler .......................................... X(34)
Largo del registro 48 bytes
## 1. CODIGO DE LA IF.
Corresponde a la identificación del banco según la codificación dada por esta Comisión.
## 2. IDENTIFICACION DEL ARCHIVO.
Corresponde a la identificación del archivo. Debe ser
"D43".
## 3. FECHA.
Corresponde al último día (aaaammdd) del último período que se solicita informar en el archivo.
Estructura de los registros
## 01. Período de la transferencia ..................... 9(04)
## 02. Tipo de transferencia ........................... 9(02)
## 03. Tramo del valor original de la vivienda en UF ... 9(02)
## 04. Número de viviendas ............................. 9(08)
05. Saldo de la deuda al momento de la transferencia ............................................. 9(14)
## 06. Número promedio de dividendos morosos ........... 9(03)
## 07. Valor de la transferencia ....................... 9(14)
## 08. Filler .......................................... X(01)
Largo del registro 48 bytes Circular N°2.268 / 28.08.2020 por Resolución N° 3870

### ARCHIVO D50
CODIGO : D50
NOMBRE : Acreedores Financieros SISTEMA : Deudores PERIODICIDAD : Mensual PLAZO : 10 días hábiles En este archivo deben informarse todas las personas que hayan mantenido saldos positivos de alguna clase de acreencia durante el mes al que se refiere la información, aun cuando estos no estén vigentes al término del mes.
Primer registro
## 01. Código de la Institución Financiera ......... 9(04)
## 02. Identificación del archivo .................. X(03)
## 03. Periodo ..................................... P(06)
## 04. Filler ...................................... X(151)
Largo del registro 164 bytes
## 01. CODIGO DE LA IF
Corresponde a la identificación de la institución financiera según los códigos dados por esta Comisión.
## 02. IDENTIFICACION DEL ARCHIVO
Corresponde a la identificación del archivo. Debe ser
"D50".
## 03. PERIODO
Corresponde al mes al que se refiere la información, según lo solicitado.
Estructura de los registros
## 01. Rut del cliente ............................. R(09)VX(01)
## 02. Nombre o razón social del cliente ........... X(50)
## 03. Número interno de identificación de la
operación ................................... X(30)
## 04. Tipo de acreencia.......................... . 9(02)
## 05. Tipo de cliente............................. 9(02)
## 06. Número de abonos............................ 9(14)
## 07. Monto de abonos............................. 9(14)
## 08. Número de cargos............................ 9(14)
## 09. Monto de cargos............................. 9(14)
## 10. Saldo a fin de mes.......................... 9(14)
Largo del registro 164 bytes Circular N°2.268 / 28.08.2020 por Resolución N° 3870

### ARCHIVO D51
Hoja 1
CODIGO : D51
NOMBRE : CRÉDITOS PARA EL FINANCIAMIENTO DE ESTUDIOS
SUPERIORES SISTEMA : Deudores PERIODICIDAD : Trimestral.
PLAZO : 15 días hábiles.
En el archivo se informaran antecedentes a nivel de operaciones de los deudores directos de créditos otorgados para el financiamiento de estudios superiores.
Los créditos que deben informase son aquellos que cumplen con las especificaciones indicadas en el Capítulo 18-5 de la Recopilación Actualizada de Normas.
La información requerida deberá ser enviada trimestralmente, referida a los meses de marzo, junio, septiembre y diciembre.
Primer registro
1. Código del banco ............................................................................ 9(03)
2. Identificación del archivo ............................................................... X(03)
3. Período ............................................................................................ F(06)
## 4. Filler……………………………………………………………………………………X(200)
Largo del registro .......... 212 bytes
## 1. CÓDIGO DE LA INSTITUCIÓN.
Corresponde a la identificación de la institución según la codificación dada por esta Comisión.
## 2. IDENTIFICACIÓN DEL ARCHIVO.
Corresponde a la identificación del archivo. Debe ser "D51".
## 3. PERÍODO.
Corresponde al año-mes (aaaamm) a que se refiere la información.
Estructura de los registros
1. Rut .................................................................................................. R(09)VX(01)
2 Número interno de identificación de la operación ........................ X(30)
3. Tipo de producto ............................................................................ 9(02)
4. Titular de la obligación ................................................................... 9(01)
5. Nivel educacional ........................................................................... 9(01)
6. Tipo de establecimiento educacional ............................................. 9(01)
7. Base del financiamiento ................................................................. .9(01)
8. Porcentaje máximo de la base financiado ...................................... .9(03) V9
(02)
9. Moneda y reajustabilidad ............................................................... .9(01)
10. Tipo de tasa de interés .................................................................... 9(01)
## 11. Tasa de interés de la operación ......................................................
9(03)V9(02) Circular N°2.268 / 28.08.2020 por Resolución N° 3870

### ARCHIVO D52
Hoja 1
CODIGO : D52
NOMBRE : TASAS DE INTERÉS DE OPERACIONES REALIZADAS
### EN LÍNEAS DE CRÉDITO.
SISTEMA : Deudores PERIODICIDAD : Según Vigencia Tasa Máxima Convencional PLAZO : 5 días hábiles bancarios En este archivo se deben informar todas las operaciones de crédito de dinero cursadas en el período de vigencia de una Tasa Máxima Convencional (TMC) determinada, es decir, desde el día de su publicación y hasta el día anterior al de publicación de la TMC siguiente, que se originan por el uso de líneas de crédito asociadas a cuentas corrientes, tarjetas de créditos u otras que sean de disponibilidad inmediata, a las cuales se les haya aplicado una tasa de interés mayor a cero. Todas las cifras de montos deberán ser informadas en pesos.
Primer registro
01. Código de la institución financiera…. ....................................... .9(04)
02. Identificación del archivo ......................................................... X(03)
03. Fecha ......................................................................................... F(08)
04. Filler…………………………………………….........................................X(111)
Largo del registro 126 bytes
## 01. CÓDIGO DE LA INSTITUCION FINANCIERA
Corresponde al código de identificación de la institución financiera según la codificación asignada por esta Comisión.
## 02. IDENTIFICACIÓN DEL ARCHIVO.
Corresponde a la identificación del archivo. Debe ser "D52".
## 03. FECHA.
Corresponde a la fecha (aaaammdd) de publicación de la TMC que le es aplicable a las operaciones informadas.
### REGISTROS SIGUIENTES
Los registros siguientes contendrán distinto tipo de información, la que se identificará en el primer campo de cada registro con los siguientes códigos:
Código Tipo de registro (contenido)
01 Créditos pactados en cuotas asociados a líneas de tarjetas de crédito.
02 Línea de crédito rotativa asociada a tarjeta de crédito.
03 Línea de crédito asociada a cuenta corriente.
04 Línea de crédito de disponibilidad inmediata, distinta de aquellas
asociadas a tarjetas de crédito y cuentas corrientes.
05 Operaciones con cargo inmediato a la línea rotativa asociada a las
tarjetas de crédito Circular N°2.268 / 28.08.2020 por Resolución N° 3870

### ARCHIVO D53
Hoja 1
CODIGO : D53
NOMBRE : TASAS DE INTERÉS DE CRÉDITOS.
SISTEMA : Deudores PERIODICIDAD : Semanal PLAZO : 4 días hábiles bancarios En este archivo deben informarse todas las operaciones de crédito de dinero en moneda nacional no reajustable por importes menores o iguales a 200 UF y por plazos mayores o iguales a 90 días, a las cuales se les haya aplicado una tasa de interés mayor a cero, cursadas en la semana anterior al envío, exceptuándose las operaciones que se originan por el uso de líneas de crédito asociadas a cuentas corrientes, tarjetas de crédito u otras que sean de disponibilidad inmediata. Todas las cifras de montos deberán ser informados en pesos.
Primer registro
01. Código de la institución financiera ........................................... .9(04)
02. Identificación del archivo ......................................................... X(03)
03. Fecha ......................................................................................... F(08)
04. Filler…………………………………………….........................................X(173)
Largo del registro 188 bytes
## 01. CÓDIGO DE LA INSTITUCIÓN FINANCIERA.
Corresponde al código de identificación de la institución financiera según la codificación asignada por esta Comisión.
## 02. IDENTIFICACIÓN DEL ARCHIVO.
Corresponde a la identificación del archivo. Debe ser "D53".
## 03. FECHA.
Corresponde al último día (aaaammdd) de la semana a que se refiere la información.
Estructura de los registros.
01. Fecha de la operación ............................................................... F(08)
02. Número de identificación de la operación ................................ X(30)
03. Tasa de interés mensual ............................................................ 9(03)V9(04)
04. Plazo contractual ....................................................................... 9(03)V9(02)
05. Monto de la operación .............................................................. 9(14)
06. Monto de la primera cuota........................................................ 9(14)
07. Monto de la última cuota .......................................................... 9(14)
08. Número de cuotas pactadas ...................................................... 9(03)
09. Días de gracia ............................................................................ 9(03)
10. Descuento por planilla .............................................................. 9(02)
Circular N°2.268 / 28.08.2020 por Resolución N° 3870

### ARCHIVO D54
Hoja 2 El primer registro (01), debe dar cuenta de todas las garantías constituidas a favor de la entidad, respecto de los clientes que mantienen colocaciones y/o créditos contingentes de acuerdo con el Compendio de Normas Contables, o que tienen créditos castigados para los que no se ha finalizado su proceso de recuperación por la vía de la garantía.
El segundo registro (02), debe incluir a todas las personas naturales o jurídicas cuyas operaciones se encuentren caucionadas con las garantías informadas en el primer registro. Para cada garantía y operaciones vinculadas a ella, sólo debe reportarse el deudor directo informado en los archivos contables de colocaciones enviados a esta Comisión.
Registro que contiene información de garantías constituidas
1. Tipo de registro ................................................................................. 9(02)
2 RUT del garante, dueño del bien o emisor ...................................... R(09)VX(01)
3. Nombre o razón social del garante, dueño del bien o emisor .......... X(50)
4. Nombre del instrumento ................................................................... X(50)
5. País… ................................................................................................. X(03)
6. Categoría de riesgo ............................................................................ 9(04)
7. Número interno de identificación de la garantía .............................. X(30)
8. Tipo de garantía ................................................................................ 9(04)
9. Valor inicial de la garantía ................................................................ 9(14)
10. Valor de la garantía ........................................................................... 9(14)
11. Tipo de valor de la garantía ............................................................... 9(01)
12. Fecha de tasación, valoración o clasificación ................................... F(08)
13. Monto del seguro ............................................................................... 9(14)
14. Fecha de vencimiento del seguro ...................................................... F(08)
15. Valor de gestión de la garantía .......................................................... 9(14)
16. Porcentaje de ajuste de la garantía ................................................... 9(02)V9(04)
17. Valor ajustado de la garantía ............................................................ 9(14)
Largo del registro .................... 246 bytes Definición de términos
## 1. TIPO DE REGISTRO
Corresponde al código que identifica el tipo de registro. Debe ser “01”.
## 2. RUT DEL GARANTE, DUEÑO DEL BIEN O EMISOR
Corresponde al RUT del garante o del dueño del bien corporal entregado en garantía. En caso de que exista más de un dueño de ese bien, se informará sólo uno, particularmente aquel al cual le serán garantizados sus créditos con éste.
Cuando se trate de garantías financieras, se informará el RUT del emisor de los instrumentos de deuda o de capital, el RUT de la sociedad cuando corresponda a derechos sobre ella o el RUT del obligado al pago de otras garantías reales financieras, según sea el caso.
Circular N°2.268 / 28.08.2020 por Resolución N° 3870

### ARCHIVO D54
Hoja 3
## 3. NOMBRE O RAZÓN SOCIAL DEL GARANTE, DUEÑO DEL BIEN O
EMISOR Corresponde al nombre o razón social de la persona cuyo RUT se informa en el campo 2.
## 4. NOMBRE DEL INSTRUMENTO
Corresponde al código que identifica al instrumento prendado. En el caso de instrumentos emitidos en Chile se deberá utilizar el nemotécnico asignado por la bolsa de valores reconocida por la Comisión, donde se transe el instrumento.
Cuando se trate de instrumentos emitidos en el exterior, se deberá reportar el código ISIN, y si este no existiera, el nemotécnico asignado en la bolsa del país en que esté registrado. En los casos en que el instrumento no posea ninguna de las codificaciones anteriormente señaladas o estas no correspondan, por ejemplo porque no es un instrumento financiero transado en bolsa de valores, el campo se llenará con el número interno de identificación de la garantía asignado por la entidad y que debe informarse en el campo 7 de este registro. Cuando en el registro se informen garantías que no corresponden a prendas sobre instrumentos de deuda o de capital, este campo se informará en blanco.
## 5. PAÍS
Corresponde informar el código del país, de acuerdo con la Tabla 45, correspondiente al emisor del instrumento financiero, al avalista o fiador o de la localización del bien corporal, según corresponda.
## 6. CATEGORÍA DE RIESGO
Para los garantes (avalistas o fiadores), corresponde a la más reciente clasificación de riesgo asignada a estos por una firma calificadora local o internacional, reconocida por esta Comisión, según la Tabla 92. Si no existe alguna de esas clasificaciones de riesgo, en este campo se debe incluir la clasificación efectuada por el banco según lo dispuesto en el numeral 2.1 del Capítulo B-1 del Compendio de Normas Contables, utilizando el respectivo código de la tabla 13 definido para este archivo. Se entiende que son reconocidas por esta Comisión las firmas locales inscritas en su registro y las internacionales mencionadas en el Capítulo 1-12 de la Recopilación Actualizada de Normas.
Similarmente, para las garantías que correspondan a instrumentos financieros, en este campo se debe indicar la clasificación de riesgo del respectivo instrumento, según su naturaleza y de acuerdo a las Tablas 92, 93 o 94. En el caso de la primera tabla, se debe informar la clasificación en escala global y si no la posee su clasificación en escala nacional. Si existe más de una agencia informante debe utilizarse la información más reciente, o en su defecto la clasificación más baja.
Cuando no exista clasificación para un instrumento, o en caso de que en el registro se informe otro tipo de garantías financieras o garantías sobre bienes corporales, debe informarse el campo con 9999.
## 7. NÚMERO INTERNO DE IDENTIFICACIÓN DE LA GARANTÍA
Corresponde al código que identifica en forma unívoca en la institución financiera, la garantía constituida sobre un determinado bien, el cual no deberá modificarse mientras la garantía no se haya se extinguido completamente.
Cuando una misma garantía se componga de una serie de bienes homogéneos, cuya valorización en su conjunto tiene a fin determinar el valor de una unidad económica, el mencionado código debe informase sólo una vez. En el caso de garantías financieras, cada instrumento deberá informarse en forma independiente.
Circular N°2.268 / 28.08.2020 por Resolución N° 3870

### ARCHIVO D57
Hoja 2
11. Monto garantizado ............................................................................. 9(14)
12. Mayor valor de los créditos otorgados ............................................... 9(14)
13. Filler ................................................................................................... X(01)
Largo del registro ........... 120 bytes Definición de términos
## 1. FECHA
Corresponde a la fecha (AAAAMMDD) de cada día hábil bancario del mes a la cual está referida la información del registro.
## 2. CÓDIGO DEL BANCO DEUDOR
Corresponde al código que identifica al banco deudor, según se indica en el anexo N° 3 del Capítulo 6-1 de la Recopilación Actualizada de Normas. Cuando se trate de una Entidad de Contraparte Central constituida al amparo de la Ley N° 20.345, para efectos de lo dispuesto en el N° 3 del Título I del Capítulo 12-3 de la citada Recopilación, la Comisión asignará el código correspondiente.
## 3. NÚMERO INTERNO DE IDENTIFICACIÓN DE LA OPERACIÓN
Corresponde al código interno de identificación asignado en forma única por el banco a la operación de crédito, el que debe ser utilizado en todos los archivos en que sea requerido. Los derivados celebrados bajo un acuerdo marco de compensación bilateral o cuya contraparte es una Entidad de Contraparte Central (ECC), según las disposiciones del numeral 3.3 del Capítulo 12-1 de la Recopilación Actualizada de Normas, serán identificados con un código interno común.
## 4. TIPO DE ACREEDOR DIRECTO
Identifica el tipo de acreedor directo de la operación individualizada en el campo anterior, según lo indicado en el numeral 5 del Título I del Capítulo 12-3 de la Recopilación Actualizada de Normas, de acuerdo la siguiente codificación:
Código Tipo de acreedor
01 Banco
02 Filial establecida en Chile
03 Sociedad de Apoyo al Giro
04 Filial o sucursal establecida en el exterior
## 5. FECHA DE LA OPERACIÓN
Se informará la fecha (AAAAMMDD) de otorgamiento del crédito. En caso que exista una novación de la operación que sustituya a la originalmente pactada, corresponde informar esta última fecha, al igual que en el caso de cada operación con derivados celebrados bajo un mismo acuerdo de compensación bilateral o en una ECC (según las disposiciones del Capítulo 12-1). Cuando se trate de créditos contingentes se informará la fecha en que se pactó el monto total comprometido.
## 6. FECHA DE VENCIMIENTO
Se informará la fecha (AAAAMMDD) de vencimiento o de su próxima renovación pactada. En caso que se trate de una operación sin vencimiento definido el campo deberá llenarse con “19000101”.
Circular N°2.268 / 28.08.2020 por Resolución N° 3870

SISTEMA DE INSTITUCIONES/ Generalidades/ hoja 2
f) Archivo I08: Antecedentes del gobierno corporativo del
banco.
El archivo I08 debe contener información de las personas que participan en el gobierno corporativo del banco y de los distintos comités y sus integrantes.
g) Archivo I09: Antecedentes generales de filiales y
sociedades de apoyo al giro del banco.
En el archivo I09 debe entregarse información básica de las filiales y sociedades de apoyo al giro en las que tenga participación el banco, como también el detalle de todos los accionistas o socios de ellas.
h) Archivo I10: Antecedentes de directores y gerentes de
filiales y sociedades de apoyo al giro del banco.
El archivo I10 debe contener información de los directores, gerentes y representantes legales de las filiales y sociedades de apoyo al giro en las que tenga participación el banco.
i) Archivo I11: Parque de cajeros automáticos y tiempos de
indisponibilidad o Downtime.
Este archivo debe incluir la identificación de todos los cajeros automáticos de la institución bancaria, así como de su funcionamiento, de acuerdo con las normas del Capítulo 1-7 de la Recopilación Actualizada de Normas de esta Comisión.
j) Archivo I12: Incidentes de Ciberseguridad
En este archivo se informarán todos los incidentes en materia de Ciberseguridad ocurridos en el mes de referencia, incluida la información actualizada o complementaria de incidentes reportados en periodos anteriores.
k) Archivo I13: Listado de personas relacionadas
Este archivo contiene información de las personas o entidades relacionadas con la propiedad o gestión del banco y la identificación de los grupos a los cuales se vinculan, de acuerdo a los criterios establecidos en el Capítulo 12-4 de la Recopilación Actualizada de Normas, para efectos del control de los límites de que trata el artículo 84 N° 2 de la Ley General de Bancos (LGB). Además, se identifica a cada una de las personas naturales y jurídicas relacionadas que, de conformidad con las disposiciones del artículo 84 N° 4 de la LGB y el Capítulo 12-12 de dicha Recopilación, están impedidas de obtener crédito en el banco de que se trate.
Circular N°2.268 / 28.08.2020 por Resolución N° 3870

SISTEMA DE INSTITUCIONES/ Generalidades/ hoja 3 La incorporación de nuevas personas relacionadas debe hacerse en forma automática, esto es, sin que medien otras comunicaciones a esta Comisión, puesto que la información de los cambios se obtiene por el mero procesamiento del archivo.
Los bancos que no dispongan de toda la información necesaria en relación con la conformación de algún grupo, deberán efectuar oportunamente las consultas del caso a este Organismo, a fin de enviar la nómina actualizada con todos los datos exigidos.
Por su parte, la eliminación en las nóminas de una persona relacionada sólo puede hacerse con la conformidad previa de esta Comisión, salvo que se trate de personas relacionadas por gestión a la institución. Por consiguiente, se eliminará sin la conformidad previa los siguientes casos: i) cuando se trate de un grupo de relacionados por gestión, debido a que la persona que lo origina ha dejado de pertenecer a la institución o por otra circunstancia ha perdido su calidad de relacionado; y, ii) cuando se trate de personas que conformen el grupo identificado con el código "9XXX", donde "XXX"
corresponde al código del banco. En todos los demás casos el banco debe enviar por carta los antecedentes que justifican la eliminación, a fin de obtener la conformidad que permita efectuarla.
Circular N°2.268 / 28.08.2020 por Resolución N° 3870

### ARCHIVO I01
CODIGO : I01
NOMBRE : Accionistas SISTEMA : Instituciones PERIODICIDAD : Trimestral: Marzo, Junio, Septiembre y Diciembre PLAZO : 6 días hábiles Primer registro
## 1. CODIGO DE LA IF.
Corresponde a la identificación de la institución financiera según la codificación dada por esta Comisión.
## 2. IDENTIFICACION DEL ARCHIVO.
Corresponde a la identificación del archivo. Debe ser
"I01".
## 3. PERIODO.
Corresponde al mes al que se refiere la información, la que se obtendrá según la situación del libro de accionistas al último día de cada trimestre calendario.
Estructura de los registros
## 1. Rut accionista .............................. R(09)VX(01)
## 2. Nombre del accionista ....................... X(50)
## 3. Serie ....................................... X(01)
## 4. Número de acciones suscritas pagadas ........ 9(15)
## 5. Número de acciones suscritas no pagadas ..... 9(15)
## 6. Filler ...................................... X(01)
Largo del registro 92 bytes Circular N°2.268 / 28.08.2020 por Resolución N° 3870

### ARCHIVO I03
CODIGO : I03
NOMBRE : Directores, apoderados generales y personas relacionadas con ellos.
SISTEMA : Instituciones PERIODICIDAD : Trimestral: marzo, junio, septiembre y diciembre PLAZO : 3 días hábiles Primer registro
## 1. CODIGO DE LA IF.
Corresponde a la identificación de la institución financiera según la codificación dada por esta Comisión.
## 2. IDENTIFICACION DEL ARCHIVO.
Corresponde a la identificación del archivo. Debe ser
"I03".
## 3. PERIODO.
Corresponde al mes a que se refiere la información.
Estructura de los registros
## 1. Rut ......................................... R(09)VX(01)
## 2. Nombre o razón social ....................... X(50)
## 3. Relación .................................... 9(02)
Largo del registro 62 bytes Circular N°2.268 / 28.08.2020 por Resolución N° 3870

### ARCHIVO I05
CODIGO : I05
NOMBRE : Gravámenes sobre acciones.
SISTEMA : Instituciones PERIODICIDAD : Trimestral: Marzo, Junio, Septiembre y Diciembre PLAZO : 6 días hábiles Primer registro
## 1. CODIGO DE LA IF.
Corresponde a la identificación de la institución financiera según la codificación dada por esta Comisión.
## 2. IDENTIFICACION DEL ARCHIVO.
Corresponde a la identificación del archivo. Debe ser
"I05".
## 3. PERIODO.
Corresponde al mes al que se refiere la información, la que se obtendrá según la situación del Registro de Accionistas al último día de cada trimestre calendario.
Estructura de los registros
## 1. Rut accionista .............................. R(09)VX(01)
## 2. Nombre del accionista ....................... X(50)
## 3. Serie ....................................... X(01)
## 4. Número de acciones .......................... 9(15)
## 5. Gravámenes .................................. 9(01)
## 6. Rut beneficiario ............................ R(09)VX(01)
## 7. Nombre del beneficiario ..................... X(50)
## 8. Filler ...................................... X(01)
Largo del registro 138 bytes Definición de términos
## 1. RUT ACCIONISTA.
Corresponde al RUT del accionista.
## 2. NOMBRE O RAZON SOCIAL DEL ACCIONISTA.
Corresponde al nombre o razón social del accionista.
Circular N°2.268 / 28.08.2020 por Resolución N° 3870

Archivo I06 / hoja 5
## 1. TIPO DE REGISTRO.
Corresponde al código que identifica el tipo de registro. Debe ser “2”.
## 2. IDENTIFICACION DE LA OFICINA.
Corresponde al código que identifica en forma unívoca en la institución financiera a la oficina. El código quedará alineado a la izquierda y el resto del campo con blancos.
## 3. OFICINA DE LA CUAL DEPENDE.
Incluirá el código que identifica en forma unívoca en la institución financiera a la oficina de la cual depende la informada en el registro (identificada en el campo anterior). El código quedará alineado a la izquierda y el resto del campo con blancos.
## 4. HORARIO INICIAL 1.
Corresponde al horario de apertura de la oficina.
Normalmente será “0900” salvo que la Comisión haya autorizado aperturas para algunos o todos los servicios antes de esa hora o se trate de la Isla de Pascua.
## 5. HORARIO FINAL 1.
Indica la hora de cierre para atención en horario normal. Será “1400”, a menos que se trate de la Isla de Pascua o que el banco haya ampliado la atención de sus oficinas hasta las 16 hrs. al amparo de lo dispuesto en el N° 1 del título II del Capítulo 1-8 de la Recopilación Actualizada de Normas.
6 y 7. DATOS SOBRE HORARIOS 2.
Corresponde a los horarios especiales autorizados para atender alguno o todos los servicios permitidos, de acuerdo con lo indicado en el N° 2 del título II del Capítulo 1-8 de la Recopilación Actualizada de Normas.
Las atenciones especiales a que se refiere el N° 3 de ese título y que no requieren de autorización, no se informan en este archivo.
8 a 11. DATOS SOBRE FUNCIONARIOS Y EMPLEADOS EXTERNOS.
En estos campos debe informarse la cantidad de personas, separadas por género, que trabajan en la oficina en forma permanente a sueldo u honorarios, por un mínimo de media jornada. No sólo incluye los que trabajan físicamente en el lugar que corresponde a la dirección de la oficina que se informa, sino también a los que prestan servicios en otros lugares y que dependen de la oficina que se informa en el registro (casa matriz, sucursales u otras).
Por trabajadores externos se entienden aquellas personas que trabajan para la oficina en labores propias del giro, en forma permanente y por un mínimo de media jornada, y que corresponden a personal aportado por empresas externas con las cuales se ha contratado la correspondiente prestación de servicios.
Circular N°2.268 / 28.08.2020 por Resolución N° 3870

### ARCHIVO I07
Hoja 1
CODIGO : I07
NOMBRE : PRESIDENTES, DIRECTORES, GERENTES Y EJECUTIVOS PRINCIPALES
SISTEMA : Instituciones PERIODICIDAD : Sin periodicidad. Debe remitirse cada vez que ocurra un cambio en los datos del último archivo enviado.
PLAZO : 3 días hábiles a contar de la fecha de algún cambio en un cargo que debe informarse.
En este archivo debe entregarse la lista de las personas que están ejerciendo o han ejercido los cargos que deben ser informados a esta Comisión según el artículo 68 de la Ley sobre Mercado de Valores. Por lo tanto, mediante la entrega de este archivo dentro del plazo indicado, se dará cumplimiento a lo establecido en ese artículo.
La lista que en cada oportunidad debe proporcionarse incluirá los cargos ocupados desde el 1° de enero de 2010 en adelante, fecha a partir de la cual rige la obligación impuesta por el artículo 17 de la Ley 18.045.
El archivo dará cuenta de todos los movimientos que se produzcan con motivo de nombramientos, subrogaciones o vacancias. Por lo tanto, una misma persona estará informada en el archivo tantas veces como distintos cargos o períodos en un mismo cargo haya ejercido.
Primer registro
1. Código del banco ........................................................................... 9(03)
2. Identificación del archivo .............................................................. X(03)
3. Fecha para identificar el archivo ................................................... F(08)
4. Filler ............................................................................................... X(66)
Largo del registro ......... 80 bytes
## 1. CÓDIGO DEL BANCO
Corresponde al código que identifica al banco.
## 2. IDENTIFICACIÓN DEL ARCHIVO
Corresponde a la identificación del archivo. Debe ser "I07".
## 3. FECHA PARA IDENTIFICAR EL ARCHIVO
Corresponde a la fecha (aaaammdd) de envío de este archivo.
Estructura de los registros
1. Rut ................................................................................................. R(09)VX(01)
2. Nombre .......................................................................................... X(50)
3. Código del cargo ............................................................................. 9(02)
4. Titularidad ..................................................................................... 9(01)
5. Fecha de inicio ............................................................................... F(08)
6. Fecha de término ........................................................................... F(08)
7. Causal de término o suspensión .................................................... 9(01)
Largo del registro ......... 80 bytes Circular N°2.268 / 28.08.2020 por Resolución N° 3870

CODIGO : I12
NOMBRE : Incidentes de Ciberseguridad SISTEMA : Instituciones PERIODICIDAD : Mensual PLAZO : 10 días hábiles.
Mediante este archivo los bancos informarán todos los incidentes en materia de Ciberseguridad ocurridos en el mes en curso, incluida la información actualizada o complementaria de incidentes reportados en periodos anteriores. Se entenderá por incidente de Ciberseguridad todo evento que ponga en riesgo o afecte negativamente los activos de información de la institución, así como de la infraestructura que la soporta.
Consideraremos alertas a aquellos eventos registrados pero no materializados.
El objetivo de este archivo es contar con una base consolidada de los eventos en materia de Ciberseguridad y dar seguimiento a los mismos.
### PRIMER REGISTRO
1. Código del banco .................................................................................... 9(04)
2. Identificación del archivo ....................................................................... X(03)
3. Período .................................................................................................... F(06)
## 4. Filler…………………………………………………………………………………………….X(185)
Largo del registro ............. 198 bytes
## 1. CÓDIGO DE LA IFI.
Corresponde a la identificación de la institución financiera, según la codificación dada por esta Comisión.
## 2. IDENTIFICACIÓN DEL ARCHIVO.
Corresponde a la identificación del archivo. Debe ser "I12".
## 3. PERIODO.
Corresponde al mes (AAAAMM) al que se refiere la información.
Registros siguientes Los registros siguientes contendrán información sobre incidentes y alertas, a la fecha que se refiere la información, lo que se informará en el primer campo de cada registro con los
siguientes códigos:
Código Tipo de registro
1 Incidentes
2 Alertas
Registro que contiene el detalle de los incidentes En este registro se deben informar todos los incidentes materializados.
1. Tipo de registro ...................................................................................... 9(01)
2. Número interno de identificación del incidente .................................... X(30)
3. Número de identificación del incidente otorgado por la SBIF .............. X(30)
4. Fecha del incidente ................................................................................. F(08)
5. Hora del incidente .................................................................................. 9(06)
6. Fecha del reporte .................................................................................... F(08)
Circular N°2.268 / 28.08.2020 por Resolución N° 3870

### ARCHIVO I13
Hoja 2 Definición de términos
## 1. RUT
Corresponde al RUT de toda persona o entidad relacionada al banco, que haya cumplido con dicha condición dentro del periodo (mes) de reporte.
Se deben incluir todas las personas o entidades relacionadas, independientemente que tengan créditos u otras operaciones vigentes durante el periodo informado, considerando las que ya formaban parte del listado en el periodo anterior, así como las que ingresaron y salieron del listado durante el periodo de reporte.
Lo anterior incluye a las sociedades filiales, de apoyo al giro y coligadas a que se refieren los títulos II, III y IV del Capítulo 11-6 de la Recopilación Actualizada de Normas, al igual que las empresas filiales y demás sociedades establecidas en el exterior de que tratan los títulos IV y V del Capítulo 11-7 de dicha Recopilación.
## 2. NOMBRE O RAZÓN SOCIAL
Corresponde al nombre o la razón social del deudor relacionado cuyo RUT se informó en el campo anterior.
## 3. NÚMERO DE GRUPO
Corresponde al número asignado al grupo de personas relacionadas, según la codificación entregada por esta Comisión, al que se vincula cada persona o entidad relacionada. Dado que una persona o entidad puede pertenecer a más de un grupo, su RUT y nombre se repetirá para cada uno de estos.
## 4. INCORPORACIÓN O ELIMINACIÓN DEL LISTADO
Identifica las personas o entidades que fueron incorporadas o eliminadas del listado de personas relacionadas durante el periodo de reporte, así como aquellas que ya formaban parte del mismo, considerando la siguiente
codificación:
Código Tipo de movimiento
0 Incorporado previamente*
1 Incorporado durante el periodo
2 Eliminado durante el periodo**
*
Incorporado en el listado en reportes previos.
**
Las personas o entidades eliminadas de los listados durante el periodo de reporte ya no deberán ser informadas en el archivo del mes siguiente, a menos que deba ser reincorporado por nuevas causales.
## 5. FECHA DE INCORPORACIÓN O ELIMINACIÓN DEL LISTADO
Corresponde la fecha (AAAAMMDD) del día hábil bancario cuando la persona fue incorporada o eliminada del registro.
Se entenderá como fecha de incorporación a la fecha del reporte en que el banco vinculó al relacionado a un respectivo grupo existente. Cuando se trate de un nuevo grupo, corresponderá a la fecha en la cual este Organismo informó al banco el número asignado. En caso que no se disponga de la fecha exacta de incorporación al momento de la entrada en vigencia de este archivo, el campo deberá llenarse con “19000101”.
Circular N°2.268 / 28.08.2020 por Resolución N° 3870

CODIGO : I14
NOMBRE : Transferencias electrónicas de fondos y servicios conexos:
disponibilidad e inmediatez SISTEMA : Instituciones PERIODICIDAD : Mensual PLAZO : 10 días hábiles.
Reportarán este archivo todos aquellos bancos que posean uno o más sitios Web institucionales y/o aplicaciones móviles que permitan efectuar transferencias electrónicas de fondos a las que se refiere el numeral 4.1 del Capítulo 1-7 de la Recopilación Actualizada de Normas, incluidas aquellas transferencias realizadas entre clientes de un mismo banco, y otros servicios en línea como bloqueo de cuentas y consultas de saldo. La información entregada en este archivo corresponde tanto a eventos registrados durante el mes reportado, así como a datos diarios de transferencias electrónicas ordenadas por los canales señalados en el mismo periodo.
### PRIMER REGISTRO
1. Código del banco .................................................................................... 9(04)
2. Identificación del archivo ....................................................................... X(03)
3. Período .................................................................................................... F(06)
## 4. Filler…………………………………………………………………………………………….X(53)
Largo del registro ............. 66 bytes
## 1. CÓDIGO DEL BANCO.
Corresponde a la identificación de la institución financiera, según la codificación dada por esta Comisión.
## 2. IDENTIFICACIÓN DEL ARCHIVO.
Corresponde a la identificación del archivo. Debe ser "I14".
## 3. PERIODO.
Corresponde al mes (AAAAMM) al que se refiere la información.
Registros siguientes Los registros siguientes contendrán información de distinta índole, por lo cual en el primer campo de cada registro se identificará con uno de los siguientes códigos:
Código Tipo de registro
01 Uptime de servicios por canal
02 Mantenciones programadas por canal y servicio asociado
03 Indisponibilidad por canal y servicio asociado
04 Tiempos de transferencia electrónica de fondos enviadas
Registro que indica el Uptime de servicios por canal
1. Tipo de registro ............................................................................................... 9(02)
2. Tipo de canal .................................................................................................... 9(02)
3. Identificador de canal ...................................................................................... 9(03)
4. Tipo de servicio ................................................................................................ 9(02)
5. Uptime.............................................................................................................. 9(03)V(02)
6. Filler ................................................................................................................. X(52)
Largo del registro ............. 66 bytes Circular N°2.268 / 28.08.2020 por Resolución N° 3870

### ARCHIVO E02
CODIGO : E02
NOMBRE : BIENES RECIBIDOS O ADJUDICADOS EN PAGO
SISTEMA : Estadístico PERIODICIDAD : Trimestral: referido a marzo, junio, septiembre y diciembre.
PLAZO : 7 días hábiles En este archivo debe entregarse información detallada de los bienes recibidos en pago o adjudicados en remate judicial, que mantiene la institución financiera al último día del mes al que se refiere la información.
Primer registro
## 1. Código de la Institución Financiera......... 9(03)
## 2. Identificación del archivo................ .. X(03)
## 3. Período de referencia....................... P(06)
## 4. Filler...................................... X(336)
Largo del registro 348 bytes
## 1. CODIGO DE LA IF.
Corresponde a la identificación de la institución financiera según la codificación dada por esta Comisión.
## 2. IDENTIFICACION DEL ARCHIVO.
Corresponde a la identificación del archivo. Debe ser
"E02".
## 3. PERIODO.
Corresponde al mes (aaaamm) al que se refiere la información.
Estructura de los registros
## 1. Rut del deudor .............................. R(09)VX(01)
## 2. Nombre del deudor ........................... X(50)
## 3. Número de identificación del bien ........... X(30)
## 4. Tipo de bien recibido en pago o adjudicado .. 9(02)
## 5. Descripción del bien ........................ X(60)
## 6. Número de identificación de la garantía ..... X(30)
## 7. Rut del dador en pago ....................... R(09)VX(01)
## 8. Nombre del dador en pago .................... X(50)
## 9. Monto de deuda previa a la adjudicación ..... 9(14)
## 10. Forma de adquisición ........................ 9(01)
## 11. Exposición contable ......................... 9(01)
Circular N°2.268 / 28.08.2020 por Resolución N° 3870

### ARCHIVO E03
CODIGO : E03
NOMBRE : VENTA DE BIENES RECIBIDOS O ADJUDICADOS EN
PAGO SISTEMA : Estadístico PERIODICIDAD : Trimestral: referido a marzo, junio, septiembre y diciembre.
PLAZO : 7 días hábiles En este archivo debe entregarse información de todos los bienes recibidos en pago o adjudicados en remate judicial, que hayan sido enajenados en el curso del trimestre calendario que se informa.
Primer registro
## 1. Código de la Institución Financiera......... 9(03)
## 2. Identificación del archivo................ .. X(03)
## 3. Período de referencia....................... P(06)
## 4. Filler...................................... X(190)
Largo del registro 202 bytes
## 1. CODIGO DE LA IF.
Corresponde a la identificación de la institución financiera según la codificación dada por esta Comisión.
## 2. IDENTIFICACION DEL ARCHIVO.
Corresponde a la identificación del archivo. Debe ser
"E03".
## 3. PERIODO.
Corresponde al período (aaaamm) al que se refiere la información.
Estructura de los registros
## 1. Rut del comprador del bien .................. R(09)VX(01)
## 2. Nombre del comprador del bien ............... X(50)
## 3. Número de identificación del bien ........... x(30)
## 4. Tipo de bien vendido ........................ 9(02)
## 5. Descripción del bien ........................ x(60)
## 6. Fecha de enajenación del bien ............... F(08)
## 7. Valor de enajenación del bien................9(14)
## 8. Valor libro a la fecha de enajenación del
bien.........................................9(14)
## 9. Monto financiado por la institución ......... 9(14)
Largo del registro 202 bytes Circular N°2.268 / 28.08.2020 por Resolución N° 3870

### ARCHIVO E04
Hoja 1
CODIGO : E04
NOMBRE : RECLAMOS DE USUARIOS
SISTEMA : Estadístico PERIODICIDAD : Mensual PLAZO : 7 días hábiles
“En este archivo deben incluirse todos los reclamos recibidos del público, procesados por la institución a través de la unidad especializada para la atención integral de público, instaurada en conformidad con las Circulares N°
3.054 de 4 de mayo de 2000 y N° 3.284 de 14 de septiembre de 2004.
Se entiende por reclamos todos aquellos que un usuario (persona natural o jurídica), cliente o no, haga a la institución por cualquiera de los canales de que ésta disponga para estos fines (vía presencial, vía web, vía telefónica, otros), sin importar si proceden directamente de los usuarios o son recibidas a través de esta Comisión, del Servicio Nacional del Consumidor o de cualquier otro órgano.” Primer registro
01. Código de la IF ........................................................................... 9(04)
02. Identificación del archivo .......................................................... X(03)
03. Período ...................................................................................... P(06)
04. Filler……………………………………………..........................................X(53)
Largo del registro 66 bytes
## 01. CODIGO DE LA IF:
Corresponde a la identificación de la institución financiera según los códigos dados por esta Comisión.
## 02. IDENTIFICACION DEL ARCHIVO:
Corresponde a la identificación del archivo. Debe ser "E04".
## 03. PERÍODO:
Corresponde al mes (AAAAMM) al que se refiere la información.
Estructura de los registros.
01. RUT............................................................................................ R(09) VX(01)
02. Número del reclamo .................................................................. X(30)
03. Clasificación del reclamo........................................................... X(07)
04. Vía de ingreso ............................................................................ 9(02)
05. Fecha de recepción .................................................................... F(08)
06. Fecha de cierre .......................................................................... F(08)
07 Filler .......................................................................................... X(01)
Largo del registro .................... ….66 bytes Circular N°2.268 / 28.08.2020 por Resolución N° 3870

### ARCHIVO E05
Hoja 1
CODIGO : E05
NOMBRE : CIERRE DE PRODUCTOS
SISTEMA : Estadístico PERIODICIDAD : Mensual PLAZO : 07 días hábiles En este archivo deben informarse todos los cierres de productos efectivamente cursados, así como todas las solicitudes de cierres de productos que aún no hayan sido ejecutadas, independientemente de si hubieren sido solicitadas por el titular o llevados a efecto por decisión de la institución, durante el período informado.
Primer registro
## 01. Código del banco………………………………………………………….9(04)
## 02. Identificación del archivo……………………………………………..X(03)
## 03. Período…………………………………………………………………….…P(06)
## 04. Filler……………………………………………...................................X(49)
Largo del registro 62 Bytes
## 01. CÓDIGO DEL BANCO.
Corresponde a la identificación de la institución financiera según los códigos dados por esta Comisión.
## 02. IDENTIFICACION DEL ARCHIVO.
Corresponde a la identificación del archivo. Debe ser "E05".
## 03. PERÍODO.
Corresponde al mes (AAAAMM) al que se refiere la información.
### REGISTROS SIGUIENTES
Los registros siguientes contendrán distinto tipo de información, la que se identificará en el primer campo de cada uno de ellos con los siguientes códigos:
Código Tipo de registro (contenido)
1 Cierres de productos efectivamente cursados.
2 Solicitudes de cierres de productos que aún no han sido ejecutadas.
Circular N°2.268 / 28.08.2020 por Resolución N° 3870

### ARCHIVO P15
CODIGO : P15
NOMBRE : COMPOSICION INSTITUCIONAL DE LAS
COLOCACIONES SISTEMA : Productos PERIODICIDAD : Mensual PLAZO : 9 días hábiles Primer registro
## 1. CODIGO DE LA IF.
Corresponde a la identificación de la institución financiera según la codificación dada por esta Comisión.
## 2. IDENTIFICACION DEL ARCHIVO.
Corresponde a la identificación del archivo. Debe ser
"P15".
## 3. PERIODO.
Corresponde al mes al que se refiere la información.
Estructura de los registros
## 1. Identificación del producto ................. 9(03)
## 2. Región ...................................... 9(02)
## 3. Moneda ...................................... X(03)
## 4. Composición institucional ................... 9(03)
## 5. Saldo a fin de mes .......................... 9(14)
## 6. Filler ...................................... X(01)
Largo del registro 26 bytes Definición de términos
## 1. IDENTIFICACION DEL PRODUCTO.
Corresponde al código del producto clasificado bajo
"Colocaciones Efectivas", "Colocaciones en Letras de Crédito", "Operaciones de leasing" u "Operaciones con Pacto de Retrocompra", de acuerdo a la tabla 21
"Productos".
Circular N°2.268 / 28.08.2020 por Resolución N° 3870

### ARCHIVO P16
CODIGO : P16
NOMBRE : COLOCACIONES POR ACTIVIDAD ECONOMICA
SISTEMA : Productos PERIODICIDAD : Mensual PLAZO : 9 días hábiles Primer registro
## 1. CODIGO DE LA IF.
Corresponde a la identificación de la institución financiera según la codificación dada por esta Comisión.
## 2. IDENTIFICACION DEL ARCHIVO.
Corresponde a la identificación del archivo. Debe ser
"P16".
## 3. PERIODO.
Corresponde al mes al que se refiere la información.
Estructura de los registros
## 1. Identificación del producto ................. 9(03)
## 2. Región ...................................... 9(02)
## 3. Moneda ...................................... X(03)
## 4. Actividad económica ......................... 9(02)
## 5. Saldo a fin de mes .......................... 9(14)
Largo del registro 24 bytes Definición de términos
## 1. IDENTIFICACION DEL PRODUCTO.
Corresponde al código del producto clasificado bajo
"Colocaciones Efectivas", "Colocaciones en Letras de Crédito", "Operaciones de leasing" u "Operaciones con Pacto de Retrocompra", de acuerdo a la tabla 21
"Productos".
Circular N°2.268 / 28.08.2020 por Resolución N° 3870

### ARCHIVO P30
CODIGO : P30
NOMBRE : COLOCACIONES EN LETRAS DE CREDITO Y
### MUTUOS HIPOTECARIOS ENDOSABLES.
PERIODICIDAD : Mensual PLAZO : 9 días hábiles En este archivo se incluirá información referida a colocaciones en letras de crédito y mutuos hipotecarios endosables que se mantienen al cierre del mes, incluidos los mutuos hipotecarios endosables a favor de terceros administrados por la institución.
Los valores monetarios se expresarán en pesos.
Primer registro
## 1. Código de la institución financiera ........ 9(03)
## 2. Identificación del archivo .................. X(03)
## 3. Período ..................................... P(06)
## 4. Filler ...................................... X(50)
Largo del registro 62 bytes
## 1. CODIGO DE LA IF.
Corresponde a la identificación de la institución financiera, según la codificación dada por esta Comisión.
## 2. IDENTIFICACION DEL ARCHIVO.
Corresponde a la identificación del archivo. Debe ser
"P30".
## 3. PERIODO.
Corresponde al mes al que se refiere la información.
Estructura de los registros
## 1. Código del producto ......................... 9(02)
## 2. Plazo original .............................. 9(02)
## 3. Plazo residual .............................. 9(02)
## 4. Número operaciones sin morosidad de 90
días o más .................................. 9(07)
## 5. Monto de operaciones sin morosidad de 90
días o más .................................. 9(14) Circular N°2.268 / 28.08.2020 por Resolución N° 3870

### ARCHIVO P33
CODIGO : P33
NOMBRE : AHORRO PREVISIONAL VOLUNTARIO.
PERIODICIDAD : Mensual.
PLAZO : 9 días hábiles Primer registro
## 1. Código de la institución financiera ........ 9(03)
## 2. Identificación del archivo .................. X(03)
## 3. Período ..................................... P(06)
## 4. Filler ...................................... X(170)
Largo del registro 182 bytes
## 1. CODIGO DE LA IF.
Corresponde a la identificación de la institución financiera, según la codificación dada por esta Comisión.
## 2. IDENTIFICACION DEL ARCHIVO.
Corresponde a la identificación del archivo. Debe ser
"P33".
## 3. PERIODO.
Corresponde al año-mes al que se refiere la información.
Estructura de los registros
## 01. Modalidad de ahorro previsional ............. 9(01)
## 02. Tipo de plan de ahorro previsional .......... 9(01)
## 03. Número de contratos vigentes ............... 9(08)
## 04. Saldo total acumulado ...................... 9(14)
## 05. Número de depósitos del mes ................ 9(08)
## 06. Monto de depósitos del mes ................. 9(14)
## 07. Número de traspasos provenientes de otras
entidades .................................. 9(08)
## 08. Monto de traspasos provenientes de otras
entidades .................................. 9(14)
## 09. Número de traspasos destinados a otras
entidades .................................. 9(08)
## 10. Monto de traspasos destinados a otras
entidades .................................. 9(14)
## 11. Número de retiros del mes .................. 9(08)
## 12. Monto de retiros del mes ................... 9(14)
## 13. Intereses abonados durante el mes .......... 9(14)
Circular N°2.268 / 28.08.2020 por Resolución N° 3870

### ARCHIVO P34
CODIGO : P34
NOMBRE : TRASPASOS DE AHORRO PREVISIONAL VOLUNTARIO.
PERIODICIDAD : Mensual.
PLAZO : 9 días hábiles Primer registro
## 1. Código de la institución financiera ........ 9(03)
## 2. Identificación del archivo .................. X(03)
## 3. Período ..................................... P(06)
## 4. Filler ...................................... X(12)
Largo del registro 24 bytes
## 1. CODIGO DE LA IF.
Corresponde a la identificación de la institución financiera, según la codificación dada por esta Comisión.
## 2. IDENTIFICACION DEL ARCHIVO.
Corresponde a la identificación del archivo. Debe ser
"P34".
## 3. PERIODO.
Corresponde al año-mes al que se refiere la información.
Estructura de los registros
## 01. Modalidad de ahorro previsional ............. 9(01)
## 02. Tipo de traspaso ............................ 9(01)
03 Tipo de entidad asociada al traspaso ........ 9(01)
## 04. Monto de los traspasos ...................... 9(14)
## 05. Filler ...................................... X(07)
Largo del registro 24 bytes Definición de términos
## 01. MODALIDAD DE AHORRO PREVISIONAL.
Indicará la modalidad de ahorro previsional según la clasificación de códigos siguiente:
1 Ahorros con depósitos convenidos.
2 Ahorros con depósitos voluntarios.
Circular N°2.268 / 28.08.2020 por Resolución N° 3870

### ARCHIVO P35
CODIGO : P35
NOMBRE : TIPO DE DEPOSITANTE DE AHORRO PREVISIONAL
VOLUNTARIO.
PERIODICIDAD : Mensual.
PLAZO : 9 días hábiles Primer registro
## 1. Código de la institución financiera ........ 9(03)
## 2. Identificación del archivo .................. X(03)
## 3. Período ..................................... P(06)
## 4. Filler ...................................... X(34)
Largo del registro 46 bytes
## 1. CODIGO DE LA IF.
Corresponde a la identificación de la institución financiera, según la codificación dada por esta Comisión.
## 2. IDENTIFICACION DEL ARCHIVO.
Corresponde a la identificación del archivo. Debe ser
"P35".
## 3. PERIODO.
Corresponde al año-mes al que se refiere la información.
Estructura de los registros
## 01. Modalidad de ahorro previsional ............. 9(01)
## 02. Tipo de plan de ahorro previsional .......... 9(01)
## 03. Régimen tributario .......................... 9(01)
## 04. Tramo de edad ............................... 9(03)
## 05. Tramo de saldo .............................. 9(03)
06 Tipo de género .............................. 9(01)
## 07. Número de cuentas ........................... 9(08)
## 08. Bonificación fiscal ......................... 9(14)
## 09. Total acumulado ............................. 9(14)
Largo del registro 46 bytes Definición de términos
## 01. MODALIDAD DE AHORRO PREVISIONAL
Indicará la modalidad de ahorro previsional según la clasificación de códigos siguiente:
1 Ahorros con depósitos convenidos.
2 Ahorros con depósitos voluntarios.
Circular N°2.268 / 28.08.2020 por Resolución N° 3870

### ARCHIVO P36
CODIGO : P36
NOMBRE : ESTADO DE EMISIONES Y COLOCACIONES DE
BONOS SISTEMA : Productos PERIODICIDAD : Mensual PLAZO : 09 días hábiles En este archivo, se deberán reportar todas las emisiones de bonos vigentes a la fecha de referencia de la información. Se entenderá por tales a todas aquellas series inscritas en el registro mantenido por esta Comisión, hayan o no sido colocadas, cuyo plazo de colocación no haya vencido o no se encuentren totalmente amortizadas.
Primer registro
## 01. Código de la IF ............................. 9(03)
## 02. Identificación del archivo .................. X(03)
## 03. Período ..................................... P(06)
## 04. Filler...................................... X(216)
Largo del registro 228 bytes
## 01. CODIGO DE LA IF:
Corresponde a la identificación de la institución financiera según los códigos dados por esta Comisión.
## 02. IDENTIFICACION DEL ARCHIVO:
Corresponde a la identificación del archivo. Debe ser
"P36".
## 03. PERIODO:
Corresponde al mes al que se refiere la información, según lo solicitado.
Estructura de los registros
## 01. Serie ....................................... X(15)
## 02. Tipo de Bono ................................ 9(02)
## 03. Clasificadora de Riesgo 1 ................... 9(02)
## 04. Clasificación de Riesgo 1 ................... X(04)
## 05. Clasificadora de Riesgo 2 ................... 9(02)
## 06. Clasificación de Riesgo 2 ................... X(04)
## 07. Amortización ................................ 9(02)
## 08. Número de inscripción ....................... X(15)
## 09. Fecha de inscripción ........................ F(08)
Circular N°2.268 / 28.08.2020 por Resolución N° 3870

Archivo P36 / hoja 3
## 05. CLASIFICADORA DE RIESGO 2.
Identifica a la otra firma evaluadora que ha clasificado los bonos, según:
### 10 FITCH CHILE CLASIFICADORA DE RIESGOS LTDA.
### 20 FELLER-RATE CLASIFICADORA DE RIESGO LTDA.
### 30 CLASIFICADORA DE RIESGO HUMPHREYS LTDA.
### 40 INTERNATIONAL CREDIT RATING COMPAÑIA CLASIFICADORA DE RIESGO LTDA.
## 06. CLASIFICACION DE RIESGO 2
Corresponde a la clasificación actualizada asignada a los bonos por la firma identificada en el campo 05.
Estas clasificaciones deben ser informadas en este campo ajustadas a la izquierda y el resto de sus dígitos en blancos cuando corresponda.
## 07. AMORTIZACION.
Indica las condiciones establecidas para la amortización del bono, según los siguientes códigos:
01 Amortización periódica sin derecho a prepago.
02 Amortización no periódica sin derecho a prepago.
03 Amortización periódica con derecho a prepago.
04 Amortización no periódica con derecho a prepago.
Por amortización periódica se entiende aquella en que se paga parte del capital en cada cupón. No periódica será aquella en que existen cupones en que solo se pagan intereses.
El derecho a prepago se refiere a la facultad del emisor de efectuar alguna amortización extraordinaria, reembolsando anticipadamente todo o parte del capital
(aplicable sólo a bonos ordinarios).
## 08. NUMERO DE INSCRIPCION.
Corresponde al número de inscripción de la emisión en el Registro de Valores de la Comisión.
## 09. FECHA DE INSCRIPCION.
Se debe expresar la fecha en que se efectuó el registro de la emisión.
## 10. FECHA LIMITE PARA LA COLOCACION.
Corresponde a la fecha de vencimiento del plazo para la colocación.
Circular N°2.268 / 28.08.2020 por Resolución N° 3870

### ARCHIVO P37
CODIGO : P37
NOMBRE : TARJETAS DE DEBITO Y DE CAJEROS AUTOMATICOS
SISTEMA : Productos PERIODICIDAD : Mensual PLAZO : 9 días hábiles
### PRIMER REGISTRO
## 1. Código de la IF ............................. 9(03)
## 2. Identificación del archivo .................. X(03)
## 3. Período ..................................... P(06)
## 4. Filler...................................... X(40)
Largo del registro 52 bytes
## 1. CODIGO DE LA IF:
Corresponde a la identificación de la institución financiera según la codificación dada por esta Comisión.
## 2. IDENTIFICACION DEL ARCHIVO:
Corresponde a la identificación del archivo. Debe ser
"P37".
## 3. PERIODO:
Corresponde al mes (aaaamm) al que se refiere la información.
### REGISTROS SIGUIENTES
Los registros siguientes contendrán información de distinta índole, por lo cual en el primer campo de cada registro se identificará de qué información se trata, según los
siguientes códigos:
Código Tipo de registro (contenido)
01 Número de cuentas y tarjetas vigentes con operaciones en el mes, según tipo de cuenta y comuna.
02 Número y monto de las operaciones efectuadas en el
mes en el país y en el exterior.
Circular N°2.268 / 28.08.2020 por Resolución N° 3870

### ARCHIVO P38
Hoja 1
CODIGO : P38
NOMBRE : TARJETAS DE CRÉDITO
SISTEMA : Productos PERIODICIDAD : Mensual PLAZO : 9 días hábiles Primer registro
1. Código del banco ................................................................................ 9(03)
2. Identificación del archivo ................................................................... X(03)
3. Período ................................................................................................ P(06)
4. Filler .................................................................................................... X(28)
Largo del registro .......... 40 bytes
## 1. CÓDIGO DEL BANCO
Corresponde al código que identifica al banco.
## 2. IDENTIFICACIÓN DEL ARCHIVO
Corresponde a la identificación del archivo. Debe ser "P38".
## 3. PERÍODO
Corresponde a mes (AAAAMM) a que se refiere la información.
Registros siguientes Los registros siguientes contendrán información de distinta índole, por lo cual en el primer campo de cada registro se identificará de qué información se trata, según los siguientes códigos:
Código Tipo de registro (contenido)
01 Número de contratos y tarjetas según su vigencia, uso y marcas.
02 Cobertura de las tarjetas como medio de pago en el territorio nacional.
03 Número y monto de las transacciones con tarjetas de crédito en el
mes.
04 Tramo y monto de las líneas de crédito.
05 Tipos y plazos de las obligaciones por el uso de tarjetas de crédito.
06 Obligaciones agrupadas por tramo de morosidad.
La información acerca de las obligaciones debe incluirse de acuerdo a las cláusulas de los títulos, contratos vigentes o convenios de pago posteriores.
Para dicho efecto se deberán aplicar las instrucciones sobre montos adeudados y criterios de exclusión e inclusión de obligaciones, establecidos en el Capítulo
18-5 de la Recopilación Actualizada de Normas y recogidos en el archivo D10.
Circular N°2.268 / 28.08.2020 por Resolución N° 3870

### ARCHIVO P39
CODIGO : P39
NOMBRE : TARJETAS DE CREDITO Y DEBITO. UTILIZACION
### COMO MEDIO DE PAGO.
SISTEMA : Productos PERIODICIDAD : Mensual PLAZO : 9 días hábiles
### PRIMER REGISTRO
## 1. Código de la IF ............................. 9(03)
## 2. Identificación del archivo .................. X(03)
## 3. Período ..................................... P(06)
## 4. Filler...................................... X(40)
Largo del registro 52 bytes
## 1. CODIGO DE LA IF:
Corresponde a la identificación de la institución financiera según la codificación dada por esta Comisión.
## 2. IDENTIFICACION DEL ARCHIVO:
Corresponde a la identificación del archivo. Debe ser
"P39".
## 3. PERIODO:
Corresponde al mes (aaaamm) al que se refiere la información.
### REGISTROS SIGUIENTES
Los registros siguientes contendrán información de distinta índole, por lo cual en el primer campo de cada registro se identificará de qué información se trata, según los
siguientes códigos:
Código Tipo de registro (contenido)
01 Operaciones realizadas en el mes según los tipos de
tarjeta, lugar de uso, rubro de los establecimientos y tipo de operaciones.
02 Número de establecimientos afiliados y terminales
utilizados, en las operaciones realizadas en el mes.
Circular N°2.268 / 28.08.2020 por Resolución N° 3870

### ARCHIVO P40
Hoja 2 Registros para informar instrumentos de deuda de terceros
1. Tipo de registro .................................................................................. 9(02)
2. Código tenedor ................................................................................... 9(03)
3. Fecha .................................................................................................. F(08)
4. Fecha de negociación .......................................................................... F(08)
5. Tipo de cartera .................................................................................... 9(01)
6. Emisor ................................................................................................. R(09)VX(01)
7. País del emisor .................................................................................... 9(03)
8. Familia de instrumentos .................................................................... 9(02)
9. Nemotécnicos ..................................................................................... X(20)
10. Tipo de rendimiento ........................................................................... 9(01)
11. Periodicidad del cupón ....................................................................... 9(01)
12 Fecha de último corte cupón .............................................................. F(08)
13. Fecha de próximo corte cupón ........................................................... F(08)
14. Fecha de vencimiento instrumento .................................................... F(08)
15. Derivados incrustados u opcionalidad ............................................... 9(02)
16. Nominal inicial ................................................................................... 9(14)V9(02)
17. Nominal actual ................................................................................... 9(14)V9(02
18. Moneda del nominal ........................................................................... 9(03)
19. Moneda de reajuste ............................................................................ 9(03)
20. Tipo de tasa de emisión ...................................................................... 9(07)
21. Tasa de emisión .................................................................................. 9(02)V9(02)
22. Tera ..................................................................................................... 9(02)V9(04)
23. Valor par ............................................................................................. 9(14)V9(02)
24. Tipo de tasa de compra ....................................................................... 9(07)
25. Tasa de compra ................................................................................... s9(02)V9(02)
26. Costo de adquisición ........................................................................... 9(14)
27. Costo amortizado ................................................................................ 9(14)
28. Valor razonable ................................................................................... 9(14)
29. Tipo de tasa de valoración .................................................................. 9(07)
30. Tasa de valoración .............................................................................. s9(02)V9(02)
31. Tipo de valoración .............................................................................. 9(01)
32 Precio del instrumento ....................................................................... 9(06)V9(02)
33. Duración modificada .......................................................................... 9(02)V9(02)
34. Convexidad ......................................................................................... 9(04)V9(04)
35. Valor de deterioro ............................................................................... 9(14)
36. Condición del instrumento ................................................................. 9(01)
37. Fecha de inicio condición ................................................................... F(08)
38. Fecha final condición .......................................................................... F(08)
Largo del registro 274bytes
## 1. TIPO DE REGISTRO
Corresponde al código que identifica el tipo de registro. Debe ser “01”.
## 2. CÓDIGO TENEDOR
Corresponde al código del tenedor (banco, filial bancaria o sucursal en el exterior) del instrumento de deuda, según la codificación dada por esta Comisión.
## 3. FECHA
Corresponde a la fecha (día de la semana) a la que se refiere la información del registro.
Circular N°2.268 / 28.08.2020 por Resolución N° 3870

### ARCHIVO P40
Hoja 6
## 34. CONVEXIDAD
Se indicará la convexidad, entendida como el cambio en la duración modificada sobre un nominal de 100, con cuatro decimales, expresada en años
(de 365 o 360 días, de acuerdo a la convención de la tasa de valorización del instrumento).
## 35. VALOR DE DETERIORO
Corresponde al monto en pesos identificado como deterioro crediticio para los instrumentos incluidos en el registro. El campo se llenará con ceros al no existir o no ser aplicable el valor del deterioro.
## 36. CONDICIÓN DEL INSTRUMENTO
Indica la condición en que se encuentran los instrumentos, según los
siguientes códigos:
1 Sin restricciones para su venta o cesión
2 Entregado en pacto
3 Entregado en garantía (excepto pacto)
9 Otras condiciones que impiden su venta o cesión.
## 37. FECHA INICIO CONDICIÓN
Se indicará la fecha inicial de la condición indicada en el campo 36. Para aquellos instrumentos sin restricciones (código “01”), el campo se llenará con ceros.
## 38. FECHA FINAL CONDICIÓN
Se indicará la fecha final de la condición indicada en el campo 36. Para los instrumentos sin restricciones (código “01”), el campo se llenará con ceros.
Si la fecha final de la condición es indefinida, el campo se llenará con nueves.
Registros para informar cuotas de fondos mutuos
1. Tipo de registro .................................................................................. 9(02)
2. Código tenedor ................................................................................... 9(03)
3. Fecha .................................................................................................. F(08)
4. Fecha de compra ................................................................................. F(08)
5. Administradora del fondo .................................................................. R(09)VX(01)
6. País del fondo ..................................................................................... 9(03)
7. Tipo de fondo ...................................................................................... 9(01)
8. Número de cuotas mantenidas ........................................................... 9(14)
9. Moneda ............................................................................................... 9(03)
10. Valor inicial cuota ............................................................................... 9(14)
11. Valor cuota .......................................................................................... 9(14)
12. Valor razonable ................................................................................... 9(14)
13. Filler .................................................................................................... X(180)
Largo del registro ........ 274 bytes
## 1. TIPO DE REGISTRO
Corresponde al código que identifica el tipo de registro. Debe ser “02”.
### 2 CÓDIGO TENEDOR
Corresponde al código del tenedor (banco, filial bancaria o sucursal en el exterior) de las cuotas de fondos mutuos, según la codificación dada por esta Comisión.
Circular N°2.268 / 28.08.2020 por Resolución N° 3870

### ARCHIVO P40
Hoja 8 Registros para informar instrumentos de capital
1. Tipo de registro .................................................................................. 9(02)
2. Código tenedor ................................................................................... 9(03)
3. Fecha .................................................................................................. F(08)
4. Fecha de compra ................................................................................. F(08)
5. Nemotécnico ....................................................................................... X(14)
6. Tipo de cartera .................................................................................... 9(01)
7. Número de instrumentos mantenidos ............................................... 9(14)
8. Moneda ............................................................................................... 9(03)
9. Precio de compra ................................................................................ 9(14)
10. Valor razonable ................................................................................... 9(14)
11. Condición del instrumento ................................................................. 9(01)
12. Fecha inicio condición ........................................................................ F(08)
13. Fecha fin condición ............................................................................ F(08)
14. Filler .................................................................................................... X(176)
Largo del registro ........ 274 bytes
## 1. TIPO DE REGISTRO
Corresponde al código que identifica el tipo de registro. Debe ser “03.
## 2. CÓDIGO TENEDOR
Corresponde al código del tenedor (filial bancaria o sucursal en el exterior) del instrumento de capital, según la codificación dada por esta Comisión.
## 3. FECHA
Corresponde a la fecha a la que se refiere la información.
## 4. FECHA DE COMPRA
Corresponde a la fecha de adquisición del instrumento de capital.
## 5. NEMOTÉCNICO
Corresponde al código que identifica al instrumento en la bolsa en la que se adquirió.
### 6 TIPO DE CARTERA
Indica la clasificación de los instrumentos, debiéndose utilizar los siguientes códigos:
1 Instrumentos para negociación
2 Instrumentos disponibles para la venta
## 7. NÚMERO DE INSTRUMENTOS MANTENIDOS
Corresponde a la cantidad de instrumentos de capital informados en el registro.
## 8. MONEDA
Se deberá indicar la moneda en la que se transa el instrumento, utilizando el código de la Tabla 1.
Circular N°2.268 / 28.08.2020 por Resolución N° 3870

### ARCHIVO P41
Hoja 1
CODIGO : P41
NOMBRE : Servicios electrónicos prestados a través de Internet.
SISTEMA : Productos PERIODICIDAD : Mensual PLAZO : 10 días hábiles Reportarán este archivo todas aquellas instituciones que posean uno o más sitios Web institucionales, aún cuando no realicen la totalidad de los tipos de las operaciones aquí consultadas.
### PRIMER REGISTRO
1. Código de la institución ........................................................................ 9(03)
2. Identificación del archivo ...................................................................... X(03)
3. Período ................................................................................................... P(06)
4. Filler ....................................................................................................... X(36)
Largo del registro 48 bytes
## 1. CÓDIGO DE LA INSTITUCIÓN FINANCIERA
Corresponde a la identificación de la institución financiera, según la codificación asignada por esta Comisión.
## 2. IDENTIFICACIÓN DEL ARCHIVO
Corresponde a la identificación del archivo. Deber ser “P41”.
## 3. PERÍODO
Corresponde al año y mes (aaaamm) al que se refiere la información.
### REGISTROS SIGUIENTES
Los registros siguientes contendrán información de distinta índole, por lo cual en el primer campo de cada registro se identificará de qué información se trata, según los siguientes códigos:
Código Tipo de registro (contenido)
01 Cobertura e intensidad de uso del sitio Web
02 Tipos de operaciones realizadas en el sitio Web
Circular N°2.268 / 28.08.2020 por Resolución N° 3870

### ARCHIVO P42
Hoja 1
CODIGO : P42
NOMBRE : INFORMACIÓN DEL REGISTRO ESPECIAL DE
### MUTUOS HIPOTECARIOS VINCULADOS A LA COLOCACIÓN DE BONOS HIPOTECARIOS.
SISTEMA : Productos PERIODICIDAD : Mensual PLAZO : 09 días hábiles En este archivo se deberá informar el estado de los mutuos y sus respectivas garantías hipotecarias, vinculados a la colocación de bonos hipotecarios y que forman parte del Registro Especial de que trata el inciso segundo del artículo
69 N° 2 de la Ley General de Bancos. También se deberá entregar información
relativa a los valores mobiliarios susceptibles de ser incorporados en el citado registro.
Primer registro
01. Código de la IF .......................................................................... 9(03)
02. Identificación del archivo ......................................................... X(03)
03. Período ...................................................................................... P(06)
04. Filler……………………………………………....................................... X(138)
Largo del registro 150 bytes
## 01. CODIGO DE LA IF:
Corresponde a la identificación de la institución financiera según los códigos dados por esta Comisión.
## 02. IDENTIFICACION DEL ARCHIVO:
Corresponde a la identificación del archivo. Debe ser "P42".
## 03. PERIODO:
Corresponde al mes al que se refiere la información, según lo solicitado.
### REGISTROS SIGUIENTES
Los registros siguientes contendrán información de distinta índole, por lo cual en el primer campo de cada registro se identificará de qué información se trata, según los siguientes códigos:
Código Tipo de registro (contenido)
01 Registro Especial de Mutuos Hipotecarios
02 Valores mobiliarios de renta fija incorporados al Registro
Especial Circular N°2.268 / 28.08.2020 por Resolución N° 3870

### ARCHIVO P42
Hoja 2 Registros Especial de Mutuos Hipotecarios.
01. Tipo de registro ......................................................................... 9(02)
02. Número de inscripción del bono hipotecario ........................... X(15)
03. Número interno de identificación del mutuo ........................... X(30)
04. Tipo de mutuo hipotecario ....................................................... 9(02)
05. Fecha de anotación en el Registro ............................................ F(08)
06. Plazo original del mutuo ........................................................... 9(03)
07. Plazo residual del mutuo .......................................................... 9(03)
08. Moneda y reajustabilidad de la operación ................................ 9(03)
09. Monto original del mutuo registrado ....................................... 9(14)
10. Saldo insoluto del mutuo registrado ........................................ 9(14)
11. Tipo de tasa de interés pactada ................................................. 9(03)
12. Tasa de interés de la operación ................................................. 9(03)V9(04)
13. Ratio dividendo-ingresos .......................................................... 9(03)V9(02)
14. Código de la garantía constituida ............................................. X(30)
15. Fecha de eliminación del Registro ............................................ F(08)
16. Causal de eliminación del Registro........................................... 9(02)
17. Filler .......................................................................................... X(01)
Largo del registro .................... 150 bytes Definición de términos
## 01. TIPO DE REGISTRO.
Corresponde al código que identifica el tipo de registro. Debe ser “01”.
## 02. NUMERO DE INSCRIPCION DEL BONO HIPOTECARIO.
Número de inscripción de la emisión en el Registro de Valores de la Comisión, del bono al cual está vinculado cada mutuo.
## 03. NÚMERO INTERNO DE IDENTIFICACIÓN DEL MUTUO.
Corresponde al código interno de identificación asignado en forma única por el banco a la operación que origina el mutuo hipotecario.
## 04. TIPO DE MUTUO HIPOTECARIO.
Indicará el tipo de operación de acuerdo con los siguientes códigos:
01 Mutuos vinculados al bono hipotecario desde su origen.
02 Otros mutuos vinculados al bono hipotecario.
## 05. FECHA DE ANOTACIÓN EN EL REGISTRO.
Corresponde a la fecha en que la operación fue inscrita en el Registro Especial, de acuerdo a las disposiciones del artículo 69 N° 2 de la Ley General de Bancos y a las instrucciones impartidas en el N° 5 Capítulo 9-2 de la Recopilación Actualizada de Normas.
## 06. PLAZO ORIGINAL DEL MUTUO.
Corresponde al número de meses comprendido entre la fecha de otorgamiento del crédito y la fecha de vencimiento de la última cuota. Este campo se informará redondeando al número entero que corresponda al considerar como un mes más las fracciones iguales o superiores a 15 días.
Circular N°2.268 / 28.08.2020 por Resolución N° 3870

### ARCHIVO P42
Hoja 4
## 15. FECHA DE ELIMINACIÓN DEL REGISTRO.
En el caso de aquellos mutuos dados de baja durante el periodo de reporte, corresponde informar la fecha exacta en que el mutuo fue eliminado del Registro Especial. En caso que no corresponda el campo se llenará con ceros.
## 16. CAUSAL DE ELIMINACIÓN DEL REGISTRO.
En el caso de aquellos mutuos dados de baja durante el periodo de reporte, se indicará el motivo por el cual el mutuo fue eliminado del Registro Especial, de acuerdo con los siguientes códigos:
01 Pago de último dividendo
02 Amortización anticipada o prepago
03 Dividendos impagos o deterioro del valor de la garantía
En caso que no corresponda el campo se llenará con ceros.
Valores mobiliarios de renta fija incorporados al Registro Especial.
01. Tipo de registro ......................................................................... 9(02)
02. Número de inscripción del bono hipotecario ........................... X(15)
03. Número interno de identificación de la operación ................... X(30)
04. Tipo de valor mobiliario............................................................ 9(02)
05. Fecha de anotación del valor mobiliario en el Registro ........... F(08)
06. Valor razonable del instrumento .............................................. 9(14)
07. Fecha de eliminación del Registro ............................................ F(08)
08. Filler .......................................................................................... X(71)
Largo del registro .................... 150 bytes Definición de términos
## 01. TIPO DE REGISTRO.
Corresponde al código que identifica el tipo de registro. Debe ser “02”.
## 02. NUMERO DE INSCRIPCION DEL BONO HIPOTECARIO.
Número de inscripción de la emisión en el Registro de Valores de la Comisión, del bono al cual está vinculado cada mutuo.
## 03. NÚMERO INTERNO DE IDENTIFICACIÓN DE LA OPERACIÓN.
Corresponde al código interno de identificación asignado en forma única por el banco al valor mobiliario de renta fija, inscrito en el Registro Especial.
## 04. TIPO DE VALOR MOBILIARIO.
Indicará el tipo de valor mobiliario de renta fija vinculado al bono, de acuerdo con los siguientes códigos:
01 Instrumentos de renta fija emitidos en serie por el Banco Central
de Chile.
02 Instrumentos de renta fija emitidos en serie por la Tesorería
General de la República.
Circular N°2.268 / 28.08.2020 por Resolución N° 3870

### ARCHIVO P42
Hoja 5
03 Instrumentos de renta fija inscritos en el Registro de Valores de
la Comisión.
04 Depósitos a Plazo de bancos constituidos en Chile.
05 Letras de crédito emitidas para la adquisición de viviendas por
otras entidades bancarias.
06 Bonos hipotecarios emitidos por otras entidades bancarias.
07 Instrumentos de renta fija inscritos en el Registro de Valores de
la Comisión.
## 05. FECHA DE ANOTACIÓN DEL VALOR MOBILIARIO EN EL REGISTRO.
Corresponde a la fecha en que el instrumento fue inscrito en el Registro Especial.
## 06. VALOR RAZONABLE DEL INSTRUMENTO
Indica el valor razonable (monto en pesos) de los instrumentos incluidos en el Registro Especial, determinado conforme a lo indicado en el Capítulo
7-12 de la Recopilación Actualizada de Normas.
## 07. FECHA DE ELIMINACIÓN DEL REGISTRO.
En el caso de aquellos valores mobiliarios excluidos del Registro Especial durante el periodo de reporte, corresponde informar la fecha exacta de ocurrida tal eliminación. En caso que no corresponda el campo se llenará con ceros.
Carátula de cuadratura El archivo P42 debe entregarse con una carátula de cuadratura cuyo modelo se especifica a continuación.
MODELO Institución: __________________________________ Código : ______ Información correspondiente al mes de: ____________ Archivo : P42

| Número de Registros Informados |  |
| --- | --- |
| Número de Registros con código 01 en el primer campo |  |
| Número de Registros con código 02 en el primer campo |  |

Circular N°2.268 / 28.08.2020 por Resolución N° 3870