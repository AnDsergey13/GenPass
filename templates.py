import System
from Config import ConfigFile as cf


class TemplatesManager:
	""" """

	def __init__(self):
		""" """
		self.__default_path = cf.get_value_by_key("path_Templates")
		self.__name_file = "templates.json"
		self.__full_default_path = self.__default_path + "/" + self.__name_file

		# Создаём пустой файл шаблонов, если его нет
		if not System.is_file(self.__name_file, self.__default_path):
			empty_data = {}
			System.set_data_to_file(data=empty_data, json_file_name=self.__full_default_path)

		self.__all_templates = System.get_data_from_file(self.__full_default_path)
		# Все изменения будем производить с копией данных файла шаблонов
		# Нужно для того, чтобы работала отмена изменений в файле(при запуске GUI)
		self.__modified_all_templates = self.__all_templates.copy()

		self.__default_template = {
			"landmark phrase": "",
			"maximum password length": 64,
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


	def save_modified_templates(self):
		"""Сохранить изменённные шаблоны в файл шаблонов"""
		System.set_data_to_file(data=self.__modified_all_templates, json_file_name=self.__full_default_path)

	def has_templates_modified(self):
		"""Проверить изменились ли шаблоны"""
		return self.__modified_all_templates == self.__all_templates

	def get_template_names(self):
		"""Получить имена всех шаблонов"""
		return tuple(self.__all_templates.keys())

	def is_template_in_templates(self, template_name):
		"""Проверить существует ли имя шаблона среди всех шаблонов"""
		return template_name in self.get_template_names()

	def get_parameter_names(self, template_name):
		return tuple(self.__all_templates[template_name].keys())

	def change_template_parameter(self, template_name, parameter_name, new_parameter_value):
		""" """
		if self.is_template_in_templates(template_name):
			pass



tp = TemplatesManager()
# print(tp.get_template_names())
# tp.save_modified_templates()
print(tp.get_parameter_names("templ1"))



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
