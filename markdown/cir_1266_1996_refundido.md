<!-- source: cir_1266_1996_refundido.pdf -->
<!-- language: es -->
<!-- note: Las fórmulas matemáticas extraídas de PDFs pueden ser incompletas.
     Los bloques marcados con ⚠️ deben verificarse contra el PDF original. -->

# CIRCULAR N° 1266 — IMPARTE INSTRUCCIONES SOBRE ENVIO DE INFORMACION DE INTERMEDIACION ANUAL DE SEGUROS EFECTUADA POR CORREDORES DE SEGUROS Y VENTA DIRECTA


Esta Superintendencia, en uso de sus facultades legales, especialmente lo dispuesto en el artículo 3º, letra l), del DFL 251, de 1931, ha resuelto impartir las siguientes instrucciones :
## I INFORMACION A ENVIAR
Las entidades aseguradoras deberán remitir a esta Superintendencia información referente a:
1) Producción y comisiones por las ventas de seguros, realizadas a través de los corredores de seguros y el detalle de su intermediación por ramos.
2) Producción y comisiones por las ventas de seguros previsionales, realizadas a través de asesores previsionales o entidades de asesoría previsional, y el detalle por ramo de cada una de ellas.
3) La venta de seguros efectuada directamente por la compañía.
La información anterior deberá comprender el período transcurrido entre el 1 de enero y el 31 de diciembre de cada año. Las especificaciones con respecto al contenido y forma que deberá tener la información, se incluyen en Anexo adjunto a esta Circular.
Los archivos deberán ser generados por la entidad aseguradora. La Superintendencia pondrá a disposición de ellas en el módulo SEIL el software de validación correspondiente.
## II FORMA DE ENVIO
Las entidades aseguradoras del primer y segundo grupo, obligadas a la presentación de información de acuerdo a las normas de la presente Circular, deberán remitirlos a este Organismo, mediante el sistema SEIL habilitado en el sitio web de la Superintendencia (www.svs.cl), de acuerdo al procedimiento allí establecido, conjuntamente con los estados financieros al 31 de diciembre de cada año.
El envío de información a través del módulo SEIL se encuentra regulado por la Norma de Carácter General Nº117, de 20 de abril de 2001, de esta Superintendencia, debiendo ser utilizado dicho procedimiento igualmente para los efectos de esta Circular.
Si el envío es aceptado, la entidad recibirá un mensaje por pantalla y un mail certificando su recepción. Si el envío no es aceptado, la compañía recibirá por pantalla un mensaje de error.
Sólo podrán utilizar este sistema de envío las entidades aseguradoras que cuenten con usuario registrado en la SVS, debidamente autorizado por el Representante Legal de la sociedad a la cual pertenece.
Sobre este particular, se deberá tener presente lo siguiente:
- Todas las entidades aseguradoras deberán registrar un usuario en la SVS para el envío de la
información solicitada por la presente Circular.
- Las entidades deben obtener su código de usuario, utilizando la opción “Obtención de Código de
usuario-Clave Secreta” disponible en la página SEIL del sitio web. Será responsabilidad de la compañía cuidar y resguardar debidamente su(s) Código(s) de Usuario y en especial la Clave Secreta que éste tiene.
- Para que el usuario respectivo sea activado, el Representante Legal de la Compañía deberá
completar, firmar y enviar a esta Superintendencia el documento de autorización de habilitación de usuarios correspondiente, por cada usuario que éste habilite, el que se encuentra disponible en la página en cuestión, según lo establecido en la NCG Nº 117.
- La casilla de correo electrónico, de cada usuario, debe estar creada antes de que se solicite sea
incorporado al sistema.
## III VIGENCIA
La presente Circular entrará en vigencia para la presentación de los estados financieros correspondientes al 31 de diciembre de 1995.
## IV DEROGACION
La presente Circular deroga la Circular Nº 1.146 de 17 de enero de 1994.
## V NORMA TRANSITORIA
Sin efecto1
### A N E X O
1 De aplicación transitoria

