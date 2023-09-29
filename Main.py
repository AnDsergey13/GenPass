import Terminal
import UI as ui
from Config import ConfigFile as cf
import System

# создаём конфигурационный файл, если он отсутствует
cf.create_file()

USE_USER_INTERFACE = cf.get_value_by_key("use_GUI")
CURRENT_OS = System.getCurrentOS()

if USE_USER_INTERFACE:
	if CURRENT_OS == "Linux" or CURRENT_OS == "Windows":
		ui = ui.UIGP()
		ui.createWindow()
	elif CURRENT_OS == "Android":
		pass
	else:
		# Other
		print("Unknown operating system")
else:
	Terminal.Main()

# TODO #XX: Переамясціць код у функцыю __main__()
