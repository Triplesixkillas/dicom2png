import dicom2jpg
import os
import pydicom

dicom_dir = r'D:\checkcheck\import'
export_location = r'D:\checkcheck\export'

for filename in os.listdir(dicom_dir):
    old_file = os.path.join(dicom_dir, filename)

    if os.path.isfile(old_file):
        new_file = os.path.join(dicom_dir, os.path.splitext(filename)[0] + '.dcm')
        os.rename(old_file, new_file)

print("Расширения файлов успешно изменены.")

def is_valid_dicom(file_path):
    try:
        dicom_file = pydicom.dcmread(file_path)
        return hasattr(dicom_file, 'PixelData')
    except Exception as e:
        print(f"Ошибка при чтении {file_path}: {e}")
        return False

if __name__ == '__main__':
    valid_files = [f for f in os.listdir(dicom_dir) if is_valid_dicom(os.path.join(dicom_dir, f))]
    if valid_files:
        dicom2jpg.dicom2bmp([os.path.join(dicom_dir, f) for f in valid_files], target_root=export_location)
        print("\n\n\n\n\n\nКонвертировано")
    else:
        print("Нет валидных DICOM-файлов для конвертации.")
