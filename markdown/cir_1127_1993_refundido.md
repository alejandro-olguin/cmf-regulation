<!-- source: cir_1127_1993_refundido.pdf -->
<!-- language: es -->
<!-- note: Las fórmulas matemáticas extraídas de PDFs pueden ser incompletas.
     Los bloques marcados con ⚠️ deben verificarse contra el PDF original. -->

# CIRCULAR N° 1127 — INFORMACION DE SINIESTROS


Esta Superintendencia, en uso de sus facultades legales, considerando la necesidad de perfeccionar la estadística de siniestros, ha estimado necesario impartir instrucciones sobre la información de siniestros que deben proporcionar las compañías, de acuerdo a lo siguiente:
ARTICULO 1º:
Las compañías aseguradoras deberán informar a la Superintendencia, a más tardar el día 15 de cada mes o al día hábil siguiente, acerca de todos los pagos de siniestros realizados durante el mes inmediatamente anterior y sobre la provisión de siniestros al último día del referido mes, según las instrucciones contenidas en los anexos de esta circular.
La información solicitada corresponde a los ramos señalados en el anexo D de esta circular.
ARTICULO 2º:
La información deberá ser enviada en cinta magnética grabada a 1600 bpi, sin rótulos internos, o bien, en diskette DOS, tamaño 3.5", adjuntando una carta del Gerente de Siniestros con los siguientes datos:
- Mes al que corresponde la información.
- Número de siniestros denunciados en el mes.
- Número de siniestros pendientes a fin de mes (pendientes, liquidados parciales y controvertidos)
- Total de pagos efectuados, en UF.
- Total de provisiones, en UF.
- Total de recuperos recibidos, en UF.
ARTICULO 3º:
En los anexos adjuntos a esta circular se establece la información requerida de acuerdo al siguiente orden:
Anexo A Instrucciones generales Anexo B Estructura de registros Anexo C Descripción detallada de registros Anexo D Codificación de ramos Anexo E Codificación de actividades económicas (sólo para ramos robo e incendio y adicionales y garantía) Anexo F Codificación de tipos de seguros (Sólo para ramos de transporte e incendio y adicionales) Anexo G Codificación de coberturas (Sólo para ramos de vehículos, incendio, garantía, y adicionales)
ARTICULO 4º:
En caso de detección de errores en el proceso de validación, las compañías contarán con un plazo de 7 días corridos para enviar la información corregida.
ARTICULO 5º

El no cumplimiento a lo dispuesto en la presente Circular, dará origen a las sanciones contempladas en el artículo 44 del D.F.L. Nº 251, de 1931 y artículo 27 del Decreto Ley Nº 3.538, de 1980.
VIGENCIA La presente circular comenzará a regir para la información del mes de septiembre del año en curso.
DEROGACION Derógase, a contar del 1º de Enero de 1994, la Circular Nº 864 de 22 de Mayo de 1989.

### ANEXO A
(Instrucciones Generales)
### INFORMACION A ENVIAR
Para cada siniestro con algún pago o recupero en el mes o con provisión diferente a cero a fin del mes, las compañías generarán sólo un registro de tipo 1 (datos generales), uno o más de tipo 2 (costos) y cero o más de tipo 3
(conductor y terceros, sólo para Vehículos).
Para un siniestro los cuatro primeros campos de estos registros deben contener los mismos datos.
Los siniestros se informan uno a uno. Para cada siniestro se deberá enviar un registro con datos generales
(TIPO 1), uno o varios registros con antecedentes de costo (TIPO 2) y uno o varios registros (TIPO 3), en ese orden.
Este último tipo de registro es para identificar al conductor y a los terceros, en caso de vehículos motorizados.
Las compañías no deberán enviar datos acerca de siniestros ocurridos y no reportados.
Las indemnizaciones pagadas deben incluir los costos de liquidación (honorarios de liquidadores, abogados, y otros).
Los recuperos se informan manteniendo la concordancia con las normas de contabilización para efectos de la FECU.
Los registros de recupero, aparte de indicarse en el campo Nº 7 con código 2, se informarán con signo negativo en el campo Nº 8 (MONTO).
Si existe más de una cobertura principal o adicional afectada, los costos del siniestro se informarán en forma separada para cada cobertura principal o adicional en registros de tipo 2 (Ramos Incendio y Vehículos).
Igualmente si existe más de un tercero afectado se informarán todos, en registros separados de tipo 3.
Hay datos que se enviarán en la medida que la compañía disponga de tal información: nombre y rut del beneficiario y nombre, rut y patente de los terceros.
Todos los meses se reenviará toda la información de datos generales (registro tipo 1) y de personas involucradas (sólo Vehículos, registro tipo 3) de los siniestros que estén pendientes, liquidado parcial o controvertido de períodos anteriores.

