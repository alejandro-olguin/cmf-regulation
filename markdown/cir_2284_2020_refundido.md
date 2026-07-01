<!-- source: cir_2284_2020_refundido.pdf -->
<!-- language: es -->
<!-- note: Las fórmulas matemáticas extraídas de PDFs pueden ser incompletas.
     Los bloques marcados con ⚠️ deben verificarse contra el PDF original. -->

# CIRCULAR N° 2284

### SISTEMA DE RIESGOS
(Instrucciones generales)
## 1. ARCHIVOS DEL SISTEMA DE RIESGOS
Este sistema comprende todos los archivos signados con la letra “R”, indicados en el Catálogo de Archivos.
## 2. MONEDA
Todos los montos deberán ser informados en pesos, salvo que en las instrucciones del respectivo archivo se indique expresamente lo contrario.
Los saldos de operaciones pagaderas en monedas extranjeras deberán convertirse a pesos chilenos, de acuerdo con el tipo de cambio de representación contable utilizado por el banco.
Circular N°2.284 / 31.12.2020 por Resolución N°7192

CÓDIGO : R11
NOMBRE : CALIFICACIÓN DE BANCOS DE IMPORTANCIA
SISTÉMICA SISTEMA : Riesgo PERIODICIDAD : Mensual PLAZO : 9 días hábiles.
En este archivo se informarán los factores del índice que determina el grado de importancia sistémica de un banco, asociado a su relevancia para el funcionamiento del sistema financiero local producto de su deterioro financiero o eventual insolvencia. Entre los factores se encuentran el tamaño, la interconexión con otras entidades financieras, el grado de sustitución en la prestación de servicios financieros y la complejidad de su modelo de negocios y estructura operativa.
Todos los valores monetarios deben reflejarse en millones de pesos.
Primer registro
1. Código del banco ............................................................................................. 9(04)
2. Identificación del archivo ............................................................................... X(03)
3. Período .............................................................................................................. P(06)
4. Filler................................................................................................................... X(03)
Largo del registro ........................... 16 bytes
## 1. CÓDIGO DEL BANCO
Corresponde al código que identifica al banco.
## 2. IDENTIFICACIÓN DEL ARCHIVO
Corresponde a la identificación del archivo. Debe ser "R11".
## 3. PERÍODO
Corresponde al mes (AAAAMM) al cual se refiere la información.
Registro siguiente El registro siguiente contendrá información sobre los factores y sub-factores que establecen el grado de importancia sistémica de un banco, correspondientes al periodo al que se refiere la información.
Registro para informar factores y sub-factores del índice de importancia sistémica
1. Factor y sub-factor ................................................................................. 9(02)
2. Monto ....................................................................................................... 9(14)
Largo del registro ............. 16 bytes
## 1. FACTOR Y SUB-FACTOR
Corresponde al código asociado al factor y sub-factor de acuerdo con lo señalado en el numeral 3.1 del Capítulo 21-11 de la RAN. Se deberá indicar el factor y sub-factor según los códigos de la Tabla 106 de este Manual.
## 2. MONTO
Corresponde al monto del sub-factor reportado en el campo anterior, de acuerdo con lo señalado en el numeral 3.1 del Capítulo 21-11 de la RAN.
Circular N°2.284 / 31.12.2020 por Resolución N°7192

Archivo R11 Hoja 2 Carátula de cuadratura El archivo R11 debe entregarse con una carátula de cuadratura cuyo modelo se
especifica a continuación:
MODELO Institución: ________________________________ Código: _______ Información correspondiente al mes de: _________________ Archivo R11

| Número de registros |  |
| --- | --- |

Observaciones Para el reporte de los valores solicitados en este archivo se deben seguir los lineamientos entregados en la Tabla 106 de este Manual.
Circular N°2.284 / 31.12.2020 por Resolución N°7192

Tabla 106 Tabla 106: Sub-factores del Índice de importancia sistémica.

