# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Route88_Inventory_ModifierEntry.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Route88_Management_Modifier(QtWidgets.QMainWindow):
    def setupUi(self, Route88_Management_Modifier):
        Route88_Management_Modifier.setObjectName("Route88_Management_Modifier")
        Route88_Management_Modifier.setWindowModality(QtCore.Qt.ApplicationModal)
        Route88_Management_Modifier.resize(818, 329)
        Route88_Management_Modifier.setMinimumSize(QtCore.QSize(818, 329))
        Route88_Management_Modifier.setMaximumSize(QtCore.QSize(818, 16777215))
        Route88_Management_Modifier.setFocusPolicy(QtCore.Qt.NoFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("IcoDisplay/r_88.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Route88_Management_Modifier.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Route88_Management_Modifier)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Tab_SelectionSelectives = QtWidgets.QTabWidget(self.centralwidget)
        self.Tab_SelectionSelectives.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Tab_SelectionSelectives.sizePolicy().hasHeightForWidth())
        self.Tab_SelectionSelectives.setSizePolicy(sizePolicy)
        self.Tab_SelectionSelectives.setMinimumSize(QtCore.QSize(800, 0))
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setPointSize(10)
        self.Tab_SelectionSelectives.setFont(font)
        self.Tab_SelectionSelectives.setObjectName("Tab_SelectionSelectives")
        self.InventoryEntryWindow = QtWidgets.QWidget()
        self.InventoryEntryWindow.setObjectName("InventoryEntryWindow")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.InventoryEntryWindow)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.InventoryEntryWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setPointSize(8)
        self.groupBox.setFont(font)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 761, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(15)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.AddEntry_ItemCode = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AddEntry_ItemCode.sizePolicy().hasHeightForWidth())
        self.AddEntry_ItemCode.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setPointSize(10)
        self.AddEntry_ItemCode.setFont(font)
        self.AddEntry_ItemCode.setClearButtonEnabled(True)
        self.AddEntry_ItemCode.setObjectName("AddEntry_ItemCode")
        self.horizontalLayout_3.addWidget(self.AddEntry_ItemCode)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.AddEntry_SupplierCode = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AddEntry_SupplierCode.sizePolicy().hasHeightForWidth())
        self.AddEntry_SupplierCode.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setPointSize(10)
        self.AddEntry_SupplierCode.setFont(font)
        self.AddEntry_SupplierCode.setClearButtonEnabled(True)
        self.AddEntry_SupplierCode.setObjectName("AddEntry_SupplierCode")
        self.horizontalLayout_3.addWidget(self.AddEntry_SupplierCode)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 70, 761, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(15)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.AddEntry_ItemName = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AddEntry_ItemName.sizePolicy().hasHeightForWidth())
        self.AddEntry_ItemName.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setPointSize(10)
        self.AddEntry_ItemName.setFont(font)
        self.AddEntry_ItemName.setClearButtonEnabled(True)
        self.AddEntry_ItemName.setObjectName("AddEntry_ItemName")
        self.horizontalLayout_4.addWidget(self.AddEntry_ItemName)
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        self.AddEntry_ItemType = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AddEntry_ItemType.sizePolicy().hasHeightForWidth())
        self.AddEntry_ItemType.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setPointSize(10)
        self.AddEntry_ItemType.setFont(font)
        self.AddEntry_ItemType.setClearButtonEnabled(True)
        self.AddEntry_ItemType.setObjectName("AddEntry_ItemType")
        self.horizontalLayout_4.addWidget(self.AddEntry_ItemType)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(6, 120, 761, 31))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.AddEntry_Quantity = QtWidgets.QSpinBox(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AddEntry_Quantity.sizePolicy().hasHeightForWidth())
        self.AddEntry_Quantity.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setPointSize(10)
        self.AddEntry_Quantity.setFont(font)
        self.AddEntry_Quantity.setWrapping(True)
        self.AddEntry_Quantity.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.AddEntry_Quantity.setProperty("showGroupSeparator", False)
        self.AddEntry_Quantity.setObjectName("AddEntry_Quantity")
        self.horizontalLayout_5.addWidget(self.AddEntry_Quantity)
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.AddEntry_Cost = QtWidgets.QDoubleSpinBox(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AddEntry_Cost.sizePolicy().hasHeightForWidth())
        self.AddEntry_Cost.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setPointSize(10)
        self.AddEntry_Cost.setFont(font)
        self.AddEntry_Cost.setObjectName("AddEntry_Cost")
        self.horizontalLayout_5.addWidget(self.AddEntry_Cost)
        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_5.addWidget(self.label_7)
        self.AddEntry_DateExpiry = QtWidgets.QDateTimeEdit(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AddEntry_DateExpiry.sizePolicy().hasHeightForWidth())
        self.AddEntry_DateExpiry.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setPointSize(10)
        self.AddEntry_DateExpiry.setFont(font)
        self.AddEntry_DateExpiry.setObjectName("AddEntry_DateExpiry")
        self.horizontalLayout_5.addWidget(self.AddEntry_DateExpiry)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.InventoryEntryWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setPointSize(10)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Modifier_AddEntry = QtWidgets.QPushButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Modifier_AddEntry.sizePolicy().hasHeightForWidth())
        self.Modifier_AddEntry.setSizePolicy(sizePolicy)
        self.Modifier_AddEntry.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setPointSize(10)
        self.Modifier_AddEntry.setFont(font)
        self.Modifier_AddEntry.setObjectName("Modifier_AddEntry")
        self.horizontalLayout.addWidget(self.Modifier_AddEntry)
        self.Modifier_ClearEntry = QtWidgets.QPushButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Modifier_ClearEntry.sizePolicy().hasHeightForWidth())
        self.Modifier_ClearEntry.setSizePolicy(sizePolicy)
        self.Modifier_ClearEntry.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setPointSize(10)
        self.Modifier_ClearEntry.setFont(font)
        self.Modifier_ClearEntry.setObjectName("Modifier_ClearEntry")
        self.horizontalLayout.addWidget(self.Modifier_ClearEntry)
        self.Modifier_CloseWindow = QtWidgets.QPushButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Modifier_CloseWindow.sizePolicy().hasHeightForWidth())
        self.Modifier_CloseWindow.setSizePolicy(sizePolicy)
        self.Modifier_CloseWindow.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setPointSize(10)
        self.Modifier_CloseWindow.setFont(font)
        self.Modifier_CloseWindow.setObjectName("Modifier_CloseWindow")
        self.horizontalLayout.addWidget(self.Modifier_CloseWindow)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.Tab_SelectionSelectives.addTab(self.InventoryEntryWindow, "")
        self.EmployeeEntryWindow = QtWidgets.QWidget()
        self.EmployeeEntryWindow.setObjectName("EmployeeEntryWindow")
        self.Tab_SelectionSelectives.addTab(self.EmployeeEntryWindow, "")
        self.SupplierEntryWindow = QtWidgets.QWidget()
        self.SupplierEntryWindow.setObjectName("SupplierEntryWindow")
        self.Tab_SelectionSelectives.addTab(self.SupplierEntryWindow, "")
        self.TransactionEntryWindow = QtWidgets.QWidget()
        self.TransactionEntryWindow.setObjectName("TransactionEntryWindow")
        self.Tab_SelectionSelectives.addTab(self.TransactionEntryWindow, "")
        self.PositionEntryTable = QtWidgets.QWidget()
        self.PositionEntryTable.setObjectName("PositionEntryTable")
        self.Tab_SelectionSelectives.addTab(self.PositionEntryTable, "")
        self.horizontalLayout_2.addWidget(self.Tab_SelectionSelectives)
        Route88_Management_Modifier.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Route88_Management_Modifier)
        self.statusbar.setObjectName("statusbar")
        Route88_Management_Modifier.setStatusBar(self.statusbar)

        self.retranslateUi(Route88_Management_Modifier)
        self.Tab_SelectionSelectives.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Route88_Management_Modifier)

    def retranslateUi(self, Route88_Management_Modifier):
        _translate = QtCore.QCoreApplication.translate
        Route88_Management_Modifier.setWindowTitle(_translate("Route88_Management_Modifier", "Route88 System | Management Modifiers |"))
        self.groupBox.setTitle(_translate("Route88_Management_Modifier", "Entries To Fill"))
        self.label.setText(_translate("Route88_Management_Modifier", "Item Code"))
        self.AddEntry_ItemCode.setPlaceholderText(_translate("Route88_Management_Modifier", "Required Value To Fill..."))
        self.label_2.setText(_translate("Route88_Management_Modifier", "Supplier Code"))
        self.AddEntry_SupplierCode.setPlaceholderText(_translate("Route88_Management_Modifier", "Required Value To Fill..."))
        self.label_3.setText(_translate("Route88_Management_Modifier", "Item Name"))
        self.AddEntry_ItemName.setPlaceholderText(_translate("Route88_Management_Modifier", "Required Value To Fill..."))
        self.label_6.setText(_translate("Route88_Management_Modifier", "Type"))
        self.AddEntry_ItemType.setPlaceholderText(_translate("Route88_Management_Modifier", "Required Value To Fill..."))
        self.label_4.setText(_translate("Route88_Management_Modifier", "Quantity"))
        self.label_5.setText(_translate("Route88_Management_Modifier", "Cost"))
        self.AddEntry_Cost.setPrefix(_translate("Route88_Management_Modifier", "₱ "))
        self.label_7.setText(_translate("Route88_Management_Modifier", "Expiry Date"))
        self.groupBox_2.setTitle(_translate("Route88_Management_Modifier", "Staff Actions"))
        self.Modifier_AddEntry.setText(_translate("Route88_Management_Modifier", "Add Entry"))
        self.Modifier_ClearEntry.setText(_translate("Route88_Management_Modifier", "Clear Entry"))
        self.Modifier_CloseWindow.setText(_translate("Route88_Management_Modifier", "Close Window"))
        self.Tab_SelectionSelectives.setTabText(self.Tab_SelectionSelectives.indexOf(self.InventoryEntryWindow), _translate("Route88_Management_Modifier", "Inventory Entries"))
        self.Tab_SelectionSelectives.setTabText(self.Tab_SelectionSelectives.indexOf(self.EmployeeEntryWindow), _translate("Route88_Management_Modifier", "Employee Entries"))
        self.Tab_SelectionSelectives.setTabText(self.Tab_SelectionSelectives.indexOf(self.SupplierEntryWindow), _translate("Route88_Management_Modifier", "Supplier Entries"))
        self.Tab_SelectionSelectives.setTabText(self.Tab_SelectionSelectives.indexOf(self.TransactionEntryWindow), _translate("Route88_Management_Modifier", "Transaction Entries"))
        self.Tab_SelectionSelectives.setTabText(self.Tab_SelectionSelectives.indexOf(self.PositionEntryTable), _translate("Route88_Management_Modifier", "Position Entries"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Route88_Management_Modifier = QtWidgets.QMainWindow()
    ui = Ui_Route88_Management_Modifier()
    ui.setupUi(Route88_Management_Modifier)
    Route88_Management_Modifier.show()
    sys.exit(app.exec_())