### ANEXO B
(Estructura de Registros)
### REGISTRO TIPO
Identificación
### 1 AÑO-MES DE LA INFORMACION (AAMM) 9(4) 2 RUT DE LA COMPAÑIA 9(8) DIGITO VERIFICADOR A 3 RAMO 99 4 NUMERO DE SINIESTRO A(18) 5 TIPO DE REGISTRO 9
Datos del siniestro
### 6 FECHA DEL SINIESTRO 9(6)
7 NUEVO (SI= S, NO=N) A
### 8 ESTADO 9
Datos de la póliza siniestrada
### 9 NUMERO DE POLIZA A(13)
10 SINIESTRALIDAD (MAYOR 100% = 1 MENOR 100%=0) 9
### 11 VIGENCIA DESDE DE LA POLIZA (DDMMAA) 9(6) 12 VIGENCIA HASTA DE LA POLIZA (DDMMAA) 9(6) 13 NUMERO DE ITEMES ASOCIADOS A LA POLIZA 9(5 14 POLIZA EN COSEGURO 9 15 RUT CONTRATANTE 9(8) DIGITO VERIFICADOR A 16 NOMBRE O RAZON SOCIAL CONTRATANTE A(35) 17 RUT ASEGURADO 9(8) DIGITO VERIFICADOR A 18 NOMBRE O RAZON SOCIAL DEL ASEGURADO A(35) 19 RUT BENEFICIARIO 9(8) DIGITO VERIFICADOR A 20 NOMBRE O RAZON SOCIAL BENEFICIARIO A(35)
Sólo para Incendio y Robo
### 21 ACTIVIDAD ECONOMICA 99
22 TIPO DE SEGURO (sólo Incendio) 9
### 23 USO RESERVADO 9(15)
Para uso futuro
### 24 AUXILIAR A(20) REGISTRO TIPO
Identificación
### 1 AÑO Y MES DE LA INFORMACION (AAMM) 9(4) 2 RUT DE LA COMPAÑIA 9(8) DIGITO VERIFICADOR A
### 1 AÑO Y MES DE LA INFORMACION (AAMM) 9(4) 2 RUT DE LA COMPAÑIA 9(8) DIGITO VERIFICADOR A 3 RAMO 99 4 NUMERO DE SINIESTRO A(18) 5 TIPO DE REGISTRO 9
Costos por Cobertura
### 6 COBERTURA AFECTADA 99
7 TIPO DE COSTO (pago=1, recupero=2, provisión=3) 9
### 8 MONTO (UF) 9(10)
9 FECHA (del pago, recupero o provisión) (DDMMAA)9(6)
Para uso futuro
### 10 AUXILIAR A(20) REGISTRO TIPO
Identificación
### 1 AÑO Y MES DE LA INFORMACION (AAMM) 9(4) 2 RUT DE LA COMPAÑIA 9(8) DIGITO VERIFICADOR A 3 RAMO 9 4 NUMERO DE SINIESTRO A(18) 5 TIPO DE REGISTRO 9
Datos de pasajero
### 6 TIPO CONDUCTOR 9 7 RUT 9(8) DIGITO VERIFICADOR A 8 NOMBRE CONDUCTOR A(35) 9 PATENTE VEHICULO LETRAS A(3) NUMEROS 9(4)
Para uso futuro
### 10 AUXILIAR A(20)
### 10 AUXILIAR A(20) ANEXO C
(Descripción de los registros)
### REGISTRO TIPO
(Registro con datos generales de un siniestro) Identificación
1 Corresponde al año y mes de la información entregada
2 RUT y dígito verificador de la Compañía informante
3 Ramo según FECU (se excluye el SOAP)
4 Número del siniestro informado
5 Tipo de registro = 1
Datos del siniestro
6 Fecha de ocurrencia del siniestro
7 Se indica si el siniestro se denuncia en este período (NUEVO=S) o ya había sido ingresado antes (NUEVO=N)
8 Estado del siniestro
0 Pendiente Siniestro sin pago ni liquidación
1 Liquidado total Siniestro liquidado o rechazado.
2 Liquidado parcial Siniestro con pagos parciales.
El saldo pendiente se informa con provisión.
3 Controvertido Siniestro en litigio.
4 Post liquidado Siniestro liquidado con pago posterior a la liquidación.
9 Número de póliza madre. No se informa el ítem asociado, por lo tanto todos los siniestros de los distintos
ítemes de una póliza colectiva se deben informar a la misma póliza.
No interesa tampoco el endoso asociado.
10 Indicador de Siniestralidad: Sólo se indicará si la siniestralidad acumulada de la póliza (calculada como costo
siniestros directos/prima directa) es mayor o igual al 100% de la prima total de la póliza, ya sea en un sólo evento o en la acumulación de siniestros parciales.
0 : siniestralidad menor a 100%
1 : siniestralidad mayor o igual a 100%
11 Vigencia "desde" de la póliza (DDMMAA)
12 Vigencia "hasta" de la póliza (DDMMAA).

