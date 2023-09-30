import terminal
import qt_gui
import config
import system

# создаём конфигурационный файл, если он отсутствует
config.create_file()

USE_USER_INTERFACE = config.get_value_by_key("use_gui")
CURRENT_OS = system.get_current_os()

if USE_USER_INTERFACE:
	if CURRENT_OS == "Linux" or CURRENT_OS == "Windows":
		ui = qt_gui.UIGP()
		ui.create_window()
	elif CURRENT_OS == "Android":
		pass
	else:
		# Other
		print("Unknown operating system")
else:
	terminal.main()

# TODO: Переместить код в функцию __main__()
