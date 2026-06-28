<!-- source: cir_1970_2010_refundido.pdf -->
<!-- language: es -->
<!-- note: Las fórmulas matemáticas extraídas de PDFs pueden ser incompletas.
     Los bloques marcados con ⚠️ deben verificarse contra el PDF original. -->

# CIRCULAR N° 1970 — INSTRUYE EL ENVIO DE INFORMACION RELATIVA AL SEGURO AGRICOLA


Esta Superintendencia en uso de sus facultades legales, en especial lo establecido en el artículo 3º, letra b) del D.F.L.
251, de 1931, ha estimado oportuno impartir las siguientes instrucciones referidas al seguro agrícola.
## 1. INFORMACION A SER ENVIADA
Las entidades aseguradoras del primer grupo que vendan o hayan vendido pólizas registradas en el Depósito de Pólizas de esta Superintendencia y formen parte del Programa de Seguro Agrícola, deberán enviar la información que a continuación se indica.
Información de producción (Anexos Nº 2).
La información proporcionada en los archivos Paaaamm.txt deberá corresponder a todas la Pólizas y Endosos emitidos el mes que se informa, las que serán informadas sólo una vez.
Información de denuncias de siniestros (Anexo Nº 3).
La información contenida en el archivo Daaaamm.txt, deberá corresponder a los denuncios de siniestros aceptados durante el mes que se informa y serán enviados sólo una vez, es decir una denuncia por evento.
Será requisito para informar el denuncio de un siniestro que su póliza correspondiente haya sido previamente informada y no se encuentre cancelada, de acuerdo a las instrucciones impartidas en el Anexo N° 2 de esta Circular.
Por cada denuncio informado, entendido como el inicio en el proceso de una liquidación, se le dará término informándolo en el archivo de liquidaciones terminadas (Laaaamm.txt), según corresponda. Cada denuncio sin su correspondiente término de proceso se entenderá como siniestro en curso.
Información de liquidaciones terminadas (Anexos Nº 4).
La información contenida en los archivos Laaaamm.txt deberá corresponder a las liquidaciones terminadas durante el mes que se informa y serán enviados sólo por una vez, salvo que se trate de una reapertura de siniestro, la que se indicará de acuerdo a las instrucciones impartidas en el respectivo Anexo de esta Circular.
Será requisito necesario para informar una liquidación terminada, que la denuncia correspondiente haya sido informada previamente en algún archivo Daaaamm.txt, de acuerdo con las instrucciones contenidas en el Anexo
N° 3.
Frente a dudas relativas a las instrucciones impartidas en esta Circular, la Compañía deberá consultar a este Servicio, por escrito, sin asumir interpretaciones propias.
## 2. PERIODICIDAD Y FORMA DE ENVIO DE LA INFORMACION
La información de producción, denuncias de siniestros y liquidaciones terminadas deberá enviarse, mensualmente, durante los 10 primeros días calendarios de cada mes y deberá incluir la información del mes calendario anterior. Si el décimo día resultase inhábil, se entenderá que el plazo se extiende al día hábil siguiente.
La información deberá enviarse a esta Superintendencia, a más tardar a las 24 horas del día de vencimiento de su presentación, mediante el sistema SEIL habilitado en la página web del Servicio, de acuerdo al procedimiento establecido en Anexo Nº 1.
El envío de información a través del módulo SEIL se encuentra regulado por la Norma de Carácter General Nº117, de 20 de abril de 2001, de esta Superintendencia, debiendo ser utilizado dicho procedimiento igualmente para los efectos de esta Circular.

## 3. PROCEDIMIENTO DE REENVIO DE INFORMACION
El Sistema SEIL sólo aceptará un archivo de cada tipo, por cada mes informado, salvo que la Superintendencia autorice su reenvío, en cuyo caso deberá enviarse la totalidad de los archivos.
Se autorizará el reenvío cuando la compañía lo solicite expresamente justificando su solicitud, y la Superintendencia acoja ésta. La solicitud que haga la compañía deberá describir las modificaciones al archivo enviado inicialmente.
La solicitud de reenvío deberá hacerla un usuario habilitado en la Superintendencia para el envío de información de seguro agrícola. Para ello, se remitirá un correo electrónico a la casilla sgcsa_reenvio@svs.cl, solicitando autorización para el reenvío, las razones que lo justifican y la fecha del período que se desea reenviar.
Cuando se solicite el reenvío de información, y ésta se autorice, la Superintendencia eliminará de sus bases de datos toda la información de ese período. Por lo tanto, la compañía que hace la solicitud deberá reenviar todos los archivos de ese período.
Si la compañía está solicitando la modificación de información referente a períodos distintos, deberá hacer una solicitud por cada uno de los períodos.
Cuando la Superintendencia autorice un reenvío se lo comunicará, por medio de un correo electrónico, al usuario de origen. Una vez recepcionado el correo, la compañía podrá enviar nuevamente la información.
## 4. REQUISITOS DE PRESENTACION DE LA INFORMACION
a) Nombre de los Archivos:
Los archivos deberán llamarse únicamente como se describe a continuación:
Archivo Contenido Paaaamm.txt Pólizas y endosos Daaaamm.txt Denuncias de siniestros Laaaamm.txt Informes de liquidaciones terminadas y sus reaperturas, si corresponde Donde aaaa corresponde al año y mm al mes, en números árabes, de cierre de la información. Si el mes es inferior a 10, deberá anteponerse el dígito 0 (cero).
b) Consideraciones de grabación de los archivos a enviar:
Los archivos serán secuenciales o consecutivos de tipo texto, en código ASCII, con registros de largo fijo, cuyos formatos y contenidos se deberán ajustar a las especificaciones detalladas en los Anexos adjuntos a la presente circular.
c) Uso obligatorio del prevalidador:
La Superintendencia sólo aceptará archivos libres de errores o inconsistencias, esto es, que los reportes que entrega el prevalidador especifiquen que los archivos no contienen errores. Para ello, pondrá a disposición de las compañías que comercialicen el seguro agrícola un prevalidador de uso obligatorio, el que permite que la información sea prevalidada física y lógicamente en el mismo módulo SEIL.
## 5. INSTRUCCIONES DE CARÁCTER GENERAL
Consideraciones Generales Debe tenerse especial cuidado que el software utilizado para la generación del archivo no grabe caracteres de control. Son permitidos los siguientes caracteres:
### • A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
• a b c d e f g h i j k l m n o p q r s t u v w x y z
• 0 1 2 3 4 5 6 7 8 9
• + - _ # & % @ " . , : ; * ( ) / $ < > ! = ‘ “
• blancos o espacios
Campos numéricos
a) Ante la ausencia de información en un campo numérico deberá grabarse "0" (cero o ceros) dependiendo del
largo de éste.

