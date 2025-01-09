# Resumen del Script

Este script en Python permite procesar archivos ZIP que contienen archivos PDF, renombrar los PDFs con un formato específico, y generar un nuevo archivo ZIP con los nombres actualizados.

## Funcionalidades Principales

1. **Renombrar Archivos PDF**: Los nombres de los PDFs son modificados según un formato predefinido que incluye datos como el mes en texto (e.g., "Enero") extraídos del nombre original.
2. **Eliminar Archivos Existentes**: Si el archivo ZIP de salida ya existe, se elimina para evitar conflictos.
3. **Crear un ZIP Modificado**: Los PDFs renombrados se guardan en un nuevo archivo ZIP en una carpeta llamada `modificado`.

## Uso

1. Asegúrate de colocar el archivo ZIP que contiene los PDFs en la misma carpeta que el script.
2. Ejecuta el script con:

```bash
python nombre_del_script.py
```

3. El script procesará los PDFs dentro del ZIP y generará un nuevo ZIP renombrado en la carpeta `modificado`.

## Notas

- Los nombres de los archivos PDF deben seguir un formato específico para que el renombrado funcione correctamente.
- Si no se encuentran archivos ZIP en el directorio, el script lo indicará.

## Dependencias

Este script utiliza únicamente bibliotecas estándar de Python:
- `os`
- `zipfile`

## Personalización

Puedes ajustar la función `rename_pdf_file` para cambiar el formato de renombrado según tus necesidades.