import dicom2jpg
import os

#откуда берем
dicom_dir = r'D:\checkcheck\import'
#куда выгружаем фотки
export_location = r'D:\checkcheck\export'

for filename in os.listdir(dicom_dir):
    old_file = os.path.join(dicom_dir, filename)

    if os.path.isfile(old_file):
        new_file = os.path.join(dicom_dir, os.path.splitext(filename)[0] + '.dcm')
        os.rename(old_file, new_file)

print("Расширения файлов успешно изменены.")

if __name__ == '__main__':
    dicom2jpg.dicom2bmp(dicom_dir, target_root=export_location)
    print("\n\n\n\n\n\nКонвертировано")