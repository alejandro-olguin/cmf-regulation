<!-- source: cir_2266_2020_refundido.pdf -->
<!-- language: es -->
<!-- note: Las fórmulas matemáticas extraídas de PDFs pueden ser incompletas.
     Los bloques marcados con ⚠️ deben verificarse contra el PDF original. -->

### RECOPILACION ACTUALIZADA DE NORMAS
Capítulo 20-6 Hoja 1
2.2. Nómina de documentos protestados por el propio banco
de acuerdo con la Ley 18.092.
De conformidad con lo dispuesto en la letra b) del N° 6 del D.S. N° 950 antes mencionado, modificado por el D.S. N° 625, de 1982, los bancos que establezcan el sistema de protesto de letras de cambio de que trata el artículo 71 de la Ley 18.092, quedan obligadas a enviar semanalmente al Boletín de Informaciones Comerciales una nómina de las letras de cambio y pagarés que hubieran protestado a su vencimiento.
## 3. Envío de nóminas de deudores morosos.
De acuerdo con lo dispuesto por el D.S. N° 950, de 1928, del Ministerio de Hacienda, modificado por el D.S. N° 883, publicado en el Diario Oficial del 26 de octubre de 1992, los bancos pueden enviar al Boletín de Informaciones Comerciales de la Cámara de Comercio de Chile, una nómina de los deudores que hayan incurrido en mora en el servicio de sus préstamos o créditos a favor del respectivo banco, excluidas aquellas deudas morosas que obligatoriamente deben informarse según lo señalado en el N° 2 precedente, como asimismo aquellas correspondientes a documentos enviados a notaría para su protesto.
Los bancos que decidan hacer uso de dicha facultad enviarán las referidas nóminas dentro de los quince primeros días hábiles de cada mes con los
siguientes datos:
a) Nombre completo y RUT del deudor.
b) Importe de la deuda directa que no fue pagada por el deudor en el mes
precedente.
En ningún caso podrán incluirse como morosas las deudas cuyos créditos no consten de un título ejecutivo, por las mismas razones dadas en el Capítulo 18-5 de esta Recopilación. Tampoco podrán remitirse aquellas deudas para fines educacionales, que de conformidad a lo dispuesto por la Ley N°21.214, que modificó el artículo 17 de la Ley N°19.628, sobre protección de la vida privada, no pueden ser comunicadas.
Los bancos que opten por enviar estas nóminas quedan obligadas a: a) mantener siempre el envío mensual de la nómina; y, b) incluir en cada nómina todos los deudores que cumplan las condiciones anteriormente señaladas, sin discriminar entre ellos. Con todo, se excluirán de las nóminas los deudores que hayan solucionado su morosidad antes del envío de la respectiva nómina.
## 4. Forma de enviar la información.
Las nóminas que envíe cada oficina bancaria deben numerarse correlativamente y entregarse con la información ordenada de la forma que requiera el Boletín para su mejor procesamiento.
Los bancos deberán enviar las nóminas antes mencionadas en medios magnéticos, sin perjuicio de adjuntar, como instrumento de prueba, el respectivo listado impreso con dicha información.
En todo caso, los bancos deberán mantener en su poder una copia de las nóminas enviadas, sea en forma impresa o en medios magnéticos.
Circular N° 2.266 / 25.08.2020 por Resolución N° 3759

### ARCHIVO D10
CODIGO : D10
NOMBRE : INFORMACION DE DEUDORES ARTICULO 14 LGB
SISTEMA : Deudores PERIODICIDAD : Mensual PLAZO : 7 días hábiles En este archivo deben incluirse todos los créditos efectivos y contingentes que son objeto de refundición por esta Comisión, según lo indicado en el Capítulo 18-5 de la Recopilación Actualizada de Normas.
Primer registro
## 1. Código de la institución financiera .... 9(03)
## 2. Identificación del archivo ............. X(03)
## 3. Período ................................ 9(06)
4 Filler ................................. X(66)
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
_____ Largo del registro 78 bytes Circular N° 2.266 / 25.08.2020 por Resolución N° 3759