b) Todos los campos numéricos deberán grabarse justificados a la derecha y completarse con ceros por la
izquierda, sin separador de miles ni de decimales.
c) Para los campos numéricos se informarán con su valor absoluto, sin signos. Sólo se aceptarán como
cantidades válidas las siguientes: 0 1 2 3 4 5 6 7 8 9 Ejemplo 1: Si un campo indica el formato 9(10)v9(02) y se quiere representar el número 10.213,75 deberá informarse como: 0 0 0 0 0 1 0 2 1 3 7 5 Ejemplo 2: Cuando se quiere representar el número porcentual 2,50% en un campo numérico con formato
9(02)v9(02), éste deberá informarse como 0 2 5 0.
Campos fecha
a) Todas las fechas deben expresarse en formato aaaammdd, donde:
• aaaa: cuatro dígitos del año que corresponda.
• mm: dos dígitos del mes que corresponda.
• dd: dos dígitos del día que corresponda.
b) Si el mes o el día es menor que 10, en números árabes, debe anteponerse el dígito 0 (cero).
Campos alfanuméricos
a) Ante la ausencia de información en un campo alfanumérico deberá grabarse " " (espacio o espacios).
b) Si en la información se encuentran contenidos caracteres Ñ o ñ, estos deberán ser reemplazados por N o n
respectivamente.
Consideraciones Especiales
a) Si el formato definido para algún campo, relativo a expresiones en montos de dinero o cualquier otro, fuera
insuficiente para almacenar la información pertinente, no debe ampliarse la longitud del campo, sino que dicha situación deberá ser comunicada a esta Superintendencia para que ella reformule los formatos relativos al archivo.
b) Si alguna comuna, unidad de reajuste u otro campo que requiera la utilización de un código no se encuentra
en el módulo SEIL (Codificación S.V.S., Seguro Agrícola), la compañía no debe asignar un código, sino que deberá comunicarse a esta Superintendencia para que ella le asigne uno.
En ambos casos, el usuario habilitado para el envío de la información de la presente Circular deberá comunicarse con la Superintendencia al correo electrónico sgcsa_reenvio@svs.cl.
## 6. TRANSITORIO
El primer envío de información de Producción, Denuncias y Liquidaciones terminadas de Frutales, contendrá los datos correspondientes a todas las pólizas emitidas hasta el mes de cierre del envío de información.
## 7. VIGENCIA Y DEROGACIÓN.
La presente Circular rige a contar del 01 de abril de 2010, siendo aplicable a la información que se registre en el sistema de la compañía a partir de esa fecha, la que debe enviarse a esta Superintendencia a más tardar el día
10 de mayo de 2010. Esta Circular deroga y reemplaza a la Circular 1907.
SUPERINTENDENTE(S)

## ANEXO Nº1 PROCEDIMIENTO DE ENVÍO DE INFORMACION DEL SEGURO AGRICOLA MEDIANTE EL MODULO SEIL
Las Compañías del primer grupo que vendan o hayan vendido el seguro agrícola, deberán enviar la información señalada en los Anexos Nº2, Nº3 y Nº4 a través de la opción Sistema de Envío de Información en Línea (SEIL), disponible en el sitio Web de este Servicio (www.svs.cl). En este sitio se encuentran disponibles y actualizados para el seguro agrícola los códigos referentes a productos agrícolas, unidades físicas de medida de dichos productos, códigos de comuna, de región, de zona homogénea de seguro (ZHS).
Sólo podrán efectuar este trámite las compañías de seguros que cuenten con usuario registrado en la SVS, debidamente autorizado por el Representante Legal de la Compañía de Seguros a la cual pertenece. Sobre este particular, se deberá tener presente lo siguiente:
1) Las Compañías que vendan o hayan vendido el seguro agrícola deben obtener su código de usuario, utilizando la opción “Obtención de Código de usuario-Clave Secreta” disponible en la página SEIL del sitio Web. Será responsabilidad de la compañía cuidar y resguardar debidamente su(s) Código(s) de Usuario y en especial la Clave Secreta que éste tiene.
Se entenderá que aquella compañía que no registre un usuario en la SVS para el envío de la información solicitada por la presente Circular, no vende ni ha vendido el seguro.
En el caso de entidades que registren un usuario en la SVS para efectos de esta Circular, y que suspendan la venta del seguro agrícola, deberán informar esta situación a la Superintendencia. En dicho caso, la opción de envío de información para esa aplicación será deshabilitada. Si la compañía reinicia posteriormente las ventas, deberá solicitar la rehabilitación de la opción de envío.
2) Para que el usuario respectivo sea activado, el Representante Legal de la Compañía deberá completar, firmar y enviar a esta Superintendencia el documento de autorización de habilitación de usuarios correspondiente, por cada usuario que habilite, descrito en el Anexo A “DECLARACION DE RESPONSABILIDAD Y AUTORIZACION PARA HABILITACION DE USUARIOS SISTEMA DE ENVIO DE INFORMACION EN LINEA
(SEIL)”, de la Norma de Carácter General N° 117
3) Las Compañías de seguros del primer grupo, podrán solicitar la incorporación de la opción "Registro Seguro Agrícola” a usuarios ya activados, agregando la nueva habilitación, si es que ésta no desea activar nuevos usuarios al efecto. Para ello deberá remitir a la SVS el documento de autorización de habilitación de usuarios correspondiente, señalado en el punto 2 precedente.

## ANEXO Nº 2 REGISTRO DE PRODUCCIÓN
## 1. Definiciones
Para los efectos de esta circular, se entenderá por:
Póliza (P) al conjunto de datos que se encuentran en las condiciones particulares del contrato de seguro.
Endoso (E) al conjunto de datos que se encuentran en las condiciones particulares de cada modificación al contrato de seguro y que tenga asociado una variación de la prima neta.
Los endosos representarán siempre la modificación al contrato de seguro, nunca el estado final después de dicho cambio o modificación. Se reconocen los siguientes tipos de endosos:
• Endoso de aumento (A): Informa el nuevo valor de la superficie, del monto asegurado y de la prima
neta como consecuencia de un incremento en la superficie y/o parámetros y/o tasa.
• Endosos de disminución (D): Informa el nuevo valor de la superficie, del monto asegurado y de la
prima neta como consecuencia de una disminución en la superficie y/o parámetros y/o tasa.
• Endoso de cancelación o anulación (C): Informa los valores de datos y/o parámetros con que se
da término al contrato de seguro sin que la compañía haya asumido el riesgo. Los valores de superficie, monto asegurado y prima neta serán los mismos que figuran en la póliza ajustada por endosos.
• Endoso de cancelación anticipada (CA): Informa las condiciones y/o parámetros con que se da
término anticipado al contrato de seguro, cuando una parte de la prima original se encuentra impaga y la compañía ha agotado la posibilidad de cobrar el saldo. La compañía deberá informar en este endoso la nueva fecha de término de vigencia; la superficie y el monto asegurado se informan en cero (0) y la prima neta será igual a la prima neta de la póliza menos el monto pagado dividido por el factor 1,19 (1.00 + IVA).
• Endoso de rehabilitación (RH): Informa los valores de datos y/o parámetros con que se rehabilita el
contrato de seguro por haber desaparecido las causas que originaron su cancelación.
• Endoso de resiembra (RS): Informa los datos y parámetros con que se aplica la cobertura original a
la superficie resembrada.
## 2. Consideraciones generales.
a) Nombre propio y Razón Social del beneficiario: En caso de persona natural, el nombre, apellido paterno y
apellido materno deberán ser informados en los campos designados para estos efectos. Si se trata de una persona jurídica, la Razón Social deberá llenarse en el campo correspondiente al nombre y los campos de apellidos tanto paterno como materno deberán llenarse con espacios ó blancos.
b) Registros de largo fijo: Todos los registros, independientemente del tipo que se trate, deben tener 269
caracteres de largo.
c) Ausencia de antecedentes: El hecho de no haber emitido pólizas o endosos durante un mes, no exime a la
compañía de la obligación de enviar el archivo de producción a esta Superintendencia. En dicho caso, este sólo debe contener los registros tipo 1 y tipo 9.
d) Calibres: La suma de los porcentajes señalados en los campos PROD_CAL en el ANEXO 2: PRODUCCION,
debe sumar 100.
## 3. Contenido de los archivos Paaaamm.txt
En estos archivos se encuentran distintos registros, cuyos contenidos son los siguientes:
Registro tipo 1: identificación de la compañía de seguros Datos para la identificación de la Compañía: RUT, razón social y el período a que se refiere la información.
Sólo se deberá informar un registro de este tipo y deberá ser el primero del archivo.

