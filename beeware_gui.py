import toga
from colosseum import CSS
from colosseum.dimensions import Size, Box
from localization import get_text as _

class UIBW:
	""" """

	def __init__(self, name_app="GenPass"):
		self.name_app = name_app
		self.general_padding = 50
		
	def __build(self, app):
		box_lable_1 = toga.Box()
		label_private_key = toga.Label(text=_("Enter. Private key"))
		box_lable_1.add(label_private_key)

		box = toga.Box()

		label_private_key.style.padding = self.general_padding
		label_private_key.style.flex = 2
		box.add(label_private_key)

		private_key = toga.PasswordInput()
		private_key.style.padding = self.general_padding
		private_key.style.flex = 2
		box.add(private_key)

		is_visible_private_key = toga.Switch(text=_("Visible"))
		is_visible_private_key.style.padding = self.general_padding
		private_key.style.flex = 1
		box.add(is_visible_private_key)

		# button = toga.Button("Hello world", on_press=self.button_handler)
		# button.style.padding = self.general_padding
		# button.style.flex = 1
		# box.add(button)

		return box

	def create_window(self):
		toga.App(self.name_app, "org.beeware.helloworld", startup=self.__build).main_loop()


	def button_handler(self, widget):
		print("hello")



a = UIBW()
a.create_window()