Instrucciones para el envío de la información de producción y comisiones de corredores de seguros y de asesores previsionales, con detalle de intermediación por ramo y venta directa de agentes y empleados dependientes de la compañía.
#### A. CARACTERISTICAS DE LOS ARCHIVOS
La información requerida deberá grabarse en tres archivos, secuenciales, de tipo texto en código ASCII. El contenido y formato de los registros, deberá adaptarse a las especificaciones detalladas en los puntos C y D de este anexo.
Todas las compañías estarán obligadas al envío de los 3 archivos aun cuando no existiera información del período para alguno de ellos.
Las mutuales de seguros que a la fecha intermedian seguros generales y de vida deberán enviar cuatro archivos, dos por cada grupo de seguros. Se individualizarán en el nombre según se instruye en párrafo B. siguiente y con su Rut y Grupo 1 o 2, según corresponda, en registro de tipo 1 de cada archivo.
#### B. INDIVIDUALIZACION DE LOS ARCHIVOS
B.1 El nombre del archivo que contendrá la información de "producción y comisiones por corredor, con su detalle de intermediación por ramos” deberá ser exclusivamente el siguiente:
CSAAMMXX.TXT, donde AA y MM corresponden respectivamente a los dos dígitos del año y dos dígitos del mes hasta el cual se está informando y XX corresponderá a “sg” o “sv”, según se informe de seguros generales o de vida. Como la información es de carácter anual, MM deberá ser 12.
B.2 El nombre del archivo que contendrá la información de "producción y comisiones por asesor, con su detalle de intermediación por ramos” deberá ser exclusivamente el siguiente:
APAAMMSV.TXT, donde AA y MM corresponden respectivamente a los dos dígitos del año y dos dígitos del mes hasta el cual se está informando. Como la información es de carácter anual, MM deberá ser 12.
B.3 El nombre del archivo que contendrá la información de "identificación y vigencia de los agentes de venta y total de la venta realizada por estos y por dependientes o empleados de la compañía" deberá ser exclusivamente el siguiente:
AGAAMMXX.TXT, donde AA y MM corresponden respectivamente a los últimos dos dígitos del año y dos dígitos del mes hasta el cual se está informando y XX corresponderá a “sg” o “sv”, según se informe de seguros generales o de vida. Como la información es de carácter anual, MM deberá ser 12.
B.4 Como ejemplo, y atendido que el primer período que se debe remitir corresponde al año 2008 con cierre a diciembre del mismo año, los nombres de los archivos en el primer envío serán los siguientes:
• Compañías Seguros Generales : cs0812sg.txt
g0812sg.txt
• Compañías de Seguros de Vida : cs0812sv.txt
ap0812sv.txt ag0812sv.txt
• Mutuales que operan en ambos Grupos : cs0812sg.txt
ag0812sg.txt cs0812sv.txt ag0812sv.txt.
#### C. ESTRUCTURA DE LOS ARCHIVOS

C.1 Archivo CSAAMM.TXT
### TIPOS DE REGISTRO
Identificación (registro Tipo 1):
Contendrá la identificación de la compañía que informa. Cabe señalar que sólo se informará un registro de este tipo y deberá ser el primero del archivo.
Detalle por Corredor (registro Tipo 2):
Contendrá información relativa a la producción y comisiones de los corredores de seguros, originadas por su gestión de intermediación de seguros en el período del cual se está informando.
Detalle Ramos (registro tipo 3):
Contendrá información de la intermediación de seguros, efectuada por el corredor de seguros indicado en el registro de tipo 2 que les antecede. Deberá grabarse un registro por cada diferente ramo de seguros en que él hubiera intermediado, incluyendo pólizas de seguros con ahorro voluntario.
Deberá incorporarse los ramos correspondientes a Subtotales (100, 200, 300 y 400) y Totales (99 y
999)2, en el orden correspondiente, de acuerdo a la norma que regula la forma, contenido y presentación de los estados financieros de las compañías de seguros.
Totales (registro Tipo 4):
Contendrá información de control. Cabe señalar que sólo se informará un registro de este tipo y deberá ser el último del archivo.
Situación de excepción: Si no existe información del período a enviar, el archivo deberá contener el Registro tipo 1 y el Registro rotulado como Totales, en que el campo “TOTAL-REGISTROS” deberá indicar “2”. En todo caso todos los campos de este registro deben ser llenados de acuerdo a las pautas del párrafo Condiciones Generales.
Orden de los Registros: La porción del archivo correspondiente a los registros de tipo 2 y 3 debe ser ordenada por RUT intermediario y luego por tipo de registro. Por su parte el registro de tipo 3 debe ordenarse por el código del ramo.
Montos a Informar: el monto intermediado a informar, corresponderá a aquel enviado en FECU, de acuerdo a la norma que regula la forma, contenido y presentación de los estados financieros de las compañías de seguros.
CONTENIDO Registro tipo 1 de IDENTIFICACION

| CAMPO | DESCRIPCION | Posiciones Ini - Fin | PICTURE |
| --- | --- | --- | --- |
| TIPO | Corresponde al tipo de registro. En este caso corresponde tipo "1". | 1 - 1 | PIC 9(01) |
| RUT-CIA | Corresponde al rol único tributario de la compañía que informa. | 2 - 10 | PIC 9(09) |
| VERIFICADOR | Corresponde al dígito verificador del rol único tributario de la compañía que informa. Si es “K” debe ser informado con mayúscula. | 11 - 11 | PIC X(01) |
| GRUPO | Corresponde al grupo al cual pertenece la compañía. | 12 - 12 | PIC 9(01) |

1 Ejemplos disponibles en sitio web www.svs.cl (Mercado de Seguros / Entidades Fiscalizadas / Cías. de
Seguros Crédito / Cías. de Seguros de Vida / Cías de Seguros Generales / Destacamos)

|  | 1 : Compañías del Primer Grupo (Seg. Generales) 2 : Compañías del Segundo Grupo (Seg. de vida) |  |  |
| --- | --- | --- | --- |
| PERIODO | Indica el período al cual corresponde la información proporcionada. El formato de esta fecha será AAAAMM, donde AAAA corresponde a los 4 dígitos del año del que se informa y MM a los dos dígitos del mes hasta el cual se informa. Lo señalado en este campo deberá coincidir con lo informado en el nombre del archivo que contiene la información. | 13 -18 | PIC 9(06) |
| NOMBRE-CIA | Corresponde a la razón social de la compañía que informa. | 19 - 78 | PIC X(60) |
| FILLER | Sólo deberá grabarse espacios. | 79 - 115 | PIC X(37) |