En pólizas con vigencia indefinida se enviará (000000)
13 Número de ítemes (unidades de riesgo) asociados a la póliza al momento de informar.
14 Indica si es o no una póliza en coseguro. Permite eliminar los pagos duplicados entre la compañía líder (la que
toma el riego) y las coaseguradoras.
0 : póliza normal
1 : póliza en la cual la Cía. es líder
2 : póliza en la cual la Cía. es coaseguradora (no líder)
15 RUT y dígito verificador del contratante.
En pólizas de Garantía corresponde al afianzado o deudor.
En pólizas de Fidelidad corresponde al empleado.
16 Nombre o razón social del contratante.
17 RUT y dígito verificador del asegurado.
En pólizas de Garantía corresponde al mandante.
En pólizas de Fidelidad corresponde al empleador.
18 Nombre o razón social del asegurado
19 RUT y dígito verificador del beneficiario (si existe). En pólizas de Garantía y Fidelidad corresponde al
asegurado.
20 Nombre o razón social del beneficiario (si existe).
Sólo para Incendios, Robo y Garantía
21 Código de actividad económica (ver ANEXO E).
Sólo para Incendio y Trasporte
22 Tipo de seguro (ver ANEXO F)
Para uso futuro
23 Campo en blanco
24 Auxiliar
NOTAS:
1. Extranjeros: cada compañía enviará el RUT que desee asignarle, con la condición que tenga un dígito
verificador válido.
## 2. Para campos 19 y 20:
RUT que no se disponga: ceros Nombre que no se informa : blancos.
## 3. Nombres: Apellidos seguidos de nombres.

