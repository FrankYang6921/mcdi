# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\LZMPDev\Source\Repos\mcdi\qt_ui\EffectsAndPerformance.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_EffectsAndPerformanceForm(object):
    def setupUi(self, EffectsAndPerformanceForm):
        EffectsAndPerformanceForm.setObjectName("EffectsAndPerformanceForm")
        EffectsAndPerformanceForm.resize(551, 521)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(48, 48, 48))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(22, 22, 22))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(48, 48, 48))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(22, 22, 22))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(22, 22, 22))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(22, 22, 22))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        EffectsAndPerformanceForm.setPalette(palette)
        self.AllowStereoSpectrograph = QtWidgets.QCheckBox(EffectsAndPerformanceForm)
        self.AllowStereoSpectrograph.setGeometry(QtCore.QRect(20, 0, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.AllowStereoSpectrograph.setFont(font)
        self.AllowStereoSpectrograph.setObjectName("AllowStereoSpectrograph")
        self.AllowOverallVolume = QtWidgets.QCheckBox(EffectsAndPerformanceForm)
        self.AllowOverallVolume.setGeometry(QtCore.QRect(190, 0, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.AllowOverallVolume.setFont(font)
        self.AllowOverallVolume.setObjectName("AllowOverallVolume")
        self.AllowPitchwheel = QtWidgets.QCheckBox(EffectsAndPerformanceForm)
        self.AllowPitchwheel.setGeometry(QtCore.QRect(360, 0, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.AllowPitchwheel.setFont(font)
        self.AllowPitchwheel.setObjectName("AllowPitchwheel")
        self.Label1 = QtWidgets.QLabel(EffectsAndPerformanceForm)
        self.Label1.setGeometry(QtCore.QRect(20, 40, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.Label1.setFont(font)
        self.Label1.setObjectName("Label1")
        self.PitchFactorSpinBox = QtWidgets.QDoubleSpinBox(EffectsAndPerformanceForm)
        self.PitchFactorSpinBox.setGeometry(QtCore.QRect(210, 40, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.PitchFactorSpinBox.setFont(font)
        self.PitchFactorSpinBox.setStyleSheet("background-color: rgb(48, 48, 48);\n"
"color: rgb(255, 255, 255); \n"
"font: 10pt \"Microsoft YaHei UI\";")
        self.PitchFactorSpinBox.setMaximum(1.0)
        self.PitchFactorSpinBox.setSingleStep(0.01)
        self.PitchFactorSpinBox.setProperty("value", 1.0)
        self.PitchFactorSpinBox.setObjectName("PitchFactorSpinBox")
        self.Label2 = QtWidgets.QLabel(EffectsAndPerformanceForm)
        self.Label2.setGeometry(QtCore.QRect(20, 90, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.Label2.setFont(font)
        self.Label2.setObjectName("Label2")
        self.VolumeFactorSpinBox = QtWidgets.QDoubleSpinBox(EffectsAndPerformanceForm)
        self.VolumeFactorSpinBox.setGeometry(QtCore.QRect(210, 90, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.VolumeFactorSpinBox.setFont(font)
        self.VolumeFactorSpinBox.setStyleSheet("background-color: rgb(48, 48, 48);\n"
"color: rgb(255, 255, 255); \n"
"font: 10pt \"Microsoft YaHei UI\";")
        self.VolumeFactorSpinBox.setMaximum(1.0)
        self.VolumeFactorSpinBox.setSingleStep(0.01)
        self.VolumeFactorSpinBox.setProperty("value", 1.0)
        self.VolumeFactorSpinBox.setObjectName("VolumeFactorSpinBox")
        self.LongNoteAnalysis = QtWidgets.QCheckBox(EffectsAndPerformanceForm)
        self.LongNoteAnalysis.setGeometry(QtCore.QRect(20, 140, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.LongNoteAnalysis.setFont(font)
        self.LongNoteAnalysis.setChecked(True)
        self.LongNoteAnalysis.setObjectName("LongNoteAnalysis")
        self.LongNoteToleranceSpinBox = QtWidgets.QDoubleSpinBox(EffectsAndPerformanceForm)
        self.LongNoteToleranceSpinBox.setGeometry(QtCore.QRect(270, 140, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.LongNoteToleranceSpinBox.setFont(font)
        self.LongNoteToleranceSpinBox.setStyleSheet("background-color: rgb(48, 48, 48);\n"
"color: rgb(255, 255, 255); \n"
"font: 10pt \"Microsoft YaHei UI\";")
        self.LongNoteToleranceSpinBox.setDecimals(0)
        self.LongNoteToleranceSpinBox.setMaximum(99.0)
        self.LongNoteToleranceSpinBox.setSingleStep(1.0)
        self.LongNoteToleranceSpinBox.setProperty("value", 40.0)
        self.LongNoteToleranceSpinBox.setObjectName("LongNoteToleranceSpinBox")
        self.MaxSoundSpinBox = QtWidgets.QDoubleSpinBox(EffectsAndPerformanceForm)
        self.MaxSoundSpinBox.setGeometry(QtCore.QRect(210, 190, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.MaxSoundSpinBox.setFont(font)
        self.MaxSoundSpinBox.setStyleSheet("background-color: rgb(48, 48, 48);\n"
"color: rgb(255, 255, 255); \n"
"font: 10pt \"Microsoft YaHei UI\";")
        self.MaxSoundSpinBox.setDecimals(0)
        self.MaxSoundSpinBox.setMaximum(511.0)
        self.MaxSoundSpinBox.setSingleStep(1.0)
        self.MaxSoundSpinBox.setProperty("value", 255.0)
        self.MaxSoundSpinBox.setObjectName("MaxSoundSpinBox")
        self.Label3 = QtWidgets.QLabel(EffectsAndPerformanceForm)
        self.Label3.setGeometry(QtCore.QRect(20, 190, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.Label3.setFont(font)
        self.Label3.setObjectName("Label3")
        self.WrapLengthSpinBox = QtWidgets.QDoubleSpinBox(EffectsAndPerformanceForm)
        self.WrapLengthSpinBox.setGeometry(QtCore.QRect(210, 240, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.WrapLengthSpinBox.setFont(font)
        self.WrapLengthSpinBox.setStyleSheet("background-color: rgb(48, 48, 48);\n"
"color: rgb(255, 255, 255); \n"
"font: 10pt \"Microsoft YaHei UI\";")
        self.WrapLengthSpinBox.setDecimals(0)
        self.WrapLengthSpinBox.setMaximum(511.0)
        self.WrapLengthSpinBox.setSingleStep(1.0)
        self.WrapLengthSpinBox.setProperty("value", 127.0)
        self.WrapLengthSpinBox.setObjectName("WrapLengthSpinBox")
        self.Label4 = QtWidgets.QLabel(EffectsAndPerformanceForm)
        self.Label4.setGeometry(QtCore.QRect(20, 240, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.Label4.setFont(font)
        self.Label4.setObjectName("Label4")
        self.UseFunctionBasedTickArray = QtWidgets.QCheckBox(EffectsAndPerformanceForm)
        self.UseFunctionBasedTickArray.setGeometry(QtCore.QRect(20, 290, 411, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.UseFunctionBasedTickArray.setFont(font)
        self.UseFunctionBasedTickArray.setObjectName("UseFunctionBasedTickArray")

        self.retranslateUi(EffectsAndPerformanceForm)
        QtCore.QMetaObject.connectSlotsByName(EffectsAndPerformanceForm)

    def retranslateUi(self, EffectsAndPerformanceForm):
        _translate = QtCore.QCoreApplication.translate
        EffectsAndPerformanceForm.setWindowTitle(_translate("EffectsAndPerformanceForm", "Form"))
        self.AllowStereoSpectrograph.setText(_translate("EffectsAndPerformanceForm", "允许立体声像"))
        self.AllowOverallVolume.setText(_translate("EffectsAndPerformanceForm", "允许全局音量"))
        self.AllowPitchwheel.setText(_translate("EffectsAndPerformanceForm", "允许弯音轮"))
        self.Label1.setText(_translate("EffectsAndPerformanceForm", "弯音系数（倍率）："))
        self.Label2.setText(_translate("EffectsAndPerformanceForm", "音量系数（倍率）："))
        self.LongNoteAnalysis.setText(_translate("EffectsAndPerformanceForm", "长音分析   阈值（刻）："))
        self.Label3.setText(_translate("EffectsAndPerformanceForm", "单刻最大发音数："))
        self.Label4.setText(_translate("EffectsAndPerformanceForm", "折行长度（格）："))
        self.UseFunctionBasedTickArray.setText(_translate("EffectsAndPerformanceForm", "使用基于函数的刻阵列（实验性）"))