Archivo D10 / hoja 2 Definición de términos
## 1. RUT DEL DEUDOR.
Corresponde al RUT del deudor.
## 2. NOMBRE O RAZON SOCIAL DEL DEUDOR.
Corresponde al nombre o razón social del deudor.
## 3. TIPO DE DEUDOR
Corresponde al tipo de deudor en relación con el crédito que se informa en el registro, según se trate de:
Código Calidad del deudor
1 Deudor directo
2 Deudor indirecto
La calidad de directo o indirecto corresponderá a lo indicado en el Capítulo 12-3 de la Recopilación Actualizada de Normas, sin perjuicio de que en este archivo deben informarse sólo las obligaciones a que se refiere el Capítulo 18-5 de esa Recopilación, con las excepciones que se indican en este mismo Capítulo. Se incluirán las deudas indirectas aun cuando el deudor no tuviere deudas directas.
## 4. TIPO DE CREDITOS U OPERACIONES
Código que da cuenta del tipo de operación a que corresponde el monto incluido en el respectivo registro, según:
Código Tipo de operaciones
1 Créditos comerciales
2 Créditos de consumo
3 Créditos para vivienda
4 Operaciones financieras
5 Instrumentos de deuda adquiridos
6 Créditos contingentes
7 Cupos de líneas de crédito de libre disposición
8 Créditos para estudios superiores
Ley N°20.027
9 Créditos educacionales con garantía CORFO
10 Otros créditos para estudios superiores
11 Créditos contingentes para estudios superiores
Esta clasificación considera como:
Créditos comerciales: todos aquellos créditos que no corresponden a las operaciones que se indican a continuación.
Circular N° 2.266 / 25.08.2020 por Resolución N° 3759

Archivo D10 / hoja 3 Créditos de consumo: comprende los créditos cuyos deudores son personas naturales y que se otorgan para financiar bienes de consumo o el pago de servicios. Comprenden: a) Créditos pagaderos en cuotas; b) Créditos provenientes de la utilización de tarjetas de crédito; c) Créditos con líneas de crédito o sobregiros en cuentas corrientes; y d) Otros créditos con aquellas características.
Créditos para vivienda: corresponde a créditos que se otorgan a personas naturales para adquisición, ampliación, reparación o construcción de su vivienda. Comprende los préstamos en letras de crédito, con mutuos hipotecarios endosables u otros con aquellas características. Incluye los créditos de enlace que se hubieren otorgado antes del perfeccionamiento de los mutuos y los créditos complementarios destinados a la adquisición, ampliación, reparación o construcción de la vivienda.
Operaciones financieras: Corresponde a contratos con pacto de retroventa y obligaciones por préstamos de valores.
Instrumentos de deuda adquiridos: Corresponde a las deudas de los emisores de los instrumentos que para efectos contables forman parte de la cartera de negociación, disponibles para la venta o inversiones al vencimiento.
Créditos contingentes: Corresponde a los créditos contingentes que deben informarse según lo previsto en el Capítulo 18-5 de la Recopilación Actualizada de Normas, con excepción de las líneas de crédito que se informan con el código siguiente.
Cupos de líneas de crédito de libre disposición:
Corresponde a los créditos aprobados que pueden ser utilizados por la sola voluntad del cliente, tales como los sobregiros pactados en cuenta corriente o los cupos para tarjetas de crédito. Se trata sólo del monto correspondiente a los importes no utilizados, en que la institución está contractualmente obligada a admitir el crédito.
En el caso de las tarjetas de crédito, se entiende que el cupo corresponde sólo al monto no utilizado, debiendo incluirse en consecuencia como créditos (de consumo o comerciales, según corresponda), los montos ya utilizados, sea que el banco haya pagado o no las operaciones efectuadas con la tarjeta a la fecha a que se refiere la información.
Créditos para estudios superiores Ley N°20.027: comprende aquellos concedidos para el financiamiento de estudios superiores otorgados de acuerdo con la Ley N°20.027 CAE).
Circular N° 2.266 / 25.08.2020 por Resolución N° 3759

Archivo D10 / hoja 4 Créditos educacionales con garantías CORFO: corresponde a préstamos estudiantiles otorgados con algún tipo de garantía de CORFO.
Otros créditos para estudios superiores: comprende todos los demás créditos otorgados para el financiamiento de estudios superiores distintos a los de la Ley N° 20.027 y de aquellos con garantía CORFO.
Créditos contingentes para estudios superiores: Corresponde a los créditos contingentes asociados a préstamos educacionales de la Ley N°20.027 u otros que generen una obligación contingente.
## 5. MOROSIDAD
Debe incluirse un código para indicar la situación en que se encuentra el importe informado en relación con el cumplimiento oportuno de su pago, de acuerdo con lo siguiente:
Código Tiempo transcurrido desde el vencimiento
0 Crédito al día
1 Menos de 30 días
2 30 días o más, pero menos de 60 días
3 60 días o más, pero menos de 90 días
4 90 días o más, pero menos de 180 días
5 180 días o más, pero menos de un año
6 Un año o más, pero menos de dos años
7 Dos años o más, pero menos de tres años
8 Tres años o más, pero menos de 4 años
9 Cuatro años o más
Cuando el registro corresponda a créditos contingentes, incluidos los cupos de líneas de crédito de libre disposición, se utilizará el código “0”.
La información por morosidad debe tomar en cuenta las cláusulas contractuales y los eventuales convenios de pago posteriores, de modo que esa información refleje efectivamente lo que el deudor ha dejado de pagar según el calendario de pago vigente.
En el caso de créditos en cuotas con cláusula de aceleración, la morosidad de la parte que se hace exigible sin haberse cumplido el plazo de vencimiento normal originalmente previsto, quedará establecida según la fecha en que se hizo efectiva esa cláusula.
## 6. MONTO
Debe incluirse el monto que corresponda según lo definido en los campos anteriores.
Circular N° 2.266 / 25.08.2020 por Resolución N° 3759