Registro tipo 2: información de cabecera por póliza (P) ó endoso (E) Cada registro representa una póliza (ó endoso) y contiene antecedentes comunes a todos los ítems de la póliza (ó endoso), tal como: tipo y número de documento, moneda, fechas de vigencias, identificación del beneficiario y la prima fija. El monto asegurado y la prima variable serán la suma de los valores del mismo nombre de cada uno de los ítems que comprende la póliza (ó endoso).
Registro tipo 3: información de detalle de la póliza (P) ó endoso (E) correspondiente a Cultivos Anuales por Sistema de Rendimiento.
Cada registro representa un ítem de la póliza (ó endoso) y contiene antecedentes sobre éste, tal como:
número de ítem, comuna, producto agrícola, nivel de cobertura, unidad física, datos del terreno, rendimiento, precio, monto asegurado, tasa, prima variable, etc.
Registro tipo 4: información de detalle de la póliza (P) ó endoso (E) correspondiente a Frutales por Sistema de Daños.
Cada registro representa un ítem de la póliza (ó endoso) y contiene antecedentes de cada ítem de la póliza o del endoso, tal como: número de ítem, comuna, producto agrícola, nivel de cobertura, unidad física, datos del terreno, monto asegurado, tasa, prima variable, etc.
Registro tipo 5: información de detalle de la póliza (P) ó endoso (E) correspondiente a Frutales por Sistema de Rendimiento.
Cada registro representa un ítem de la póliza (ó endoso) y contiene antecedentes de cada ítem de la póliza o del endoso, tal como: número de ítem, comuna, producto agrícola, nivel de cobertura, unidad física, datos del terreno, rendimiento, precio por calibres, monto asegurado, tasa, prima variable, etc.
Registro tipo 9: total registros Datos de control del contenido del archivo. Se indicará el número total de registros informados. Sólo se deberá informar un registro de este tipo y deberá ser el último del archivo.
Notas importante sobre consistencia de registros:
• El número de pólizas no deberá repetirse en los registros tipo 2.
• Por cada registro tipo 2 deberá haber uno o más registros del tipo 3 ó 4 ó 5.
• El número de póliza de cada registro tipo 2 deberá encontrarse solo en uno de los registros tipo 3, ó 4
ó 5.
Nota sobre la construcción de endosos de aumento (A) y disminución (D).
a) Cuando se trate de endosos de aumento o de disminución, y sólo para dar cuenta de variaciones que
afecte a uno o más ítems de una misma póliza en cuanto a su: cobertura, rendimiento, precio(s) o tasa, esta circunstancia se informará para cada ítem en dos registros que se individualizan en el campo movimiento y que se definen de la siguiente manera:
• Movimiento 1: Su efecto es dejar en cero (0) los valores de la producción asegurada, monto y
prima neta. Es decir, restados los valores de los campos homónimos de la póliza (actualizada) el saldo debe ser cero (0). El campo movimiento se llenará con un uno (1).
• Movimiento 2: Su efecto es dejar los valores finales de la producción asegurada, monto
asegurado y prima neta. Es decir, el contenido en estos campos será el resultado de aplicar el nuevo valor en cobertura y/o calibres y/o precios y/o tasa. El campo movimiento se llenará con un dos (2).
b) Cuando se trate de endosos tipo (A) ó (D), y sólo para dar cuenta de una variación en la superficie
asegurada, y/o de la inclusión o exclusión de un ítem, esta situación se informará en un solo registro, y el campo movimiento se llenará con un cero (0). Igual cosa se hará cuando se trate de endosos de cancelación (C), endosos de cancelación anticipada (CA), endosos de rehabilitación (RH) ó endosos de resiembra (RS).
c) Los valores de monto asegurado y prima en el registro tipo 2 debe ser la resta entre el movimiento 2 y el
movimiento 1. El signo del resultado debe ser consistente con el tipo de endoso señalado en ambos registros. Es decir, si la diferencia es negativa, el endoso debe ser de tipo D y si es positiva, el endoso debe ser de tipo A.
d) Cuando se trate de póliza (P) el campo movimiento será informado en (0).

Registro tipo 1: IDEN TIFICACION DE LA COMPAÑÍA DE SEGUROS.

| CAMPO | DESCRIPCION | FORMATO | POSICION |
| --- | --- | --- | --- |
| TIPO_REGISTRO | Debe tener valor “1”. | 9(01) | 1- 1 |
| FECHA_CIERRE | Fecha de cierre de la información. Formato AAAAMMDD. | 9(08) | 2 -9 |
| RUT_ASEGURADORA | Número RUT de la Aseguradora. | 9(09) | 10 – 18 |
| VER_ASEGURADORA | Dígito verificador del RUT. | X(01) | 19 – 19 |
| ASEGURADORA | Razón Social de la Aseguradora, en letras mayúsculas. | X(80) | 20 – 99 |
| FILLER | Sólo se deben grabar espacios. | X(170) | 100 – 269 |

Registro tipo 2: INFORMACION POR POLIZA/ENDOSO

