import json
import subprocess

import System

nameFile = "Paths.json"

def isFile():
	CurrentOS = System.getCurrentOS()
	if CurrentOS == "Arch":
		try:
			subprocess.check_output(["ls", nameFile])
			return True
		except subprocess.CalledProcessError:
			return False
	elif CurrentOS == "Windows":
		# добавить команду проверки для текущей системы
		return None
	elif CurrentOS == "Android":
		# добавить команду проверки для текущей системы
		return None
	else:
		# Остальные системы
		return None

def getStandartPath():
	""" В зависимости от ОС, получаем стандарный путь для файлов"""
	CurrentOS = System.getCurrentOS()

	if CurrentOS == "Arch":
		# pwd - получить путь текущего рабочего каталога
		# utf-8 - преобразовываем в обычную строку
		unformattedString = subprocess.check_output("pwd").decode("utf-8")
		formattedString = unformattedString.strip() + "/"
		return formattedString
		
	elif CurrentOS == "Windows":
		# добавить команду для текущей системы
		return None
	elif CurrentOS == "Android":
		# добавить команду для текущей системы
		return None
	else:
		# Остальные системы
		return None

def create(pathLUK="", pathDatabase=""):
	""" Пример вызова.
		create("/", "/home")
	"""
	# Существует ли такой файл?
	if not isFile():

		if pathLUK == "":
			# Если путь не задан, то выбирается текущий каталог
			pathLUK = getStandartPath()

		if pathDatabase == "":
			# Если путь не задан, то выбирается текущий каталог
			pathDatabase = getStandartPath()

		# Cоздать файл хранения путей. Для LUK-файла и для файла базы данных
		data = {}
		data["LUK"] = pathLUK
		data["Database.json"] = pathDatabase

		with open(nameFile, "w") as f:
			json.dump(data, f)

def getPath(key):
	""" Пример вызова.
		getPath("Database.json")
		Вывод:
		/home/user/GenPass/Database.json

		То есть. Выводим путь каталога /home/user/GenPass, а потом в конец добавляем название самого файла
	"""
	with open(nameFile) as f:
		data = json.load(f)
		return data[key] + key

def changePath(key, newPath):
	""" Пример вызова.
		changePath("LUK", "/etc/luk_files")
	"""
	data = {}
	with open(nameFile) as f:
		data = json.load(f)

	data[key] = newPath

	with open(nameFile, "w") as f:
		json.dump(data, f)

# create()
changePath("Database.json", "/home/jon/Work/Notes/BACKUP/GenPass/")