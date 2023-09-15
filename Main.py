import Terminal
import UI as ui
import System

# If True is used by the interface option. If False, it works in console mode
# Если True - используется вариант с интерфейсом. Если False, то работает в консольном режиме
USE_USER_INTERFACE = False

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