| CAMPO | DESCRIPCION | FORMATO | POSICION |
| --- | --- | --- | --- |
| TIPO_REGISTRO | Debe tener valor “2”. | 9(01) | 1 – 1 |
| TIPO_DOCUMENTO | Corresponde al tipo de documento que contiene el registro. P: Póliza E: Endoso. | X(01) | 2 – 2 |
| POLIZA | Número único del contrato de seguro. | X(15) | 3 – 17 |
| TIPO_ENDOSO | Si tipo de documento es E, los valores aceptados son: A, D, C, RS, RH y CA Si tipo de documento es P, se indica con una Z. | X(02) | 18 – 19 |
| ENDOSO | Es un número correlativo dentro del número de la póliza. Si tipo de documento es E, se indica el número correlativo. Si tipo de documento es P, se indica con un cero (0) | X(11) | 20 – 30 |
| MONEDA | Sigla de la moneda en que se emitió el contrato de seguro. Siglas aceptadas: UF para Unidad de Fomento y UD unidad dólar. | X(02) | 31 – 32 |
| VIGENCIA_INICIAL | Fecha de inicio de vigencia del contrato de seguro. Formato: AAAAMMDD. | 9(08) | 33 – 40 |
| VIGENCIA_FINAL | Fecha de término de vigencia del contrato de seguro. Formato: AAAAMMDD. | 9(08) | 41 – 48 |
| EMISION | Fecha de emisión del contrato de seguro. Formato: AAAAMMDD. | 9(08) | 49 – 56 |
| POLIZA_SVS | Código con el cual la póliza se encuentra en el depósito de pólizas de la SVS que rigen el contrato de seguro. | X(09) | 57 – 65 |
| NUMERO_PROPUESTA | Número único que identifica la propuesta y único para cada Póliza. | X(15) | 66 – 80 |
| FECHA_PROPUESTA | Corresponde a la fecha establecida en la propuesta de seguro. Formato AAAAMMDD. | 9(08) | 81 – 88 |
| RUT_BENEFICIARIO | RUT de la persona natural o jurídica del beneficiario. | 9(09) | 89 – 97 |
| VER_ BENEFICIARIO | Dígito verificador del RUT del beneficiario. | X(01) | 98 – 98 |
| NOMBRE_ BENEFICIARIO | Nombre de la persona natural o razón social de la persona jurídica beneficiaria del seguro, en mayúsculas. | X(80) | 99 – 178 |
| AP_ BENEFICIARIO | Apellido paterno del beneficiario, en mayúsculas. Debe llenarse con blancos si es persona jurídica. | X(20) | 179 – 198 |

| AM_ BENEFICIARIO | Apellido materno del beneficiario, en mayúsculas. Debe llenarse con blancos o espacios si es persona jurídica. | X(20) | 199 – 218 |
| --- | --- | --- | --- |
| CANTIDAD_ITEMS | Corresponde a la cantidad de ítems con igual número de póliza que se informan en los registros tipo 3 ó 4 ó 5. | 9(02) | 219 - 220 |
| SUPERFICIE | Corresponde a la suma de superficie en hectáreas señalada en los ítems de igual número de póliza que se informan en los registros tipo 3 ó 4 ó 5. | 9(06)9(04) | 221 – 230 |
| MONTO_ASEGURADO | Corresponde a la suma del monto asegurado señalado en los ítems de igual número de póliza y que se informan en los registros tipo 3 ó 4 ó 5. | 9(09)v9(02) | 231 – 241 |
| PRIMA_VARIABLE | Corresponde a la suma de la prima variable señalada en los ítems de igual número de póliza y que se informan en los registros tipo 3 ó 4 ó 5. | 9(09)v9(02) | 242 – 252 |
| PRIMA_FIJA | Corresponde al valor señalado en la póliza. | 9(04)v9(02) | 253 – 258 |
| PRIMA_NETA | Correspondiente a la suma del campo PRIMA_VARIABLE más PRIMA_FIJA. | 9(09)v9(02) | 259 – 269 |

Registro tipo 3: INFORMACION DE DETALLE/ITEM POLIZA/ENDOSO CULTIVOS ANUALES

| CAMPO | DESCRIPCION | FORMATO | POSICION |
| --- | --- | --- | --- |
| TIPO_REGISTRO | Debe tener valor “3”. | 9(01) | 1 – 1 |
| TIPO_DOCUMENTO | Corresponde al TIPO_DOCUMENTO señalado en el registro tipo 2 con igual número de POLIZA. | X(01) | 2 – 2 |
| POLIZA | Número único del contrato de seguro. | X(15) | 3 – 17 |
| TIPO_ENDOSO | Corresponde al TIPO_ENDOSO señalado en el registro tipo 2 con igual número de POLIZA. | X(02) | 18 – 19 |
| ENDOSO | Corresponde al ENDOSO señalado en el registro tipo 2 con igual número de POLIZA. | X(11) | 20 – 30 |
| MOVIMIENTO | Corresponde a un número ordinal que permite identificar registros con información diferente en casos de endosos. Valores aceptados son: 0, 1 y 2. Ver punto 3 de este anexo. | 9(01) | 31 – 31 |
| ITEM | Corresponde a un número ordinal único y correlativo que parte con el 1 y que sirve para identificar el ítem asegurado, si se trata de una póliza (P) o para individualizar el ítem a ser modificado, si se trata de un endoso (E). | 9(02) | 32 – 33 |
| ID_COMUNA | Código de Comuna en que se encuentra la materia asegurada objeto del contrato informado. Códigos permitidos en el módulo SEIL, codificación SVS Seguro Agrícola. | X(12) | 34 – 45 |

| UNIDAD | Sigla de la unidad física de medida del cultivo asegurado en el contrato de informado. Códigos permitidos en el módulo SEIL, codificación SVS, Seguro Agrícola. | X(05) | 46 – 50 |
| --- | --- | --- | --- |
| COBERTURA | Parte de la producción esperada cubierta en el contrato de seguro. Valores posibles se señalan en las Normas de Suscripción vigente. | 9(03)v9(02) | 51 – 55 |
| ID_PRODUCTO | Código que permite identificar el producto agrícola asegurado en el contrato informado. Códigos permitidos en el módulo SEIL de la SVS, codificación SVS, Seguro Agrícola. | X(12) | 56 – 67 |
| RIEGO | Código que hace referencia a la condición de riego del producto agrícola asegurado. Códigos permitidos en el módulo SEIL, codificación SVS, Seguro Agrícola. | X(04) | 68 – 71 |
| RELIEVE | Código que hace referencia a la condición del terreno en el que se encuentra el producto agrícola asegurado. Códigos permitidos en el módulo SEIL, codificación SVS, Seguro Agrícola. | X(03) | 72 – 74 |
| SUPERFICIE | Superficie en hectáreas que contiene el producto agrícola asegurado e identificado bajo este ITEM. | 9(06)9(04) | 75 – 84 |
| REND_ASEGURADO | Producción asegurada por hectárea para este ítem, señalada en el contrato de seguro. | 9(10)v9(02) | 85 – 96 |
| PRECIO | Precio por unidad física para la producción agrícola de este ítem. | 9(06)v9(04) | 97 – 106 |
| MONTO_ASEGURADO | Valor del monto asegurado para este ítem señalado en el contrato de seguro. | 9(09)v9(02) | 107 – 117 |
| TASA | Tasa prima correspondiente al producto agrícola señalada en el contrato de seguro, para este ítem. | 9(02)v9(02) | 118 – 121 |
| PRIMA_VARIABLE | Monto asegurado multiplicado por la tasa, para este ítem. | 9(09)v9(02) | 122 – 132 |
| FILLER | Sólo se deben grabar espacios. | X(137) | 133 – 269 |

