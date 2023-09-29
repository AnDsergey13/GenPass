from Config import get_value_by_key
import System


language_folder = "locale/"


def __get_language_from_config_file():
	"""TODO: Write docstring"""
	# TODO: Перамясціць ў config?
	return get_value_by_key("LANG")


def __get_localization_file(name_file):
	"""TODO: Write docstring"""
	# FIXME: Здаецца тут няпраўда, бо вяртаюцца даныя, а не файл
	full_name = language_folder + name_file + ".json"
	return System.get_data_from_file(json_file_name=full_name)


def get_text(key):
	""" Получить текст по ключу

		Пример использования:
		_ = get_text
		print(_("Err. Invalid input"))
	"""
	name_file = __get_language_from_config_file()
	file = __get_localization_file(name_file)
	if key in file:
		return file[key]
	else:
		print("Записи с таким ключом, не существует. Введите другой")
		return None


# TODO: выделить из методов add_key_in_all_lang и del_key_in_all_lang повторяющийся код
# и вынести его в отдельный метод или декоратор
def add_key_in_all_lang(new_key: str):
	""" Добавляет новый ключ во все json файлы """
	list_file_names = System.get_file_names(remove_extensions=False)

	# Перебираем каждый json файл в папке
	for name_file in list_file_names:
		full_name = language_folder + name_file
		# Получаем данные из файла
		data = System.get_data_from_file(json_file_name=full_name)
		if new_key not in data:
			# Записываем пустое значение под новым ключом
			data[new_key] = ""
			# Сохраняем изменения
			System.set_data_to_file(data=data, json_file_name=full_name)
		else:
			print("Запись с таким ключом, уже существует. Введите другой")


def del_key_in_all_lang(key: str):
	""" Удаляет ключ во всех json файлах """
	list_file_names = System.get_file_names(remove_extensions=False)

	# Перебираем каждый json файл в папке
	for name_file in list_file_names:
		full_name = language_folder + name_file
		# Получаем данные из файла
		data = System.get_data_from_file(json_file_name=full_name)
		if key in data:
			del data[key]
			# Сохраняем изменения
			System.set_data_to_file(data=data, json_file_name=full_name)
		else:
			print("Записи с таким ключом, не существует. Введите другой")