Registro tipo 2 de DETALLE por CORREDOR

| CAMPO | DESCRIPCION | Posiciones Ini - Fin | PICTURE |
| --- | --- | --- | --- |
| TIPO | Corresponde al tipo de registro. En este caso corresponde tipo "2". | 1 - 1 | PIC 9(01) |
| RUT-INTERMEDIARIO | Corresponde al rol único tributario o R.U.T del corredor de seguros, acerca del cual se está informando. Las intermediaciones de seguros efectuadas por sociedades deben ser informadas con el R.U.T. de éstas, y en ningún caso, con el R.U.T. de alguno de los representantes legales o socios de éstas. | 2 - 10 | PIC 9(09) |
| VERIFICADOR | Corresponde al dígito verificador del rol único tributario del corredor de seguros acerca del cual se está informando. Si es “K” debe ser informado en mayúscula. | 11 - 11 | PIC X(01) |
| TIPO-INTERMEDIARIO | Se debe señalar si el corredor de seguros del que se está informando, es una persona natural o jurídica. CODIGOS VALIDOS: N : Naturales J : Jurídicas Debe ser informado en mayúscula. | 12 - 12 | PIC X(01) |
| NOMBRE- INTERMEDIARIO | Se debe señalar el nombre o la razón social completa del corredor de seguros. Los nombres de las personas naturales se llenarán en el siguiente orden: apellido paterno, apellido materno y nombres. En las personas jurídicas, se deberá usar su Razón Social y no su nombre de fantasía. | 13 - 72 | PIC X(60) |
| NRO-MESES | Se debe indicar el número de meses a que corresponde la | 73 - 74 | PIC 9(02) |

|  | producción informada. |  |  |
| --- | --- | --- | --- |
| NUMERO- ASEGURADOS | Se debe señalar el número de asegurados distintos con los cuales el corredor de seguros efectuó intermediaciones de seguros, durante el período del cual se está informando. | 75 - 82 | PIC 9(08) |
| PRODUCCION-NETA | Indicar el monto de las primas, netas del impuesto al valor agregado, de los contratos de seguros intermediados por el corredor de seguros, durante el período informado. La cifra deberá expresarse en miles de pesos, debidamente actualizada al último día del período del cual se está informando en la normativa que regula la forma, contenido y presentación de los estados financieros de las compañías de seguros. | 83 - 93 | PIC -9(11) |
| COMISIONES | Se debe señalar el monto de las comisiones pagadas y/o devengadas al corredor de seguros, por los contratos de seguros intermediados durante el período informado, el que deberá expresarse en miles de pesos debidamente actualizado al último día del período del cual se está informando, de conformidad a lo especificado para el campo PRODUCCION-NETA. | 94 – 104 | PIC -9(11) |
| PREMIOS- ASIGNACIONES | Anotar el monto de los premios y asignaciones especiales pagadas y/o devengadas al corredor de seguros en el período que se informa, cuyo origen sea, la producción acumulada, la siniestralidad de su cartera, o alguna variable similar, monto que deberá expresarse en miles de pesos debidamente actualizado al último día del período del cual se está informando, de conformidad a lo especificado para el campo PRODUCCION-NETA. | 105 – 115 | PIC -9(11) |

Registro tipo 3 de DETALLE RAMOS

| CAMPO | DESCRIPCION | Posiciones Ini - Fin | PICTURE |
| --- | --- | --- | --- |
| TIPO | Corresponde al tipo de registro. En este caso corresponde tipo "3". | 1 - 1 | PIC 9(01) |
| RUT- INTERMEDIARIO | Corresponde al rol único tributario o R.U.T. del corredor de seguros, acerca del cual se está informando en el registro de tipo 2 anterior. | 2 - 10 | PIC 9(09) |
| CODIGO-RAMO | Corresponde al Código asignado al Ramo. Sus valores están incluidos en la norma que regula la forma, contenido y presentación de los estados financieros de las compañías de seguros. En el caso de los seguros previsionales sólo se deberá informar el código del ramo principal, y no sus subdivisiones. | 11 - 13 | PIC 9(03) |
| CLASIFICACION DE RAMOS | Corresponde a la clasificación que cada ramo puede tener, dependiendo del grupo de seguros que se trate: 1. Seguros del primer grupo: | 14 -14 | PIC X (01) |

|  | • Individual (1) • Colectivo (2) • Masivo (3) • Industrial, infraestructura y comercio (4) 2. Seguros del segundo grupo: • Individuales (1) • Colectivos tradicionales (2) • Banca seguros y Retail (3) • Previsionales (excluidos los seguros de rentas vitalicias previsionales del D.L. Nº 3.500) (4) 3. Para totales 99 y 999, la clasificación es (0) |  |  |
| --- | --- | --- | --- |
| INTERMEDIACION | Corresponde indicar, por ramo, el monto total de las primas netas del impuesto al valor agregado, de los contratos de seguros intermediados por el corredor de seguros, en el ramo que se está informando, durante el período informado. El registro correspondiente al ramo de Código "99" representa el TOTAL en Seguros Generales y 999 representa el total por clasificación en seguros de Vida, debe corresponder a la cantidad informada, para el mismo corredor, en el campo PRODUCCION-NETA del Registro tipo 2 de DETALLE por Corredor. En seguros de vida, las sumas de las clasificaciones de cada ramo corresponden al ramo 100, 200, 300 y 400. Las cifras deberán expresarse en miles de pesos, debidamente actualizadas al último día del período del cual se está informando, según lo señalado para el campo "PRODUCCION-NETA" del registro de tipo 2. | 15 - 26 | PIC -9(11) |
| FILLER | Sólo debe grabarse espacios. | 27 - 115 | PIC X(89) |