### REGISTRO TIPO
(Registro con datos de costo de un siniestro) Contiene datos relativos al costo del siniestro. Se genera uno o más registros, según existan pagos en el mes (TIPO COSTO=1), recuperos (TIPO COSTO=2) y provisión (TIPO COSTO=3). Los recuperos se informan con signo negativo.
Si en un mes hay varios pagos para un siniestro, las compañías tendrán la opción de enviar un registro para cada uno de los pagos, o bien un sólo registro con el total pagado y la fecha del último pago. Lo mismo es válido en relación a los recuperos.
Para Vehículos e Incendio, si hay más de una cobertura afectada se deberá enviar la información en forma separada para cada cobertura.
Identificación
1 Corresponde al año y mes de la información entregada
2 RUT y dígito verificador de la Compañía informante.
3 Ramo según FECU (se excluye el SOAP)
4 Número del siniestro informado
5 Tipo de registro = 2
Costos por cobertura
6 Cobertura afectada ( ver Anexo G.)
7 Tipo de costo :
1 : Indemnización parcial o final
2 : Recupero
3 : Provisión
8 Monto de indemnización, recupero o provisión, con dos decimales (implícitos), en UF.
Indemnización: comprende la indemnización propiamente tal más los gastos de liquidación, y no se contempla el efecto de reaseguros.
Si un siniestro tiene varios pagos en el mes que se informa, se puede enviar un registro por cada uno de ellos , o bien enviar uno sólo con el total, indicando la fecha del último pago.
Recupero : se informa con signo negativo. El criterio para informarlo debe ser el mismo que la compañía utiliza para la FECU.
Provisión : si el siniestro está en estado Pendiente o Liquidado parcial o Controvertido se debe informar un valor de provisión, siguiendo igual criterio al usado en la FECU.
La conversión a UF se debe realizar a la fecha de cada pago o recupero.

9 Fecha del pago, recupero o provisión (DDMMAA).
Para uso futuro
10 Campo en blanco
### REGISTRO TIPO
(Registro con datos de conductores, a utilizarse sólo en el ramo de Vehículos) Sólo para el ramo Vehículos se generará un registro para informar el conductor del vehículo asegurado (TIPO CONDUCTOR = 1) y tantos registros adicionales como vehículos de terceros (TIPO CONDUCTOR = 2) existan involucrados en el siniestro.
Identificación
1 Corresponde al año y mes de la información entregada.
2 RUT y dígito verificador de la Compañía informante.
3 Ramo según FECU (se excluye el SOAP).
4 Número del siniestro informado.
5 Tipo de registro = 3.
Datos de conductor.
6 Tipo de conductor
1 : conductor del vehículo asegurado
2 : conductor de vehículo de tercero
7 RUT y dígito verificador del conductor .
En forma provisoria, en el caso de los terceros, se puede dejar en cero.
8 Nombre del conductor (apellidos, nombres)
9 Patente del vehículo.
Se informará en dos campos :
- Letras : en 3 caracteres alfanuméricos ajustados a izquierda.
- Números: en 4 caracteres numéricos ajustados a la derecha.
No se informará el dígito verificador.
Para uso futuro
10 Campo en blanco.

### ANEXO D (RAMOS FECU)
## 1. Incendio
## 2. Pérdida de Beneficios por Incendio
## 3. Terremoto
## 4. Pérdida de Beneficios por Terremoto
## 5. Riesgos de la naturaleza
## 6. Terrorismo
## 7. Otros riesgos adicionales a Incendio
## 8. Robo
## 9. Daños Físicos Vehículos Motorizados G1
## 10. Daños Físicos Vehículos Motorizados G2
## 11. Casco Marítimo
## 12. Casco Aéreo
## 13. Transporte Terrestre
## 14. Transporte Marítimo
## 15. Transporte Aéreo
## 16. Equipo Contratista
## 17. Todo Riesgo Construcción y Montaje
## 18. Avería Maquinaria
## 19. Equipo electrónico
## 20. Responsabilidad Civil Vehículos Motorizados
## 21. Responsabilidad Civil General
## 22. Multirriesgos
## 23. Accidentes Personales
## 24. Garantía
## 25. Fidelidad
## 30. Otros seguros
## 30. Otros seguros ANEXO E
(Código de actividad económica) Sólo ramos Robo e Incendio y Adicionales
1 Habitacional
2 Servicios en general (turismo, financieros, educación, salud, inmobiliarios, públicos o privados,
comunicación, etc.)
3 Almacenamiento y/o comercio mayorista
4 Comercio minorista
5 Industria química y sus derivados
6 Industria metalmecánica
7 Industria forestal y sus derivados
8 Industria alimenticia y agroindustria
9 Industria textil y cueros
10 Industria minera (extracción y refinación)
11 Industria de generación y abastecimiento de servicios públicos (agua, luz, teléfonos, gas)
12 Esparcimiento
13 Plantaciones forestales, frutales y cementeras
14 Obras civiles
15 Otras.
Sólo para Garantía
16 Construcción
17 Servicios
18 Suministros.

