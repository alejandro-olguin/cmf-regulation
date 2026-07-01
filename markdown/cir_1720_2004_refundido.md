<!-- source: cir_1720_2004_refundido.pdf -->
<!-- language: es -->
<!-- note: Las fórmulas matemáticas extraídas de PDFs pueden ser incompletas.
     Los bloques marcados con ⚠️ deben verificarse contra el PDF original. -->

# CIRCULAR N° 1720 — IMPARTE INSTRUCCIONES RELATIVAS AL ENVIO DE INFORMACIÓN SOBRE INSTRUMENTOS DE TERCEROS MANTENIDOS EN CUSTODIA POR PARTE DE LOS INTERMEDIARIOS DE VALORES Y SOBRE LOS INSTRUMENTOS DE SU CARTERA PROPIA


Esta Superintendencia en uso de sus facultades legales y de acuerdo a lo dispuesto en el artículo 4°, letra d) del decreto ley N° 3.538 de 1980 y artículo 32, letra b) de la Ley N° 18.045, ha estimado necesario requerir a los corredores de bolsa y agentes de valores, información relativa a los valores de terceros mantenidos en custodia a nombre propio y a los valores de cartera propia.
El envío de esta información se deberá efectuar a través del Módulo SEIL (“Sistema de Envío de Información en Línea”) del sitio Web www.svs.cl, según las instrucciones establecidas en la Norma de Carácter General N° 117 de 2001, o la que la modifique o reemplace, y en esta circular. Para indicar el código de información, al cual hace referencia la mencionada norma, informar IVCRT.
### INFORMACION REQUERIDA
Los intermediarios de valores deberán remitir a esta Superintendencia, los saldos por instrumento de todos los valores de propiedad de terceros que mantenga en custodia y de todos los valores pertenecientes a su cartera propia. Esta información deberá presentarse por tipo de entidad en donde se encuentra la custodia física o electrónica de los instrumentos.
La información solicitada deberá estar referida al cierre del último día de cada trimestre y se enviará a este Servicio, dentro de los primeros 10 días corridos del trimestre siguiente al que se informa. No obstante lo anterior, la información objeto de esta circular podrá ser requerida por este Servicio a una fecha distinta al cierre del trimestre, por lo que los intermediarios de valores deberán contar con los sistemas que permitan su oportuno envío en todo momento.
Para efectos del contenido y forma de envío de la información, los intermediarios de valores deberán seguir las instrucciones estipuladas en el Anexo Técnico de la presente circular.
VIGENCIA La presente circular empezará a regir a contar del 30 de junio de 2004.
### DISPOSICION TRANSITORIA
El plazo de presentación de la información correspondiente al cierre del 30 de junio de 2004, será hasta el 10 de agosto de 2004.

### ANEXO TECNICO
SECCION A: INSTRUCCIONES PARA EL ENVIO DE INFORMACION A TRAVES DE
### INTERNET, SOBRE LOS INSTRUMENTOS DE TERCEROS MANTENIDOS EN CUSTODIA Y LOS INSTRUMENTOS DE CARTERA PROPIA DE LOS INTERMEDIARIOS DE VALORES.
### A.1 CARACTERISTICA DEL ARCHIVO A ENVIAR
La información requerida deberá enviarse a través de la página Web de la Superintendencia www.svs.cl, Módulo SEIL (Sistema de Envío de Información en Línea).
La información requerida en esta circular, deberá enviarse en un archivo de tipo texto, en código ASCII, cuyo formato y estructura deberá ajustarse a las especificaciones detalladas en la Sección B de este ANEXO.
Condiciones generales para el archivo de texto:
a) El software utilizado para generar el archivo, no debe grabar caracteres de control en el
texto ingresado. Tal es el caso, por ejemplo, de los procesadores de texto.
b) Las letras ñ y Ñ deben reemplazarse por #, las palabras no deben ir acentuadas y no se
debe incluir símbolos especiales, tales como º , ª. Luego, por ejemplo, Compañía N° 393, debería grabarse como COMPA#IA NRO. 393.
c) Todas las fechas deberán informarse en formato AAAAMMDD, donde:
AAAA : cuatro dígitos del año MM : dos dígitos del mes DD : dos dígitos del día Si el mes o el día es menor que 10 en números árabes, se debe anteponer el dígito 0
(cero).
d) Los valores numéricos deberán informarse sin separadores de miles ni decimales.
### A.2 INDIVIDUALIZACION DEL ARCHIVO A ENVIAR
a) Nombre del archivo.
El nombre del archivo enviado deberá ser exclusivamente el siguiente:
cartAAAAMMDD.TXT