Registro tipo 4 de TOTALES

| CAMPO | DESCRIPCION | Posiciones Ini - Fin | PICTURE |
| --- | --- | --- | --- |
| TIPO | Corresponde al tipo de registro. En este caso corresponde tipo "4". | 1 - 1 | PIC 9(01) |
| TOTAL-ASEGURADOS | Corresponde a la suma de todos los valores informados en el campo NUMERO-ASEGURADOS del Registro tipo 2 de DETALLE. | 2 - 11 | PIC 9(10) |
| TOTAL-PROD-NETA | Corresponde a la suma de todas las cantidades informadas | 12 - 22 | PIC -9(11) |

|  | en el campo PRODUCCION-NETA del Registro tipo 2 de DETALLE |  |  |
| --- | --- | --- | --- |
| TOTAL-COMISIONES | Corresponde a la suma de todos los montos informados en el campo COMISIONES del Registro tipo 2 de DETALLE. | 23 - 33 | PIC -9(11) |
| TOTAL- ASIGNACIONES | Corresponde a la suma de todos los valores informados en campo PREMIOS-ASIGNACIONES en el Registro tipo 2 de DETALLE. | 34 - 44 | PIC -9(11) |
| TOTAL-REGISTROS | Corresponde al número total de registros informados en este archivo, desde el registro de tipo 1 hasta el registro de tipo 3, ambos inclusive. | 45 - 49 | PIC 9(05) |
| FILLER | Sólo debe grabarse espacios. | 50 – 115 | PIC X(66) |

C.2 Archivo APAAMM.TXT
### TIPOS DE REGISTRO
Identificación (registro Tipo 1): Contendrá la identificación de la compañía que informa. Cabe señalar que sólo se informará un registro de este tipo y deberá ser el primero del archivo.
Detalle por asesor (registro Tipo 2):
Contendrá información relativa a la producción y comisiones de los asesores previsionales, originadas por su gestión de asesoría previsional en el período del cual se está informando.
Detalle Ramos (registro tipo 3):
Contendrá información de la gestión de venta de seguros previsionales, efectuada por el asesor previsional, o entidad asesora previsional indicado en el registro de tipo 2 que les antecede. Deberá grabarse un registro por cada diferente ramo de seguros en que él hubiera intermediado.
Deberá incorporarse los ramos correspondientes a Subtotales (100, 200, 300 y 400) y Totales (99 y
999)3, en el orden correspondiente, de acuerdo a la norma que regula la forma, contenido y presentación de los estados financieros de las compañías de seguros.
Cabe hacer presente que los asesores previsionales sólo pueden intermediar pólizas de seguros de rentas vitalicias previsionales.
Totales (registro Tipo 4):
Contendrá información de control. Cabe señalar que sólo se informará un registro de este tipo y deberá ser el último del archivo.
Situación de excepción: Si no existe información del período a enviar, el archivo deberá contener el Registro tipo 1 y el Registro rotulado como Totales, en que el campo “TOTAL-REGISTROS” deberá indicar “2”. En todo caso todos los campos de este registro deben ser llenados de acuerdo a las pautas del párrafo Condiciones Generales.
Orden de los Registros: La porción del archivo correspondiente a los registros de tipo 2 y 3 debe ser ordenada por RUT del asesor y luego por tipo de registro. Por su parte el registro de tipo 3 debe ordenarse por el código del ramo.
Montos a Informar: el monto intermediado a informar, corresponderá a aquel enviado en FECU, de acuerdo a la norma que regula la forma, contenido y presentación de los estados financieros de las
1 Ejemplos disponibles en sitio web www.svs.cl (Mercado de Seguros / Entidades Fiscalizadas / Cías. de
Seguros Crédito / Cías. de Seguros de Vida / Cías de Seguros Generales / Destacamos) compañías de seguros.
CONTENIDO Registro tipo 1 de IDENTIFICACION

| CAMPO | DESCRIPCION | Posiciones Ini - Fin | PICTURE |
| --- | --- | --- | --- |
| TIPO | Corresponde al tipo de registro. En este caso corresponde tipo "1". | 1 - 1 | PIC 9(01) |
| RUT-CIA | Corresponde al rol único tributario de la compañía que informa. | 2 - 10 | PIC 9(09) |
| VERIFICADOR | Corresponde al dígito verificador del rol único tributario de la compañía que informa. Si es “K” debe ser informado con mayúscula. | 11 - 11 | PIC X(01) |
| GRUPO | Corresponde al grupo al cual pertenece la compañía. 2 : Compañías del Segundo Grupo (Seg. de vida) | 12 - 12 | PIC 9(01) |
| PERIODO | Indica el período al cual corresponde la información proporcionada. El formato de esta fecha será AAAAMM, donde AAAA corresponde a los 4 dígitos del año del que se informa y MM a los dos dígitos del mes hasta el cual se informa. Lo señalado en este campo deberá coincidir con lo informado en el nombre del archivo que contiene la información. | 13 - 18 | PIC 9(06) |
| NOMBRE-CIA | Corresponde a la razón social de la compañía que informa. | 19 - 78 | PIC X(60) |
| FILLER | Sólo deberá grabarse espacios. | 79 - 115 | PIC X(37) |

