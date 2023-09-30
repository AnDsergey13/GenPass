import json
import locale
import os
import sysconfig

TYPE_OS = ["Linux", "Android", "Windows", "Other"]


# FIXME: Переделать ниже
def get_language_os():
	if locale.getlocale()[0] == "ru_RU":
		return "ru_RU"
	else:
		return "en_US"


# def getLocalization():
# 	""" !!!!! переделать!!!! на json формат"""
# 	localization = []
# 	with open(f"locale/{getLanguageOS()}", 'r', encoding="utf-8") as f:
# 		for line in f.readlines():
# 			# [:-1] Cut a new line symbol. He's not needed
# 			# [:-1] Отрезаем символ новой строки. Он не нужен
# 			localization.append(line[:-1])
#
# 	return localization


def get_current_os():
	# Использовать case?
	os_ = sysconfig.get_platform()
	if os_ == "linux-x86_64":  # Linux
		return TYPE_OS[0]
	elif os_ == "linux-aarch64":  # Android
		return TYPE_OS[1]
	elif os_ == "win-amd64":  # Windows
		return TYPE_OS[2]
	else:  # Other
		return TYPE_OS[3]


def get_name_user():
	return None

# FIXME: Переделать выше


def is_file(name_file, path_file=""):
	""" """
	# TODO: Упростить логику, используя значение по умолчанию
	if path_file == "":
		path_file = get_standard_path()

	# Проверить. Будет ли косая черта работать для Windows
	# TODO: os.separator?
	full_path_with_name = path_file + "/" + name_file
	# TODO: Разница между os.path.isfile и os.path.exists?
	return os.path.isfile(full_path_with_name)


def is_path(path):
	""" """
	return os.path.isdir(path)


def get_standard_path():
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
	with open(json_file_name, encoding="UTF-8") as file:
		return json.load(file)


def set_data_to_file(data, json_file_name):
	"""Перезаписываем данные в json файл"""
	with open(json_file_name, "w", encoding="UTF-8") as file:
		json.dump(data, file, ensure_ascii=False)


def delete_luk_file():
	# TODO: Переписать?
	os.remove("LUK")