Donde "AAAA" corresponde al año, "MM" al mes y “DD” al día de la fecha de cierre de las carteras que se está informando. Si el mes o día es inferior a 10 en números árabes, se debe anteponer ceros.
b) Uso obligatorio del pre-validador.
La Superintendencia sólo aceptará archivos que estén sin errores. Para facilitar lo anterior, el módulo SEIL permitirá a los Intermediarios de valores validar la información, previo a su envío a la Superintendencia. Por lo tanto los Intermediarios deberán prevalidar los archivos y una vez que éstos no contengan errores, podrán ser enviados a este Servicio.
c) Codificaciones.
Los códigos que se deben utilizar para señalar tipo de instrumento o unidades monetarias, se encontrarán permanentemente en el módulo SEIL, opción “Codificación S.V.S.”, del sitio web de la Superintendencia.
d) Casilla de correo.
Al respecto, el intermediario de valores deberá asegurarse de que la casilla de correo electrónico del usuario que remitió la información, esté operativa.
SECCION B: DESCRIPCION DEL ARCHIVO
### B.1 DESCRIPCION DE REGISTRO
El archivo cartAAAAMMDD.txt deberá contener tres tipos de registros diferentes, identificados por la primera posición del registro.
Identificación (registro tipo 1) : Contendrá información que permita identificar al intermediario de valores que informa y el día de la información. Cabe señalar que sólo se debe informar un registro de este tipo y deberá ser el primero del archivo.
Detalle (registro tipo 2) : Contendrá información de la cartera propia y de custodia de terceros del intermediario de valores. Se deberá informar un registro por cada instrumento.
Totales (registro tipo 3) : Contendrá información de cuadratura de los registros de detalle informados. Cabe señalar que sólo se deberá informar un registro de este tipo y deberá ser el último del archivo.
Todos los tipos de registros del archivo, deben tener el mismo largo, cualquiera sea la estructura.

Registro tipo 1 de IDENTIFICACION
### CAMPO DESCRIPCION PICTURE
TIPO Tipo de registro. En este caso corresponde anotar un 1. 9(01) RUT Rol Único Tributario del Intermediario de Valores que 9(09) informa. Es obligatorio y no puede informarse en cero.
VERIFICADOR Dígito verificador del RUT del Intermediario de Valores. Es X(01) obligatorio y no puede informarse en blanco.
FECHA Corresponde a la fecha del día que se está informando, en 9(08) formato AAAAMMDD. Deber ser la misma inserta en el nombre del archivo.
NOMBRE Nombre o razón social del Intermediario de Valores que X(60) informa.
FILLER Filler. Se deberá informar espacios X(183)
Registro tipo 2 de DETALLE:
### CAMPO DESCRIPCION PICTURE
TIPO Tipo de registro. En este caso corresponde anotar un 2. 9(01) NEMOTECNICO Se deberá informar el código nemotécnico establecido por X(20) esta Superintendencia, en la Circular Nº 1.085 de 1992. Si se tratara de un instrumento del que no estuviese disponible su código nemotécnico, se deberá digitar el código SN. Sin perjuicio de lo anterior, el campo SN, no podrá utilizarse para instrumentos depositados en el Depósito Central de Valores.
NOMBRE EMISOR Deberá señalarse el nombre con el que se conoce al X(30) emisor.
TIPO Deberá señalarse el tipo de instrumento que mantiene en X(10) INSTRUMENTO cartera propia o en custodia. Para estos efectos deberá utilizar los códigos descritos en “Instrumentos” del módulo SEIL del sitio web de la Superintendencia.

CANTIDAD- Deberá registrarse el número de unidades nominales de los 9(15)V9(04) UNIDADES- instrumentos que componen la cartera propia y de custodia NOMINAL de terceros. Esta cifra deberá expresarse con cuatro decimales.
Corresponde a la moneda o unidad de reajuste en que se
### TIPO UNIDADES X(15)
encuentre expresada la cantidad de unidades nominales.
Para estos efectos deberá utilizar los códigos descritos en
“Unidades Monetarias” del módulo SEIL del sitio web de la Superintendencia. En el caso que en el campo CANTIDADUNIDADES-NOMINAL se informe cantidades (como por ejemplo, si el tipo de instrumento es “acciones”), en el campo TIPO UNIDADES deberá informar CA.
Indicar el monto total en pesos que representan los títulos
### VALORIZACION 9(15)
valorizados a su valor de mercado al cierre del día solicitado.
Corresponde al número de unidades nominales de los
### CARTERA PROPIA 9(15)V9(04)
instrumentos que componen la cartera propia del intermediario.
Corresponde al número de unidades nominales de los
### CUSTODIA DE 9(15)V9(04)
instrumentos de propiedad de terceros mantenidos en TERCEROS custodia.
Corresponde al número de unidades nominales de los
### CUSTODIA 9(15)V9(04)
instrumentos de la cartera propia mantenidos en el Depósito
### PROPIA EN DCV
Central de Valores.
Corresponde al número de unidades nominales de los
### CUSTODIA DE 9(15)V9(04)
instrumentos de propiedad de terceros mantenidos en el
### TERCEROS EN
Depósito Central de Valores.
DCV Corresponde al número de unidades nominales de los
### CUSTODIA EN 9(15)V9(04)
instrumentos de cartera propia y de propiedad de terceros SOCIEDAD mantenidos en custodia de la sociedad emisora.
EMISORA Corresponde al número de unidades nominales de los
### CUSTODIA EN EL 9(15)V9(04)
instrumentos de cartera propia y de propiedad de terceros INTERMEDIARIO mantenidos en custodia en las oficinas del propio intermediario de valores.
Corresponde al número de unidades nominales de los
### CUSTODIA EN 9(15)V9(04)
instrumentos de cartera propia y de propiedad de terceros BOLSAS mantenidos en custodia en Bolsas de Valores.
Corresponde al número de unidades nominales de los
### CUSTODIA EN 9(15)V9(04)
instrumentos de cartera propia y de propiedad de terceros OTROS mantenidos en custodia en otras entidades.

Registro tipo 3 de TOTALES:
### CAMPO DESCRIPCION PICTURE
TIPO Tipo de registro. En este caso corresponde anotar un 3. 9(01) TOTAL- Total de registros informados en el archivo, incluidos el de 9(10) REGISTROS identificación y el de totales.
FILLER Filler. Se deberá informar espacios X(251)