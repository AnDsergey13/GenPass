import sys
from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
	QApplication,
	QCheckBox,
	QComboBox,
	QDateEdit,
	QDateTimeEdit,
	QDial,
	QDoubleSpinBox,
	QFontComboBox,
	QLabel,
	QLCDNumber,
	QLineEdit,
	QMainWindow,
	QProgressBar,
	QPushButton,
	QRadioButton,
	QSlider,
	QSpinBox,
	QTimeEdit,
	QVBoxLayout,
	QWidget,
)

class UIGP:
	# def __init__(self, typeOS):
	def __init__(self):
		pass
		# self.typeOS = typeOS

	def createWindow(self):

		app = QApplication(sys.argv)

		self.w = QWidget()
		self.w.resize(450, 450)
		self.w.move(300, 300)
		self.w.setWindowTitle('GenPass')
		self.w.setWindowIcon(QtGui.QIcon('icon/Panel.png'))
		
		self.createElements()
		self.w.show()

		sys.exit(app.exec_())

	def createElements(self):
		createButton = QPushButton('Create', self.w)
		createButton.resize(100,32)
		createButton.move(30, 380)        
		# pybutton.clicked.connect(self.clickMethod)
		pass
