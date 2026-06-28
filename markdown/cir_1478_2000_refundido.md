<!-- source: cir_1478_2000_refundido.pdf -->
<!-- language: es -->
<!-- note: Las fórmulas matemáticas extraídas de PDFs pueden ser incompletas.
     Los bloques marcados con ⚠️ deben verificarse contra el PDF original. -->

# CIRCULAR N° 1478 — IMPARTE INSTRUCCIONES SOBRE VALIDACION FISICA DEL MEDIO MAGNETICO QUE RESPALDA LA INFORMACION FINANCIERA


Para todas las sociedades inscritas en el Registro de Valores, así como aquellas que por ley deban regirse por las normas de sociedades anónimas abiertas o deban presentar estados financieros de acuerdo a estas últimas. Las instrucciones de la presente Circular no son aplicables a las Compañías de Seguros.
Considerando la gran cantidad de errores que se detecta cada trimestre en el procesamiento del medio magnético que respalda la información financiera, que en cumplimiento de la normativa vigente remiten las sociedades a las que hace referencia la presente circular, esta Superintendencia ha estimado necesario hacer entrega de un software básico de validación física, que permita asegurar que la información contenida en el medio magnético se ajusta a los formatos y estructuras, definidos para tales efectos en la Circular Nº 1048 de 1991 y sus modificaciones.
Se entenderá por validación física la revisión del contenido del archivo, por ejemplo, verificar que los códigos informados correspondan a un código de FECU, que los datos vengan de acuerdo a su definición numérica o alfanumérica, que las fechas y RUT sean válidos, que en los caracteres alfanuméricos se informe texto válido sin caracteres especiales o de control, etc..
Los requerimientos de hardware y software para el funcionamiento de este programa son mínimos.
Tales requerimientos así como su instructivo de uso se encuentran detallados en Anexo Técnico.
Es obligatorio que las sociedades validen sus archivos a través de este software. La hoja de control que entrega este programa deberá venir firmada por el representante legal de la sociedad y ser presentada conjuntamente con el medio magnético y demás información financiera. Sólo se aceptarán aquellos medios magnéticos cuya hoja de control esté debidamente firmada e indique que la información no contiene errores.
Cabe hacer presente, que mientras no se recepcione el medio magnético y su hoja de control sin errores, la sociedad se encontrará en incumplimiento de las disposiciones de envío de información continua impartidas por esta Superintendencia.
Será responsabilidad de la administración de la sociedad verificar los errores de carácter lógico
(consistencia de los datos), como por ejemplo cuadraturas, razón por la cual si al cargar y validar la información en las bases de datos de la Superintendencia se detectan errores de este tipo, se solicitará que se reenvíe el medio magnético con los datos corregidos y validados nuevamente.
VIGENCIA Las instrucciones impartidas por medio de la presente circular rigen a contar de esta fecha.

### ANEXO TECNICO
## 1. Introducción
El objetivo del presente documento es servir de guía de instalación y uso de la aplicación informática denominada Validación Física FECU - "FECUSA", desarrollado por la Superintendencia de Valores y Seguros.
Este software ha sido concebido para que la información que Ud. remite a la SVS, sea enviada sin errores físicos. Además, permite imprimir el listado de errores si existen, o bien imprimir un listado de control, afirmando que la información es enviada sin errores físicos.
Esta aplicación toma como entrada el archivo "FECUmmaa.dat" que Ud. prepara cada trimestre para enviar a esta Superintendencia, según lo señalado en la Circular Nº 1.048 y sus modificaciones. Sólo valida físicamente, no incluye validaciones de cuadraturas de cuentas, ni permite ingresar datos, ni corregirlos. En el caso de que el validador arroje errores, Ud. deberá modificar los datos en la aplicación que usa para generar el archivo o directamente con el editor de texto corregir el archivo de datos.
## 2. Instalación y ejecución de la aplicación
2.1. Requerimientos de la aplicación
Para el correcto funcionamiento de la aplicación se requiere como mínimo:
- Un computador personal (PC) compatible, con procesador 80386 o superior.
- 1 Mb. de memoria RAM.
- Unidad de disco duro con al menos 150 Kb. disponibles.
- Unidad de diskette de 3 ½ pulgadas de 1.44 Mb.
- Impresora láser HP compatible, conectada a la puerta LPT1.
- Sistema Operativo: DOS 6.2, Windows95, Windows98 o Windows2000.
2.2. Instalación
Previo a realizar la instalación del software se debe verificar lo siguiente:
- El directorio c:\fecusa no debiera existir, o en su defecto, encontrarse vacío, de tal
forma que la instalación del software no elimine archivos que puedan serle útiles.
Una vez chequeado el directorio, si se encuentra en ambiente DOS debe accesar directamente la unidad de diskette correspondiente, o bien bajo ambiente windows, accesarla a través del explorador. Posteriormente, ejecute el programa INSTALAR.BAT.
El proceso de instalación creará automáticamente el directorio FECUSA y copiará en él los archivos necesarios para la ejecución del sistema, de acuerdo a la siguiente estructura:

C:\ FECUSA
Una vez terminado el proceso de instalación, el directorio deberá contener los siguientes
archivos:
Directorio FECUSA:
### FECUSA.EXE CODIGOS.DAT
2.3. Restricciones
Para asegurar un buen funcionamiento del software, es necesario tener presente la
siguiente restricción:
- Si el PC se encuentra conectado a una red, es necesario que el directorio c:\fecusa
tenga acceso de lectura y escritura, al igual que los archivos que pertenecen a ese directorio. El software no está diseñado para ser operado en red como multiusuario.
La instalación debe ser local para asegurar un buen funcionamiento de éste.
2.4. Ejecución
Para ejecutar la aplicación "FECUSA" deberá:
En ambiente DOS: situarse en el directorio C:\FECUSA, digitar FECUSA y presionar
[Enter].
En ambiente Windows: crear en su escritorio un acceso directo donde se ejecute la aplicación FECUSA, o a través del explorador ir a la carpeta C:\FECUSA y hacer doble click con el botón izquierdo del mouse, en la aplicación FECUSA.EXE. Recuerde darle accesos de escritura al directorio C:\FECUSA.
Al ingresar a la aplicación se desplegará una pantalla donde se le solicitarán los
siguientes parámetros:
- Primero se pedirá el período de proceso con formato MMAA, donde MM representa
el mes con dos dígitos (si el mes es menor a 10, es necesario completar con un cero a la izquierda), y AA representa los dos últimos dígitos para el año.
- Luego se pedirá el balance (I para balance Individual y C para balance
Consolidado), y
- Finalmente se pedirá el drive (unidad de disco) donde se encuentra el archivo. Se
debe ingresar sólo la letra que lo identifica.

Al momento de procesar, se despliega por pantalla el nombre del archivo y al término de la validación el resultado de ella. Cuando termina el proceso, se pregunta si desea imprimir el archivo de errores. Debe tener presente que este informe se elimina al momento de salir de la aplicación, por lo cual no tiene opción de imprimirlo posteriormente, salvo que nuevamente valide el archivo.
Superintendencia de Valores y Seguros Validación Física F.E.C.U. Sociedades Anónimas Ingrese Período de Validación (MMAA) :
Tipo de balance a Procesar : I Drive : C Archivo a Procesar : c: FECU1299.DAT Información SIN Errores Desea imprimir (S/N) ?