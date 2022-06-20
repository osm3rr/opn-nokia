Script for consolidation of network parameter files

Requerimientos
python >= 3.8
pandas >= 1.4.2

Junio 20/2022, puntos cubiertos a revisar:

1. Lectura de los archivos de entrada e identiicación por tecnología.

2. Identificación y arreglo de los atributos de entrada, según lo esperado en los formatos de alertas temprana, por tecnología.
 - Revisar los atributos para 4G (fallas lte)
 - Revisar los atributos para 4G (lte)
 - Revisar los atributos para 3G (WBTS y WCDMA).
 - Revisar los atributos para 2G (GSM)
 
 3. Remover los valores duplicados, según la llave que aplique por tecnología.

 4. Consolida los datos leidos en archivos excel, que fungen de plantillas por tecnología.