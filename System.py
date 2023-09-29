import json
import locale
import os
import sysconfig

TYPE_OS = ["Linux", "Android", "Windows", "Other"]


# FIXME: Переделать ниже
def getLanguageOS():
	if locale.getlocale()[0] == "ru_RU":
		return "ru_RU"
	else:
		return "en_US"


def getLocalization():
	""" !!!!! переделать!!!! на json формат"""
	localization = []
	with open(f"locale/{getLanguageOS()}", 'r', encoding="utf-8") as f:
		for line in f.readlines():
			# [:-1] Cut a new line symbol. He's not needed
			# [:-1] Отрезаем символ новой строки. Он не нужен
			localization.append(line[:-1])

	return localization


def getCurrentOS():
	# Использовать case?
	OS = sysconfig.get_platform()
	if OS == "linux-x86_64":  # Linux
		return TYPE_OS[0]
	elif OS == "linux-aarch64":  # Android
		return TYPE_OS[1]
	elif OS == "win-amd64":  # Windows
		return TYPE_OS[2]
	else:  # Other
		return TYPE_OS[3]


def getNameUser():
	return None

# FIXME: Переделать выше


def is_file(name_file, path_file=""):
	""" """
	# TODO: Спрасціць логіку, зрабіўшы значэнне па змаўчанні
	if path_file == "":
		path_file = get_standart_path()

	# Проверить. Будет ли косая черта работать для Windows
	# TODO: os.separator?
	full_path_with_name = path_file + "/" + name_file
	# TODO: Розніца паміж os.path.isfile і os.path.exists?
	return os.path.isfile(full_path_with_name)


def is_path(path):
	""" """
	return os.path.isdir(path)


def get_standart_path():
	""" """
	return os.getcwd()


def get_file_names(folder_path="locale", remove_extensions=True):
	""" """
	if remove_extensions:
		return [nameFile.replace(".json", "") for nameFile in os.listdir(folder_path)]
	else:
		return os.listdir(folder_path)


def get_data_from_file(json_file_name):
	"""Получаем данные из json файла"""
	with open(json_file_name, encoding="UTF-8") as f:
		return json.load(f)


def set_data_to_file(data, json_file_name):
	"""Перезаписываем данные в json файл"""
	with open(json_file_name, "w", encoding="UTF-8") as f:
		json.dump(data, f, ensure_ascii=False)