Registro tipo 4: INFORMACION DE DETALLE/ITEM POLIZA/ENDOSO FRUTALES (PALTOS Y ARANDANOS)

| CAMPO | DESCRIPCION | FORMATO | POSICION |
| --- | --- | --- | --- |
| TIPO_REGISTRO | Debe tener valor “4”. | 9(01) | 1 – 1 |
| TIPO_DOCUMENTO | Corresponde al TIPO_DOCUMENTO señalado en el registro tipo 2 con igual número de POLIZA. | X(01) | 2 – 2 |
| POLIZA | Número único del contrato de seguro. | X(15) | 3 – 17 |
| TIPO_ENDOSO | Corresponde al TIPO_ENDOSO señalado en el registro tipo 2 con igual número de POLIZA. | X(02) | 18 – 19 |
| ENDOSO | Corresponde al ENDOSO señalado en el registro tipo 2 con igual número de POLIZA. | X(11) | 20 – 30 |

| MOVIMIENTO | Corresponde a un número ordinal que permite identificar registros con información diferente en casos de endosos. Valores aceptados son: 0, 1 y 2. Ver punto 3 de este documento. | 9(01) | 31 – 31 |
| --- | --- | --- | --- |
| ITEM | Corresponde a un número ordinal único y correlativo que parte con el 1 y que sirve para identificar el ítem asegurado, si se trata de una póliza (P) o para individualizar el ítem a ser modificado, si se trata de un endoso (E). | 9(02) | 32 – 33 |
| ID_COMUNA | Código de Comuna en que se encuentra la materia asegurada objeto del contrato informado. Códigos permitidos en el módulo SEIL, codificación SVS Seguro Agrícola. | X(12) | 34 – 45 |
| UNIDAD | Sigla de la unidad física de medida del cultivo asegurado en el contrato de informado. Códigos permitidos en el módulo SEIL, codificación SVS, Seguro Agrícola. | X(05) | 46 – 50 |
| COBERTURA | Parte de la producción esperada cubierta en el contrato de seguro. Valores posibles se señalan en las Normas de Suscripción vigente. | 9(03)v9(02) | 51 – 55 |
| ID_PRODUCTO | Código que permite identificar el producto agrícola asegurado en el contrato informado. Códigos permitidos en el módulo SEIL de la SVS, codificación SVS, Seguro Agrícola. | X(12) | 56 – 67 |
| RIEGO | Código que hace referencia a la condición de riego del producto agrícola asegurado. Códigos permitidos en el módulo SEIL, codificación SVS, Seguro Agrícola. | X(04) | 68 – 71 |
| RELIEVE | Código que hace referencia a la condición del terreno en el que se encuentra el producto agrícola asegurado. Códigos permitidos en el módulo SEIL, codificación SVS, Seguro Agrícola. | X(03) | 72 – 74 |
| SUPERFICIE | Superficie en hectáreas que contiene el producto agrícola asegurado e identificado bajo este ITEM. | 9(06)9(04) | 75 – 84 |
| MONTO_ASEGURADO | Valor del monto asegurado para este ítem señalado en el contrato de seguro. | 9(09)v9(02) | 85 – 95 |
| TASA | Tasa prima correspondiente al producto agrícola señalada en el contrato de seguro, para este ítem. | 9(02)v9(02) | 96 – 99 |
| PRIMA_VARIABLE | Monto asegurado multiplicado por la tasa, para este ítem. | 9(09)v9(02) | 100 – 110 |
| FILLER | Sólo se deben grabar espacios. | X(159) | 111 – 269 |

Registro tipo 5: INFORMACION DE DETALLE/ITEM POLIZA/ENDOSO FRUTALES (VIDES Y MANZANOS)

| CAMPO | DESCRIPCION | FORMATO | POSICION |
| --- | --- | --- | --- |
| TIPO_REGISTRO | Debe tener valor “5”. | 9(01) | 1 – 1 |

| TIPO_DOCUMENTO | Corresponde al TIPO_DOCUMENTO señalado en el registro tipo 2 con igual número de POLIZA. | X(01) | 2 – 2 |
| --- | --- | --- | --- |
| POLIZA | Número único del contrato de seguro. | X(15) | 3 – 17 |
| TIPO_ENDOSO | Corresponde al TIPO_ENDOSO señalado en el registro tipo 2 con igual número de POLIZA. | X(02) | 18 – 19 |
| ENDOSO | Corresponde al ENDOSO señalado en el registro tipo 2 con igual número de POLIZA. | X(11) | 20 – 30 |
| MOVIMIENTO | Corresponde a un número ordinal que permite identificar registros con información diferente en casos de endosos. Valores aceptados son: 0, 1 y 2. Ver punto 3 de este documento. | 9(01) | 31 – 31 |
| ITEM | Corresponde a un número ordinal único y correlativo que parte con el 1 y que sirve para identificar el ítem asegurado, si se trata de una póliza (P) o para individualizar el ítem a ser modificado, si se trata de un endoso (E). | 9(02) | 32 – 33 |
| ID_COMUNA | Código de Comuna en que se encuentra la materia asegurada objeto del contrato informado. Códigos permitidos en el módulo SEIL, codificación SVS Seguro Agrícola. | X(12) | 34 – 45 |
| UNIDAD | Sigla de la unidad física de medida del cultivo asegurado en el contrato de informado. Códigos permitidos en el módulo SEIL, codificación SVS, Seguro Agrícola. | X(05) | 46 – 50 |
| COBERTURA | Parte de la producción esperada cubierta en el contrato de seguro. Valores posibles se señalan en las Normas de Suscripción vigente. | 9(03)v9(02) | 51 – 55 |
| ID_PRODUCTO | Código que permite identificar el producto agrícola asegurado en el contrato informado. Códigos permitidos en el módulo SEIL de la SVS, codificación SVS, Seguro Agrícola. | X(12) | 56 – 67 |
| RIEGO | Código que hace referencia a la condición de riego del producto agrícola asegurado. Códigos permitidos en el módulo SEIL, codificación SVS, Seguro Agrícola. | X(04) | 68 – 71 |
| RELIEVE | Código que hace referencia a la condición del terreno en el que se encuentra el producto agrícola asegurado. Códigos permitidos en el módulo SEIL, codificación SVS, Seguro Agrícola. | X(03) | 72 – 74 |
| SUPERFICIE | Superficie en hectáreas que contiene el producto agrícola asegurado e identificado bajo este ITEM. | 9(06)9(04) | 75 – 84 |
| REND_ESPERADO | Producción esperada por hectárea para este ítem, señalada en el contrato de seguro. | 9(10)v9(02) | 85 – 96 |

