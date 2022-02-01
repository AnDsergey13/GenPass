import sys
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
	def __init__(self, typeOS):

		self.typeOS = typeOS

	def createWindow(self):

		app = QApplication(sys.argv)

		w = QWidget()
		w.resize(250, 150)
		w.move(300, 300)
		w.setWindowTitle('Simple')
		w.show()

		sys.exit(app.exec_())
		# Arch
		if self.typeOS[0] == 0:
			pass

		elif self.typeOS[0] == 1: # Android
			pass
		elif self.typeOS[0] == 2: # Windows
			pass