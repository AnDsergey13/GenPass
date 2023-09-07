import sysconfig

TYPE_OS = ["Arch", "Android", "Windows", "Other"]

def getLanguageOS():
	import locale

	if locale.getlocale()[0] == "ru_RU":
		return "ru_RU"
	else:
		return "en_US"

def getLocalization():
	""" !!!!! переделать!!!! на json формат"""
	localization = []
	with open(f"locale/{getLanguageOS()}",'r', encoding="utf-8") as f:
		for line in f.readlines():
			# [:-1] Cut a new line symbol. He's not needed 
			# [:-1] Отрезаем символ новой строки. Он не нужен
			localization.append(line[:-1])

	return localization

def getCurrentOS():
	OS = sysconfig.get_platform()
	if OS == "linux-x86_64": # Arch Linux and other?
		return TYPE_OS[0]
	elif OS == "linux-aarch64": # Android
		return TYPE_OS[1]
	elif OS == "win-amd64": # Windows
		return TYPE_OS[2] 
	else: # Оther
		return TYPE_OS[3]

def getNameUser():
	return None