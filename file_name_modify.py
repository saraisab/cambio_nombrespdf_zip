import os
import zipfile


def rename_pdf_file(name_pdf):
    """
    Renames the pdf file
    :param name_pdf: str: name of the pdf to change
    :return: the new name to the pdf file
    """
    # Months dictionary
    months = {
        "01": "Enero",
        "02": "Febrero",
        "03": "Marzo",
        "04": "Abril",
        "05": "Mayo",
        "06": "Junio",
        "07": "Julio",
        "08": "Agosto",
        "09": "Septiembre",
        "10": "Octubre",
        "11": "Noviembre",
        "12": "Diciembre"
    }
    list = name_pdf.split('_')
    month_number = months[list[7][0:2]]
    return f"NDOC_PRV_{list[4]}{list[6].lstrip('0')}_{month_number}{list[7][-2:]}.pdf"


def delete_file_if_exists(path):
    """
    Delete file modified if exists
    :param path: path: string
    """
    if os.path.exists(path):
        os.remove(path)
        print(f'El archivo {path} ha sido borrado.\n')


def create_new_zip():
    """
    Creates a new zip file in the folder especificated
    """
    lines = "-" * 20
    folder = os.getcwd()
    path_modified = os.path.join(folder, 'modificado', 'exportar_spec.zip')
    delete_file_if_exists(path_modified)
    # Aseguramos que la carpeta de salida exista
    os.makedirs(os.path.dirname(path_modified), exist_ok=True)

    zip_files_found = False  # Para verificar si encontramos archivos ZIP

    for file in os.listdir(folder):  # Busco en la carpeta los archivos
        if file.endswith('zip'):  # Si encuentra un archivo ZIP
            zip_files_found = True
            zip_original_path = os.path.join(folder, file)

            print(f"Procesando archivo ZIP: {zip_original_path}\n{lines}")

            # Leer el archivo ZIP original
            with zipfile.ZipFile(zip_original_path, mode='r') as zip_original:
                # Crear o abrir el archivo ZIP modificado
                with zipfile.ZipFile(path_modified, mode='a') as zip_temporal:
                    # Iterar sobre los archivos dentro del ZIP original
                    for pdf_file in zip_original.namelist():
                        # Renombrar el archivo
                        new_name = rename_pdf_file(pdf_file)
                        # Leer el contenido del archivo del ZIP original
                        content = zip_original.read(pdf_file)
                        # Escribir el contenido en el nuevo archivo ZIP con el nuevo nombre
                        zip_temporal.writestr(new_name, content)

    if not zip_files_found:
        print(f"No se encontraron archivos ZIP en la carpeta.\n{lines}")
    else:
        print(f"Proceso completado. El archivo ZIP modificado se encuentra en: {path_modified}\n{lines}")


if __name__ == '__main__':
    create_new_zip()
    print('Proceso finalizado')
    input('Presione cualquier tecla para continuar...')



