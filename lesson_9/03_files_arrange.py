# -*- coding: utf-8 -*-


# Нужно написать скрипт для упорядочивания фотографий (вообще любых файлов)
# Скрипт должен разложить файлы из одной папки по годам и месяцам в другую.
# Например, так:
#   исходная папка
#       icons/cat.jpg
#       icons/man.jpg
#       icons/new_year_01.jpg
#   результирующая папка
#       icons_by_year/2018/05/cat.jpg
#       icons_by_year/2018/05/man.jpg
#       icons_by_year/2017/12/new_year_01.jpg
#
# Входные параметры основной функции: папка для сканирования, целевая папка.
# Имена файлов в процессе работы скрипта не менять, год и месяц взять из времени создания файла.
# Обработчик файлов делать в обьектном стиле - на классах.
#
# Файлы для работы взять из архива icons.zip - раззиповать проводником в папку icons перед написанием кода.
# Имя целевой папки - icons_by_year (тогда она не попадет в коммит)
#
# Пригодятся функции:
#   os.walk
#   os.path.dirname
#   os.path.join
#   os.path.normpath
#   os.path.getmtime
#   time.gmtime
#   os.makedirs
#   shutil.copy2
#
# Чтение документации/гугла по функциям - приветствуется. Как и поиск альтернативных вариантов :)
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

import os, time, shutil

#   +  os.walk - генерация имён файлов в дереве каталогов, сверху вниз (если topdown равен True),
#   либо снизу вверх (если False). Для каждого каталога функция walk
#   возвращает кортеж (путь к каталогу, список каталогов, список файлов)

#   os.path.dirname - os.path.dirname(path) - возвращает имя директории пути path.

#   +  os.path.join - os.path.join(path1[, path2[, ...]]) - соединяет пути с учётом особенностей операционной системы.

#   +  os.path.normpath - os.path.normpath(path) - нормализует путь, убирая избыточные разделители и ссылки на
#   предыдущие директории. На Windows преобразует прямые слеши в обратные.

#   +  os.path.getmtime - os.path.getmtime(path) - время последнего изменения файла, в секундах.

#   +  time.gmtime - time.gmtime([сек]) - преобразует время, выраженное в секундах с начала
#   эпохи в struct_time, где DST флаг всегда равен нулю.

#   os.makedirs - os.makedirs(path, mode=0o777, exist_ok=False) - создаёт директорию,
#   создавая при этом промежуточные директории.

#   shutil.copy2

import os, time, shutil


class FileOrganize:

    def __init__(self, path_for_organize, path_result):
        self.path_for_organize = os.path.normpath(path_for_organize)
        self.path_result = os.path.normpath(path_result)
        self.path_to_file = []

    def path_file(self):
        """Возвращает пути к файлам"""
        files = os.walk(self.path_for_organize)
        for dirpath, dirnames, filenames in files:
            for file in filenames:
                self.path_to_file.append(os.path.join(dirpath, file))

    def new_folder(self):
        """Берет по порядку файл и создает пустую папку,
        затем вызывает функцию копирования данного файла в созданную папку """
        for path in self.path_to_file:
            time_in_sec = os.path.getmtime(path)
            real_time = time.gmtime(time_in_sec)
            os.makedirs(os.path.join(self.path_result, str(real_time[0]), str(real_time[1])), exist_ok=True)
            shutil.copy2(path, os.path.join(self.path_result, str(real_time[0]), str(real_time[1])))


folder = FileOrganize()
folder.path_file()
folder.new_folder()

# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Основная функция должна брать параметром имя zip-файла и имя целевой папки.
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