| Código | Factor | Sub-factor |
| --- | --- | --- |
| 1 | Tamaño | Activos consolidados locales. |
| 2 | Interconexión local | Activos dentro del sistema financiero chileno. |
| 3 | Interconexión local | Pasivos dentro del sistema financiero chileno. |
| 4 | Sustituibilidad local | Monto de actividades de pago. |
| 5 | Sustituibilidad local | Número de actividades de pago |
| 6 | Sustituibilidad local | Depósitos. |
| 7 | Sustituibilidad local | Colocaciones. |
| 8 | Complejidad | Contratos derivados OTC. |
| 9 | Complejidad | Activos inter-jurisdiccionales. |
| 10 | Complejidad | Pasivos inter-jurisdiccionales. |
| 11 | Complejidad | Activos a valor razonable. |
| 12 | Complejidad | Activos de terceros bajo la administración del banco. |

Definiciones
1. Activos Consolidados Locales: Corresponde a los activos a nivel local del
banco y sus filiales con domicilio en Chile, de acuerdo a los criterios contables de aceptación general que se refiere el Compendio de Normas Contables para bancos, al cierre del mes de referencia del archivo.
2. Activos dentro del sistema financiero chileno: Corresponde a todos los
activos del banco a nivel consolidado global cuyas contrapartes sean entidades financieras fiscalizadas por esta Comisión, bancarios o no bancarias, en Chile, al cierre del mes de referencia del archivo. Los activos deberán valorarse de acuerdo con los criterios contables de aceptación general que se refiere el Compendio de Normas Contables para bancos. En aquellos contratos derivados en que se establezca la obligación de liquidar o pagar el valor razonable acumulado antes de su vencimiento, se deberá deducir de su valor el monto compensado.
Las entidades financieras quedarán determinadas por los códigos entre 212 y 237 de la tabla 11 de este Manual.
3. Pasivos dentro del sistema financiero chileno: Corresponde a todos los
pasivos del banco a nivel consolidado global cuyas contrapartes sean entidades financieras fiscalizadas por esta Comisión, bancarias o no bancarias, en Chile, al cierre del mes de referencia del archivo. Los pasivos deberán valorarse de acuerdo con los criterios contables de aceptación general que se refiere el Compendio de Normas Contables para bancos. En aquellos contratos derivados en que se establezca la obligación de liquidar o pagar el valor razonable acumulado antes de su vencimiento, se deberá deducir de su valor el monto compensado.
Para determinar el país de la contraparte se debe considerar la emisión primaria de los instrumentos. Las entidades financieras quedarán determinadas por los códigos entre 212 y 237 de la tabla 11 de este Manual.
Circular N°2.284 / 31.12.2020 por Resolución N°7192

