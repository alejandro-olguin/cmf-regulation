<!-- source: cir_1716_2004_refundido.pdf -->
<!-- language: es -->
<!-- note: Las fórmulas matemáticas extraídas de PDFs pueden ser incompletas.
     Los bloques marcados con ⚠️ deben verificarse contra el PDF original. -->

# CIRCULAR N° 1716 — ENVIO DE INFORMACION DEL SEGURO OBLIGATORIO DE ACCIDENTES CAUSADOS POR VEHICULOS MOTORIZADOS AL SERVICIO DE REGISTRO CIVIL E IDENTIFICACION.


Para todas las entidades aseguradoras Esta Superintendencia, en uso de sus facultades y conforme lo dispuesto en el artículo 18º de la Ley N°18.490, ha estimado necesario impartir las siguientes instrucciones sobre forma, contenido y oportunidad de la información relativa al Seguro Obligatorio de Accidentes Causados por Vehículos Motorizados (SOAP), que las aseguradoras deben enviar al Servicio de Registro Civil e Identificación (SRCeI), para su anotación en el Registro Nacional de Vehículos Motorizados.
I Oportunidad y Medio de Envío de Datos Las aseguradoras deberán enviar al SRCeI, la información de los seguros obligatorios que contraten dentro de los primeros 10 días hábiles del mes siguiente al mes de inicio de la vigencia de los seguros. El envío de la información señalada deberá efectuarse en forma electrónica, y ajustarse a las instrucciones establecidas en Anexo 1 de esta Circular.
Una vez procesados el SRCeI pondrá a disposición de las compañías, el resultado del proceso de los datos remitidos.
## II Estructura del Nombre Externo de los Archivos
Caso 1:
Los archivos ingresados por las compañías correspondientes a periodos normales, deberán tener la siguiente
estructura en su nombre:
<Abreviatura>+<Abreviatura N1> Donde Abreviatura corresponde al nombre abreviado de la compañía, según Tabla 1 del Anexo N°2 y Abreviatura N1 corresponde al mes según lo indicado en Tabla 2 del Anexo N°2.
Por ejemplo, en el caso de la compañía de seguros cruz del sur, el archivo quedaría de la siguiente manera: ( CRUMAY ), esto significa el archivo de Mayo de la compañía Cruz del Sur.
Caso 2:
Los archivos ingresados por las compañías correspondientes a correcciones de información, deberán tener la siguiente estructura en su nombre:
<Abreviatura>+<Abreviatura N2> Donde Abreviatura corresponde al nombre abreviado de la compañía, según Tabla 1 del Anexo N°2 y Abreviatura N2 corresponde al mes según lo indicado en Tabla 2 del Anexo N°2.
Por ejemplo, en el caso de la compañía de seguros cruz del sur, el archivo quedaría de la siguiente manera: ( CRUCMY ), esto significa el archivo de correcciones de Mayo de la compañía Cruz del Sur.
Caso 3:
Para aquellas compañías que no tuvieron movimiento durante el mes, deberán informar enviando un archivo el cual deberá tener la siguiente estructura en su nombre:
<Abreviatura>+<Abreviatura N3> Donde Abreviatura corresponde al nombre abreviado de la compañía, según Tabla 1 del Anexo N°2 y Abreviatura

N1 corresponde al mes según lo indicado en Tabla 2 del Anexo N°2.
Por ejemplo, en el caso de la compañía de seguros cruz del sur, el archivo quedaría de la siguiente manera: ( CRUVMY ), esto significa que Cruz del Sur en el mes de Mayo, no tuvo movimiento o ingreso de Seguros SOAP.
## III Estructura de Archivos Entrada y Salida del Sistema
1.- Archivo de Entrada
El archivo con los datos del SOAP que las compañías envíen al SRCeI, deberá ajustarse estrictamente a la estructura que se indica a continuación:
Estructura archivo de entrada:

