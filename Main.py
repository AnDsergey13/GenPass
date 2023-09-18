import Terminal
import UI as ui
from Config import ConfigFile as cf
import System


USE_USER_INTERFACE = cf.get_value_by_key("use_GUI")

LANGUAGE_LOCALIZATION = System.getLocalization()
CURRENT_OS = System.getCurrentOS()

if USE_USER_INTERFACE:
	if CURRENT_OS == "Linux" or CURRENT_OS == "Windows":
		ui = ui.UIGP(LANGUAGE_LOCALIZATION)
		ui.createWindow()

	elif CURRENT_OS == "Android":
		pass

	else:
		# Other
		print("Unknown operating system")
else:
	Terminal.Main(LANGUAGE_LOCALIZATION)
