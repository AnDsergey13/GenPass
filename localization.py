from Config import ConfigFile as cf
import System


class LanguageManager:
	""" """
	language_folder = "locale/"

	@staticmethod
	def __get_language_from_config_file():
		""" """
		return cf.get_value_by_key("LANG")

	@staticmethod
	def __get_localization_file(name_file):
		""" """
		full_name = __class__.language_folder + name_file + ".json"
		return System.get_data_from_file(json_file_name=full_name)

	@staticmethod
	def get_value_by_key(key):
		""" Пример использования:
			_ = LanguageManager.get_value_by_key
			print(_("Err. Invalid input"))
		"""
		name_file = __class__.__get_language_from_config_file()
		file = __class__.__get_localization_file(name_file)
		if key in file:
			return file[key]
		else:
			print("Записи с таким ключом, не существует. Введите другой")
			return None

	# TODO выделить из методов add_key_in_all_lang и del_key_in_all_lang повторяющийся код
	# И вынести его в отдельный метод или декоратор
	@staticmethod
	def add_key_in_all_lang(new_key: str):
		""" Добавляет новый ключ во все json файлы """
		list_file_names = System.get_file_names(remove_extensions=False)

		# Перебираем каждый json файл в папке
		for name_file in list_file_names:
			full_name = __class__.language_folder + name_file
			# Получаем данные из файла
			data = System.get_data_from_file(json_file_name=full_name)
			if new_key not in data:
				# Записываем пустое значение под новым ключом
				data[new_key] = ""
				# Сохраняем изменения
				System.set_data_to_file(data=data, json_file_name=full_name)
			else:
				print("Запись с таким ключом, уже существует. Введите другой")

	@staticmethod
	def del_key_in_all_lang(key: str):
		""" Удаляет ключ во всех json файлах """
		list_file_names = System.get_file_names(remove_extensions=False)

		# Перебираем каждый json файл в папке
		for name_file in list_file_names:
			full_name = __class__.language_folder + name_file
			# Получаем данные из файла
			data = System.get_data_from_file(json_file_name=full_name)
			if key in data:
				del data[key]
				# Сохраняем изменения
				System.set_data_to_file(data=data, json_file_name=full_name)
			else:
				print("Записи с таким ключом, не существует. Введите другой")