| REND_ASEGURADO | Producción asegurada por hectárea para este ítem, señalada en el contrato de seguro. | 9(10)v9(02) | 97– 108 |
| --- | --- | --- | --- |
| PROD_CAL_E1 | Porcentaje de la producción física asegurada que se espera obtener en la superficie de este ítem para este calibre de exportación. Debe ser mayor que cero (0) y menor ó igual a cien (100). | 9(3)v9(02) | 109 – 113 |
| PROD_CAL_E2 | Porcentaje de la producción física asegurada que se espera obtener en la superficie de este ítem para este calibre de exportación. Si hay producción para este calibre, debe ser mayor a cero (0) y menor a cien (100). Si no hay producción para este calibre, se llena con ceros (0) | 9(3)v9(02) | 114 – 118 |
| PROD_CAL_E3 | Porcentaje de la producción física asegurada que se espera obtener en la superficie de este ítem para este calibre de exportación. Si hay producción para este calibre, debe ser mayor a cero (0) y menor a cien (100). Si no hay producción para este calibre, se llena con ceros (0) | 9(3)v9(02) | 119 – 123 |
| PROD_CAL_E4 | Porcentaje de la producción física asegurada que se espera obtener en la superficie de este ítem para este calibre de exportación. Si hay producción para este calibre, debe ser mayor a cero (0) y menor a cien (100). Si no hay producción para este calibre, se llena con ceros (0) | 9(3)v9(02) | 124 – 128 |
| PROD_CAL_E5 | Porcentaje de la producción física asegurada que se espera obtener en la superficie de este ítem para este calibre de exportación. Si hay producción para este calibre, debe ser mayor a cero (0) y menor a cien (100). Si no hay producción para este calibre, se llena con ceros (0) | 9(3)v9(02) | 129 – 133 |
| PROD_CAL_N1 | Porcentaje de la producción física asegurada que se espera obtener en la superficie de este ítem para este calibre para consumo país. Si hay producción para este calibre, debe ser mayor a cero (0) y menor a cien (100). Si no hay producción para este calibre, se llena con ceros (0) | 9(3)v9(02) | 134 – 138 |
| PROD_CAL_N2 | Porcentaje de la producción física asegurada que se espera obtener en la superficie de este ítem para este calibre para consumo país. Si hay producción para este calibre, debe ser mayor a cero (0) y menor a cien (100). Si no hay producción para este calibre, se llena con ceros (0) | 9(3)v9(02) | 139 – 143 |
| PRECIO_CAL_E1 | Precio por unidad física para la producción agrícola de este ítem asignada a este calibre de exportación. Debe ser el valor especificado en la póliza. | 9(06)v9(04) | 144 – 153 |

| PRECIO_CAL_E2 | Precio por unidad física para la producción agrícola de este ítem asignada a este calibre de exportación. Si no hay producción para este calibre, su valor es cero (0). | 9(06)v9(04) | 154 – 163 |
| --- | --- | --- | --- |
| PRECIO_CAL_E3 | Precio por unidad física para la producción agrícola de este ítem asignada a este calibre de exportación. Si no hay producción para este calibre, su valor es cero (0). | 9(06)v9(04) | 164 – 173 |
| PRECIO_CAL_E4 | Precio por unidad física para la producción agrícola de este ítem asignada a este calibre de exportación. Si no hay producción para este calibre, su valor es cero (0). | 9(06)v9(04) | 174 – 183 |
| PRECIO_CAL_E5 | Precio por unidad física para la producción agrícola de este ítem asignada a este calibre de exportación. Si no hay producción para este calibre, su valor es cero (0). | 9(06)v9(04) | 184 – 193 |
| PRECIO_CAL_N1 | Precio por unidad física para la producción agrícola de este ítem asignada a este calibre para consumo país. Debe ser el valor especificado en la póliza. | 9(06)v9(04) | 194 – 203 |
| PRECIO_CAL_N2 | Precio por unidad física para la producción agrícola de este ítem asignada a este calibre para consumo país. Si no hay producción para este calibre, su valor es cero (0). | 9(06)v9(04) | 204 – 213 |
| MONTO_ASEGURADO | Valor del monto asegurado para este ítem señalado en el contrato de seguro. | 9(09)v9(02) | 214 – 224 |
| TASA | Tasa prima correspondiente al producto agrícola señalada en el contrato de seguro, para este ítem. | 9(02)v9(02) | 225 – 228 |
| PRIMA_VARIABLE | Monto asegurado multiplicado por la tasa, para este ítem. | 9(09)v9(02) | 229 – 239 |
| FILLER | Sólo se deben grabar espacios. | X(30) | 240– 269 |

Registro tipo 9: TOTAL REGISTROS

| CAMPO | DESCRIPCION | FORMATO | POSICION |
| --- | --- | --- | --- |
| TIPO_REGISTRO | Debe tener valor “9”. | 9(01) | 1 – 1 |
| TOTAL_REGISTROS | Número total de registros informados en el archivo. Esto es, suma de la cantidad de registros tipo 1, 2, 3 y 4. | 9(08) | 2 – 9 |
| FILLER | Sólo se deben grabar espacios. | X(260) | 10 – 269 |

## ANEXO Nº 3 REGISTRO DE DENUNCIAS DE SINIESTROS
## 1. Definiciones
Para los efectos de esta circular, se entenderá por:
a) Denuncia de siniestro (D): El conjunto de antecedentes que dan cuenta del aviso de denuncia de siniestro
efectuado por el asegurado, recibida por la compañía aseguradora y reconocida por ésta como cierta, según se señala en el punto 4 más abajo.
b) Riesgo: Fenómeno climático señalado en el contrato de seguro, que causa daño a un cultivo, afectando su
producción y o calidad ocasionando pérdidas económicas. Se ha de tener presente que en un evento pueden concurrir más de un fenómeno climático, y que un cultivo puede sufrir más de un evento en el período de cobertura.
## 2. Consideraciones generales
a) Registros de largo fijo: Todos los registros, independientemente del tipo que se trate, deben tener 99
caracteres de largo.
b) Existencia previa: Para informar la denuncia de un siniestro, es necesario que exista la póliza correspondiente
y ésta no se encuentre cancelada o anulada.
c) Ausencia de antecedentes: Si durante el período a informar no hubiese denuncias de siniestros, la compañía
debe enviar el archivo de denuncias con los registros tipo 1 y tipo 3 a esta Superintendencia.
## 3. Contenido de los archivos Daaaamm.txt
Registro tipo 1: identificación de la compañía de seguros Datos para la identificación de la Compañía: RUT, razón social y el período a que se refiere la información.
Sólo se deberá informar un registro de este tipo y deberá ser el primero del archivo.
Registro tipo 2: denuncias de siniestros Datos contenidos en el documento de denuncia de siniestro registrado por la compañía.
Registro tipo 3: total registros Datos de control del contenido del archivo. Se indicará el número total de registros informados. Sólo se deberá informar un registro de este tipo y deberá ser el último del archivo.
## 4. Formato de cada tipo de registro
Registro tipo 1: IDENTIFICACIÓN DE LA COMPAÑÍA DE SEGUROS