Registro tipo 2 de DETALLE por ASESOR

| CAMPO | DESCRIPCION | Posiciones Ini - Fin | PICTURE |
| --- | --- | --- | --- |
| TIPO | Corresponde al tipo de registro. En este caso corresponde tipo "2". | 1 - 1 | PIC 9(01) |
| RUT-ASESOR | Corresponde al rol único tributario o R.U.T del asesor previsional, acerca del cual se está informando. Las ventas de seguros previsionales efectuadas por entidades de asesoría deben ser informadas con el R.U.T. de éstas, y en ningún caso, con el R.U.T. de alguno de los representantes legales o socios de éstas. | 2 - 10 | PIC 9(09) |
| VERIFICADOR | Corresponde al dígito verificador del rol único tributario del asesor o entidad de asesoría previsional acerca del cual se | 11 - 11 | PIC X(01) |

|  | está informando. Si es “K” debe ser informado en mayúscula. |  |  |
| --- | --- | --- | --- |
| TIPO-ASESOR | Se debe señalar si el asesor previsional del que se está informando, es una persona natural o jurídica. CODIGOS VALIDOS: N : Naturales J : Jurídicas Debe ser informado en mayúscula. | 12 - 12 | PIC X(01) |
| NOMBRE-ASESOR | Se debe señalar el nombre o la razón social completa del asesor o entidad de asesoría previsional. Los nombres de las personas naturales se llenarán en el siguiente orden: apellido paterno, apellido materno y nombres. En las personas jurídicas, se deberá usar su Razón Social y no su nombre de fantasía. | 13 - 72 | PIC X(60) |
| NRO-MESES | Se debe indicar el número de meses a que corresponde la producción informada. | 73 - 74 | PIC 9(02) |
| NUMERO- ASEGURADOS | Se debe señalar el número de asegurados distintos con los cuales el asesor o entidad de asesoría previsional efectuó intermediaciones de seguros previsionales, durante el período del cual se está informando. | 75 - 82 | PIC 9(08) |
| PRODUCCION-NETA | Indicar el monto de las primas, netas del impuesto al valor agregado, de los contratos de seguros previsionales, intermediados por el asesor o entidad de asesoría previsional, durante el período informado. La cifra deberá expresarse en miles de pesos, debidamente actualizada al último día del período del cual se está informando la normativa que regula la forma, contenido y presentación de los estados financieros de las compañías de seguros. | 83 - 93 | PIC -9(11) |
| COMISIONES | Se debe señalar el monto de las comisiones pagadas y/o devengadas al asesor o entidad de asesoría previsional, por los contratos de seguros previsionales intermediados durante el período informado, el que deberá expresarse en miles de pesos debidamente actualizado al último día del período del cual se está informando, de conformidad a lo especificado para el campo PRODUCCION-NETA. | 94 – 104 | PIC -9(11) |
| FILLER | Sólo debe grabarse espacios. | 105 – 115 | PIC X(11) |

Registro tipo 3 de DETALLE RAMOS

| CAMPO | DESCRIPCION | Posiciones Ini - Fin | PICTURE |
| --- | --- | --- | --- |
| TIPO | Corresponde al tipo de registro. En este caso corresponde tipo "3". | 1 - 1 | PIC 9(01) |
| RUT-ASESOR | Corresponde al rol único tributario o R.U.T. del asesor o entidad de asesoría previsional, acerca del cual se está informando en el registro de tipo 2 anterior. | 2 - 10 | PIC 9(09) |
| CODIGO-RAMO | Corresponde al Código asignado al Ramo. Sus valores están incluidos en la norma que regula la forma, contenido y presentación de los estados financieros de las compañías de seguros. En el caso de los seguros previsionales sólo se deberá informar el código del ramo principal, y no sus subdivisiones. | 11 - 13 | PIC 9(03) |
| CLASIFICACION DE RAMOS | Corresponde a la clasificación que cada ramo puede tener: 1. Seguros del segundo grupo: • Previsionales (excluidos los seguros de ahorro voluntario, sean individual o colectivo) (4) 2. Total 999 la clasificación es 0 | 14-14 | PIC X (01) |
| INTERMEDIACION | Corresponde indicar, por ramo, el monto total de las primas netas del impuesto al valor agregado, de los contratos de seguros previsionales intermediados por el asesor o entidad de asesoría previsional, en el ramo que se está informando, durante el período informado. El registro correspondiente al ramo de “400” que representa el TOTAL en Seguros Previsionales, debe corresponder a la cantidad informada, para el mismo asesor, en el campo PRODUCCION-NETA del Registro tipo 2 de DETALLE por asesor. Las cifras deberán expresarse en miles de pesos, debidamente actualizadas al último día del período del cual se está informando, según lo señalado para el campo "PRODUCCION-NETA" del registro de tipo 2. | 15 - 26 | PIC -9(11) |
| FILLER | Sólo debe grabarse espacios. | 27 - 115 | PIC X(89) |

