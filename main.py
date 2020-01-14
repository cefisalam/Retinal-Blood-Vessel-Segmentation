# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BloodVessel.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

# Import Essential Libraries
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import random
import numpy as np
import cv2 as cv
from numpy.fft import fft2, ifft2
from os.path import isfile

# Start of GUI Initialization
class Ui_BloodVessel(object):
    def setupUi(self, BloodVessel):
        BloodVessel.setObjectName("BloodVessel")
        BloodVessel.resize(1138, 744)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("VIBOT.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        BloodVessel.setWindowIcon(icon)
        BloodVessel.setAutoFillBackground(True)
        BloodVessel.setStyleSheet("rgb (162, 254, 255)\n"
"background-color: rgb(97, 221, 255);")
        BloodVessel.setSizeGripEnabled(False)
        BloodVessel.setModal(False)
        self.label = QtWidgets.QLabel(BloodVessel)
        self.label.setGeometry(QtCore.QRect(160, 10, 831, 61))
        self.label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.InputConsole = QtWidgets.QGroupBox(BloodVessel)
        self.InputConsole.setGeometry(QtCore.QRect(260, 610, 661, 111))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(1, 1, 1))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(117, 80, 123))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(176, 120, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(146, 100, 154))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(58, 40, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(78, 53, 82))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(1, 1, 1))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(1, 1, 1))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(1, 1, 1))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(117, 80, 123))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(58, 40, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(1, 1, 1))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(117, 80, 123))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(176, 120, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(146, 100, 154))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(58, 40, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(78, 53, 82))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(1, 1, 1))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(1, 1, 1))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(1, 1, 1))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(117, 80, 123))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(58, 40, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(58, 40, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(117, 80, 123))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(176, 120, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(146, 100, 154))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(58, 40, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(78, 53, 82))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(58, 40, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(1, 1, 1))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(58, 40, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(117, 80, 123))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(117, 80, 123))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(117, 80, 123))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.InputConsole.setPalette(palette)
        self.InputConsole.setAlignment(QtCore.Qt.AlignCenter)
        self.InputConsole.setFlat(False)
        self.InputConsole.setCheckable(False)
        self.InputConsole.setObjectName("InputConsole")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.InputConsole)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 40, 591, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.LoadImageButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.LoadImageButton.setObjectName("LoadImageButton")
        self.horizontalLayout.addWidget(self.LoadImageButton)
        self.SegmentButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.SegmentButton.setObjectName("SegmentButton")
        self.horizontalLayout.addWidget(self.SegmentButton)
        self.ResetButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.ResetButton.setObjectName("ResetButton")
        self.horizontalLayout.addWidget(self.ResetButton)
        self.InputLabel = QtWidgets.QLabel(BloodVessel)
        self.InputLabel.setGeometry(QtCore.QRect(90, 90, 211, 211))
        self.InputLabel.setText("")
        self.InputLabel.setObjectName("InputLabel")
        self.label_5 = QtWidgets.QLabel(BloodVessel)
        self.label_5.setGeometry(QtCore.QRect(40, 580, 81, 101))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("VIBOT.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.GreenLabel = QtWidgets.QLabel(BloodVessel)
        self.GreenLabel.setGeometry(QtCore.QRect(360, 90, 211, 211))
        self.GreenLabel.setText("")
        self.GreenLabel.setObjectName("GreenLabel")
        self.InvertLabel = QtWidgets.QLabel(BloodVessel)
        self.InvertLabel.setGeometry(QtCore.QRect(890, 90, 211, 211))
        self.InvertLabel.setText("")
        self.InvertLabel.setObjectName("InvertLabel")
        self.AdapThreshLabel = QtWidgets.QLabel(BloodVessel)
        self.AdapThreshLabel.setGeometry(QtCore.QRect(620, 90, 211, 211))
        self.AdapThreshLabel.setText("")
        self.AdapThreshLabel.setObjectName("AdapThreshLabel")
        self.WeinerLabel = QtWidgets.QLabel(BloodVessel)
        self.WeinerLabel.setGeometry(QtCore.QRect(360, 360, 211, 211))
        self.WeinerLabel.setText("")
        self.WeinerLabel.setObjectName("WeinerLabel")
        self.OtsuLabel = QtWidgets.QLabel(BloodVessel)
        self.OtsuLabel.setGeometry(QtCore.QRect(620, 360, 211, 211))
        self.OtsuLabel.setText("")
        self.OtsuLabel.setObjectName("OtsuLabel")
        self.SharpLabel = QtWidgets.QLabel(BloodVessel)
        self.SharpLabel.setGeometry(QtCore.QRect(90, 360, 211, 211))
        self.SharpLabel.setText("")
        self.SharpLabel.setObjectName("SharpLabel")
        self.OutputLabel = QtWidgets.QLabel(BloodVessel)
        self.OutputLabel.setGeometry(QtCore.QRect(890, 360, 211, 211))
        self.OutputLabel.setText("")
        self.OutputLabel.setObjectName("OutputLabel")
        self.label_2 = QtWidgets.QLabel(BloodVessel)
        self.label_2.setGeometry(QtCore.QRect(150, 305, 91, 17))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(BloodVessel)
        self.label_3.setGeometry(QtCore.QRect(620, 305, 211, 20))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(BloodVessel)
        self.label_4.setGeometry(QtCore.QRect(940, 305, 111, 16))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(BloodVessel)
        self.label_6.setGeometry(QtCore.QRect(410, 305, 111, 20))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(BloodVessel)
        self.label_7.setGeometry(QtCore.QRect(920, 575, 151, 16))
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(BloodVessel)
        self.label_8.setGeometry(QtCore.QRect(640, 575, 171, 16))
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(BloodVessel)
        self.label_9.setGeometry(QtCore.QRect(380, 575, 171, 16))
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(BloodVessel)
        self.label_10.setGeometry(QtCore.QRect(130, 575, 131, 17))
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")

        self.retranslateUi(BloodVessel)
        QtCore.QMetaObject.connectSlotsByName(BloodVessel)

    def retranslateUi(self, BloodVessel):
        _translate = QtCore.QCoreApplication.translate
        BloodVessel.setWindowTitle(_translate("BloodVessel", "Blood Vessel Segmentation"))
        self.label.setText(_translate("BloodVessel", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; font-style:italic; color:#75507b;\">Retinal Blood Vessel Segmentation using Morphological Operations</span></p></body></html>"))
        self.InputConsole.setTitle(_translate("BloodVessel", "Console"))
        self.LoadImageButton.setText(_translate("BloodVessel", "Load Image"))
        self.SegmentButton.setText(_translate("BloodVessel", "Segment"))
        self.ResetButton.setText(_translate("BloodVessel", "Reset"))
        self.label_2.setText(_translate("BloodVessel", "Input Image"))
        self.label_3.setText(_translate("BloodVessel", "Adaptive Thresholded Image"))
        self.label_4.setText(_translate("BloodVessel", "Inverted Image"))
        self.label_6.setText(_translate("BloodVessel", "Green Channel"))
        self.label_7.setText(_translate("BloodVessel", "Blood Vessel Image"))
        self.label_8.setText(_translate("BloodVessel", "Otsu Thresholded Image"))
        self.label_9.setText(_translate("BloodVessel", "Weiner Filtered Image"))
        self.label_10.setText(_translate("BloodVessel", "Sharpened Image"))
# End of GUI Initialization

        # Connect All Push Buttons to the corresponding functions
        self.LoadImageButton.clicked.connect(self.on_LoadImageButton_clicked)
        self.SegmentButton.clicked.connect(self.on_SegmentButton_clicked)
        self.SegmentButton.setEnabled(False)
        self.ResetButton.clicked.connect(self.on_ResetButton_clicked)

    def on_LoadImageButton_clicked(self):
        # Load an Image with File Picker (Found on https://doc.qt.io/qt-5/qfiledialog.html)
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(BloodVessel,"Select an Image","","Image Files (*.jpg *.jpeg *.JPG *.tif *.tiff *.png *.bmp)", options=options)
        if isfile(fileName):
            # Read the Image
            img = cv.imread(fileName)
            global Img
            Img = img
            # Show the Message (Found on https://doc.qt.io/qtforpython/PySide2/QtWidgets/QMessageBox.html)
            msgBox = QMessageBox()
            msgBox.setStyleSheet("QLabel{min-width:300 px; font-size: 16px;} QPushButton{ width:100px; font-size:12px; }")
            msgBox.setText("Image Loaded Successfully")
            msgBox.exec_()
            self.SegmentButton.setEnabled(True)
        else:
            # Show the Message
            msgBox = QMessageBox()
            msgBox.setStyleSheet("QLabel{min-width:300 px; font-size: 16px;} QPushButton{ width:100px; font-size:12px; }")
            msgBox.setText("Attention!")
            msgBox.setInformativeText("No Image Loaded!!!")
            msgBox.exec_()

    def on_SegmentButton_clicked(self):
        # Extract the Color Channels of the Input Image
        b,g,r = cv.split(Img);

        # Perform Adaptive Thresholding using Gaussian Kernel
        th = cv.adaptiveThreshold(g,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,15,2);

        # Invert the Binary Image
        not_th = cv.bitwise_not(th)

        # Sharpen the Inverted Image
        kernel = np.array([[-1,-1,-1],
                   [-1, 9,-1],
                   [-1,-1,-1]])
        sharpened = cv.filter2D(not_th, -1, kernel)

        # Perform Weiner Filtering
        w_kernel = np.array([[0.0128,0.0876,0.0128],
                   [0.0876,0.5986,0.0876],
                   [0.0128,0.0876,0.0128]])
        Weiner = wiener_filter(sharpened, w_kernel, 50)

        # Perform Otsu Thresholding
        ret3,th3 = cv.threshold(Weiner,0,255,cv.THRESH_OTSU)

        # Perform Morphological Opening to extract the blood vessels.
        m_kernel = np.ones((3,3),np.uint8)
        opening = cv.morphologyEx(th3, cv.MORPH_OPEN, m_kernel)

        # Show the Results
        input = cv.resize(Img, (211, 211))
        input = cv.cvtColor(input, cv.COLOR_BGR2RGB)
        h, w, ch = input.shape
        bytesPerLine = ch * w
        convertToQtFormat = QtGui.QImage(input, w, h, bytesPerLine, QtGui.QImage.Format_RGB888)
        pixmap = QPixmap(convertToQtFormat)
        self.InputLabel.setPixmap(pixmap)

        g = cv.resize(g, (211, 211))
        h, w = g.shape
        bytesPerLine = w
        convertToQtFormat = QtGui.QImage(g, w, h, bytesPerLine, QtGui.QImage.Format_Grayscale8)
        pixmap = QPixmap(convertToQtFormat)
        self.GreenLabel.setPixmap(pixmap)

        th = cv.resize(th, (211, 211))
        h, w = th.shape
        bytesPerLine = w
        convertToQtFormat = QtGui.QImage(th, w, h, bytesPerLine, QtGui.QImage.Format_Grayscale8)
        pixmap = QPixmap(convertToQtFormat)
        self.AdapThreshLabel.setPixmap(pixmap)

        not_th = cv.resize(not_th, (211, 211))
        h, w = not_th.shape
        bytesPerLine = w
        convertToQtFormat = QtGui.QImage(not_th, w, h, bytesPerLine, QtGui.QImage.Format_Grayscale8)
        pixmap = QPixmap(convertToQtFormat)
        self.InvertLabel.setPixmap(pixmap)

        sharpened = cv.resize(sharpened, (211, 211))
        h, w = sharpened.shape
        bytesPerLine = w
        convertToQtFormat = QtGui.QImage(sharpened, w, h, bytesPerLine, QtGui.QImage.Format_Grayscale8)
        pixmap = QPixmap(convertToQtFormat)
        self.SharpLabel.setPixmap(pixmap)

        a,b = cv.threshold(Weiner,0,255,cv.THRESH_BINARY)
        b = cv.resize(b, (211, 211))
        h, w = b.shape
        bytesPerLine = w
        convertToQtFormat = QtGui.QImage(b, w, h, bytesPerLine, QtGui.QImage.Format_Grayscale8)
        pixmap = QPixmap(convertToQtFormat)
        self.WeinerLabel.setPixmap(pixmap)

        th3 = cv.resize(th3, (211, 211))
        h, w = th3.shape
        bytesPerLine = w
        convertToQtFormat = QtGui.QImage(th3, w, h, bytesPerLine, QtGui.QImage.Format_Grayscale8)
        pixmap = QPixmap(convertToQtFormat)
        self.OtsuLabel.setPixmap(pixmap)

        opening = cv.resize(opening, (211, 211))
        h, w = opening.shape
        bytesPerLine = w
        convertToQtFormat = QtGui.QImage(opening, w, h, bytesPerLine, QtGui.QImage.Format_Grayscale8)
        pixmap = QPixmap(convertToQtFormat)
        self.OutputLabel.setPixmap(pixmap)

    def on_ResetButton_clicked(self):
        self.SegmentButton.setEnabled(False)
        self.InputLabel.clear()
        self.GreenLabel.clear()
        self.AdapThreshLabel.clear()
        self.InvertLabel.clear()
        self.SharpLabel.clear()
        self.WeinerLabel.clear()
        self.OtsuLabel.clear()
        self.OutputLabel.clear()

def wiener_filter(img, kernel, K):
    dummy = np.copy(img)
    kernel = np.pad(kernel, [(0, dummy.shape[0] - kernel.shape[0]), (0, dummy.shape[1] - kernel.shape[1])], 'constant')
    # Fourier Transform
    dummy = fft2(dummy)
    kernel = fft2(kernel)
    kernel = np.conj(kernel) / (np.abs(kernel) ** 2 + K)
    dummy = dummy * kernel
    dummy = np.abs(ifft2(dummy))
    return np.uint8(dummy)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BloodVessel = QtWidgets.QDialog()
    ui = Ui_BloodVessel()
    ui.setupUi(BloodVessel)
    BloodVessel.show()
    sys.exit(app.exec_())
