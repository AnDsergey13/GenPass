import json
import os
import subprocess

import System


def in_key(func):
	def wrapper(key, *args):
		""" Проверяем, содержится ли введённый ключ в списке ключей"""
		if key in ConfigManager.getListAvailableKeys():
			return func(key, *args)
		else:
			print(f"Параметр KEY, указан не верно! Допустимые значения = {ConfigManager.getListAvailableKeys()}")
	return wrapper

# Декоратор для запуска необходимой команды из списка команд
def run_command(commandName):
	def decorator(func):
		def wrapper():
			CurrentOS = System.getCurrentOS()
			allCommands = ConfigManager.OS_Conmands.get(CurrentOS)
			command = allCommands.get(commandName)
			# Возвращаем результат лямбда-функции из списка команд
			return command()
		return wrapper
	return decorator


class ConfigManager:
	nameFile = "Config.json"

	listAvailableKeys = ["Database", "LANG", "LUK", "GUI"]

	OS_Conmands = {
		"Linux": {
			"isFile": lambda: os.path.exists(__class__.nameFile),
			"getStandartPath": lambda: subprocess.check_output("pwd").decode("utf-8").strip() + "/",
			# Пример: полученную строку с названиями файлов "en_US\nes_ES.json\nru_RU" преобразуем в ["en_US", "es_ES.json", "ru_RU"]
			"getFileNames": lambda: subprocess.check_output(["ls", "locale"]).decode("utf-8").split("\n")[:-1]
		},
		"Windows": {
			# Проверить команды для Windows
			"isFile": None,
			"getStandartPath": None,
			"getFileNames": None
		},
		"Android": {
			# Проверить команды для Android
			"isFile": None,
			"getStandartPath": None,
			"getFileNames": None
		}
	}

	# Нужен ли этот метод???
	@staticmethod
	def getNameFile():
		# Получаем название файла настроек
		return __class__.nameFile

	# Нужен ли этот метод???
	@staticmethod
	def setNameFile(newName):
		# Изменяем название файла настроек
		__class__.nameFile = newName


	@run_command("isFile")
	def __isFile():
		pass

	@run_command("getStandartPath")
	def __getStandartPath():
		pass

	@run_command("getFileNames")
	def __getFileNames():
		pass
	

	@staticmethod
	def __get_formated_list_file_names(list_file_names):
		# Удаляем расширение .json в именах файлов, чтобы проще было потом проверять
		return [nameFile.replace(".json", "") for nameFile in list_file_names]
	
	@staticmethod
	def check_language_in_list(language, list_file_names):
		return language in list_file_names


	def __getDataInFile(nameFile="Config.json"):
		""" Получаем все данные из конфигурационного файла"""
		with open(nameFile) as f:
			return json.load(f)

	def __setDataInFile(data, nameFile="Config.json"):
		""" Перезаписываем данные из конфигурационного файла"""
		with open(nameFile, "w") as f:
			json.dump(data, f)
	
	# todo Сделать проверку на правильность введённых путей(pathLUK, pathDatabase)
	# todo Сделать проверку на правильность введённого (use_GUI)
	@staticmethod
	def createFile(use_GUI=True, LANG="", pathLUK="", pathDatabase=""):
		""" Создаёт конфигурационный файл с базовыми настройками
			Пример вызова.
			createFile(True, "es_ES", "/", "/home")
			ConfigManager.createFile(LANG="en_EN")
		"""
		# Существует ли такой файл? Проверка сделана с целью защиты от перезаписи файла при повторном запуске функции
		if not __class__.__isFile():

			# Устанавливаем значния по умолчанию, если язык не был введён
			if LANG == "":
				LANG = System.getLanguageOS()
			# Проверяем введённый язык на правильность ввода
			elif not __class__.check_language_in_list(
				LANG, 
				__class__.__get_formated_list_file_names(__class__.__getFileNames())
				):
				# И если он не правильный, то автоматически выбираем язык по умолчанию
				LANG = System.getLanguageOS()
				print(f"Указанного языка не существует. Выбран {LANG} по умолчанию")
			
			# Устанавливаем значния по умолчанию, если путь не был задан
			if pathLUK == "":
				pathLUK = __class__.__getStandartPath()
			if pathDatabase == "":
				pathDatabase = __class__.__getStandartPath()

			# Cоздать файл хранения настроек
			data = {}
			data["use_GUI"] = str(use_GUI)
			data["LANG"] = LANG
			data["pathLUK"] = pathLUK
			data["pathDatabase"] = pathDatabase

			__class__.__setDataInFile(data)

	@staticmethod
	def getListAvailableKeys():
		""" Получаем список доступных ключей для файла конфигураций"""
		return __class__.listAvailableKeys

	@staticmethod
	@in_key
	def getValue(key):
		""" Пример вызова.
			getValue("pathDatabase")
			Вывод:
			/home/user/GenPass/Database.json
		"""
		# Получаем данные
		data = __class__.__getDataInFile()
		return data[key]

	@staticmethod
	@in_key
	def changeValue(key, newValue):
		""" Пример вызова.
			ConfigManager.changeValue("pathLUK", "/home/Work/Python/")
			ConfigManager.changeValue("LANG", "en_US")
		"""
		# Получаем данные
		data = __class__.__getDataInFile()
		# Изменяем на новые
		data[key] = newValue
		# Записываем в файл конфигурации
		__class__.__setDataInFile(data)

# ConfigManager.createFile()