Registro tipo 4 de TOTALES

| CAMPO | DESCRIPCION | Posiciones Ini - Fin | PICTURE |
| --- | --- | --- | --- |
| TIPO | Corresponde al tipo de registro. En este caso corresponde tipo "4". | 1 - 1 | PIC 9(01) |
| TOTAL-ASEGURADOS | Corresponde a la suma de todos los valores informados en el campo NUMERO-ASEGURADOS del Registro tipo 2 de | 2 - 11 | PIC 9(10) |

|  | DETALLE. |  |  |
| --- | --- | --- | --- |
| TOTAL-PROD-NETA | Corresponde a la suma de todas las cantidades informadas en el campo PRODUCCION-NETA del Registro tipo 2 de DETALLE | 12 - 22 | PIC -9(11) |
| TOTAL-COMISIONES | Corresponde a la suma de todos los montos informados en el campo COMISIONES del Registro tipo 2 de DETALLE. | 23 - 33 | PIC -9(11) |
| TOTAL-REGISTROS | Corresponde al número total de registros informados en este archivo, desde el registro de tipo 1 hasta el registro de tipo 3, ambos inclusive. | 34 - 38 | PIC -9(5) |
| FILLER | Sólo debe grabarse espacios. | 39 - 115 | PIC 9(77) |

C.3. Archivo AGAAMMXX.TXT
### TIPOS DE REGISTRO
Identificación (registro Tipo 1):
Contendrá la identificación de la compañía que informa. Cabe señalar que sólo se informará un registro de este tipo y deberá ser el primero del archivo.
Agentes de Venta (registro Tipo 2):
Contendrá información relativa a identificación y vigencia de los Agentes de Venta, a que se refieren la Norma de Carácter General Nº 49, de 9 de septiembre de 1994, modificada por las NCG Nºs. 90, 121 y
127, y la Norma de Carácter General Nº 91, de 21 de enero de 2000, modificada por la NCG 116.
Venta directa del período (registro Tipo 3) Contendrá información referida al total de venta directa en seguros no previsionales y previsionales y el total de comisiones del período informado, respecto de los Agentes de Venta y Empleados o dependientes que presten funciones de venta para la compañía. Se informará asociado al RUT de la compañía. Sólo se informará un registro de este tipo y deberá ser el penúltimo del archivo.
Totales (registro Tipo 4):
Contendrá información de control referida al total de ventas del período informado. Cabe señalar que sólo se informará un registro de este tipo y deberá ser el último del archivo.
Situación de excepción: Si no existe información del período a enviar, el archivo deberá contener el Registro Tipo 1 y el Registro rotulado como Totales, en que el campo “TOTAL-REGISTROS” deberá indicar “2”. En todo caso todos los campos de este registro deben ser llenados de acuerdo a las pautas del párrafo Condiciones Generales.
Orden de los Registros: El archivo debe enviarse ordenado por tipo de registro. La porción del archivo correspondiente a los registros tipo 2 debe ser ordenada por el campo RUT agente.
CONTENIDO Registro tipo 1 de IDENTIFICACION

| CAMPO | DESCRIPCION | Posiciones Ini - Fin | PICTURE |
| --- | --- | --- | --- |
| TIPO | Corresponde al tipo de registro. En este caso corresponde tipo "1". | 1 - 1 | PIC 9(01) |
| RUT-CIA | Corresponde al rol único tributario de la compañía que informa. | 2 - 10 | PIC 9(09) |

| VERIFICADOR | Corresponde al dígito verificador del rol único tributario de la compañía que informa. Si es “K” debe ser informado en mayúscula. | 11 - 11 | PIC X(01) |
| --- | --- | --- | --- |
| GRUPO | Corresponde al grupo al cual pertenece la compañía. 1 : Compañías del Primer Grupo (Seg. Generales) 2 : Compañías del Segundo Grupo (Seg. de vida) | 12 - 12 | PIC 9(01) |
| PERIODO | Indica el período al cual corresponde la información proporcionada. El formato de esta fecha será AAAAMM, donde AAAA corresponde a los 4 dígitos del año del que se informa y MM a los dos dígitos del mes hasta el cual se informa. Lo señalado en este campo deberá coincidir con lo informado en el nombre del archivo que contiene la información. | 13 - 18 | PIC 9(06) |
| NOMBRE-CIA | Corresponde a la razón social de la compañía que informa. | 19 - 78 | PIC X(60) |
| FILLER | Sólo deberá grabarse espacios. | 79 - 88 | PIC X(10) |

Registro tipo 2 de AGENTES DE VENTA