| CAMPO | DESCRIPCION | FORMATO | POSICION |
| --- | --- | --- | --- |
| TIPO_REGISTRO | Debe tener valor “1”. | 9(01) | 1 – 1 |
| FECHA_CIERRE | Fecha de cierre de la información. Formato AAAAMMDD | 9(08) | 2 – 9 |
| RUT_ASEGURADORA | Número del RUT de la Aseguradora que informa.. | 9(09) | 10 – 18 |
| VER_ASEGURADORA | Dígito verificador del RUT. | X(01) | 19 – 19 |
| ASEGURADORA | Razón Social de la Aseguradora que informa, en mayúsculas. | X(80) | 20 – 99 |

Registro tipo 2: DENUNCIAS DE SINIESTROS

| CAMPO | DESCRIPCION | FORMATO | POSICION |
| --- | --- | --- | --- |
| TIPO_REGISTRO | Debe tener valor “2”. | 9(01) | 1 – 1 |

| SINIESTRO | Número único con que la aseguradora identifica el siniestro. | X(15) | 2 – 16 |
| --- | --- | --- | --- |
| POLIZA | Número del contrato de seguro afectado por el siniestro. | X(15) | 17-31 |
| FECHA_DENUNCIA | Fecha del documento de denuncia de siniestro. Formato AAAAMMDD | 9(08) | 32– 39 |
| FECHA_OCURRENCIA | Fecha de ocurrencia del siniestro señalada en la denuncia. Formato AAAAMMDD | 9(08) | 40 – 47 |
| RIESGO | Código del evento climático que da origen a esta denuncia. Este código se forma con un 1 en una o más de las posiciones que indica la siguiente tabla 1: Sequía agrícola 2: Lluvia excesiva/extemporánea 3: Helada 4: Granizo 5: Nieve 6: Viento perjudicial Las posiciones no usadas se completan con 0. | X(06) | 48 –53 |
| FILLER | Sólo se deben grabar espacios. | X(46) | 54 – 99 |

Registro tipo 3: TOTAL REGISTROS

| CAMPO | DESCRIPCION | FORMATO | POSICION |
| --- | --- | --- | --- |
| TIPO_REGISTRO | Debe tener valor “3”. | 9(01) | 1 – 1 |
| TOTAL_REGISTROS | Número total de registros informados en el archivo. Esto es, suma de la cantidad de registros tipo 1, 2 y 3. | 9(08) | 2 – 9 |
| FILLER | Sólo se deben grabar espacios. | X(90) | 10 – 99 |

## ANEXO Nº 4 REGISTRO DE LIQUIDACIONES TERMINADAS.
## 1. Definiciones.
Para los efectos de esta circular, se entenderá por:
a) Informe de liquidación: Corresponde al documento emitido por el Liquidador de Seguros ó la Compañía
en el que se establece, entre otras cosas, la procedencia o improcedencia del siniestro denunciado, de la cobertura; la determinación de las pérdidas y el monto de la indemnización sugerida, todo de acuerdo a lo establecido en la normativa y en particular en el contrato de seguro.
b) Reapertura: Son datos complementarios a un siniestro ya informado. Esto se hará con un nuevo registro,
denominado reapertura, con igual estructura al del Informe de liquidación anterior. Contendrá los valores actuales del siniestro, es decir, sus datos deberán reemplazar al informado anteriormente. El registro con el siniestro informado originalmente tendrá en el campo reapertura un valor (0), y la o las reaperturas siguientes un número correlativo dentro del número de siniestro partiendo con un (1).
c) Estado: Los informes de liquidación terminados pueden presentar sólo uno de los siguientes tres estados:
• ACI: Aceptados Con Indemnización bajo las siguientes circunstancias:
(cid:190) CI: Costos incurridos.
(cid:190) PIRD: Pérdida indemnizable por variación de rendimiento ó daños.
(cid:190) PIRC: Pérdida indemnizable por variación de rendimiento y calidad.
• ASI: Aceptados Sin Indemnización. En esta categoría se encuentran los informes que, si bien el
siniestro fue aceptado no hubo opción a indemnización debido a una de las siguientes
circunstancias:
(cid:190) DDA: Desistimiento del asegurado,
(cid:190) PNI: Pérdida no indemnizable.
• RSI: Declaraciones de siniestros que no fueron aceptadas o acogidas a trámite debido a una de
las siguientes circunstancias:
(cid:190) IDO: Incumplimiento de obligaciones por parte del asegurado.
(cid:190) OTR: Otras causas.
d) Riesgo: Fenómeno o evento climático señalado en el contrato de seguro, que causa daño a un cultivo,
afectando su producción ocasionando pérdidas económicas. Se ha de tener presente que en un evento pueden concurrir más de un fenómeno climático, y que un cultivo puede sufrir más de un evento en el período de cobertura.
## 2. Consideraciones generales.
a) Existencia previa de denuncia: Para informar un siniestro es necesario haber previamente informado su
denuncia, deberá conservar el mismo número de siniestro y de póliza.
b) Existencia previa de siniestro: Para informar la reapertura de un siniestro, es necesario que éste haya sido
previamente informado.
c) Registros de largo fijo: Todos los registros, independientemente del tipo que se trate, deben tener 130
caracteres de largo.
d) Ausencia de antecedentes: Si durante el período a informar no hubiese liquidaciones de siniestros terminadas
(o reaperturas), la compañía debe enviar el archivo de siniestros con los registros tipo 1 y tipo 3 a esta Superintendencia.
## 3. Contenido de los archivos Laaaamm.txt
Registro tipo 1: identificación de la compañía de seguros Datos para la identificación de la Compañía: RUT, razón social y el período a que se refiere la información.
Sólo se deberá informar un registro de este tipo y deberá ser el primero del archivo.

Registro tipo 2: información por liquidación de siniestro informado Este registro contiene antecedentes de carácter general del informe de liquidación y que se señala en el punto 4 de este anexo, tal como: Número de siniestro y numero de póliza afectada, fechas del informe y ocurrencia del siniestro, estado y su descripción, monto indemnizable, deducible, gastos de siniestro e identificación del liquidador de seguro.
Registro tipo 3: total registros Datos de control del contenido del archivo. Se indicará el número total de registros informados. Sólo se deberá informar un registro de este tipo y deberá ser el último del archivo.
## 4. Reglas de consistencia.
Clasificación de siniestros terminados y reglas de consistencia aplicables a la liquidación de siniestros terminados.

