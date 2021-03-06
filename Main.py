import Terminal
# import UI as ui

import sysconfig

def getLanguageOS():
	import locale

	if locale.getdefaultlocale()[0] == "ru_RU":
		return "ru_RU"
	else:
		return "en_US"

def getLocalization():
	localization = []
	with open(f"locale/{getLanguageOS()}",'r', encoding="utf-8") as f:
		for line in f.readlines():
			# [:-1] Cut a new line symbol. He's not needed 
			# [:-1] Отрезаем символ новой строки. Он не нужен
			localization.append(line[:-1])

	return localization

def getCurrentOS():
	TYPE_OS = [
		[0, "Arch"],
		[1, "Android"],
		[2, "Windows"],
		[3, "Other"]
	]

	OS = sysconfig.get_platform()
	if OS == "linux-x86_64": # Arch Linux and other?
		return TYPE_OS[0]
	elif OS == "linux-aarch64": # Android
		return TYPE_OS[1]
	elif OS == "win-amd64": # Windows
		return TYPE_OS[2] 
	else: # Оther
		return TYPE_OS[3]

# If True is used by the interface option. If False, it works in console mode
# Если True - используется вариант с интерфейсом. Если False, то работает в консольном режиме
USE_USER_INTERFACE = False

LANGUAGE_LOCALIZATION = getLocalization()
CURRENT_OS = getCurrentOS()

if USE_USER_INTERFACE:
	if CURRENT_OS[0] == 0:
		# Arch linux and other?
		ui = ui.UIGP(LANGUAGE_LOCALIZATION)
		ui.createWindow()

	elif CURRENT_OS[0] == 1:
		pass # Android

	elif CURRENT_OS[0] == 2:
		ui = ui.UIGP(LANGUAGE_LOCALIZATION)
		ui.createWindow()
		pass # Windows
	else:
		pass # Оther
		print("Unknown operating system")
else:
	Terminal.Main(LANGUAGE_LOCALIZATION)