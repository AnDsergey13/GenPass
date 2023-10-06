from kivy.app import App
from kivy.uix.label import Label
from kivy.config import Config
from kivy.properties import StringProperty


class UIGP(App):
	window_title = StringProperty("GenPass")

	def build(self):
		self.title = self.window_title
		label = Label(text="Моя программа\nусё працуе")
		return label


if __name__ == "__main__":
	# Настройка окна, включая заголовок
	Config.set('graphics', 'width', '200')
	Config.set('graphics', 'height', '200')
	# Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
	Config.set('kivy', 'window_icon', 'icon/Panel.png')
	UIGP().run()
