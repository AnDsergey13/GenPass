import sys
import time
from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class UIGP:
	# def __init__(self, typeOS):
	def __init__(self, width=450, height=450, pos_x=300, pos_y=300):
		# self.typeOS = typeOS
		self.width = width
		self.height = height
		self.pos_x = pos_x
		self.pos_y = pos_y

		self.password = "empty"

	def getWightWindow(self):
		return self.width

	def getHeightWindow(self):
		return self.height

	def setVisiblePrivateKey(self, value):
		if value == 0:
			self.e1.setEchoMode(QLineEdit.Password)
		else:
			self.e1.setEchoMode(QLineEdit.Normal)

	def setVisibleLandmarkPhrase(self, value):
		if value == 0:
			self.e2.setEchoMode(QLineEdit.Password)
		else:
			self.e2.setEchoMode(QLineEdit.Normal)

	def createWindow(self):
		self.app = QApplication(sys.argv)

		self.w = QWidget()
		self.w.resize(self.getWightWindow(), self.getHeightWindow())
		self.w.move(self.pos_x, self.pos_y)
		self.w.setWindowTitle('GenPass')
		self.w.setWindowIcon(QtGui.QIcon('icon/Panel.png'))
		
		x_lbl = 15
		y_lbl_1 = 15
		dist_between_lbl = 95
		self.l1 = QLabel(self.w)
		self.l1.move(x_lbl, y_lbl_1)
		self.l1.setText("Enter the private key:")

		y_lbl_2 = y_lbl_1 + dist_between_lbl
		self.l2 = QLabel(self.w)
		self.l2.move(x_lbl, y_lbl_2)
		self.l2.setText("Enter the landmark phrase:")

		x_offset_cb = 315
		y_offset_lbl = 30
		self.cb1 = QCheckBox("Visible", self.w)
		self.cb1.setChecked(True)
		self.cb1.move(x_lbl + x_offset_cb, y_lbl_1 + y_offset_lbl)
		self.cb1.stateChanged.connect(self.setVisiblePrivateKey)

		dist_between_edit = dist_between_lbl
		self.e1 = QLineEdit(self.w)
		self.e1.resize(300, 32)
		self.e1.move(x_lbl, y_lbl_1 + y_offset_lbl)

		self.cb2 = QCheckBox("Visible", self.w)
		self.cb2.setChecked(True)
		self.cb2.move(x_lbl + x_offset_cb, y_lbl_1 + y_offset_lbl + dist_between_edit)
		self.cb2.stateChanged.connect(self.setVisibleLandmarkPhrase)
		
		self.e2 = QLineEdit(self.w)
		self.e2.resize(300, 32)
		self.e2.move(x_lbl, y_lbl_1 + y_offset_lbl + dist_between_edit)

		x_btn = 30
		y_btn = 380
		w_btn = 100
		h_btn = 32
		dist_between_btn = 100
		self.ButtonCreate(w_btn, h_btn, x_btn, y_btn)
		self.ButtonClear(w_btn + 100, h_btn, x_btn + w_btn + dist_between_btn, y_btn)

		self.w.show()

		sys.exit(self.app.exec())


	def ButtonCreate(self, width=100, height=32, x=0, y=0):
		buttonCreate = QPushButton('Create', self.w)
		buttonCreate.resize(width, height)
		buttonCreate.move(x, y)
		buttonCreate.clicked.connect(self.CopyPassInClipboard)

	def ButtonClear(self, width=100, height=32, x=0, y=0):
		buttonClear = QPushButton('Clear', self.w)
		buttonClear.resize(width, height)
		buttonClear.move(x, y)
		buttonClear.clicked.connect(self.ClearAll)      
		

	def CopyPassInClipboard(self):
		clipboard = QApplication.clipboard()
		clipboard.setText(self.password)

	def ClearAll(self):
		# Clearing the clipboard
		# Очистка буфера
		clipboard = QApplication.clipboard()
		clipboard.clear()

		# Cleaning components
		# Очистка компонентов
		self.e1.clear()
		self.e2.clear()


ui = UIGP()
ui.createWindow()