Archivo D10 / hoja 5 En general, de acuerdo con lo indicado en el Capítulo 18-5 de la Recopilación Actualizada de Normas, los valores que deben informarse en este archivo son aquellos que se obtienen de acuerdo con las condiciones convenidas para los créditos otorgados, sin considerar los intereses penales pactados para el período de mora transcurrido ni gastos de cobranza.
En el caso de operaciones contingentes, corresponderá al monto que podría traducirse en un crédito efectivo.
Los créditos u operaciones pagaderas en moneda extranjera se expresarán en pesos según el tipo de cambio de representación contable utilizado por el banco.
Las operaciones reajustables deberán estar calculadas según el valor del factor o unidad de cuenta pactado (UF, tipo de cambio, etc.) correspondiente al día a que se refiere la información.
Lo indicado anteriormente es sin perjuicio de la disposición transitoria del Capítulo 18-5 antes referido, en relación con los créditos que se informaron como castigados hasta el 31 de diciembre de 2008.
Carátula de cuadratura El archivo D10 debe entregarse con una carátula de cuadratura cuyo modelo se especifica a continuación.
MODELO Institución: __________________________________ Código: ________ Información correspondiente al mes de: ____________ Archivo D10

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

Circular N° 2.266 / 25.08.2020 por Resolución N° 3759

### TEXTO ACTUALIZADO
Cooperativas Circular N°102 Hoja1
### TEXTO ACTUALIZADO
Disposición: CIRCULAR N° 102 (de 16.05.94) Para: COOPERATIVAS Materia: Envío de nóminas de deudores morosos al Boletín de Informaciones Comerciales.
ACTUALIZACIONES:
Modificaciones introducidas mediante acuerdos adoptados por el Consejo de la Comisión para el Mercado Financiero*:
Circular N°2.266 de 25.08.2020 por Resolución N° 3759
* De acuerdo a lo dispuesto en el artículo noveno transitorio de la Ley N°21.130, y lo establecido en
el Decreto con Fuerza de Ley Nº2, expedido a través del Ministerio de Hacienda y publicado en el Diario Oficial el 2 de mayo de 2019, la Comisión para el Mercado Financiero asumió las competencias de la Superintendencia de Bancos e Instituciones Financieras a partir del 1º de junio de 2019, determinándose igualmente esa fecha para la supresión de esta última.

### TEXTO ACTUALIZADO
Cooperativas Circular N°102 Hoja2 Envío de nóminas de deudores morosos al Boletín de Informaciones Comerciales De acuerdo con lo dispuesto por el D.S. N°950, de 1928, del Ministerio de Hacienda, modificado por el D.S. N° 883 de 1992 y por el D.S.
N°259, publicado en el Diario Oficial del 28 de abril de 1994, las cooperativas de ahorro y crédito pueden enviar al Boletín de Informaciones Comerciales de la Cámara de Comercio de Chile, una nómina de los deudores que hayan incurrido en mora en el servicio de sus préstamos o créditos a favor de la respectiva cooperativa, excluidas aquellas deudas correspondientes a documentos enviados a notaría para su protesto.
Las cooperativas que decidan hacer uso de dicha facultad enviarán las referidas nóminas dentro de los quince primeros días hábiles de cada mes con los siguientes datos y ordenada en la forma que requiera el Boletín para su procesamiento:
a) Nombre completo y RUT del deudor.
b) Importe de la deuda directa que no fue pagada por el deudor
en el mes precedente.
En ningún caso podrán incluirse como morosas las deudas cuyos créditos no consten de un título ejecutivo porque éstos son, de acuerdo a nuestra legislación, los únicos que formalmente dan cuenta de una obligación cuyo cumplimiento puede exigirse compulsivamente. Tampoco podrán remitirse aquellas deudas para fines educacionales, que de conformidad a lo dispuesto por la Ley N°21.214, que modificó el artículo 17 de la Ley N°19.628, sobre protección de la vida privada, no pueden ser comunicadas.
Las cooperativas que opten por enviar estas nóminas quedan obligadas a: a) mantener siempre el envío mensual de la nómina; y, b) incluir en cada nómina todos los deudores que cumplan las condiciones anteriormente señaladas, sin discriminar entre ellos. Con todo, se excluirán de las nóminas los deudores que hayan solucionado su morosidad antes del envío de la respectiva nómina.
Circular N° 2.266