|  | Nombre Campo |  |  | Tipo |  |  | Largo |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Código Aseguradora (*) |  |  | Numérico |  |  | 2 |  |  |
| Letras Patente |  |  | Alfabético |  |  | 2 |  |  |
| Número Patente |  |  | Numérico |  |  | 4 |  |  |
| Dígito verificador Patente |  |  | Alfanumérico |  |  | 1 |  |  |
| Marca Vehículo |  |  | Alfanumérico |  |  | 20 |  |  |
| Modelo Vehículo |  |  | Alfanumérico |  |  | 25 |  |  |
| Año Fabricación |  |  | Numérico |  |  | 4 |  |  |
| Número Motor |  |  | Alfanumérico |  |  | 20 |  |  |
| Tipo Póliza |  |  | Numérico |  |  | 1 |  |  |
| Número Póliza |  |  | Numérico |  |  | 8 |  |  |
|  | Fecha de Inicio Vigencia |  |  |  |  |  |  |  |
| Día |  |  | Numérico |  |  | 2 |  |  |
| Mes |  |  | Numérico |  |  | 2 |  |  |
| Año |  |  | Numérico |  |  | 4 |  |  |
|  | Fecha de Vencimiento |  |  |  |  |  |  |  |
| Día |  |  | Numérico |  |  | 2 |  |  |
| Mes |  |  | Numérico |  |  | 2 |  |  |
| Año |  |  | Numérico |  |  | 4 |  |  |
| Largo Total Registro |  |  |  |  |  | 103 |  |  |

(*) El “Código Aseguradora” corresponde al código asignado por el Servicio de Registro Civil e Identificación a la compañía. En caso que una compañía desee iniciar la venta de este seguro, y no se encuentre en la Tabla1, anexa a esta Circular, o cambie su Razón Social, se fusione o sufra cualquier otro cambio en su propiedad o nombre, deberá solicitar un nuevo código a dicho Servicio, en la forma y oportunidad determinada por éste. (ver Anexo N°3).
2.- Archivo de Salida
El archivo con el resultado del proceso efectuado por el SRCeI, se estructurará según el formato que se indica a
continuación:
Estructura archivo de Salida:

|  | Nombre Campo |  |  | Tipo |  |  | Largo |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Número Póliza |  |  | Numérico |  |  | 8 |  |  |
| Patente |  |  |  |  |  |  |  |  |
| Letras |  |  | Alfabético |  |  | 2 |  |  |
| Números |  |  | Numérico |  |  | 4 |  |  |
| Dígito Verificador |  |  | Alfanumérico |  |  | 1 |  |  |
| Marca Vehículo |  |  | Alfabético |  |  | 20 |  |  |
| Modelo Vehículo |  |  | Alfabético |  |  | 25 |  |  |
| Tipo Vehículo |  |  | Alfabético |  |  | 4 |  |  |
| Año Fabricación |  |  | Numérico |  |  | 4 |  |  |
| Número Motor |  |  | Alfanumérico |  |  | 20 |  |  |
| Run Propietario |  |  | Alfanumérico |  |  | 10 |  |  |
| Número Póliza |  |  | Numérico |  |  | 8 |  |  |
|  | Flag de Ingreso o Rechazo |  |  |  |  |  |  |  |
| PPU |  |  | Numérico |  |  | 1 |  |  |
| Marca |  |  | Numérico |  |  | 1 |  |  |
| Modelo |  |  | Numérico |  |  | 1 |  |  |
| Año Fabricación |  |  | Numérico |  |  | 1 |  |  |
| Motor |  |  | Numérico |  |  | 1 |  |  |
| Seguro |  |  | Numérico |  |  | 1 |  |  |
| Compañía |  |  | Numérico |  |  | 1 |  |  |
| Fecha vencimiento Póliza |  |  | Numérico |  |  | 1 |  |  |
| Tipo Seguro |  |  | Numérico |  |  | 1 |  |  |
| Número del Seguro |  |  | Numérico |  |  | 1 |  |  |
| Actualización de la BDD |  |  | Numérico |  |  | 1 |  |  |
| Largo Total Registro |  |  |  |  |  | 109 |  |  |

IV Corrección de Datos y Reprocesos Las compañías deberán adoptar todas las medidas necesarias para la anotación oportuna de los certificados SOAP en el Registro Nacional de Vehículos Motorizados. El no envío de la información, el envío fuera de plazo o el envío con errores que imposibiliten la anotación de los certificados SOAP, serán consideradas infracciones graves a lo dispuesto en la presente Circular.
Sin perjuicio de lo anterior, las compañías podrán efectuar correcciones a los datos informados, tomando en consideración las sugerencias que formulará el SRCeI en el archivo de salida, y enviar un archivo de correcciones, dentro de los plazos establecidos para este efecto por el SRCeI. Si en alguna oportunidad debe enviar correcciones para más de un mes, éstas deben efectuarse en archivos separados, de acuerdo a las instrucciones de esta Circular.
Asimismo, las compañías podrán enviar archivos para su reproceso solo dos (2) veces para un mes en particular, un tercer envío será rechazado.
## V Vigencia y Aplicación:
La presente circular rige a contar de esta fecha y se aplicará al envío de información correspondiente a los certificados SOAP cuya vigencia se inicie en abril de 2004.
## VI Derogación Derógase a contar de esta fecha, la Circular N°666, de 1986 de esta Superintendencia.