| CAMPO | DESCRIPCION | Posiciones Ini - Fin | PICTURE |
| --- | --- | --- | --- |
| TIPO | Corresponde al tipo de registro. En este caso corresponde tipo "2". | 1 - 1 | PIC 9(01) |
| RUT-AGENTE | Corresponde al rol único tributario o R.U.T del agente de venta, acerca del cual se está informando. La identificación de las personas jurídicas deben ser informadas con el R.U.T. de éstas, y en ningún caso, con el R.U.T. de alguno de los representantes legales o socios de ellas. | 2 - 10 | PIC 9(09) |
| VERIFICADOR | Corresponde al dígito verificador del rol único tributario del agente de venta acerca del cual se está informando. | 11 - 11 | PIC X(01) |
| TIPO-AGENTE | Se debe señalar si el agente de venta del que se informa, es una persona natural o jurídica. CODIGOS VALIDOS: N : Naturales J : Jurídicas Debe ser informado en mayúscula. | 12 - 12 | PIC X(01) |
| NOMBRE-AGENTE | Se debe señalar el nombre o la razón social completa del agente de venta. Los nombres de las personas naturales se llenarán en el siguiente orden: apellido paterno, apellido | 13 - 72 | PIC X(60) |

|  | materno y nombres. En las personas jurídicas, se deberá usar su Razón Social y no su nombre de fantasía. |  |  |
| --- | --- | --- | --- |
| FECHA-INSCRIPCION | Se debe indicar la fecha de inscripción, del agente de ventas que se está informando, en el Registro establecido en las Normas de Carácter General Nºs. 49 y 91, de septiembre de 1994 y enero de 2000, según corresponda. El formato debe ser "AAAAMMDD", donde "AAAA" corresponde a los cuatro dígitos del año, "MM" al mes y "DD" al día, en que se procedió a su inscripción. NOTA : Si un agente de venta, en el curso del período que se está informando, tuviese más de una inscripción vigente, deberá informarse en registros separados tantas veces como así haya ocurrido. Para tal efecto, deberá comunicarse en el orden cronológico correspondiente. | 73 - 0 | PIC (08) |
| FECHA-TERMINO | Corresponde informar la fecha de término del contrato, según conste en el Registro Especial de Agentes de Ventas, establecido en la Norma de Carácter General Nº 49, de septiembre de 1994, o eliminación del Registro de Agentes de Ventas de Rentas Vitalicias, cuando corresponda. El formato debe ser "AAAAMMDD", donde "AAAA" corresponde a los cuatro dígitos del año, "MM" al mes y "DD" al día, en que se dio término al contrato. Si el Agente, al término del período que se esté informando, permanece "vigente" sólo se rellenará con ceros ("00000000"). | 81 - 88 | PIC 9(08) |

Registro de Tipo 3 de VENTA DIRECTA DEL PERIODO

| CAMPO | DESCRIPCION | Posiciones Ini - Fin | PICTURE |
| --- | --- | --- | --- |
| TIPO | Corresponde al tipo de registro. En este caso corresponde tipo “3”. | 1 – 1 | PIC 9(01) |
| RUT-COMPAÑIA | Corresponde al rol único tributario o R.U.T. de la Compañía de Seguros que está informando. | 2 – 10 | PIC 9(09) |
| VENTA-NO-PREV-DE- AGENTES | Indicar la SUMA TOTAL DE LOS MONTOS de las primas, netas del impuesto al valor agregado, de las ventas de seguros, generales y de vida, no establecidos en el D.L. Nº3.500, de 1980, efectuadas por LOS AGENTES INFORMADOS PARA EL PERIODO. La cifra deberá expresarse en miles de pesos, debidamente actualizada al último día del período del cual se está informando, según lo señalado para el campo “PRODUCCION-NETA” del registro de tipo 2 del archivo | 11 - 21 | PIC-9(10) |

|  | “CSAAMMXX.TXT”. |  |  |
| --- | --- | --- | --- |
| VENTA-NO-PREV-DE- LA COMPAÑIA | Indicar la SUMA TOTAL DE LOS MONTOS de las primas, netas del impuesto al valor agregado, de las ventas de seguros, generales y de vida, no establecidos en el D.L. Nº3.500, de 1980, efectuadas por los empleados o dependientes de la Compañía que presten funciones de ventas para ésta, durante el período. La cifra deberá expresarse en miles de pesos, debidamente actualizada al último día del período del cual se está informando, según lo señalado para el campo “PRODUCCION-NETA” del registro de tipo 2 del archivo “CSAAMMXX.TXT”. | 22 - 32 | PIC-9(10) |
| VENTA-PREV-DE- AGENTES | Indicar la SUMA TOTAL DE LOS MONTOS de las primas, netas del impuesto al valor agregado, de las ventas de seguros, establecidos en el D.L. Nº3.500, de 1980, efectuadas por LOS AGENTES INFORMADOS PARA EL PERIODO. La cifra deberá expresarse en miles de pesos, debidamente actualizada al último día del período del cual se está informando, según lo señalado para el campo “PRODUCCION-NETA” del registro de tipo 2 del archivo “CSAAMMXX.TXT”. | 33 - 43 | PIC-9(10) |
| VENTA-PREV-DE-LA- COMPAÑÍA | Indicar la SUMA TOTAL DE LOS MONTOS de las primas, netas del impuesto al valor agregado, de las ventas de seguros, establecidos en el D.L. Nº3.500, de 1980, efectuadas por empleados o dependientes de la Compañía que presten funciones de ventas para ésta, durante el período. La cifra deberá expresarse en miles de pesos, debidamente actualizada al último día del período del cual se está informando, según lo señalado para el campo “PRODUCCION-NETA” del registro de tipo 2 del archivo “CSAAMMXX.TXT”. | 44 - 54 | PIC-9(10) |
| COMIS-TOTAL-A- AGENTES | Se debe señalar el TOTAL de las comisiones pagadas y/o devengadas por los agentes de ventas, por los contratos de seguros comercializados durante el período informado, el que deberá expresarse en miles de pesos debidamente actualizado al último día del período del cual se está informando, de conformidad a lo especificado para el campo PRODUCCION-NETA del registro de tipo 2 del archivo “CSAAMMXX.TXT”. | 55 - 65 | PIC-9(10) |
| COMIS-TOTAL-A- EMPLEADOS | Se debe señalar el TOTAL de las comisiones pagadas y/o devengadas por los dependientes o empleados de la compañía por los contratos de seguros comercializados | 66 - 76 | PIC -9(10) |

