#############################################################
#			-Sistem Berbasis Mikrokontroler-				#
#	Displaying Ultrasonic Data from Arduino using Python	#
#															#
#	Modified by		: Dananjaya Ariateja					#
#	Departement		: Electrical Engineering,				#
#					  Universitas Gadjah Mada				#
#	Last Modified	: 23 September 2017						#
#############################################################	

import sys, os, glob
from PyQt4 import QtCore, QtGui, uic
import serial, time, threading

qtCreatorFile = "myGUI.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtGui.QMainWindow, Ui_MainWindow):
	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		Ui_MainWindow.__init__(self)
		self.setupUi(self)
		self.pushButton_OpenSerial.clicked.connect(self.OpenSerial)
		self.pushButton_Exit.clicked.connect(self.AppExit)
		self.pushButton_On.clicked.connect(self.On)
		self.pushButton_Off.clicked.connect(self.Off)
		self.pushButton_us.pressed.connect(self.Sensor)
		self.pushButton_Clear.clicked.connect(self.Clear)
		
		self.pushButton_us.setEnabled(False)
		self.pushButton_On.setEnabled(False)
		self.pushButton_Off.setEnabled(False)
		self.pushButton_Clear.setEnabled(False)

		
	def OpenSerial(self):
		self.OpenSerial = 0
		while self.OpenSerial < 100:
			self.OpenSerial += 0.0001
			self.progressBar.setValue(self.OpenSerial)
			
		if self.pushButton_OpenSerial.text()=='Open Serial':
			self.ser = serial.Serial("COM3", "115200", timeout=0.1)
			if self.ser.isOpen():
				self.pushButton_us.setEnabled(True)
				self.pushButton_On.setEnabled(True)
				self.pushButton_Off.setEnabled(True)
				self.pushButton_Clear.setEnabled(True)
				self.pushButton_OpenSerial.setText('Close Serial')
				self.textEdit_LogMessage.append("Opening serial port... OK")
								
			else:
				self.textEdit_LogMessage.append("can not open serial port")
		else:
			if self.ser.isOpen():
				self.ser.close()
				self.pushButton_OpenSerial.setText('Open Serial')
				self.pushButton_us.setEnabled(False)
				self.pushButton_On.setEnabled(False)
				self.pushButton_Off.setEnabled(False)
				self.pushButton_Clear.setEnabled(False)
				self.textEdit_LogMessage.append("Closing serial port... OK")
				
	def On(self):
		self.ser.write('H'.encode())
		self.textEdit_LogMessage.append("Led On")
	
	def Off(self):
		self.ser.write('L'.encode())
		self.textEdit_LogMessage.append("Led Off")
	
	def Sensor(self):
		self.ser.write('S'.encode())
		self.bytesToRead = self.ser.inWaiting()
		if (self.bytesToRead > 0):
			rxdata = self.ser.read(self.bytesToRead)
			self.textEdit_LogMessage.append(str(rxdata.decode()))
			self.lcdNumber.display(str(rxdata.decode()))
	
	def Clear(self):
		self.textEdit_LogMessage.clear()
		self.lcdNumber.display(str(0))

	def AppExit(self):
		choice = QtGui.QMessageBox.question(self, 'Quit Application',
                                            "Are you want to quit?",
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
		if choice == QtGui.QMessageBox.Yes:
			sys.exit()
		else:
			pass

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
