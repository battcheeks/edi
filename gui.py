# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1090, 938)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.frame)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 234, 1100))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.toolBox = QtWidgets.QToolBox(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolBox.sizePolicy().hasHeightForWidth())
        self.toolBox.setSizePolicy(sizePolicy)
        self.toolBox.setObjectName("toolBox")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setGeometry(QtCore.QRect(0, 0, 210, 103))
        self.page_3.setObjectName("page_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.page_3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.scrollArea_3 = QtWidgets.QScrollArea(self.page_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea_3.sizePolicy().hasHeightForWidth())
        self.scrollArea_3.setSizePolicy(sizePolicy)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_5 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_5.setGeometry(QtCore.QRect(0, 0, 184, 77))
        self.scrollAreaWidgetContents_5.setObjectName("scrollAreaWidgetContents_5")
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_5)
        self.horizontalLayout_4.addWidget(self.scrollArea_3)
        self.toolBox.addItem(self.page_3, "")
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setGeometry(QtCore.QRect(0, 0, 210, 103))
        self.page_6.setObjectName("page_6")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.page_6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.scrollArea_4 = QtWidgets.QScrollArea(self.page_6)
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollArea_4.setObjectName("scrollArea_4")
        self.scrollAreaWidgetContents_6 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_6.setGeometry(QtCore.QRect(0, 0, 184, 77))
        self.scrollAreaWidgetContents_6.setObjectName("scrollAreaWidgetContents_6")
        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_6)
        self.horizontalLayout_5.addWidget(self.scrollArea_4)
        self.toolBox.addItem(self.page_6, "")
        self.verticalLayout.addWidget(self.toolBox)
        self.toolBox_2 = QtWidgets.QToolBox(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolBox_2.sizePolicy().hasHeightForWidth())
        self.toolBox_2.setSizePolicy(sizePolicy)
        self.toolBox_2.setObjectName("toolBox_2")
        self.page_7 = QtWidgets.QWidget()
        self.page_7.setGeometry(QtCore.QRect(0, 0, 210, 103))
        self.page_7.setObjectName("page_7")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.page_7)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.scrollArea_5 = QtWidgets.QScrollArea(self.page_7)
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollArea_5.setObjectName("scrollArea_5")
        self.scrollAreaWidgetContents_7 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_7.setGeometry(QtCore.QRect(0, 0, 184, 77))
        self.scrollAreaWidgetContents_7.setObjectName("scrollAreaWidgetContents_7")
        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_7)
        self.horizontalLayout_6.addWidget(self.scrollArea_5)
        self.toolBox_2.addItem(self.page_7, "")
        self.page_8 = QtWidgets.QWidget()
        self.page_8.setGeometry(QtCore.QRect(0, 0, 210, 103))
        self.page_8.setObjectName("page_8")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.page_8)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.scrollArea_6 = QtWidgets.QScrollArea(self.page_8)
        self.scrollArea_6.setWidgetResizable(True)
        self.scrollArea_6.setObjectName("scrollArea_6")
        self.scrollAreaWidgetContents_14 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_14.setGeometry(QtCore.QRect(0, 0, 184, 77))
        self.scrollAreaWidgetContents_14.setObjectName("scrollAreaWidgetContents_14")
        self.scrollArea_6.setWidget(self.scrollAreaWidgetContents_14)
        self.horizontalLayout_7.addWidget(self.scrollArea_6)
        self.toolBox_2.addItem(self.page_8, "")
        self.verticalLayout.addWidget(self.toolBox_2)
        self.toolBox_3 = QtWidgets.QToolBox(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolBox_3.sizePolicy().hasHeightForWidth())
        self.toolBox_3.setSizePolicy(sizePolicy)
        self.toolBox_3.setObjectName("toolBox_3")
        self.page_9 = QtWidgets.QWidget()
        self.page_9.setGeometry(QtCore.QRect(0, 0, 210, 103))
        self.page_9.setObjectName("page_9")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.page_9)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.scrollArea_7 = QtWidgets.QScrollArea(self.page_9)
        self.scrollArea_7.setWidgetResizable(True)
        self.scrollArea_7.setObjectName("scrollArea_7")
        self.scrollAreaWidgetContents_15 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_15.setGeometry(QtCore.QRect(0, 0, 184, 77))
        self.scrollAreaWidgetContents_15.setObjectName("scrollAreaWidgetContents_15")
        self.scrollArea_7.setWidget(self.scrollAreaWidgetContents_15)
        self.horizontalLayout_8.addWidget(self.scrollArea_7)
        self.toolBox_3.addItem(self.page_9, "")
        self.page_10 = QtWidgets.QWidget()
        self.page_10.setGeometry(QtCore.QRect(0, 0, 210, 103))
        self.page_10.setObjectName("page_10")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.page_10)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.scrollArea_14 = QtWidgets.QScrollArea(self.page_10)
        self.scrollArea_14.setWidgetResizable(True)
        self.scrollArea_14.setObjectName("scrollArea_14")
        self.scrollAreaWidgetContents_16 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_16.setGeometry(QtCore.QRect(0, 0, 184, 77))
        self.scrollAreaWidgetContents_16.setObjectName("scrollAreaWidgetContents_16")
        self.scrollArea_14.setWidget(self.scrollAreaWidgetContents_16)
        self.horizontalLayout_9.addWidget(self.scrollArea_14)
        self.toolBox_3.addItem(self.page_10, "")
        self.verticalLayout.addWidget(self.toolBox_3)
        self.toolBox_4 = QtWidgets.QToolBox(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolBox_4.sizePolicy().hasHeightForWidth())
        self.toolBox_4.setSizePolicy(sizePolicy)
        self.toolBox_4.setObjectName("toolBox_4")
        self.page_15 = QtWidgets.QWidget()
        self.page_15.setGeometry(QtCore.QRect(0, 0, 210, 103))
        self.page_15.setObjectName("page_15")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.page_15)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.scrollArea_15 = QtWidgets.QScrollArea(self.page_15)
        self.scrollArea_15.setWidgetResizable(True)
        self.scrollArea_15.setObjectName("scrollArea_15")
        self.scrollAreaWidgetContents_17 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_17.setGeometry(QtCore.QRect(0, 0, 184, 77))
        self.scrollAreaWidgetContents_17.setObjectName("scrollAreaWidgetContents_17")
        self.scrollArea_15.setWidget(self.scrollAreaWidgetContents_17)
        self.horizontalLayout_16.addWidget(self.scrollArea_15)
        self.toolBox_4.addItem(self.page_15, "")
        self.page_16 = QtWidgets.QWidget()
        self.page_16.setGeometry(QtCore.QRect(0, 0, 210, 103))
        self.page_16.setObjectName("page_16")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.page_16)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.scrollArea_16 = QtWidgets.QScrollArea(self.page_16)
        self.scrollArea_16.setWidgetResizable(True)
        self.scrollArea_16.setObjectName("scrollArea_16")
        self.scrollAreaWidgetContents_18 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_18.setGeometry(QtCore.QRect(0, 0, 184, 77))
        self.scrollAreaWidgetContents_18.setObjectName("scrollAreaWidgetContents_18")
        self.scrollArea_16.setWidget(self.scrollAreaWidgetContents_18)
        self.horizontalLayout_17.addWidget(self.scrollArea_16)
        self.toolBox_4.addItem(self.page_16, "")
        self.verticalLayout.addWidget(self.toolBox_4)
        self.toolBox_5 = QtWidgets.QToolBox(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolBox_5.sizePolicy().hasHeightForWidth())
        self.toolBox_5.setSizePolicy(sizePolicy)
        self.toolBox_5.setObjectName("toolBox_5")
        self.page_17 = QtWidgets.QWidget()
        self.page_17.setGeometry(QtCore.QRect(0, 0, 210, 103))
        self.page_17.setObjectName("page_17")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.page_17)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.scrollArea_17 = QtWidgets.QScrollArea(self.page_17)
        self.scrollArea_17.setWidgetResizable(True)
        self.scrollArea_17.setObjectName("scrollArea_17")
        self.scrollAreaWidgetContents_19 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_19.setGeometry(QtCore.QRect(0, 0, 184, 77))
        self.scrollAreaWidgetContents_19.setObjectName("scrollAreaWidgetContents_19")
        self.scrollArea_17.setWidget(self.scrollAreaWidgetContents_19)
        self.horizontalLayout_18.addWidget(self.scrollArea_17)
        self.toolBox_5.addItem(self.page_17, "")
        self.page_18 = QtWidgets.QWidget()
        self.page_18.setGeometry(QtCore.QRect(0, 0, 210, 103))
        self.page_18.setObjectName("page_18")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.page_18)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.scrollArea_18 = QtWidgets.QScrollArea(self.page_18)
        self.scrollArea_18.setWidgetResizable(True)
        self.scrollArea_18.setObjectName("scrollArea_18")
        self.scrollAreaWidgetContents_20 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_20.setGeometry(QtCore.QRect(0, 0, 184, 77))
        self.scrollAreaWidgetContents_20.setObjectName("scrollAreaWidgetContents_20")
        self.scrollArea_18.setWidget(self.scrollAreaWidgetContents_20)
        self.horizontalLayout_19.addWidget(self.scrollArea_18)
        self.toolBox_5.addItem(self.page_18, "")
        self.verticalLayout.addWidget(self.toolBox_5)
        self.toolBox_6 = QtWidgets.QToolBox(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolBox_6.sizePolicy().hasHeightForWidth())
        self.toolBox_6.setSizePolicy(sizePolicy)
        self.toolBox_6.setObjectName("toolBox_6")
        self.page_19 = QtWidgets.QWidget()
        self.page_19.setGeometry(QtCore.QRect(0, 0, 210, 103))
        self.page_19.setObjectName("page_19")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout(self.page_19)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.scrollArea_19 = QtWidgets.QScrollArea(self.page_19)
        self.scrollArea_19.setWidgetResizable(True)
        self.scrollArea_19.setObjectName("scrollArea_19")
        self.scrollAreaWidgetContents_21 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_21.setGeometry(QtCore.QRect(0, 0, 184, 77))
        self.scrollAreaWidgetContents_21.setObjectName("scrollAreaWidgetContents_21")
        self.scrollArea_19.setWidget(self.scrollAreaWidgetContents_21)
        self.horizontalLayout_20.addWidget(self.scrollArea_19)
        self.toolBox_6.addItem(self.page_19, "")
        self.page_20 = QtWidgets.QWidget()
        self.page_20.setGeometry(QtCore.QRect(0, 0, 210, 103))
        self.page_20.setObjectName("page_20")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.page_20)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.scrollArea_20 = QtWidgets.QScrollArea(self.page_20)
        self.scrollArea_20.setWidgetResizable(True)
        self.scrollArea_20.setObjectName("scrollArea_20")
        self.scrollAreaWidgetContents_22 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_22.setGeometry(QtCore.QRect(0, 0, 184, 77))
        self.scrollAreaWidgetContents_22.setObjectName("scrollAreaWidgetContents_22")
        self.scrollArea_20.setWidget(self.scrollAreaWidgetContents_22)
        self.horizontalLayout_21.addWidget(self.scrollArea_20)
        self.toolBox_6.addItem(self.page_20, "")
        self.verticalLayout.addWidget(self.toolBox_6)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.horizontalLayout.addWidget(self.scrollArea_2)
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.scrollArea_21 = QtWidgets.QScrollArea(self.frame)
        self.scrollArea_21.setWidgetResizable(True)
        self.scrollArea_21.setObjectName("scrollArea_21")
        self.scrollAreaWidgetContents_23 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_23.setGeometry(QtCore.QRect(0, 0, 234, 863))
        self.scrollAreaWidgetContents_23.setObjectName("scrollAreaWidgetContents_23")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_23)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.stackedWidget = QtWidgets.QStackedWidget(self.scrollAreaWidgetContents_23)
        self.stackedWidget.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_13 = QtWidgets.QWidget()
        self.page_13.setObjectName("page_13")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout(self.page_13)
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.scrollArea_22 = QtWidgets.QScrollArea(self.page_13)
        self.scrollArea_22.setWidgetResizable(True)
        self.scrollArea_22.setObjectName("scrollArea_22")
        self.scrollAreaWidgetContents_24 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_24.setGeometry(QtCore.QRect(0, 0, 180, 382))
        self.scrollAreaWidgetContents_24.setObjectName("scrollAreaWidgetContents_24")
        self.scrollArea_22.setWidget(self.scrollAreaWidgetContents_24)
        self.horizontalLayout_22.addWidget(self.scrollArea_22)
        self.stackedWidget.addWidget(self.page_13)
        self.page_14 = QtWidgets.QWidget()
        self.page_14.setObjectName("page_14")
        self.stackedWidget.addWidget(self.page_14)
        self.verticalLayout_2.addWidget(self.stackedWidget)
        self.stackedWidget_2 = QtWidgets.QStackedWidget(self.scrollAreaWidgetContents_23)
        self.stackedWidget_2.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.page_23 = QtWidgets.QWidget()
        self.page_23.setObjectName("page_23")
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout(self.page_23)
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.scrollArea_23 = QtWidgets.QScrollArea(self.page_23)
        self.scrollArea_23.setWidgetResizable(True)
        self.scrollArea_23.setObjectName("scrollArea_23")
        self.scrollAreaWidgetContents_25 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_25.setGeometry(QtCore.QRect(0, 0, 180, 381))
        self.scrollAreaWidgetContents_25.setObjectName("scrollAreaWidgetContents_25")
        self.scrollArea_23.setWidget(self.scrollAreaWidgetContents_25)
        self.horizontalLayout_23.addWidget(self.scrollArea_23)
        self.stackedWidget_2.addWidget(self.page_23)
        self.page_24 = QtWidgets.QWidget()
        self.page_24.setObjectName("page_24")
        self.stackedWidget_2.addWidget(self.page_24)
        self.verticalLayout_2.addWidget(self.stackedWidget_2)
        self.scrollArea_21.setWidget(self.scrollAreaWidgetContents_23)
        self.horizontalLayout.addWidget(self.scrollArea_21)
        self.horizontalLayout_2.addWidget(self.frame)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tab_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.scrollArea = QtWidgets.QScrollArea(self.tab_3)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 477, 836))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_3.addWidget(self.scrollArea)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.tab_4)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.scrollArea_8 = QtWidgets.QScrollArea(self.tab_4)
        self.scrollArea_8.setWidgetResizable(True)
        self.scrollArea_8.setObjectName("scrollArea_8")
        self.scrollAreaWidgetContents_8 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_8.setGeometry(QtCore.QRect(0, 0, 477, 836))
        self.scrollAreaWidgetContents_8.setObjectName("scrollAreaWidgetContents_8")
        self.scrollArea_8.setWidget(self.scrollAreaWidgetContents_8)
        self.horizontalLayout_10.addWidget(self.scrollArea_8)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.tab_5)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.scrollArea_9 = QtWidgets.QScrollArea(self.tab_5)
        self.scrollArea_9.setWidgetResizable(True)
        self.scrollArea_9.setObjectName("scrollArea_9")
        self.scrollAreaWidgetContents_9 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_9.setGeometry(QtCore.QRect(0, 0, 477, 836))
        self.scrollAreaWidgetContents_9.setObjectName("scrollAreaWidgetContents_9")
        self.scrollArea_9.setWidget(self.scrollAreaWidgetContents_9)
        self.horizontalLayout_11.addWidget(self.scrollArea_9)
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.tab_6)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.scrollArea_10 = QtWidgets.QScrollArea(self.tab_6)
        self.scrollArea_10.setWidgetResizable(True)
        self.scrollArea_10.setObjectName("scrollArea_10")
        self.scrollAreaWidgetContents_10 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_10.setGeometry(QtCore.QRect(0, 0, 477, 836))
        self.scrollAreaWidgetContents_10.setObjectName("scrollAreaWidgetContents_10")
        self.scrollArea_10.setWidget(self.scrollAreaWidgetContents_10)
        self.horizontalLayout_12.addWidget(self.scrollArea_10)
        self.tabWidget.addTab(self.tab_6, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.tab_7)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.scrollArea_11 = QtWidgets.QScrollArea(self.tab_7)
        self.scrollArea_11.setWidgetResizable(True)
        self.scrollArea_11.setObjectName("scrollArea_11")
        self.scrollAreaWidgetContents_11 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_11.setGeometry(QtCore.QRect(0, 0, 477, 836))
        self.scrollAreaWidgetContents_11.setObjectName("scrollAreaWidgetContents_11")
        self.scrollArea_11.setWidget(self.scrollAreaWidgetContents_11)
        self.horizontalLayout_13.addWidget(self.scrollArea_11)
        self.tabWidget.addTab(self.tab_7, "")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.tab_8)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.scrollArea_12 = QtWidgets.QScrollArea(self.tab_8)
        self.scrollArea_12.setWidgetResizable(True)
        self.scrollArea_12.setObjectName("scrollArea_12")
        self.scrollAreaWidgetContents_12 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_12.setGeometry(QtCore.QRect(0, 0, 477, 836))
        self.scrollAreaWidgetContents_12.setObjectName("scrollAreaWidgetContents_12")
        self.scrollArea_12.setWidget(self.scrollAreaWidgetContents_12)
        self.horizontalLayout_14.addWidget(self.scrollArea_12)
        self.tabWidget.addTab(self.tab_8, "")
        self.tab_9 = QtWidgets.QWidget()
        self.tab_9.setObjectName("tab_9")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.tab_9)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.scrollArea_13 = QtWidgets.QScrollArea(self.tab_9)
        self.scrollArea_13.setWidgetResizable(True)
        self.scrollArea_13.setObjectName("scrollArea_13")
        self.scrollAreaWidgetContents_13 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_13.setGeometry(QtCore.QRect(0, 0, 477, 836))
        self.scrollAreaWidgetContents_13.setObjectName("scrollAreaWidgetContents_13")
        self.scrollArea_13.setWidget(self.scrollAreaWidgetContents_13)
        self.horizontalLayout_15.addWidget(self.scrollArea_13)
        self.tabWidget.addTab(self.tab_9, "")
        self.horizontalLayout_2.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.toolBox.setCurrentIndex(0)
        self.toolBox_2.setCurrentIndex(0)
        self.toolBox_3.setCurrentIndex(0)
        self.toolBox_4.setCurrentIndex(0)
        self.toolBox_5.setCurrentIndex(0)
        self.toolBox_6.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(6)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), _translate("MainWindow", "Page 1"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_6), _translate("MainWindow", "Page 2"))
        self.toolBox_2.setItemText(self.toolBox_2.indexOf(self.page_7), _translate("MainWindow", "Page 1"))
        self.toolBox_2.setItemText(self.toolBox_2.indexOf(self.page_8), _translate("MainWindow", "Page 2"))
        self.toolBox_3.setItemText(self.toolBox_3.indexOf(self.page_9), _translate("MainWindow", "Page 1"))
        self.toolBox_3.setItemText(self.toolBox_3.indexOf(self.page_10), _translate("MainWindow", "Page 2"))
        self.toolBox_4.setItemText(self.toolBox_4.indexOf(self.page_15), _translate("MainWindow", "Page 1"))
        self.toolBox_4.setItemText(self.toolBox_4.indexOf(self.page_16), _translate("MainWindow", "Page 2"))
        self.toolBox_5.setItemText(self.toolBox_5.indexOf(self.page_17), _translate("MainWindow", "Page 1"))
        self.toolBox_5.setItemText(self.toolBox_5.indexOf(self.page_18), _translate("MainWindow", "Page 2"))
        self.toolBox_6.setItemText(self.toolBox_6.indexOf(self.page_19), _translate("MainWindow", "Page 1"))
        self.toolBox_6.setItemText(self.toolBox_6.indexOf(self.page_20), _translate("MainWindow", "Page 2"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Tab 2"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Page"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "Page"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), _translate("MainWindow", "Page"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_8), _translate("MainWindow", "Page"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_9), _translate("MainWindow", "Page"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())