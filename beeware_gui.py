# TODO
# + Добавить простейший пример
# + Провести сборку под Android

import toga

class UIBW:
	""" """

	def __init__(self, name_app):
		self.name_app = "GenPass"

	def __build(self, app):
		box = toga.Box()

		button = toga.Button("Hello world", on_press=self.button_handler)
		button.style.padding = 50
		button.style.flex = 1
		box.add(button)

		return box

	def create_window(self):
		toga.App(self.name_app, "org.beeware.helloworld", startup=self.__build).main_loop()


	def button_handler(self, widget):
		print("hello")


a = UIBW()