Tabla 106 Hoja 2
## 4. Monto de actividades de pago: Corresponde a los montos asociados a
pagos intermediados en la economía local, durante el mes de referencia del archivo, ya sea directamente o a través de cámaras de compensación. Para esto, se deben considerar las instrucciones de transferencia de fondos emitidas directamente en el sistema LBTR (MT103, MT202, MT202COV, MT205 y MT205COV), tanto en moneda nacional como en dólares; como también sus saldos netos deudores que se liquidan en LBTR, informados por la Institución de Turno, tanto de la Cámara de Compensación de Cheques y otros documentos en moneda nacional y en dólares en el país, como de la Cámara de Compensación de Cajeros Automáticos en el país;
además de los montos de las órdenes de pago aceptadas por la Cámara de Compensación de Pagos de Alto Valor en Moneda Nacional en el país (pagos brutos), para su compensación y posterior liquidación en el sistema LBTR.
Las cifras en dólares se informan en pesos, de acuerdo al tipo de cambio de representación contable.
## 5. Número de actividades de pago: Corresponde al número de pagos
intermediados en la economía local, del banco y sus filiales locales, durante el mes de referencia del archivo, ya sea directamente o a través de cámaras de compensación. Se considera el número de pagos que hagan los tarjeta habientes a través de tarjetas de crédito, débito o provisión de fondos, incluyendo los pagos automáticos (PAC y PAT y pago automático de nómina).
Además, se incluye el número de cheques que se compensan durante el mes en la Cámara de Compensación de Cheques y otros documentos en moneda nacional y en dólares en el país, como también aquellos girados y pagados contra cuentas del mismo banco, y la cantidad de transferencias electrónicas de fondos que se realicen tanto entre cuentas dentro del mismo banco, como en aquellas en que el abono en cuenta o pago al respectivo beneficiario deba efectuarse en otro banco, a las que se refiere las disposiciones del Capítulo 1-7 de la RAN.
6. Depósitos: Corresponde a los depósitos a la vista, otros saldos y cuentas a la
vista, depósitos a plazo y cuentas de ahorro a plazo y otros saldos acreedores a plazo, al cierre del mes de referencia del archivo. Se debe considerar el nivel de consolidación local, y las cuentas contables asociadas a “Depósitos y otras obligaciones a la vista” y “Depósitos y otras captaciones a plazo” de acuerdo con los criterios contables de aceptación general que se refiere el Compendio de Normas Contables para bancos.
7. Colocaciones: Corresponde a las colocaciones de consumo, hipotecarias
para la vivienda, préstamos comerciales, créditos de comercio exterior, deudores en cuentas corrientes, operaciones de factoraje, operaciones de leasing y otros créditos y cuentas por cobrar, al cierre del mes de referencia del archivo.
Se debe considerar el nivel de consolidación local, y las cuentas contables asociadas a “Total Colocaciones”, brutas de provisiones específicas, de acuerdo con los criterios contables de aceptación general que se refiere el Compendio de Normas Contables para bancos.
8. Contratos derivados OTC: Corresponde al valor nocional de contratos
negociados de manera bilateral y que no han sido novados en una Entidad de Contraparte Central, al cierre del mes de referencia del archivo. Se considera la información a nivel consolidado global, excluyendo entonces los derivados entre el banco y sus filiales.
## 9. Activos inter-jurisdiccionales: Corresponde a todas las posiciones
activas, créditos, títulos de deuda y derivados, a nivel consolidado global con contrapartes en el exterior, al cierre del mes de referencia del archivo. Para ello se debe considerar los activos en el cual el país de residencia de la contraparte sea distinto a Chile. La información reportada debe tener consistencia con otros archivos que se utilicen para otros efectos (C17 y D05).
Circular N°2.284 / 31.12.2020 por Resolución N°7192

Tabla 106 Hoja 3
10. Pasivos inter-jurisdiccionales: Corresponde a todas las posiciones pasivas,
depósitos, títulos de deuda y derivados, a nivel consolidado global con contrapartes en el exterior, al cierre del mes de referencia del archivo. Para ello se debe considerar los pasivos en el cual el país de residencia de la contraparte sea distinto a Chile. La información reportada debe tener consistencia con otros archivos que se utilicen para otros efectos (C17). Para determinar el país de la contraparte se debe considerar la emisión primaria de los instrumentos.
11. Activos a valor razonable: Corresponde a los instrumentos a valor razonable
de acuerdo con lo instruido en el Capítulo 7-12 de la RAN, excluyendo derivados, al cierre del mes de referencia del archivo. Para ello se debe considerar los activos a nivel consolidado global, de acuerdo con los criterios contables de aceptación general que se refiere el Compendio de Normas Contables para bancos. De dicho cómputo se deben excluir los activos líquidos de nivel 1 y 2, de acuerdo con lo establecido en la tabla 87 de este Manual.
12. Activos de terceros bajo la administración del banco: Considera los
activos adquiridos a nombre propio con recursos de terceros, a nivel consolidado global, al cierre del mes de referencia del archivo. La información reportada debe ser consistente con la cuenta “recursos de terceros gestionados por el banco”, de acuerdo con la información complementaria del Compendio de Normas Contables para bancos.
Circular N°2.284 / 31.12.2020 por Resolución N°7192