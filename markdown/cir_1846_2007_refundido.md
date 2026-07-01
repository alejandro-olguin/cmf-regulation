<!-- source: cir_1846_2007_refundido.pdf -->
<!-- language: es -->
<!-- note: Las fórmulas matemáticas extraídas de PDFs pueden ser incompletas.
     Los bloques marcados con ⚠️ deben verificarse contra el PDF original. -->

# CIRCULAR N° 1846 — INSTRUCCIONES APLICABLES A LA VENTA DEL SEGURO OBLIGATORIO DE ACCIDENTES PERSONALES, CONFORME CONVENIO DE TRANSPORTE DE PASAJEROS POR CARRETERA ENTRE TACNA Y ARICA CON LA REPÚBLICA DEL PERÚ


Esta Superintendencia en uso de sus facultades legales, y lo dispuesto en el artículo 21 del D.S. N° 265 de 2005 del Ministerio de Relaciones Exteriores, que promulga el Convenio de Transporte de Pasajeros por Carretera entre Tacna y Arica con la República del Perú, en adelante “el Convenio” y en la Ley N° 18.490, sobre el Seguro Obligatorio de Accidentes Personales (SOAP), ha estimado necesario impartir las siguientes instrucciones sobre extensión de la cobertura del SOAP hasta Perú, conforme lo establecido en el Convenio referido.
Para los vehículos que, conforme al Convenio, deban contratar la extensión de la cobertura del SOAP a los accidentes de tránsito ocurridos durante la prestación del servicio de transporte colectivo de pasajeros por carretera entre las ciudades de Arica y Tacna, acreditará dicha extensión agregando al certificado establecido por la Circular N°1459 para el SOAP, un certificado o impreso en la forma que defina la aseguradora contratante, que contenga al menos la Placa Patente del Vehículo y la siguiente leyenda: “El presente seguro extiende su cobertura a los accidentes de tránsito ocurridos durante la prestación del servicio de transporte colectivo de pasajeros por carretera entre las ciudades de Arica y Tacna en sus diferentes modalidades, en conformidad a lo dispuesto en el D.S. 265 de
2005, del Ministerio de Relaciones Exteriores.”.
La vigencia de la extensión de la cobertura debe corresponder a la misma del SOAP que rige para la cobertura en territorio nacional.
Las aseguradoras que contraten la extensión de la cobertura del SOAP de que trata esta Circular, deberán informar a esta Superintendencia respecto a los seguros contratados con dicha extensión de cobertura, en la forma y de acuerdo a las especificaciones que se detallan en Anexo adjunto. Dicha información deberá enviarse a más tardar el último día del mes siguiente en el cual se suscribió la extensión de cobertura.
Vigencia: La presente circular rige a contar de esta fecha.
### SUPERINTENDENTE (S)

ANEXO Los datos de los vehículos que contrataron la extensión de la cobertura del SOAP hasta la ciudad de Tacna, en Perú, deberán enviarse ajustándose estrictamente a lo siguiente:
Se deberá enviar archivo de texto plano, con los registros que se indican a continuación, a través del correo electrónico soaptacna@svs.cl, con nombre ‘soaptacna.nnnnnnnn”, siendo nnnnnnnn el número de R.U.T. (sin dígito verificador) de la compañía de seguros. Los registros se deben informar con separación de punto y coma (;) entre campos.
El formato de cada registro es el siguiente:
Registro 1 de identificación de la compañía

| Campo N° | Nombre del Campo | Descripción del Contenido | Formato |
| --- | --- | --- | --- |
| 1 | TIPO-REGISTRO | Tipo de registro, en este caso debe grabar 1. | 9(1) |
| 2 | RUT-ASEGURADORA | Rol Unico Tributario de la compañía de seguros que está enviando los datos (sin dígito verificador). | 9(9) |
| 3 | NOMBRE-ASEGURADORA | Razón Social de la compañía que está enviando los datos. | X(60) |
| 4 | FECHA-CIERRE | Debe registrar la fecha de cierre de la venta de los registros informados en el archivo. AAAAMMDD | 9(8) |
| 5 | FILLER | Solo debe grabar espacios. | X(23) |

Registro 2 detalle de los seguros extendidos hasta Tacna

| Campo N° | Nombre del Campo | Descripción del Contenido | Formato |
| --- | --- | --- | --- |
| 1 | TIPO-REGISTRO | Tipo de registro, en este caso debe grabar 2. | 9(1) |
| 2 | LETRAS-PLACA-PATENTE | Letras de la placa patente del vehículo que extendió la cobertura del SOAP hasta Tacna. | X(4) |
| 3 | NUMERO-PLACA-PATENTE | Número de la placa patente del vehículo que extendió la cobertura del SOAP hasta Tacna. | 9(4) |
| 4 | DIGITO-PATENTE | Dígito verificador de la placa patente del vehículo que extendió la cobertura del SOAP hasta Tacna. | 9(1) |
| 5 | TIPO-VEHICULO | Debe registrar el tipo de vehículo que extendió la cobertura del SOAP hasta Tacna: 1: taxi 2: bus 3: otro | 9(1) |
| 6 | MARCA-VEHICULO | Marca del vehículo que extendió la cobertura del SOAP hasta Tacna.. | X (20) |
| 7 | MODELO-VEHICULO | Modelo del vehículo que extendió la cobertura del SOAP hasta Tacna. | X (30) |
| 8 | NUM-MOTOR | Número de motor del vehículo que extendió la cobertura del SOAP hasta Tacna. | X(20) |
| 9 | ANO-FABRICACION | Año de fabricación del vehículo que extendió la cobertura del SOAP hasta Tacna. AAAA | 9(4) |
| 10 | INICIO-VIGENCIA | Inicio de la vigencia de la extensión de la cobertura hasta Tacna. AAAAMMDD | 9(8) |
| 11 | FIN-VIGENCIA | Termino de la vigencia de la extensión de la cobertura hasta Tacna. AAAAMMDD | 9(8) |

### CONSIDERACIONES GENERALES
Debe tenerse especial cuidado que el software utilizado para la generación del archivo no grabe caracteres de control.

Campos numéricos.
Ante la ausencia de información en un campo numérico deberá grabarse "0" (cero o ceros) dependiendo del largo de éste. Todos los campos numéricos deberán grabarse justificados a la derecha y completarse con ceros por la izquierda, sin separador de miles ni de decimales.
Para los campos numéricos se aceptarán como cantidades válidas las siguientes: 0 1 2 3 4 5 6 7 8 9 Campos fecha Todas las fechas deben expresarse en formato AAAAMMDD, donde:
AAAA: cuatro dígitos del año que corresponda.
MM: dos dígitos del mes que corresponda.
DD: dos dígitos del día que corresponda.
Si el mes o el día es menor que 10, en números árabes, debe anteponerse el dígito 0 (cero).
Campos alfanuméricos Ante la ausencia de información en un campo alfanumérico deberá grabarse " " (espacio o espacios). Si en la información se encuentran contenidos caracteres Ñ o ñ, estos deberán ser reemplazados por # exclusivamente.
Consideraciones Especiales Si el formato definido para algún campo, fuera insuficiente para almacenar la información pertinente, no debe ampliarse la longitud del campo, sino que dicha situación deberá ser comunicada a esta Superintendencia para que ella reformule los formatos relativos al archivo. En este caso la compañía deberá comunicarlo y pedir instrucciones a través del correo electrónico soaptacna@svs.cl.