ANEXO
Envío Electrónico de Datos al SRCeI para las compañías dentro de la AACH El acceso para la entrega de los archivos deberá ser realizada en la dirección web http://www.aach.cl , y dentro de esta en la Sección Usuarios Asociados – SRCEI.
Envío Electrónico de Datos al SRCeI para las compañías NO asociadas a la AACH Aquellas compañías que no se encuentren asociadas a la AACH, deberán enviar un CDRW y una carta dirigida a Jefe de Informática, ubicado en Huérfanos 1570, 3° piso, indicando el nombre del archivo a ser procesado según Anexo 2 y la cantidad de registros que contiene el archivo. Además en la carta se debe indicar el mes al cual corresponde el proceso.
Método de Contingencia En caso que el sitio web proporcionado por la AACH para el envío de Soap NO este habilitado, las compañías, deberán enviar la información necesaria para procesar mediante un CDRW y una carta dirigida a Jefe de Informática, ubicado en Huérfanos 1570, 3° piso, indicando al nombre del archivo a ser procesado según Tabla 1 y la cantidad de registros que contiene el archivo, además en la carta se debe indicar el mes al cual corresponde el proceso.

ANEXO
Tabla 1

| Nombre Compañía |  |  | Cod. | Abreviatura |
| --- | --- | --- | --- | --- |
| ABN-AMRO SEGUROS GENERALES |  | 48 |  | ABN |
| AGF ALLIANZ CHILE CIA. DE SEGUROS GENERALES S.A. |  | 50 |  | AGF |
| ASEGURADORA DE MAGALLANES S A |  | 14 |  | MAG |
| BCI SEGUROS GENERALES S.A. |  | 60 |  | BCI |
| CONSORCIO NACIONAL |  | 43 |  | CNS |
| CRUZ DEL SUR S. A. |  | 3 |  | CRU |
| ING SEGUROS DE VIDA S.A. |  | 52 |  | ING |
| ING SEGUROS GENERALES S.A. |  | 53 |  | INGV |
| LA CHILENA CONSOLIDADA S A |  | 9 |  | CHI |
| LA INTERAMERICANA |  | 22 |  | INT |
| LA INTERAMERICANA SEGUROS DE VIDA S.A. |  | 37 |  | INTV |
| LAS AMERICAS |  | 42 |  | AME |
| ISE CHILE |  | 45 |  | ISE |
| MAPFRE SEGUROS GENERALES |  | 47 |  | MAP |
| RENTA NACIONAL S A |  | 25 |  | REN |
| ROYAL & SUN ALLIANCE SEGUROS S.A. |  | 49 |  | ROY |
| SEGUROS SECURITY PREVISION GENERALES S.A. |  | 51 |  | SEC |

Tabla 2

| Mes |  |  | Abreviatura N1 |  |  | Abreviatura N2 | Abreviatura N3 |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Enero |  | ENE |  |  | CEN |  | VEN |  |
| Febrero |  | FEB |  |  | CFE |  | VFE |  |
| Marzo |  | MAR |  |  | CMA |  | VMA |  |
| Abril |  | ABR |  |  | CAB |  | VAB |  |
| Mayo |  | MAY |  |  | CMY |  | VMY |  |
| Junio |  | JUN |  |  | CJN |  | VJN |  |
| Julio |  | JUL |  |  | CJL |  | VJL |  |
| Agosto |  | AGO |  |  | CAG |  | VAG |  |
| Septiembre |  | SPT |  |  | CSP |  | VSP |  |
| Octubre |  | OCT |  |  | COC |  | VOC |  |
| Noviembre |  | NOV |  |  | CNV |  | VNV |  |
| Diciembre |  | DIC |  |  | CDI |  | VDI |  |

ANEXO
Creación de Código para las Compañías Aseguradoras Las compañías deberán enviar una carta con copia original a nombre del Director del SRCeI, solicitando la creación de un código para realizar procesos Soap.
En esta carta deberán especificar las razones por las cuales realizan esta solicitud, sean por que no se encuentre en la Tabla1, del Anexo 2 de esta Circular, o cambie su Razón Social, se fusione o sufra cualquier otro cambio en su propiedad o nombre.
Todo cambio deberá ser informado oportunamente al SRCeI, para evitar el no proceso de la información enviada por cada compañía.
El SRCeI, enviará un oficio a la SVS informando del cambio solicitado por la compañía en cuestión, adjuntado la copia original de la solicitud.