| CONDICION DEL SINIESTRO |  | REGLAS DE CONSISTENCIA |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Estado | Descripción | SUPERFICIE | PRODUCCION REAL | GASTOS | INDEMNIZACION |
| Aceptado con indemnización (ACI) | • Costo incurrido (CI) | = 0 | = 0 | > 0 | 0 < I <= MA |
|  | • Pérdida indemnizable (PIRD) por variación de rendimiento o daños. | > 0 (1) | 0 < PR(2) < PA | > 0 | 0 < I <= MA |
|  | • Pérdida indemnizable (PIRC) por variación de rendimiento y calidad | > 0 (1) | 0 < PR(2) | > 0 | 0 < I <= MA |
| Aceptado sin indemnización (ASI) | • Desistimiento del asegurado (DDA) | = 0 | = 0 | > 0 | = 0 |
|  | • Pérdida no indemnizable (PNI) | = 0 | 0 <= PR | > 0 | = 0 |
| Rechazado sin indemnización (RSI) | • Incumplimiento de obligaciones (IDO) • Otros (OTR) | = 0 | = 0 | >= 0 | = 0 |

| Sigla | Descripción |
| --- | --- |
| MA | Monto asegurado |
| I | Indemnización |
| PR | Producción real |
| PA | Producción asegurada |
| CI | Costo directo incurrido |
| PI | Pérdida de producción indemnizable a uno o más riesgos cubiertos con derecho a indemnización. |
| DDA | Desistimiento del asegurado por cualquier motivo. |
| PNI | Pérdida de producción no indemnizable debido a: Producción real mayor a la asegurada, sin daño en primera inspección, otros. |
| IDO | Incumplimiento de obligaciones, tal como: Denuncia fuera de plazo, Sin denuncia, Riesgo declarado no cubierto, Riesgo fuera de vigencia, Riesgo no cubierto o inexistente, Cambio de condiciones originales, Manejo inadecuado, otros. |
| OTR | Motivos o circunstancias que no dan origen a un informe de liquidación. |

Notas:
• (1) Corresponde a la superficie asegurada, considerando una tolerancia de ±10% por medición defectuosa
o imprecisa.

• (2) Es la producción que corresponde a la superficie asegurada, después de hacer ajustes por infraseguro o
sobreseguro, si corresponde. Para el caso de pérdidas por rendimiento y calidad, se considerará una tolerancia de +15% para recoger la eventual medición defectuosa o imprecisa.
## 5. Formato de cada tipo de registro
Registro tipo 1: IDENTIFICACIÓN DE LA COMPAÑÍA DE SEGUROS

| CAMPO | DESCRIPCION | FORMATO | POSICION |
| --- | --- | --- | --- |
| TIPO_REGISTRO | Debe tener valor “1”. | 9(01) | 1 – 1 |
| FECHA_CIERRE | Fecha de cierre de la información. Formato AAAAMMDD | 9(08) | 2 – 9 |
| RUT_ASEGURADORA | Número del RUT de la Aseguradora que informa. | 9(09) | 10 – 18 |
| VER_ASEGURADORA | Dígito verificador del RUT. | X(01) | 19 – 19 |
| ASEGURADORA | Razón Social de la Aseguradora que informa, en mayúsculas. | X(80) | 20 – 99 |
| FILLER | Sólo se deben grabar espacios | X(31) | 100 – 130 |

Registro tipo 2: INFORMACION POR SINIESTRO

| CAMPO | DESCRIPCION | FORMATO | POSICION |
| --- | --- | --- | --- |
| TIPO_REGISTRO | Debe tener valor “2”. | 9(01) | 1 – 1 |
| SINIESTRO | Número único con que la Compañía identifica el siniestro. | X(15) | 2 – 16 |
| REAPERTURA | Número único con que identifica al envío del informe original y sus posteriores modificaciones. El primer informe se informará con 00 y los siguientes con 01, 02, etc. | X(02) | 17 – 18 |
| POLIZA | Número del contrato de seguro afectado por el siniestro. | X(15) | 19 – 33 |
| FECHA_INFORME | Fecha del informe de liquidación. Formato AAAAMMDD. | 9(08) | 34 – 41 |
| FECHA_OCURRENCIA | Fecha comprobada de ocurrencia del siniestro. Formato AAAAMMDD. | 9(08) | 42 – 49 |
| RIESGO | Para ESTADO de siniestro ACI ó ASI, el código causa de siniestro se señala con un (1) en la posición que indica la siguiente tabla. Las posiciones no usadas se completan con (0). 1: Sequía agrícola 2: Lluvia excesiva/extemporánea 3: Helada 4: Granizo 5: Nieve 6: Viento perjudicial Para estado de siniestro RSI, el campo se informa con (000000) | X(06) | 50 – 55 |
| ESTADO | Se indicará uno de los tres estados ACI: Siniestro aceptado con indemnización. ASI: Siniestro aceptado sin indemnización. RSI: Siniestro rechazado sin indemnización. | X(03) | 56 – 58 |
| DESCRIPCION | Valores permitidos Para ESTADO = ACI: CI, PIRD ó PIRC Para ESTADO = ASI: DDA o PNI Para ESTADO = RSI: IDO ó OTR Ver punto 4) reglas de Consistencia Anexo N°4. | X(04) | 59 – 62 |

| SUPERFICIE | Corresponde a la superficie señalada en el Informe de Liquidación de este siniestro. | 9(06)v9(04) | 63 – 72 |
| --- | --- | --- | --- |
| PRODUCCION_REAL | Corresponde a la producción real señalada en el Informe de Liquidación de este siniestro. | 9(10)v9(02) | 73 – 84 |
| GASTOS | Corresponde a los gastos directos imputables a este siniestro, expresados en UF. | 9(10)v9(02) | 85 –96 |
| INDEMNIZACION | Corresponde a la indemnización señalada en el Informe de Liquidación de este siniestro. | 9(10)v9(02) | 97 – 108 |
| DEDUCIBLE | Corresponde al deducible señalado en el Informe de Liquidación de este siniestro. | 9(10)v9(02) | 109 – 120 |
| RUT_LIQUIDADOR | RUT del Liquidador de Seguros. Si fuese la Compañía, informar su RUT | 9(09) | 121 – 129 |
| VER_LIQUIDADOR | Dígito verificador del RUT. | X(01) | 130 – 130 |

Registro tipo 3: TOTAL REGISTROS

| CAMPO | DESCRIPCION | FORMATO | POSICION |
| --- | --- | --- | --- |
| TIPO_REGISTRO | Debe tener valor “3”. | 9(01) | 1 – 1 |
| TOTAL_REGISTROS | Número total de registros informados en el archivo. Esto es, suma de la cantidad de registros tipo 1, 2, y 3. | 9(08) | 2 – 9 |
| FILLER | Sólo se deben grabar espacios. | X(121) | 10 – 130 |