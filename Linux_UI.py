import sys
from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class UIGP:
	def __init__(self, localization):
		self.localization = localization
		self.privateKey = ""
		self.landmarkPhrase = ""
		self.password = ""
		self.numberSymbolsLUK = 5000

	# Private key
	def setPrivateKey(self, string):
		print("PK = ", string)
		self.privateKey = string
		
	def getPrivateKey(self):
		return self.privateKey

	# Landmark phrase
	def setLandmarkPhrase(self, string):
		print("LP = ", string)
		self.landmarkPhrase = string
		
	def getLandmarkPhrase(self):
		return self.landmarkPhrase

	# Number symbols LUK
	def setNumberSymbolsLUK(self, number):
		print("LUK = ", number)
		self.numberSymbolsLUK = number
		
	def getNumberSymbolsLUK(self):
		return self.numberSymbolsLUK

	# Password
	def setPassword(self, string):
		print("Password = ", string)
		self.password = string


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

	def createWindow(self, width=450, height=450, pos_x=300, pos_y=300):
		app = QApplication(sys.argv)

		self.w = QWidget()
		self.w.resize(width, height)
		self.w.move(pos_x, pos_y)
		self.w.setWindowTitle('GenPass')
		self.w.setWindowIcon(QtGui.QIcon('icon/Panel.png'))
		
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
		lbl_PK.setText(self.localization[0])

		self.edt_PK = QLineEdit(self.w)
		self.edt_PK.resize(300, h_components)
		self.edt_PK.move(left_offset_from_window, y_lbl_1 + y_offset_from_lbl)
		self.edt_PK.textChanged[str].connect(self.setPrivateKey)

		cb_PK = QCheckBox(self.localization[7], self.w)
		cb_PK.setChecked(True)
		cb_PK.move(left_offset_from_window + x_offset_cb, y_lbl_1 + y_offset_from_lbl)
		cb_PK.stateChanged.connect(self.setVisiblePrivateKey)

		# LandmarkPhrase
		y_lbl_2 = y_lbl_1 + dist_y_between_lbl
		lbl_LP = QLabel(self.w)
		lbl_LP.move(left_offset_from_window, y_lbl_2)
		lbl_LP.setText(self.localization[1])

		self.edt_LP = QLineEdit(self.w)
		self.edt_LP.resize(300, h_components)
		self.edt_LP.move(left_offset_from_window, y_lbl_2 + y_offset_from_lbl)
		self.edt_LP.textChanged[str].connect(self.setLandmarkPhrase)

		cb_LP = QCheckBox(self.localization[7], self.w)
		cb_LP.setChecked(True)
		cb_LP.move(left_offset_from_window + x_offset_cb, y_lbl_2 + y_offset_from_lbl)
		cb_LP.stateChanged.connect(self.setVisibleLandmarkPhrase)

		# LUK-file
		y_lbl_3 = y_lbl_2 + dist_y_between_lbl
		lbl_LUK = QLabel(self.w)
		lbl_LUK.move(left_offset_from_window, y_lbl_3)
		lbl_LUK.setText(self.localization[6])
		
		self.edt_LUK = QLineEdit(self.w)
		self.edt_LUK.resize(200, h_components)
		self.edt_LUK.move(left_offset_from_window, y_lbl_3 + y_offset_from_lbl)
		self.edt_LUK.textChanged[str].connect(self.setNumberSymbolsLUK)

		x_offset_btn = 270
		btn_Gen = QPushButton(self.localization[10], self.w)
		btn_Gen.resize(w_btn + 50, h_components)
		btn_Gen.move(left_offset_from_window + x_offset_btn, y_lbl_3 + y_offset_from_lbl)
		# btn_Gen.clicked.connect(self.ClearAll)


		# Bottom buttons
		y_offset_from_btn = 45
		self.lbl_message = QLabel(self.w)
		self.lbl_message.move(left_offset_from_window, y_btn - y_offset_from_btn)
		self.lbl_message.resize(300, h_components)

		btn_Create = QPushButton(self.localization[8], self.w)
		btn_Create.resize(w_btn, h_components)
		btn_Create.move(left_offset_from_window, y_btn)
		btn_Create.clicked.connect(self.CopyPassInClipboard)

		btn_Clear = QPushButton(self.localization[9], self.w)
		btn_Clear.resize(w_btn + 100, h_components)
		btn_Clear.move(left_offset_from_window + w_btn + 100, y_btn)
		btn_Clear.clicked.connect(self.ClearAll)

	def CopyPassInClipboard(self):
		clipboard = QApplication.clipboard()
		clipboard.setText(self.password)
		self.lbl_message.setText(self.localization[11])

	def ClearAll(self):
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




# privateKey = ui.getPrivateKey()
# landmarkPhrase = ui.getLandmarkPhrase()

# encryptedPrivateKey = gp.getHashString(privateKey)
# encryptedLandmarkPhrase = gp.getHashString(landmarkPhrase)

# UnicodePrivateKey = gp.convertToUnicode(encryptedPrivateKey)[::-1]
# UnicodeLandmarkPhrase = gp.convertToUnicode(encryptedLandmarkPhrase)

# A = gp.encryptionXOR(UnicodeLandmarkPhrase, UnicodePrivateKey)

# if not gp.isLUKfile():
# 	numberLUKsymbols = getNumLUKsymbols()
# 	gp.createLUK(numberLUKsymbols)

# hashLUK = gp.getHashLUK().upper()

# B = gp.convertToUnicode(hashLUK)

# result = gp.convertToString(gp.encryptionXOR(A, B))
# ui.setPassword(result)