### ANEXO F
(Sólo para ramos de Transporte e Incendio y adicionales)
### TIPO DE SEGURO
Incendio
1 Bienes Físicos
2 Lucro Cesante y/o Perjuicios por Paralización
Transporte
3 Avería Gruesa

### ANEXO G
(Sólo para ramos de Vehículos, Incendio, Garantía y adicionales)
### COBERTURAS AFECTADAS
Ramo Vehículos Motorizados.
(Póliza POL 1 92 120 y cláusulas adicionales y opcionales correspondientes. Si la compañía opera con otras pólizas y cláusulas se deberá, en lo posible hacer la equivalencia).
1 Daños materiales (POL 1 92 120, *)
2 Robo o hurto (POL 1 92 120, * *)
3 Uso no autorizado (POL 1 92 120, * * * )
4 Responsabilidad Civil (POL 1 92 120)
5 Robo de accesorios (CAD 1 92 121)
6 Daños causados por sismo (CAD 1 92 126)
7 Daños por actos terroristas y huelga (CAD 1 92 122)
8 Daños por actos maliciosos (CAD 1 92 123)
9 Daños por riesgos de naturaleza (CAD 1 92 124)
10 Pérdida total solamente (COP 1 93 009)
11 Otros
* Cobertura 1), de artículo 3º
* * Coberturas 2a), 2b) y 2c) de artículo 3º
* * * Cobertura 2d) de artículo 3º
Ramo Incendio
(Póliza POL 1 90 006 y POL 1 93 026, y cláusulas adicionales y opcionales correspondientes. Si la compañía opera con otras pólizas y cláusulas se deberá, en lo posible, hacer la equivalencia).
1 Cobertura básica (Incendio Ordinario) (POL 1 90 006)
2 Cobertura básica (Perjuicios por Paralización) (POL 1 93 026)
3 Incendio o explosión a consecuencia directa de huelga, desorden popular o actos terroristas (CAD 1 90 011)
4 Daños materiales a consecuencia directa de huelga o desorden popular (CAD 1 90 012)
5 Saqueo durante huelga o desorden popular (CAD 1 90 013)
6 Daños materiales causados por aeronaves (CAD 1 90 007)
7 Daños materiales causados por roturas de cañerías o por desbordamiento de estanques matrices (CAD 1 90
009)
8 Descomposición de productos depositados en frigoríficos (CAD 1 90 010)
9 Daños materiales causados por peso de nieve o hielo (CAD 1 90 024)
10 Remoción de escombros (CAD 1 90 025)
11 Incendio a consecuencia de fenómenos de la naturaleza excepto sismo (CAD 1 91 003)
12 Daños materiales causados por viento (CAD 1 90 014)
13 Daños materiales causados por filtración de lluvia, inundación y desbordamiento de cauces (CAD 1 90 015)
14 Daños materiales causados por salida de mar (CAD 1 90 016)
15 Incendio a consecuencia de sismo (CAD 1 91 002)
16 Daños materiales causados por sismo (CAD 1 90 019)
17 Daños materiales causados por explosión (CAD 1 90 020)
18 Combustión espontánea (CAD 1 90 021)
19 Daños materiales causados por Vehículos Motorizados (CAD 1 90 008)
20 Daños materiales a harina de pescado (CAD 1 90 022)
21 Avalanchas, aluviones y deslizamientos (CAD 1 90 017)
22 Daños materiales por choques o colisión con objetos fijos o flotantes, incluyendo naves (CAD 1 90 023)

23 Otros
Garantía
24 Seriedad de oferta
25 Cumplimiento de contrato
26 Correcta inversión de anticipo
27 Canje de retenciones