|  | durante el período informado, el que deberá expresarse en miles de pesos debidamente actualizado al último día del período del cual se está informando, de conformidad a lo especificado para el campo PRODUCCION-NETA. del registro de tipo 2 del archivo “CSAAMMXX.TXT”. |  |  |
| --- | --- | --- | --- |
| FILLER | Sólo debe grabarse espacios. | 77 - 88 | PIC X(12) |

Registro tipo 4 de TOTALES

| CAMPO | DESCRIPCION | Posiciones Ini - Fin | PICTURE |
| --- | --- | --- | --- |
| TIPO | Corresponde al tipo de registro. En este caso corresponde tipo "3". | 1 - 1 | PIC 9(01) |
| TOTAL-REGISTROS | Corresponde al número total de registros informados en este archivo, desde el registro de tipo 1 hasta el registro de tipo 4, ambos inclusive. | 2 - 6 | PIC 9(05) |
| FILLER | Sólo debe grabarse espacios. | 7 - 88 | PIC X(82) |

#### D. CONSIDERACIONES GENERALES
## 1. Ante la ausencia justificada de información:
- En un campo numérico sin signo deberá grabarse "0" (cero o ceros) desde la primera
hasta la última posición del campo.
Ej. Campo de PIC 9(05), se grabará:

| 0 | 0 | 0 | 0 | 0 |
| --- | --- | --- | --- | --- |

- En un campo numérico con signo deberá grabarse un espacio en la primera posición y
rellenar con "0" (cero o ceros) las restantes posiciones hasta completar el largo del campo.
Ej. Campo de PIC -9(10), se grabará:

|  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

- En un campo alfanumérico, se grabará espacios en todas las posiciones del campo.
## 2. Posicionamiento:
- Los campos alfanuméricos deberán grabarse justificados a la izquierda y rellenar con
espacios las restantes posiciones hasta la última posición del campo Ej. Campo de PIC X(11), valor "JUAN", se grabará:

| J | U | A | N |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

- Los campos numéricos sin signo deben justificarse a la derecha y rellenar las primeras
posiciones con "0" (cero o ceros) Ej. Campo de PIC 9(06), valor "178", se grabará:

| 0 | 0 | 0 | 1 | 7 | 8 |
| --- | --- | --- | --- | --- | --- |

- Los campos numéricos con signo deben justificarse a la derecha, conservando la
primera posición para el signo y rellenar las siguientes posiciones con "0" (cero o ceros) Si el campo numérico es positivo, en la posición del signo se puede grabar un signo más "+" o grabar un espacio Ej. Campo de PIC -9(10), valor "456781", se grabará:

| + | 0 | 0 | 0 | 0 | 4 | 5 | 6 | 7 | 8 | 1 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

| 0 | 0 | 0 | 0 | 4 | 5 | 6 | 7 | 8 | 1 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Si el número es negativo, en la primera posición se deberá grabar un signo menos "-"
Ej. Campo de PIC -9(11), valor "-1234567", se grabará:

| - | 0 | 0 | 0 | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

3. El nombre de cada uno de los dos archivos, será fijo, de acuerdo a lo indicado en el punto B
de este Anexo. No se aceptará nombres distintos a los señalados.
4. Las palabras no deben contener letras con acento y no se debe incluir caracteres especiales,
tales como, º,ª,@, etc. Los caracteres Ñ y ñ deberán reemplazarse por el carácter #.
5. Las expresiones numéricas no deben contener caracteres separadores de unidades de mil o
millón.
6. Los códigos de “TIPO-INTERMEDIARIO” en archivo CSAAMMXX.TXT deben informarse en
mayúsculas (N o J).
7. El código de “TIPO-AGENTE” en archivo AGAAMMXX.TXT debe ser informado en mayúscula
(N o J).
8. El verificador de R.U.T. debe ser informado en mayúscula cuando corresponda a “K”, en
cualesquier de los archivos en que se deba informar y tantas veces como ocurra.
9. Si el formato definido para algún campo, relativo a expresiones en montos de dinero o
cualquier otro, fuera insuficiente para almacenar la información pertinente, NO DEBE
### AMPLIARSE LA LONGITUD DEL CAMPO, NI INFORMARSE UN DATO QUE NO
CORRESPONDA AL VERDADERO, sino que deberá comunicarse a esta Superintendencia para que ella reformule los formatos relativos al archivo.