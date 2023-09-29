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

		self.updateCheckLUKfile()

	# Private key
	def setPrivateKey(self, string):
		# print("PK = ", string)
		self.privateKey = string

	def getPrivateKey(self):
		return self.privateKey

	# Landmark phrase
	def setLandmarkPhrase(self, string):
		# print("LP = ", string)
		self.landmarkPhrase = string

	def getLandmarkPhrase(self):
		return self.landmarkPhrase

	# Number symbols LUK
	def setNumberSymbolsLUK(self, number):
		# print("LUK = ", number)
		self.numberSymbolsLUK = number

	def getNumberSymbolsLUK(self):
		return self.numberSymbolsLUK


	def setVisiblePrivateKey(self, value):
		if value == 0:
			self.edt_PK.setEchoMode(QLineEdit.Password)
		else:
			self.edt_PK.setEchoMode(QLineEdit.Normal)

	def setVisibleLandmarkPhrase(self, value):
		if value == 0:
			self.edt_LP.setEchoMode(QLineEdit.Password)
		else:
			self.edt_LP.setEchoMode(QLineEdit.Normal)

	def updateCheckLUKfile(self):
		self.isVisibleEdtLUK = gp.isLUKfile()

	def createWindow(self, width=450, height=450, pos_x=300, pos_y=300):
		app = QApplication(sys.argv)

		self.w = QWidget()
		self.w.resize(width, height)
		self.w.move(pos_x, pos_y)
		self.w.setWindowTitle('GenPass')
		# TODO #XX: Замяніць на QApplication.windowIcon
		# https://doc.qt.io/qt-6/qwidget.html#windowIcon-prop
		self.w.setWindowIcon(QIcon('icon/Panel.png'))

		self.createComponents()

		self.w.show()
		sys.exit(app.exec())


	def createComponents(self):
		h_components = 32
		w_btn = 100
		left_offset_from_window = 15
		y_lbl_1 = 15

		y_offset_from_lbl = 30
		dist_y_between_lbl = 95
		x_offset_cb = 315

		y_btn = 400

		# PrivateKey
		lbl_PK = QLabel(self.w)
		lbl_PK.move(left_offset_from_window, y_lbl_1)
		lbl_PK.setText(self.get_localized_text("Enter. Private key"))

		self.edt_PK = QLineEdit(self.w)
		self.edt_PK.resize(300, h_components)
		self.edt_PK.move(left_offset_from_window, y_lbl_1 + y_offset_from_lbl)
		self.edt_PK.textChanged[str].connect(self.setPrivateKey)

		cb_PK = QCheckBox(self.get_localized_text("Visible"), self.w)
		cb_PK.setChecked(True)
		cb_PK.move(left_offset_from_window + x_offset_cb, y_lbl_1 + y_offset_from_lbl)
		cb_PK.stateChanged.connect(self.setVisiblePrivateKey)

		# LandmarkPhrase
		y_lbl_2 = y_lbl_1 + dist_y_between_lbl
		lbl_LP = QLabel(self.w)
		lbl_LP.move(left_offset_from_window, y_lbl_2)
		lbl_LP.setText(self.get_localized_text("Enter. Landmark phrase"))

		self.edt_LP = QLineEdit(self.w)
		self.edt_LP.resize(300, h_components)
		self.edt_LP.move(left_offset_from_window, y_lbl_2 + y_offset_from_lbl)
		self.edt_LP.textChanged[str].connect(self.setLandmarkPhrase)

		cb_LP = QCheckBox(self.get_localized_text("Visible"), self.w)
		cb_LP.setChecked(True)
		cb_LP.move(left_offset_from_window + x_offset_cb, y_lbl_2 + y_offset_from_lbl)
		cb_LP.stateChanged.connect(self.setVisibleLandmarkPhrase)

		# LUK-file
		y_lbl_3 = y_lbl_2 + dist_y_between_lbl
		lbl_LUK = QLabel(self.w)
		lbl_LUK.move(left_offset_from_window, y_lbl_3)
		lbl_LUK.setText(self.get_localized_text("Enter. Size LUK-file"))

		self.edt_LUK = QLineEdit(self.w)
		self.edt_LUK.resize(200, h_components)
		self.edt_LUK.move(left_offset_from_window, y_lbl_3 + y_offset_from_lbl)
		self.edt_LUK.textChanged[str].connect(self.setNumberSymbolsLUK)

		self.setVisibleEdtLUK()

		x_offset_btn = 270
		btn_Gen = QPushButton(self.get_localized_text("Create. LUK-file"), self.w)
		btn_Gen.resize(w_btn + 50, h_components)
		btn_Gen.move(left_offset_from_window + x_offset_btn, y_lbl_3 + y_offset_from_lbl)
		btn_Gen.clicked.connect(self.createNewLUKfile)


		# Bottom buttons
		y_offset_from_btn = 45
		self.lbl_message = QLabel(self.w)
		self.lbl_message.resize(435, h_components)
		self.lbl_message.move(left_offset_from_window, y_btn - y_offset_from_btn)

		btn_Create = QPushButton(self.get_localized_text("Create"), self.w)
		btn_Create.resize(w_btn, h_components)
		btn_Create.move(left_offset_from_window, y_btn)
		btn_Create.clicked.connect(self.createPassword)

		btn_Clear = QPushButton(self.get_localized_text("Clear"), self.w)
		btn_Clear.resize(w_btn + 100, h_components)
		btn_Clear.move(left_offset_from_window + w_btn + 100, y_btn)
		btn_Clear.clicked.connect(self.clearAll)

	def getAvailabilityLUKfile(self):
		return self.isVisibleEdtLUK

	def setVisibleEdtLUK(self):
		if self.getAvailabilityLUKfile():
			self.edt_LUK.setEnabled(False)
		else:
			self.edt_LUK.setEnabled(True)

	def deleteLUKfile(self):
		# TODO #XX: Перанесці з гэтага модуля?
		import os
		os.remove("LUK")

	def createNewLUKfile(self):
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
			self.deleteLUKfile()
			self.updateCheckLUKfile()
			self.setVisibleEdtLUK()
		else:
			print("no")


	def processingNumLUK(self, string):
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

	def getNumSymbolsLUK(self):
		# The greater the number of characters specified, the greater the entropy of the LUK-file
		# Чем больше указано количество символов, тем больше энтропия ЛУК-файла
		numberLUKsymbols = self.getNumberSymbolsLUK()

		numberLUKsymbols = self.processingNumLUK(numberLUKsymbols)
		if numberLUKsymbols != -1:
			return numberLUKsymbols
		else:
			return -1

	def createPassword(self):
		privateKey = self.getPrivateKey()
		landmarkPhrase = self.getLandmarkPhrase()

		encryptedPrivateKey = gp.getHashString(privateKey)
		encryptedLandmarkPhrase = gp.getHashString(landmarkPhrase)

		UnicodePrivateKey = gp.convertToUnicode(encryptedPrivateKey)[::-1]
		UnicodeLandmarkPhrase = gp.convertToUnicode(encryptedLandmarkPhrase)

		A = gp.encryptionXOR(UnicodeLandmarkPhrase, UnicodePrivateKey)

		if not gp.isLUKfile():
			numberLUKsymbols = self.getNumSymbolsLUK()
			if numberLUKsymbols != -1:
				gp.createLUK(numberLUKsymbols)

		if gp.isLUKfile():
			hashLUK = gp.getHashLUK().upper()
			B = gp.convertToUnicode(hashLUK)
			result = gp.convertToString(gp.encryptionXOR(A, B))
			self.copyPassInClipboard(result)

	def copyPassInClipboard(self, password):
		clipboard = QApplication.clipboard()
		clipboard.setText(password)
		# Вывод сообщения. Пароль успешно создан и скопирован
		self.lbl_message.setText(self.get_localized_text("Password copied"))

	def clearAll(self):
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
