import toga
from icecream import ic
from colosseum import CSS
from colosseum.dimensions import Size, Box
from localization import get_text as _

class UIBW:
	""" """

	def __init__(self, name_app="GenPass"):
		self.name_app = name_app
		self.general_padding = 20
		self.private_key_visible = True

	def __build(self, app):
		self.box = toga.Box()

		# label_private_key = toga.Label(text=_("Enter. Private key"))
		# label_private_key.style.padding = self.general_padding
		# label_private_key.style.flex = 2
		# box.add(label_private_key)

		self.private_key = toga.PasswordInput(placeholder=_("Enter. Private key"))
		self.private_key.style.padding = self.general_padding
		self.private_key.style.flex = 2
		self.box.add(self.private_key)

		is_visible_private_key = toga.Switch(text=_("Visible"), on_change=self.run_switch_private_key)
		is_visible_private_key.style.padding = self.general_padding
		is_visible_private_key.style.flex = 1
		self.box.add(is_visible_private_key)

		# button = toga.Button("Hello world", on_press=self.button_handler)
		# button.style.padding = self.general_padding
		# button.style.flex = 1
		# box.add(button)

		return self.box

	def run_switch_private_key(self, widget):
		ic(self.private_key.remove)
		return self.box

	def create_window(self):
		toga.App(self.name_app, "org.beeware.helloworld", startup=self.__build).main_loop()


	def button_handler(self, widget):
		ic("hello")



a = UIBW()
a.create_window()