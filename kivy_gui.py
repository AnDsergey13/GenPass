from kivy.app import App
from kivy.uix.label import Label

from kivy.core.window import Window

Window.size = (600, 500)
Window.clearcolor = (0,255,255, 1)
Window.title = "GenPass"

class UIGP(App):
	""" """

	def build(self):
		lable = Label(text="Моя программа\nусё працуе")

		return lable


if __name__ == "__main__":
	UIGP().run()