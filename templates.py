import System
from Config import ConfigFile as cf


class TemplatesManager:
	""" """
	
	name_file = "templates.json"

	template = {
		"landmark phrase": "",
		"maximum password length": 64,
		")": False,
		"=": False,
		"_": False,
		'"': False,
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

	# @staticmethod
	# def __init__():
		
	# создание пустого файла
	@staticmethod
	def create_empty_file():
		path_file = cf.get_value_by_key("path_Templates")
		if not System.is_file(name_file=__class__.name_file, path_file=path_file):
			print("файл создан")
			data = {}
			System.set_data_to_file(data=data, json_file_name=__class__.name_file)

	@staticmethod
	def delete_template():
		pass

	@staticmethod
	def save_changes():
		pass

	@staticmethod
	def create_new_entry():
		pass


tp = TemplatesManager()
tp.create_empty_file