import json
import os
import subprocess

import System

# Декоратор для запуска необходимой команды из списка команд
# Как работает wrapper и decorator???
def run_command(commandName):
	def decorator(func):
		def wrapper():
			CurrentOS = System.getCurrentOS()
			allCommands = OS_Conmands.get(CurrentOS)
			command = allCommands.get(commandName)
			# Возвращаем результат лямбда-функции из списка команд
			return command()
		return wrapper
	return decorator


class ConfigManager:
	nameFile = "Config.json"

	OS_Conmands = {
		"Linux": {
			"isFile" : lambda: os.path.exists(__class__.nameFile),
			"getStandartPath": lambda: subprocess.check_output("pwd").decode("utf-8").strip() + "/",
			"newCommand" : None 
		},
		"Windows": {
			"isFile": lambda: os.path.exists(__class__.nameFile),
			"getStandartPath": lambda: subprocess.check_output("pwd").decode("utf-8").strip() + "/",
			"newCommand" : None 
		},
		"Android": {
			"isFile": None,  # Добавить команду для Android, если необходимо
			"getStandartPath": None,  # Добавить команду для Android, если необходимо
			"newCommand" : None 
		}
	}

	# Нужен ли этот метод???
	# Получаем название файла настроек
	@staticmethod
	def getNameFile():
		return __class__.nameFile

	# Нужен ли этот метод???
	# Изменяем название файла настроек
	@staticmethod
	def setNameFile(newName):
		__class__.nameFile = newName

	@run_command("isFile")
	def __isFile():
		pass

	@run_command("getStandartPath")
	def __getStandartPath():
		pass


	def __getDataInFile(nameFile="Config.json"):
		with open(nameFile) as f:
			return json.load(f)

	def __setDataInFile(data, nameFile="Config.json"):
		with open(nameFile, "w") as f:
			json.dump(data, f)

	@staticmethod
	def create(pathLUK="", pathDatabase=""):
		""" Пример вызова.
			create("/", "/home")
		"""
		# Существует ли такой файл?
		if not __class__.__isFile():

			# Если путь в атрибутах не задан, то выбирается текущий каталог
			if pathLUK == "":
				pathLUK = __class__.__getStandartPath()
			if pathDatabase == "":
				pathDatabase = __class__.__getStandartPath()

			# Cоздать файл хранения путей. Для LUK-файла и для файла базы данных
			data = {}
			data["LUK"] = pathLUK
			data["Database.json"] = pathDatabase

			__class__.__setDataInFile(data)

	@staticmethod
	def getPath(key):
		""" Пример вызова.
			getPath("Database.json")
			Вывод:
			/home/user/GenPass/Database.json
		"""
		# То есть. Выводим путь каталога /home/user/GenPass, а потом в конец добавляем название самого файла
		data = __class__.__getDataInFile()
		return data[key] + key

	@staticmethod
	def changePath(key, newPath):
		""" Пример вызова.
			changePath("LUK", "/etc/luk_files")
		"""
		# Получаем данные 
		data = __class__.__getDataInFile()
		data[key] = newPath
		__class__.__setDataInFile(data)

