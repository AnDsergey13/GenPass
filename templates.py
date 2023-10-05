import system
from config import get_value_by_key


class TemplatesManager:
	""" """

	__default_template = {
		"landmark phrase": "",
		"maximum password length": 64,
		"ignore characters": {
			")": False,
			"=": False,
			"_": False,
			"\"": False,
			":": False,
			"|": False,
			",": False,
			"^": False,
			".": False,
			"\\": False,
			"%": False,
			";": False,
			"#": False,
			"(": False,
			"*": False,
			"/": False,
			"'": False,
			"`": False,
			"?": False,
			"]": False,
			"-": False,
			"<": False,
			"}": False,
			"[": False,
			">": False,
			"{": False,
			"!": False,
			"&": False,
			"$": False,
			"@": False,
			"+": False
		}
	}

	def __init__(self):
		""" """
		self.__default_path = get_value_by_key("path_Templates")
		self.__name_file = "templates.json"
		self.__full_default_path = self.__default_path + "/" + self.__name_file

		# Создаём пустой файл шаблонов, если его нет
		if not system.is_file(self.__name_file, self.__default_path):
			# TODO переименовать переменные
			empty_data = {}
			data = self.__add_empty_template(empty_data)
			system.set_data_to_file(data=data, json_file_name=self.__full_default_path)

		self.__all_templates = system.get_data_from_file(self.__full_default_path)
		# Все изменения будем производить с копией данных файла шаблонов
		# Нужно для того, чтобы работала отмена изменений в файле(при запуске GUI)
		self.__modified_all_templates = self.__all_templates.copy()

		self.__default_mode = False


	def __add_empty_template(self, templates):
		"""Добавляет пустой/базовый шаблон в список шаблонов"""
		templates[""] = __class__.__default_template
		return templates


	def save_modified_templates(self):
		"""Сохранить изменённные шаблоны в файл шаблонов"""
		system.set_data_to_file(data=self.__modified_all_templates, json_file_name=self.__full_default_path)

	def cancel_modified_templates(self):
		""" """
		self.__modified_all_templates = self.__all_templates


	def set_mode_working_with_template(self, new_mode: bool):
		"""Задать режим работы с шаблоном

		При new_mode=False создаётся новый шаблон, при mode=True выбранный шаблон изменяется"""
		self.__default_mode = new_mode

	def get_mode_working_with_template(self):
		""" """
		return self.__default_mode


	def get_names_all_templates(self):
		"""Получить имена всех шаблонов"""
		return tuple(self.__all_templates.keys())

	def is_template_in_templates(self, template_name):
		"""Проверить существует ли имя шаблона среди всех шаблонов"""
		return template_name in self.get_names_all_templates()


	def get_names_all_parameters(self, template_name):
		"""Получить имена всех параметров"""
		return tuple(self.__all_templates[template_name].keys())

	def change_template_parameter(self, template_name, parameter_name, new_parameter_value):
		""" """
		if self.is_template_in_templates(template_name):
			pass


	def check_templates_have_changed(self):
		"""Проверить изменились ли шаблоны"""
		return self.__modified_all_templates == self.__all_templates



tp = TemplatesManager()
print(tp.get_names_all_templates())


# tp.save_modified_templates()
# print(tp.get_parameter_names("templ1"))



# def set_param_modified_template(self):
# 	""" """
# 	pass

# def get_param_modified_template(self):
# 	""" """
# 	pass

# def create_empty_template(self, template_name, **kwargs):
# 	""" """

# 	if kwargs == None:
# 		pass
# 	pass


# def __set_default_path(self, default_path):
# 	""" """
# 	self.__default_path = default_path

# def __get_default_path(self):
# 	""" """
# 	return self.__default_path


# def create_empty_file(self):
# 	"""Создание пустого файла"""
# 	pass


# def delete_template(self):
# 	""" """
# 	pass


# def delete_template(self):
# 	""" """
# 	pass
