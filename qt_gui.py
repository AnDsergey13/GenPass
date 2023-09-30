import sys
from PyQt5.QtGui import QIcon
# from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QCheckBox, QLabel, QLineEdit, QMessageBox, QPushButton, QWidget

import gen_pass as gp
from localization import get_text


class UIGP:
	def __init__(self):
		self.get_localized_text = get_text
		self.privateKey = ""
		self.landmarkPhrase = ""
		self.password = ""
		self.numberSymbolsLUK = ""

		self.update_check_luk_file()

	# Private key
	def set_private_key(self, string):
		# print("PK = ", string)
		self.privateKey = string

	def get_private_key(self):
		return self.privateKey

	# Landmark phrase
	def set_landmark_phrase(self, string):
		# print("LP = ", string)
		self.landmarkPhrase = string

	def get_landmark_phrase(self):
		return self.landmarkPhrase

	# Number symbols LUK
	def set_luk_symbols_number(self, number):
		# print("LUK = ", number)
		self.numberSymbolsLUK = number

	def get_luk_symbols_number(self):
		return self.numberSymbolsLUK


	def set_visible_private_key(self, value):
		if value == 0:
			self.edt_PK.setEchoMode(QLineEdit.Password)
		else:
			self.edt_PK.setEchoMode(QLineEdit.Normal)

	def set_visible_landmark_phrase(self, value):
		if value == 0:
			self.edt_LP.setEchoMode(QLineEdit.Password)
		else:
			self.edt_LP.setEchoMode(QLineEdit.Normal)

	def update_check_luk_file(self):
		self.isVisibleEdtLUK = gp.is_luk_file()

	def create_window(self, width=450, height=450, pos_x=300, pos_y=300):
		app = QApplication(sys.argv)

		self.w = QWidget()
		self.w.resize(width, height)
		self.w.move(pos_x, pos_y)
		self.w.setWindowTitle('GenPass')
		# TODO: Заменить на QApplication.windowIcon
		# https://doc.qt.io/qt-6/qwidget.html#windowIcon-prop
		self.w.setWindowIcon(QIcon('icon/Panel.png'))

		self.create_components()

		self.w.show()
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

		# PrivateKey
		label_private_key = QLabel(self.w)
		label_private_key.move(offset_from_left_window_border, y_label_1)
		label_private_key.setText(self.get_localized_text("Enter. Private key"))

		self.line_edit_private_key = QLineEdit(self.w)
		self.line_edit_private_key.resize(300, components_height)
		self.line_edit_private_key.move(offset_from_left_window_border, y_label_1 + y_offset_from_label)
		self.line_edit_private_key.textChanged[str].connect(self.set_private_key)

		check_box_private_key = QCheckBox(self.get_localized_text("Visible"), self.w)
		check_box_private_key.setChecked(True)
		check_box_private_key.move(offset_from_left_window_border + x_offset_check_box, y_label_1 + y_offset_from_label)
		check_box_private_key.stateChanged.connect(self.set_visible_private_key)

		# LandmarkPhrase
		y_label_2 = y_label_1 + distance_y_between_labels
		label_landmark_phrase = QLabel(self.w)
		label_landmark_phrase.move(offset_from_left_window_border, y_label_2)
		label_landmark_phrase.setText(self.get_localized_text("Enter. Landmark phrase"))

		self.line_edit_landmark_phrase = QLineEdit(self.w)
		self.line_edit_landmark_phrase.resize(300, components_height)
		self.line_edit_landmark_phrase.move(offset_from_left_window_border, y_label_2 + y_offset_from_label)
		self.line_edit_landmark_phrase.textChanged[str].connect(self.set_landmark_phrase)

		check_box_landmark_phrase = QCheckBox(self.get_localized_text("Visible"), self.w)
		check_box_landmark_phrase.setChecked(True)
		check_box_landmark_phrase.move(offset_from_left_window_border + x_offset_check_box, y_label_2 + y_offset_from_label)
		check_box_landmark_phrase.stateChanged.connect(self.set_visible_landmark_phrase)

		# LUK-file
		y_label_3 = y_label_2 + distance_y_between_labels
		label_luk = QLabel(self.w)
		label_luk.move(offset_from_left_window_border, y_label_3)
		label_luk.setText(self.get_localized_text("Enter. Size LUK-file"))

		self.edt_LUK = QLineEdit(self.w)
		self.edt_LUK.resize(200, components_height)
		self.edt_LUK.move(offset_from_left_window_border, y_label_3 + y_offset_from_label)
		self.edt_LUK.textChanged[str].connect(self.set_luk_symbols_number)

		self.set_visible_edt_luk()

		x_offset_btn = 270
		btn_Gen = QPushButton(self.get_localized_text("Create. LUK-file"), self.w)
		btn_Gen.resize(buttons_width + 50, components_height)
		btn_Gen.move(offset_from_left_window_border + x_offset_btn, y_label_3 + y_offset_from_label)
		btn_Gen.clicked.connect(self.create_new_luk_file)


		# Bottom buttons
		y_offset_from_btn = 45
		self.lbl_message = QLabel(self.w)
		self.lbl_message.resize(435, components_height)
		self.lbl_message.move(offset_from_left_window_border, y_button - y_offset_from_btn)

		btn_Create = QPushButton(self.get_localized_text("Create"), self.w)
		btn_Create.resize(buttons_width, components_height)
		btn_Create.move(offset_from_left_window_border, y_button)
		btn_Create.clicked.connect(self.create_password)

		btn_Clear = QPushButton(self.get_localized_text("Clear"), self.w)
		btn_Clear.resize(buttons_width + 100, components_height)
		btn_Clear.move(offset_from_left_window_border + buttons_width + 100, y_button)
		btn_Clear.clicked.connect(self.clear_all)

	def get_availability_luk_file(self):
		return self.isVisibleEdtLUK

	def set_visible_edt_luk(self):
		if self.get_availability_luk_file():
			self.edt_LUK.setEnabled(False)
		else:
			self.edt_LUK.setEnabled(True)

	def delete_luk_file(self):
		# TODO: Перенести из этого модуля?
		import os
		os.remove("LUK")

	def create_new_luk_file(self):
		# msg = QMessageBox.question(
		# 	self.w,
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
			self.delete_luk_file()
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
				self.lbl_message.setText(message)

				# The signal that the data entered did not pass conditions
				# Сигнал о том, что вводимые данные не прошли условия
				return -1

			elif int(string) > 1000 and int(string) < 1000000:
				return int(string)
			elif int(string) >= 1000000:
				# If the number is more than a million
				# Если число больше миллиона
				message = self.get_localized_text("Err. LUK-file. Less than 1000000").partition('.')[2]
				self.lbl_message.setText(message)

				# The signal that the data entered did not pass conditions
				# Сигнал о том, что вводимые данные не прошли условия
				return -1
		except:
			# Input Error. Symbols should not be used
			# Ошибка ввода. Не должны использоваться символы
			message = self.get_localized_text("Err. Invalid input").partition('.')[2]
			self.lbl_message.setText(message)

			# The signal that the data entered did not pass conditions
			# Сигнал о том, что вводимые данные не прошли условия
			return -1

	def get_num_symbols_luk(self):
		# The greater the number of characters specified, the greater the entropy of the LUK-file
		# Чем больше указано количество символов, тем больше энтропия ЛУК-файла
		numberLUKsymbols = self.get_luk_symbols_number()

		numberLUKsymbols = self.processing_num_luk(numberLUKsymbols)
		if numberLUKsymbols != -1:
			return numberLUKsymbols
		else:
			return -1

	def create_password(self):
		privateKey = self.get_private_key()
		landmarkPhrase = self.get_landmark_phrase()

		encryptedPrivateKey = gp.get_hash_string(privateKey)
		encryptedLandmarkPhrase = gp.get_hash_string(landmarkPhrase)

		UnicodePrivateKey = gp.convert_to_unicode(encryptedPrivateKey)[::-1]
		UnicodeLandmarkPhrase = gp.convert_to_unicode(encryptedLandmarkPhrase)

		A = gp.encryption_xor(UnicodeLandmarkPhrase, UnicodePrivateKey)

		if not gp.is_luk_file():
			numberLUKsymbols = self.get_num_symbols_luk()
			if numberLUKsymbols != -1:
				gp.create_luk(numberLUKsymbols)

		if gp.is_luk_file():
			hashLUK = gp.get_hash_luk().upper()
			B = gp.convert_to_unicode(hashLUK)
			result = gp.convert_to_string(gp.encryption_xor(A, B))
			self.copy_password_in_clipboard(result)

	def copy_password_in_clipboard(self, password):
		clipboard = QApplication.clipboard()
		clipboard.setText(password)
		# Вывод сообщения. Пароль успешно создан и скопирован
		self.lbl_message.setText(self.get_localized_text("Password copied"))

	def clear_all(self):
		# Clearing the clipboard
		# Очистка буфера
		clipboard = QApplication.clipboard()
		clipboard.clear()

		# Cleaning components
		# Очистка компонентов
		self.edt_PK.clear()
		self.edt_LP.clear()
		self.edt_LUK.clear()
		self.lbl_message.clear()
