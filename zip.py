import os
import zipfile
import pandas as pd
from PyPDF2 import PdfReader
import warnings

warnings.filterwarnings("ignore", category=UserWarning, module='openpyxl.styles.stylesheet')


def create_archive():
    # Проверяем существует ли папка
    if not os.path.exists(r'C:\\Users\\sv_pa\\PycharmProjects\\QA_GURU_HW_6\\tmp'):
        # Создаем папку если её нет
        os.mkdir(r'C:\\Users\\sv_pa\\PycharmProjects\\QA_GURU_HW_6\\tmp')

    # Создаем архив
    with zipfile.ZipFile(r'C:\\Users\\sv_pa\\PycharmProjects\\QA_GURU_HW_6\\tmp\\archive.zip', 'w') as zf:
        # Добавляем файлы в архив
        for file in ['B-4.xlsx', 'NEW_FILE.csv', '']:
            # Склеиваем путь к файлам которые добавляют в архив
            add_file = os.path.join(r'C:\\Users\\sv_pa\\PycharmProjects\\QA_GURU_HW_6', file)
            # Добавляем файл в архив
            zf.write(add_file, os.path.basename(add_file))

# Проверяем содержимое файлов внутри архива без распаковки
def check_files_inside_zip(zip_path):
    with zipfile.ZipFile(zip_path, 'r') as zf:
        for filename in zf.namelist():
            print(f"\\nChecking {filename}:")

            if filename.endswith('.pdf'):
                # Читаем метаданные PDF
                with zf.open(filename, 'r') as f:  # Убедитесь, что файл открывается в двоичном режиме
                    reader = PdfReader(f)
                    info = reader.metadata
                    print(info.get('/Title'))

            elif filename.endswith('.xlsx'):
                # Просматриваем лист Excel
                with zf.open(filename) as f:
                    df = pd.read_excel(f, engine="openpyxl")
                    print(df.head())

            elif filename.endswith('.csv'):
                # Просматриваем строки CSV
                with zf.open(filename) as f:
                    data = f.read().decode('utf-8')
                    print(data.splitlines()[:5])

# Создаем архив
create_archive()

# Проверяем содержимое архива
check_files_inside_zip(r'C:\\Users\\sv_pa\\PycharmProjects\\QA_GURU_HW_6\\tmp\\archive.zip')


