# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created: Sat Aug 30 01:25:49 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from lib.qt import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(426, 626)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.build = QtGui.QComboBox(Dialog)
        self.build.setObjectName("build")
        self.verticalLayout.addWidget(self.build)
        self.line = QtGui.QFrame(Dialog)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.label_2 = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.formLayout_4 = QtGui.QFormLayout()
        self.formLayout_4.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_4.setObjectName("formLayout_4")
        self.resolutionLabel = QtGui.QLabel(Dialog)
        self.resolutionLabel.setObjectName("resolutionLabel")
        self.formLayout_4.setWidget(0, QtGui.QFormLayout.LabelRole, self.resolutionLabel)
        self.vid_res = QtGui.QComboBox(Dialog)
        self.vid_res.setObjectName("vid_res")
        self.formLayout_4.setWidget(0, QtGui.QFormLayout.FieldRole, self.vid_res)
        self.depthLabel = QtGui.QLabel(Dialog)
        self.depthLabel.setObjectName("depthLabel")
        self.formLayout_4.setWidget(1, QtGui.QFormLayout.LabelRole, self.depthLabel)
        self.vid_depth = QtGui.QComboBox(Dialog)
        self.vid_depth.setObjectName("vid_depth")
        self.formLayout_4.setWidget(1, QtGui.QFormLayout.FieldRole, self.vid_depth)
        self.horizontalLayout_2.addLayout(self.formLayout_4)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.textureFilterLabel = QtGui.QLabel(Dialog)
        self.textureFilterLabel.setObjectName("textureFilterLabel")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.textureFilterLabel)
        self.vid_texfilter = QtGui.QComboBox(Dialog)
        self.vid_texfilter.setObjectName("vid_texfilter")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.vid_texfilter)
        self.antialiasingLabel = QtGui.QLabel(Dialog)
        self.antialiasingLabel.setObjectName("antialiasingLabel")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.antialiasingLabel)
        self.vid_aa = QtGui.QComboBox(Dialog)
        self.vid_aa.setObjectName("vid_aa")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.vid_aa)
        self.anisotropicFilterLabel = QtGui.QLabel(Dialog)
        self.anisotropicFilterLabel.setObjectName("anisotropicFilterLabel")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.anisotropicFilterLabel)
        self.vid_af = QtGui.QComboBox(Dialog)
        self.vid_af.setObjectName("vid_af")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.vid_af)
        self.horizontalLayout_2.addLayout(self.formLayout)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.line_3 = QtGui.QFrame(Dialog)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        self.label_3 = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.formLayout_3 = QtGui.QFormLayout()
        self.formLayout_3.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_3.setObjectName("formLayout_3")
        self.playbackDeviceLabel = QtGui.QLabel(Dialog)
        self.playbackDeviceLabel.setObjectName("playbackDeviceLabel")
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.playbackDeviceLabel)
        self.snd_playback = QtGui.QComboBox(Dialog)
        self.snd_playback.setObjectName("snd_playback")
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.FieldRole, self.snd_playback)
        self.captureDeviceLabel = QtGui.QLabel(Dialog)
        self.captureDeviceLabel.setObjectName("captureDeviceLabel")
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.LabelRole, self.captureDeviceLabel)
        self.snd_capture = QtGui.QComboBox(Dialog)
        self.snd_capture.setObjectName("snd_capture")
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.FieldRole, self.snd_capture)
        self.verticalLayout.addLayout(self.formLayout_3)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.snd_efx = QtGui.QCheckBox(Dialog)
        self.snd_efx.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.snd_efx.setObjectName("snd_efx")
        self.horizontalLayout_5.addWidget(self.snd_efx)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.sampleRateLabel = QtGui.QLabel(Dialog)
        self.sampleRateLabel.setObjectName("sampleRateLabel")
        self.horizontalLayout_5.addWidget(self.sampleRateLabel)
        self.snd_samplerate = QtGui.QSpinBox(Dialog)
        self.snd_samplerate.setObjectName("snd_samplerate")
        self.horizontalLayout_5.addWidget(self.snd_samplerate)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.line_4 = QtGui.QFrame(Dialog)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout.addWidget(self.line_4)
        self.label_4 = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.ctrl_joystick = QtGui.QComboBox(Dialog)
        self.ctrl_joystick.setObjectName("ctrl_joystick")
        self.verticalLayout.addWidget(self.ctrl_joystick)
        self.line_6 = QtGui.QFrame(Dialog)
        self.line_6.setFrameShape(QtGui.QFrame.HLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.verticalLayout.addWidget(self.line_6)
        self.label_6 = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.formLayout_2 = QtGui.QFormLayout()
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setObjectName("formLayout_2")
        self.connectionTypeLabel = QtGui.QLabel(Dialog)
        self.connectionTypeLabel.setObjectName("connectionTypeLabel")
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.connectionTypeLabel)
        self.net_type = QtGui.QComboBox(Dialog)
        self.net_type.setObjectName("net_type")
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.net_type)
        self.connectionSpeedLabel = QtGui.QLabel(Dialog)
        self.connectionSpeedLabel.setObjectName("connectionSpeedLabel")
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.connectionSpeedLabel)
        self.net_speed = QtGui.QComboBox(Dialog)
        self.net_speed.setObjectName("net_speed")
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.net_speed)
        self.horizontalLayout_4.addLayout(self.formLayout_2)
        self.formLayout_6 = QtGui.QFormLayout()
        self.formLayout_6.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_6.setObjectName("formLayout_6")
        self.forceLocalPortLabel = QtGui.QLabel(Dialog)
        self.forceLocalPortLabel.setObjectName("forceLocalPortLabel")
        self.formLayout_6.setWidget(0, QtGui.QFormLayout.LabelRole, self.forceLocalPortLabel)
        self.net_port = QtGui.QLineEdit(Dialog)
        self.net_port.setObjectName("net_port")
        self.formLayout_6.setWidget(0, QtGui.QFormLayout.FieldRole, self.net_port)
        self.forceIPAddressLabel = QtGui.QLabel(Dialog)
        self.forceIPAddressLabel.setObjectName("forceIPAddressLabel")
        self.formLayout_6.setWidget(1, QtGui.QFormLayout.LabelRole, self.forceIPAddressLabel)
        self.net_ip = QtGui.QLineEdit(Dialog)
        self.net_ip.setObjectName("net_ip")
        self.formLayout_6.setWidget(1, QtGui.QFormLayout.FieldRole, self.net_ip)
        self.horizontalLayout_4.addLayout(self.formLayout_6)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.line_5 = QtGui.QFrame(Dialog)
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.verticalLayout.addWidget(self.line_5)
        self.label_5 = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.cmdButton = QtGui.QPushButton(Dialog)
        self.cmdButton.setObjectName("cmdButton")
        self.verticalLayout.addWidget(self.cmdButton)
        self.line_2 = QtGui.QFrame(Dialog)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.runButton = QtGui.QPushButton(Dialog)
        self.runButton.setDefault(True)
        self.runButton.setObjectName("runButton")
        self.horizontalLayout.addWidget(self.runButton)
        self.cancelButton = QtGui.QPushButton(Dialog)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout.addWidget(self.cancelButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "FreeSpace 2 Open build", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Video", None, QtGui.QApplication.UnicodeUTF8))
        self.resolutionLabel.setText(QtGui.QApplication.translate("Dialog", "Resolution :", None, QtGui.QApplication.UnicodeUTF8))
        self.depthLabel.setText(QtGui.QApplication.translate("Dialog", "Color depth :", None, QtGui.QApplication.UnicodeUTF8))
        self.textureFilterLabel.setText(QtGui.QApplication.translate("Dialog", "Texture filter :", None, QtGui.QApplication.UnicodeUTF8))
        self.antialiasingLabel.setText(QtGui.QApplication.translate("Dialog", "Antialiasing :", None, QtGui.QApplication.UnicodeUTF8))
        self.anisotropicFilterLabel.setText(QtGui.QApplication.translate("Dialog", "Anisotropic filtering :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "Audio", None, QtGui.QApplication.UnicodeUTF8))
        self.playbackDeviceLabel.setText(QtGui.QApplication.translate("Dialog", "Playback device :", None, QtGui.QApplication.UnicodeUTF8))
        self.captureDeviceLabel.setText(QtGui.QApplication.translate("Dialog", "Capture device :", None, QtGui.QApplication.UnicodeUTF8))
        self.snd_efx.setText(QtGui.QApplication.translate("Dialog", "Enable EFX", None, QtGui.QApplication.UnicodeUTF8))
        self.sampleRateLabel.setText(QtGui.QApplication.translate("Dialog", "Sample rate :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog", "Controller", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Dialog", "Network", None, QtGui.QApplication.UnicodeUTF8))
        self.connectionTypeLabel.setText(QtGui.QApplication.translate("Dialog", "Connection type :", None, QtGui.QApplication.UnicodeUTF8))
        self.connectionSpeedLabel.setText(QtGui.QApplication.translate("Dialog", "Connection speed :", None, QtGui.QApplication.UnicodeUTF8))
        self.forceLocalPortLabel.setText(QtGui.QApplication.translate("Dialog", "Force local port :", None, QtGui.QApplication.UnicodeUTF8))
        self.forceIPAddressLabel.setText(QtGui.QApplication.translate("Dialog", "Force IP address :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Dialog", "Advanced settings", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdButton.setText(QtGui.QApplication.translate("Dialog", "Command line flags for Mod name", None, QtGui.QApplication.UnicodeUTF8))
        self.runButton.setText(QtGui.QApplication.translate("Dialog", "Launch", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setText(QtGui.QApplication.translate("Dialog", "Close", None, QtGui.QApplication.UnicodeUTF8))

