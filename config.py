import system


# TODO: Использовать многоязычный docstrings (PEP 257? Sphinx? docutils?), не в функции, а отдельным файлом
# https://stackoverflow.com/questions/27214065/how-to-docstring-in-python-for-multiple-languages
# нужна ли генерация html документации? https://youtu.be/BWIrhgCAae0

def _in_key(func):
	def wrapper(key, *args):
		""" Проверяем, содержится ли введённый ключ в файле конфигураций"""
		data = system.get_data_from_file(json_file_name=get_file_name())
		if key in data:
			return func(key, *args)
		else:
			# TODO: Предусмотреть локализацию
			print(f"Параметр KEY, указан не верно! Допустимые значения = {list(data.keys())}")
	return wrapper


_settings_file_name = "Config.json"

template_for_creating_file = {
	"use_gui": None,
	"LANG": "",
	"path_LUK": "",
	"path_Database": ""
}


def __get_template():
	"""Получаем шаблон для создания конфигурационного файла"""
	return template_for_creating_file


def get_file_name():
	"""Получаем название конфигурационного файла"""
	return _settings_file_name


def set_file_name(new_name):
	"""Изменяем название конфигурационного файла"""
	# TODO: Сделать проверку корректности введённого имени
	global _settings_file_name
	_settings_file_name = new_name


def __check_language_in_list(language, list_of_languages):
	"""Существует ли указанный язык в списке языков"""
	return language in list_of_languages


@_in_key
def get_value_by_key(key):
	""" Извлекаем данные из файла, по ключу

		Пример вызова.
		get_value_by_key("path_Database")
		Вывод:
		/home/user/GenPass/Database.json
	"""
	# Получаем данные
	data = system.get_data_from_file(json_file_name=get_file_name())
	return data[key]


@_in_key
def change_value_by_key(key, new_value):
	""" Изменяем данные в файле по ключу

		Пример вызова.
		change_value_by_key("path_LUK", "/home/Work/Python/")
	"""
	# Получаем данные
	data = system.get_data_from_file(json_file_name=get_file_name())
	# Изменяем на новые
	data[key] = new_value
	# Записываем в файл конфигурации
	system.set_data_to_file(data=data, json_file_name=get_file_name())


def create_file():
	""" Создаёт конфигурационный файл с отсутствующими настройками"""

	# Проверка сделана с целью защиты от перезаписи файла при повторном запуске функции
	if not system.is_file(get_file_name()):
		# Получаем шаблон
		data = __get_template()
		# Создаём новый конфигурационный файл по шаблону
		system.set_data_to_file(data=data, json_file_name=get_file_name())

		# Устанавливаем значения по умолчанию
		__write_down_basic_settings()


def __write_down_basic_settings():
	""" """
	change_value_by_key("use_gui", _get_basic_gui_settings())
	change_value_by_key("LANG", __get_basic_language())

	standard_path = system.get_standard_path()
	if system.is_path(standard_path):
		change_value_by_key("path_LUK", standard_path)
		change_value_by_key("path_Database", standard_path)
	else:
		# TODO: Предусмотреть локализацию
		print(f"Указанный путь {standard_path} - не корректен! Оставляем пустые значения")


# TODO: Сделать проверку try/except для типа вводимого сообщения
def __get_basic_language(language=""):
	""" """
	if language == "":
		# Если предпочтительный язык не был введён, то выбираем язык текущей операционной системы
		return system.get_language_os()
	elif not __check_language_in_list(language, system.get_file_names()):
		# Проверяем введённый язык на правильность ввода
		# И если он не правильный, то автоматически выбираем язык по умолчанию
		language_os = system.get_language_os()
		# TODO: Предусмотреть локализацию
		print(f"Указанного языка не существует. Выбран {language_os} по умолчанию")
		return language_os
	else:
		# Если указанный язык был введён правильно, то возвращаем его для дальнейших операций
		return language


def _get_basic_gui_settings(use_gui=False):
	""" """
	default_value = False
	try:
		convert_use_gui = bool(use_gui)
	except (ValueError, TypeError) as err:
		print(err)
		# TODO: Предусмотреть локализацию
		print(f"GUI. Config. Установлено значение по умолчанию = {default_value}")
		return default_value
	else:
		return convert_use_gui
