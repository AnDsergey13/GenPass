import sys
from PyQt5.QtGui import QIcon
# from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QCheckBox, QLabel, QLineEdit, QMessageBox, QPushButton, QWidget

import gen_pass as gp
from localization import get_text
from system import delete_luk_file


class UIGP:
	"""TODO: Написать docstring"""
	def __init__(self):
		self.get_localized_text = get_text
		self.private_key = ""
		self.landmark_phrase = ""
		self.password = ""
		self.luk_symbols_number = ""

		self.update_check_luk_file()

	# Private key
	def set_private_key(self, string):
		# print("PK = ", string)
		self.private_key = string

	def get_private_key(self):
		return self.private_key

	# Landmark phrase
	def set_landmark_phrase(self, string):
		# print("LP = ", string)
		self.landmark_phrase = string

	def get_landmark_phrase(self):
		return self.landmark_phrase

	# Number symbols LUK
	def set_luk_symbols_number(self, number):
		# print("LUK = ", number)
		self.luk_symbols_number = number

	def get_luk_symbols_number(self):
		return self.luk_symbols_number

	# Input visibility
	def set_visible_private_key(self, value):
		if value == 0:
			self.line_edit_private_key.setEchoMode(QLineEdit.Password)
		else:
			self.line_edit_private_key.setEchoMode(QLineEdit.Normal)

	def set_visible_landmark_phrase(self, value):
		if value == 0:
			self.line_edit_landmark_phrase.setEchoMode(QLineEdit.Password)
		else:
			self.line_edit_landmark_phrase.setEchoMode(QLineEdit.Normal)

	def update_check_luk_file(self):
		self.is_visible_edit_luk = gp.is_luk_file()

	def create_window(self, width=450, height=450, pos_x=300, pos_y=300):
		app = QApplication(sys.argv)

		self.window = QWidget()
		self.window.resize(width, height)
		self.window.move(pos_x, pos_y)
		self.window.setWindowTitle('GenPass')
		# TODO: Заменить на QApplication.windowIcon
		# https://doc.qt.io/qt-6/qwidget.html#windowIcon-prop
		self.window.setWindowIcon(QIcon('icon/Panel.png'))

		self.create_components()

		self.window.show()
		sys.exit(app.exec())

	def create_components(self):
		components_height = 32
		buttons_width = 100
		offset_from_left_window_border = 15
		y_label_1 = 15

		y_offset_from_label = 30
		distance_y_between_labels = 95
		x_offset_check_box = 315

		y_button = 400

		# TODO: Maybe use with expression and tuple for typical actions?

		# Private Key
		label_private_key = QLabel(self.window)
		label_private_key.move(offset_from_left_window_border, y_label_1)
		label_private_key.setText(self.get_localized_text("Enter. Private key"))

		self.line_edit_private_key = QLineEdit(self.window)
		self.line_edit_private_key.resize(300, components_height)
		self.line_edit_private_key.move(offset_from_left_window_border, y_label_1 + y_offset_from_label)
		self.line_edit_private_key.textChanged[str].connect(self.set_private_key)

		check_box_private_key = QCheckBox(self.get_localized_text("Visible"), self.window)
		check_box_private_key.setChecked(True)
		check_box_private_key.move(offset_from_left_window_border + x_offset_check_box, y_label_1 + y_offset_from_label)
		check_box_private_key.stateChanged.connect(self.set_visible_private_key)

		# Landmark Phrase
		y_label_2 = y_label_1 + distance_y_between_labels
		label_landmark_phrase = QLabel(self.window)
		label_landmark_phrase.move(offset_from_left_window_border, y_label_2)
		label_landmark_phrase.setText(self.get_localized_text("Enter. Landmark phrase"))

		self.line_edit_landmark_phrase = QLineEdit(self.window)
		self.line_edit_landmark_phrase.resize(300, components_height)
		self.line_edit_landmark_phrase.move(offset_from_left_window_border, y_label_2 + y_offset_from_label)
		self.line_edit_landmark_phrase.textChanged[str].connect(self.set_landmark_phrase)

		check_box_landmark_phrase = QCheckBox(self.get_localized_text("Visible"), self.window)
		check_box_landmark_phrase.setChecked(True)
		check_box_landmark_phrase.move(offset_from_left_window_border + x_offset_check_box, y_label_2 + y_offset_from_label)
		check_box_landmark_phrase.stateChanged.connect(self.set_visible_landmark_phrase)

		# LUK-file
		y_label_3 = y_label_2 + distance_y_between_labels
		label_luk = QLabel(self.window)
		label_luk.move(offset_from_left_window_border, y_label_3)
		label_luk.setText(self.get_localized_text("Enter. Size LUK-file"))

		self.line_edit_luk = QLineEdit(self.window)
		self.line_edit_luk.resize(200, components_height)
		self.line_edit_luk.move(offset_from_left_window_border, y_label_3 + y_offset_from_label)
		self.line_edit_luk.textChanged[str].connect(self.set_luk_symbols_number)

		self.set_visible_edt_luk()

		x_offset_button = 270
		button_generate = QPushButton(self.get_localized_text("Create. LUK-file"), self.window)
		button_generate.resize(buttons_width + 50, components_height)
		button_generate.move(offset_from_left_window_border + x_offset_button, y_label_3 + y_offset_from_label)
		button_generate.clicked.connect(self.create_new_luk_file)

		# Bottom buttons
		y_offset_from_button = 45
		self.label_message = QLabel(self.window)
		self.label_message.resize(435, components_height)
		self.label_message.move(offset_from_left_window_border, y_button - y_offset_from_button)

		button_create = QPushButton(self.get_localized_text("Create"), self.window)
		button_create.resize(buttons_width, components_height)
		button_create.move(offset_from_left_window_border, y_button)
		button_create.clicked.connect(self.create_password)

		button_clear = QPushButton(self.get_localized_text("Clear"), self.window)
		button_clear.resize(buttons_width + 100, components_height)
		button_clear.move(offset_from_left_window_border + buttons_width + 100, y_button)
		button_clear.clicked.connect(self.clear_all)

	def get_availability_luk_file(self):
		return self.is_visible_edit_luk

	def set_visible_edt_luk(self):
		if self.get_availability_luk_file():
			self.line_edit_luk.setEnabled(False)
		else:
			self.line_edit_luk.setEnabled(True)

	def create_new_luk_file(self):
		# msg = QMessageBox.question(
		# 	self.window,
		# 	'PyQt5 message',
		# 	"Do you like PyQt5?",
		# 	QMessageBox.Yes | QMessageBox.No,
		# 	QMessageBox.No
		# )

		msg = QMessageBox()
		# msg.setText("The document has been modified.")

		msg.setWindowTitle(self.get_localized_text("Danger"))
		msg.setText(self.get_localized_text("Attention. LUK-file. Overwrite"))
		msg.setIcon(QMessageBox.Warning)
		msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
		msg.setDefaultButton(QMessageBox.Cancel)
		msg.exec()

		print(msg)
		print(QMessageBox.Yes, QMessageBox.No)
		if msg == QMessageBox.Yes:
			print("yes")
			delete_luk_file()
			self.update_check_luk_file()
			self.set_visible_edt_luk()
		else:
			print("no")

	def processing_num_luk(self, string):
		# If you press Enter, the default values are set to 5000.
		# Если нажать Enter, то устанавливаются значения по умолчанию равным 5000.
		if string == "":
			string = 5000
			return int(string)

		try:
			if int(string) < 1001:
				message = self.get_localized_text("Err. LUK-file. Greater than 1000").partition('.')[2]
				self.label_message.setText(message)

				# The signal that the data entered did not pass conditions
				# Сигнал о том, что вводимые данные не прошли условия
				return -1

			elif int(string) > 1000 and int(string) < 1000000:
				return int(string)
			elif int(string) >= 1000000:
				# If the number is more than a million
				# Если число больше миллиона
				message = self.get_localized_text("Err. LUK-file. Less than 1000000").partition('.')[2]
				self.label_message.setText(message)

				# The signal that the data entered did not pass conditions
				# Сигнал о том, что вводимые данные не прошли условия
				return -1
		except:
			# Input Error. Symbols should not be used
			# Ошибка ввода. Не должны использоваться символы
			message = self.get_localized_text("Err. Invalid input").partition('.')[2]
			self.label_message.setText(message)

			# The signal that the data entered did not pass conditions
			# Сигнал о том, что вводимые данные не прошли условия
			return -1

	def get_num_symbols_luk(self):
		# The greater the number of characters specified, the greater the entropy of the LUK-file
		# Чем больше указано количество символов, тем больше энтропия ЛУК-файла
		luk_symbols_number = self.get_luk_symbols_number()

		luk_symbols_number = self.processing_num_luk(luk_symbols_number)
		if luk_symbols_number != -1:
			return luk_symbols_number
		else:
			return -1

	def create_password(self):
		private_key = self.get_private_key()
		landmark_phrase = self.get_landmark_phrase()

		encrypted_private_key = gp.get_hash_string(private_key)
		encrypted_landmark_phrase = gp.get_hash_string(landmark_phrase)

		# Invert the elements, since during the XOR operation, the same keys should not turn into zero. And when the keys were swapped, the same password was not created.
		# Инвертируем элементы, так как при операции XOR, одинаковые ключи не должны превращаться в ноль. И при перестановке ключей местами, не создавался одинаковый пароль.
		unicode_private_key = gp.convert_to_unicode(encrypted_private_key)[::-1]
		unicode_landmark_phrase = gp.convert_to_unicode(encrypted_landmark_phrase)

		a = gp.encryption_xor(unicode_landmark_phrase, unicode_private_key)

		# In the absence of a LUK-file, we generate the number of characters and create it
		# При отсутствии ЛУК-файла, генерируем количество символов и создаём его
		if not gp.is_luk_file():
			luk_symbols_number = self.get_num_symbols_luk()
			if luk_symbols_number != -1:
				gp.create_luk(luk_symbols_number)

		# If you do not change the hash to all capital letters, then the final password will be without capital letters (why?). Which reduces the complexity of the password itself.
		# Если не изменять Хеш на все заглавные буквы, то конечный пароль будет без заглавных букв (почему?). Что уменьшает сложность самого пароля.
		if gp.is_luk_file():
			luk_hash = gp.get_hash_luk().upper()

			b = gp.convert_to_unicode(luk_hash)
			result = gp.convert_to_string(gp.encryption_xor(a, b))

			self.copy_password_in_clipboard(result)

	def copy_password_in_clipboard(self, password):
		clipboard = QApplication.clipboard()
		clipboard.setText(password)
		# Вывод сообщения. Пароль успешно создан и скопирован
		self.label_message.setText(self.get_localized_text("Password copied"))

	def clear_all(self):
		# Clearing the clipboard
		# Очистка буфера
		clipboard = QApplication.clipboard()
		clipboard.clear()

		# Cleaning components
		# Очистка компонентов
		self.line_edit_private_key.clear()
		self.line_edit_landmark_phrase.clear()
		self.line_edit_luk.clear()
		self.label_message.clear()
