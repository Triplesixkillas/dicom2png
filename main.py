import dicom2jpg
import os
import pydicom
import concurrent.futures
import numpy as np

dicom_dir = r'D:\checkcheck\import'
export_location = r'D:\checkcheck\export'


def is_valid_dicom(file_path):
    try:
        dicom_file = pydicom.dcmread(file_path, stop_before_pixels=True)
        return hasattr(dicom_file, 'PixelData')
    except Exception as e:
        print(f"Ошибка при чтении {file_path}: {e}")
        return False


def process_dicom_file(file_path, target_root):
    if not is_valid_dicom(file_path):
        print(f"Файл {file_path} не является валидным DICOM файлом. Пропускаем.")
        return

    try:
        dicom2jpg.dicom2bmp(file_path, target_root)
        print(f"Файл {file_path} успешно конвертирован.")
    except Exception as e:
        print(f"Ошибка при конвертации {file_path}: {e}")


if __name__ == '__main__':
    valid_files = [os.path.join(dicom_dir, f) for f in os.listdir(dicom_dir)
                   if f.lower().endswith('.dcm') or is_valid_dicom(os.path.join(dicom_dir, f))]

    if valid_files:
        try:
            with concurrent.futures.ProcessPoolExecutor() as executor:
                future_to_file = {executor.submit(process_dicom_file, f, export_location): f for f in valid_files}
                for future in concurrent.futures.as_completed(future_to_file):
                    file = future_to_file[future]
                    try:
                        future.result()
                    except Exception as e:
                        print(f"Ошибка при обработке {file}: {e}")
        except Exception as e:
            print(f"Ошибка в процессе конвертации: {e}")
    else:
        print("Нет валидных DICOM-файлов для конвертации.")
