import os
import re
import sqlite3
import sys
from PyQt5 import uic, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
totall = 0
samquan = 1
pquan = 1
ipquan = 1
macquan = 1
ppquan = 1
dellquan = 1
standquan = 1
printquan = 1
support = 1
user_name_local = "None"
userr = None

class SoMain(QWidget):
    def __init__(self):
        super().__init__()
        ui_path = "../ui/items.ui"
        uic.loadUi(ui_path, self)
        self.setFixedSize(1040, 590)
        self.setWindowTitle('SoMain')
        if hasattr(self, 'main') and hasattr(self, 'inventory'):
            self.main.setCurrentWidget(self.inventory)
        else:
            print("stackedWidget or Dashboard not found in the UI file")
        self.connectbtns()
        self.setupui()
        self.setui()
        self.officeui()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateusername)
        self.timer.start(100)
        self.cart_items = []
        if not self.cart_items:
            self.outt.hide()

    def updateusername(self):
        global user_name_local
        if user_name_local == "None":
            self.LOSTART.setText("Login")
            self.LOSTART.setEnabled(True)
        else:
            self.LOSTART.setText(f"Welcome {user_name_local}!!!")
            self.LOSTART.setEnabled(False)


    def setupui(self):
        self.pone.setPixmap(
            QtGui.QPixmap("../icons/phoneplace.jpg"))
        self.laptop.setPixmap(
            QtGui.QPixmap("../icons/laptops.jpg"))
        self.offices.setPixmap(
            QtGui.QPixmap("../icons/office.jpg"))

    def connectbtns(self):
        self.LOSTART.clicked.connect(self.login)
        self.ponebtn.clicked.connect(self.pones)
        self.quanadd.clicked.connect(self.addtoquan)
        self.quanmin.clicked.connect(self.removequan)
        self.rerer.clicked.connect(self.addtoquan3)
        self.uii.clicked.connect(self.removequan3)
        self.tensor.clicked.connect(self.addtoquan2)
        self.cartadd3.clicked.connect(self.cart__ip)
        self.cartadd2.clicked.connect(self.cart__p)
        self.opp.clicked.connect(self.removequan2)
        self.addtocart.clicked.connect(self.cart__)
        self.activecart.hide()
        self.activecart_4.hide()
        self.activecart_2.hide()
        self.cartbox.clicked.connect(self.load_cart)
        self.cartbox_4.clicked.connect(self.load_cart)
        self.cartbox_2.clicked.connect(self.load_cart)
        self.nextitem.clicked.connect(self.next_item)
        self.previtem.clicked.connect(self.prev_item)
        self.nextitem_2.clicked.connect(self.next_item2)
        self.previtem_2.clicked.connect(self.prev_item2)
        self.nextitem_3.clicked.connect(self.next_item3)
        self.previtem_3.clicked.connect(self.prev_item3)
        self.back.clicked.connect(self.dropback)
        self.back_3.clicked.connect(self.pones)
        self.laptopbtn.clicked.connect(self.laptops__)
        self.officebtn.clicked.connect(self.office_s)
        self.outt.clicked.connect(self.checkout)

##----------------------------------------(Offices)----------------------------------##

    def office_s(self):
        if hasattr(self, 'main') and hasattr(self, 'office'):
            self.main.setCurrentWidget(self.office)
        else:
            print("stackedWidget or Dashboard not found in the UI file")
        self.itemm2()
        self.activecart_8.hide()
        self.activecart_9.hide()
        self.activecart_7.hide()
        self.previtem_9.clicked.connect(self.prev__item1)
        self.previtem_8.clicked.connect(self.prev__item7)
        self.previtem_7.clicked.connect(self.prev__item8)
        self.nextitem_9.clicked.connect(self.next__item1)
        self.nextitem_8.clicked.connect(self.next__item7)
        self.nextitem_7.clicked.connect(self.next__item8)
        self.cartbox_6.clicked.connect(self.load_cart)
        self.back_4.clicked.connect(self.dropback__)
        self.pushButton_16.clicked.connect(self.cart__bookstnd)
        self.pushButton_14.clicked.connect(self.cart__printer)
        self.pushButton_15.clicked.connect(self.cart__desk)
        self.plusss.clicked.connect(self.addto_quan11)
        self.minusss.clicked.connect(self.remove_quan12)
        self.plusssss.clicked.connect(self.addtoquan_13)
        self.min.clicked.connect(self.removequan_14)
        self.addddd.clicked.connect(self.addtoquan_15)
        self.minn.clicked.connect(self.removequan_16)

    def itemm2(self):
        if hasattr(self, 'types_2') and hasattr(self, 'mac_'):
            self.types_3.setCurrentWidget(self.printer)
        else:
            print("stackedWidget or Dashboard not found in the UI file")

    def officeui(self):
        try:
            self.label_85.setPixmap(
                QtGui.QPixmap("../icons/angle-double-right.png"))
            self.label_95.setPixmap(
                QtGui.QPixmap("../icons/angle-double-right.png"))
            self.label_105.setPixmap(
                QtGui.QPixmap("../icons/angle-double-right.png"))
            icon5 = QIcon("../icons/left.png")
            self.back_4.setIcon(icon5)
            icon5 = QIcon("../icons/left.png")
            self.back_3.setIcon(icon5)
            icon6 = QIcon("../icons/shopping-cart.png")
            self.cartbox_8.setIcon(icon6)
            icon6 = QIcon("../icons/shopping-cart.png")
            self.cartbox_7.setIcon(icon6)
            icon6 = QIcon("../icons/shopping-cart.png")
            self.cartbox_9.setIcon(icon6)
            icon9 = QIcon("../icons/left.png")
            self.previtem_7.setIcon(icon9)
            icon8 = QIcon("../icons/right.png")
            self.nextitem_7.setIcon(icon8)
            icon9 = QIcon("../icons/left.png")
            self.previtem_8.setIcon(icon9)
            icon8 = QIcon("../icons/right.png")
            self.nextitem_8.setIcon(icon8)
            icon9 = QIcon("../icons/left.png")
            self.previtem_9.setIcon(icon9)
            icon8 = QIcon("../icons/right.png")
            self.nextitem_9.setIcon(icon8)
            icon = QIcon("../icons/square-plus.png")
            self.plusss.setIcon(icon)
            icon2 = QIcon("../icons/square-minus.png")
            self.minusss.setIcon(icon2)
            icon = QIcon("../icons/square-plus.png")
            self.plusssss.setIcon(icon)
            icon2 = QIcon("../icons/square-minus.png")
            self.min.setIcon(icon2)
            icon = QIcon("../icons/square-plus.png")
            self.addddd.setIcon(icon)
            icon2 = QIcon("../icons/square-minus.png")
            self.minn.setIcon(icon2)
            self.label_96.setPixmap(
                QtGui.QPixmap("../icons/st1.jpg"))
            self.label_108.setPixmap(
                QtGui.QPixmap("../icons/o1].jpg"))
            self.label_86.setPixmap(
                QtGui.QPixmap("../icons/pr1.jpg"))
        except Exception as e:
            print(e)

    def prev__item1(self):
        try:
            if hasattr(self, 'types_3') and hasattr(self, 'pixel_3'):
                self.types_3.setCurrentWidget(self.pixel_3)
            else:
                print("stackedWidget or Dashboard not found in the UI file")
        except Exception as e:
            print(e)

    def prev__item7(self):
        try:
            if hasattr(self, 'types_3') and hasattr(self, 'samsun_3'):
                self.types_3.setCurrentWidget(self.samsun_3)
            else:
                print("stackedWidget or Dashboard not found in the UI file")
        except Exception as e:
            print(e)

    def prev__item8(self):
        try:
            if hasattr(self, 'types_3') and hasattr(self, 'printer'):
                self.types_3.setCurrentWidget(self.printer)
            else:
                print("stackedWidget or Dashboard not found in the UI file")
        except Exception as e:
            print(e)

    def next__item1(self):
        try:
            if hasattr(self, 'types_3') and hasattr(self, 'pixel_3'):
                self.types_3.setCurrentWidget(self.pixel_3)
            else:
                print("stackedWidget or Dashboard not found in the UI file")
        except Exception as e:
            print(e)

    def next__item7(self):
        try:
            if hasattr(self, 'types_3') and hasattr(self, 'printer'):
                self.types_3.setCurrentWidget(self.printer)
            else:
                print("stackedWidget or Dashboard not found in the UI file")
        except Exception as e:
            print(e)

    def next__item8(self):
        try:
            if hasattr(self, 'types_3') and hasattr(self, 'pixel_3'):
                self.types_3.setCurrentWidget(self.pixel_3)
            else:
                print("stackedWidget or Dashboard not found in the UI file")
        except Exception as e:
            print(e)

    def cart__bookstnd(self):
        global standquan
        price = "46,560"
        standquantit = standquan
        itemname = "Book Support Stand"
        image_path = "../icons/o1].jpg"
        selected_color = self.comboBox_9.currentText()
        if selected_color == "Select Color":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Invalid Selection")
            msg.setText("Please select a color.")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
        else:
            self.cart_items.append((itemname, standquantit, selected_color, price, image_path))
            msg_box = QMessageBox(self)
            msg_box.setText("Do You Want to View Your Cart?")
            msg_box.setWindowTitle('Book Stand Added!')
            msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            msg_box.setDefaultButton(QMessageBox.No)
            reply = msg_box.exec_()
            if reply == QMessageBox.Yes:
                self.load_cart()
            self.activecart_8.show()
            self.outt.show()

    def cart__printer(self):
        global printquan
        price = "125,000"
        printerquan = printquan
        itemname = "Hp DESKJET Plus 4120"
        image_path = "../icons/pr1.jpg"
        selected_color = self.comboBox_7.currentText()
        if selected_color == "Select Color":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Invalid Selection")
            msg.setText("Please select a valid color.")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
        else:
            self.cart_items.append((itemname, printerquan, selected_color, price, image_path))
            msg_box = QMessageBox(self)
            msg_box.setText("Do You Want to View Your Cart?")
            msg_box.setWindowTitle('Hp Added!')
            msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            msg_box.setDefaultButton(QMessageBox.No)
            reply = msg_box.exec_()
            if reply == QMessageBox.Yes:
                self.load_cart()
            self.activecart_9.show()
            self.outt.show()

    def cart__desk(self):
        global support
        price = "49,000"
        supportquantity = support
        itemname = "Stand Desk for PC"
        image_path = "../icons/st1.jpg"
        selected_color = self.comboBox_8.currentText()
        if selected_color == "Select Color":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Invalid Selection")
            msg.setText("Please select a valid color.")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
        else:
            self.cart_items.append((itemname, supportquantity, selected_color, price, image_path))
            msg_box = QMessageBox(self)
            msg_box.setText("Do You Want to View Your Cart?")
            msg_box.setWindowTitle('iPhone 15 Added!')
            msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            msg_box.setDefaultButton(QMessageBox.No)
            reply = msg_box.exec_()
            if reply == QMessageBox.Yes:
                self.load_cart()
            self.activecart_7.show()
            self.outt.show()

    def addto_quan11(self):
        global standquan
        try:
            standquan = (standquan + 1)
        except Exception as e:
            print(e)
        self.label_176.setText(str(standquan))

    def remove_quan12(self):
        global standquan
        if standquan > 1:
            standquan = standquan - 1
        else:
            standquan = 1
        self.label_176.setText(str(standquan))

    def addtoquan_13(self):
        global printquan
        try:
            printquan = (printquan + 1)
        except Exception as e:
            print(e)
        self.label_174.setText(str(printquan))

    def removequan_14(self):
        global printquan
        if printquan > 1:
            printquan = printquan - 1
        else:
            printquan = 1
        self.label_174.setText(str(printquan))

    def addtoquan_15(self):
        global support
        try:
            support = (support + 1)
        except Exception as e:
            print(e)
        self.label_175.setText(str(support))

    def removequan_16(self):
        global support
        if support > 1:
            support = support - 1
        else:
            support = 1
        self.label_175.setText(str(support))

    def dropback__(self):
        if hasattr(self, 'main') and hasattr(self, 'inventory'):
            self.main.setCurrentWidget(self.inventory)
        else:
            print("stackedWidget or Dashboard not found in the UI file")




##--------------------------(Laptop)----------------------------------------------##

    def laptops__(self):
        if hasattr(self, 'main') and hasattr(self, 'laptops'):
            self.main.setCurrentWidget(self.laptops)
        else:
            print("stackedWidget or Dashboard not found in the UI file")
        self.itemm()
        self.laptopui()
        self.activecart_3.hide()
        self.activecart_5.hide()
        self.activecart_6.hide()
        self.previtem_6.clicked.connect(self.prev__item)
        self.previtem_4.clicked.connect(self.prev__item4)
        self.previtem_5.clicked.connect(self.prev__item5)
        self.nextitem_6.clicked.connect(self.next__item)
        self.nextitem_4.clicked.connect(self.next__item4)
        self.nextitem_5.clicked.connect(self.next__item5)
        self.cartbox_6.clicked.connect(self.load_cart)
        self.back_2.clicked.connect(self.dropback_)
        self.addmac.clicked.connect(self.cart__mac)
        self.apppc.clicked.connect(self.cart__pc)
        self.adddell.clicked.connect(self.cart__dell)
        self.opo.clicked.connect(self.addto_quan)
        self.yuu.clicked.connect(self.remove_quan)
        self.plus.clicked.connect(self.addtoquan_3)
        self.minus.clicked.connect(self.removequan_3)
        self.look.clicked.connect(self.addtoquan_2)
        self.non.clicked.connect(self.removequan_2)

    def itemm(self):
        if hasattr(self, 'types_2') and hasattr(self, 'mac_'):
            self.types_2.setCurrentWidget(self.mac_)
        else:
            print("stackedWidget or Dashboard not found in the UI file")

    def laptopui(self):
        try:
            self.caaa.setPixmap(
                QtGui.QPixmap("../icons/angle-double-right.png"))
            self.label_76.setPixmap(
                QtGui.QPixmap("../icons/angle-double-right.png"))
            self.label_66.setPixmap(
                QtGui.QPixmap("../icons/angle-double-right.png"))
            icon5 = QIcon("../icons/left.png")
            self.back_2.setIcon(icon5)
            icon5 = QIcon("../icons/left.png")
            self.back_3.setIcon(icon5)
            icon6 = QIcon("../icons/shopping-cart.png")
            self.cartbox_3.setIcon(icon6)
            icon6 = QIcon("../icons/shopping-cart.png")
            self.cartbox_5.setIcon(icon6)
            icon6 = QIcon("../icons/shopping-cart.png")
            self.cartbox_6.setIcon(icon6)
            icon9 = QIcon("../icons/left.png")
            self.previtem_6.setIcon(icon9)
            icon8 = QIcon("../icons/right.png")
            self.nextitem_6.setIcon(icon8)
            icon9 = QIcon("../icons/left.png")
            self.previtem_5.setIcon(icon9)
            icon8 = QIcon("../icons/right.png")
            self.nextitem_5.setIcon(icon8)
            icon9 = QIcon("../icons/left.png")
            self.previtem_4.setIcon(icon9)
            icon8 = QIcon("../icons/right.png")
            self.nextitem_4.setIcon(icon8)
            icon = QIcon("../icons/square-plus.png")
            self.plus.setIcon(icon)
            icon2 = QIcon("../icons/square-minus.png")
            self.minus.setIcon(icon2)
            icon = QIcon("../icons/square-plus.png")
            self.opo.setIcon(icon)
            icon2 = QIcon("../icons/square-minus.png")
            self.yuu.setIcon(icon2)
            icon = QIcon("../icons/square-plus.png")
            self.look.setIcon(icon)
            icon2 = QIcon("../icons/square-minus.png")
            self.non.setIcon(icon2)
            self.mac.setPixmap(
                QtGui.QPixmap("../icons/a1.jpg"))
            self.dell.setPixmap(
                QtGui.QPixmap("../icons/l1.jpg"))
            self.orr.setPixmap(
                QtGui.QPixmap("../icons/pp1.jpg"))
        except Exception as e:
            print(e)

    def prev__item5(self):
        try:
            if hasattr(self, 'types_2') and hasattr(self, 'mac_'):
                self.types_2.setCurrentWidget(self.mac_)
            else:
                print("stackedWidget or Dashboard not found in the UI file")
        except Exception as e:
            print(e)

    def prev__item(self):
        try:
            if hasattr(self, 'types_2') and hasattr(self, 'delll'):
                self.types_2.setCurrentWidget(self.delll)
            else:
                print("stackedWidget or Dashboard not found in the UI file")
        except Exception as e:
            print(e)

    def prev__item4(self):
        try:
            if hasattr(self, 'types_2') and hasattr(self, 'x360'):
                self.types_2.setCurrentWidget(self.x360)
            else:
                print("stackedWidget or Dashboard not found in the UI file")
        except Exception as e:
            print(e)

    def next__item5(self):
        try:
            if hasattr(self, 'types_2') and hasattr(self, 'delll'):
                self.types_2.setCurrentWidget(self.delll)
            else:
                print("stackedWidget or Dashboard not found in the UI file")
        except Exception as e:
            print(e)

    def next__item4(self):
        try:
            if hasattr(self, 'types_2') and hasattr(self, 'mac_'):
                self.types_2.setCurrentWidget(self.mac_)
            else:
                print("stackedWidget or Dashboard not found in the UI file")
        except Exception as e:
            print(e)

    def next__item(self):
        try:
            if hasattr(self, 'types_2') and hasattr(self, 'x360'):
                self.types_2.setCurrentWidget(self.x360)
            else:
                print("stackedWidget or Dashboard not found in the UI file")
        except Exception as e:
            print(e)

    def cart__mac(self):
        global macquan
        price = "2,999,999"
        macquantity = macquan
        itemname = "Apple MacBook Pro M3"
        image_path = "../icons/a1.jpg"
        selected_color = self.comboBox_4.currentText()
        if selected_color == "Select Color":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Invalid Selection")
            msg.setText("Please select a color.")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
        else:
            self.cart_items.append((itemname, macquantity, selected_color, price, image_path))
            msg_box = QMessageBox(self)
            msg_box.setText("Do You Want to View Your Cart?")
            msg_box.setWindowTitle('MacBook Added!')
            msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            msg_box.setDefaultButton(QMessageBox.No)
            reply = msg_box.exec_()
            if reply == QMessageBox.Yes:
                self.load_cart()
            self.activecart_6.show()
            self.outt.show()

    def cart__pc(self):
        global ppquan
        price = "610,000"
        pcquantity = ppquan
        itemname = "Hp EliteBook X360"
        image_path = "../icons/pp1.jpg"
        selected_color = self.comboBox_5.currentText()
        if selected_color == "Select Color":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Invalid Selection")
            msg.setText("Please select a valid color.")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
        else:
            self.cart_items.append((itemname, pcquantity, selected_color, price, image_path))
            msg_box = QMessageBox(self)
            msg_box.setText("Do You Want to View Your Cart?")
            msg_box.setWindowTitle('Hp Added!')
            msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            msg_box.setDefaultButton(QMessageBox.No)
            reply = msg_box.exec_()
            if reply == QMessageBox.Yes:
                self.load_cart()
            self.activecart_3.show()
            self.outt.show()

    def cart__dell(self):
        global dellquan
        price = "785,000"
        dellquantity = dellquan
        itemname = "DELL Latitude 3310"
        image_path = "../icons/l1.jpg"
        selected_color = self.comboBox_6.currentText()
        if selected_color == "Select Color":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Invalid Selection")
            msg.setText("Please select a valid color.")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
        else:
            self.cart_items.append((itemname, dellquantity, selected_color, price, image_path))
            msg_box = QMessageBox(self)
            msg_box.setText("Do You Want to View Your Cart?")
            msg_box.setWindowTitle('iPhone 15 Added!')
            msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            msg_box.setDefaultButton(QMessageBox.No)
            reply = msg_box.exec_()
            if reply == QMessageBox.Yes:
                self.load_cart()
            self.activecart_3.show()
            self.outt.show()

    def addto_quan(self):
        global macquan
        try:
            macquan = (macquan + 1)
        except Exception as e:
            print(e)
        self.label_171.setText(str(macquan))

    def remove_quan(self):
        global macquan
        if macquan > 1:
            macquan = macquan - 1
        else:
            macquan = 1
        self.label_171.setText(str(macquan))

    def addtoquan_2(self):
        global ppquan
        try:
            ppquan = (ppquan + 1)
        except Exception as e:
            print(e)
        self.label_172.setText(str(ppquan))

    def removequan_2(self):
        global ppquan
        if ppquan > 1:
            ppquan = ppquan - 1
        else:
            ppquan = 1
        self.label_172.setText(str(ppquan))

    def addtoquan_3(self):
        global dellquan
        try:
            dellquan = (dellquan + 1)
        except Exception as e:
            print(e)
        self.label_173.setText(str(dellquan))

    def removequan_3(self):
        global dellquan
        if dellquan > 1:
            dellquan = dellquan - 1
        else:
            dellquan = 1
        self.label_173.setText(str(dellquan))

    def dropback_(self):
        if hasattr(self, 'main') and hasattr(self, 'inventory'):
            self.main.setCurrentWidget(self.inventory)
        else:
            print("stackedWidget or Dashboard not found in the UI file")

        ##-------------------------(Login)--------------------------------------------------##
    def login(self):
        try:
            login_dialog = loginDialog()
            login_dialog.exec_()
            print("Navigation successful.")
        except Exception as e:
            print(f"Error navigating to reset password screen: {e}")




    ##---------------------------(Pones)---------------------------------------------------
    def dropback(self):
        if hasattr(self, 'main') and hasattr(self, 'inventory'):
            self.main.setCurrentWidget(self.inventory)
        else:
            print("stackedWidget or Dashboard not found in the UI file")

    def next_item(self):
        try:
            if hasattr(self, 'types') and hasattr(self, 'ipone'):
                self.types.setCurrentWidget(self.ipone)
            else:
                print("stackedWidget or Dashboard not found in the UI file")
        except Exception as e:
            print(e)

    def prev_item(self):
        try:
            if hasattr(self, 'types') and hasattr(self, 'samsun'):
                self.types.setCurrentWidget(self.samsun)
            else:
                print("stackedWidget or Dashboard not found in the UI file")
        except Exception as e:
            print(e)

    def prev_item2(self):
        try:
            if hasattr(self, 'types') and hasattr(self, 'ipone'):
                self.types.setCurrentWidget(self.ipone)
            else:
                print("stackedWidget or Dashboard not found in the UI file")
        except Exception as e:
            print(e)

    def next_item2(self):
        try:
            if hasattr(self, 'types') and hasattr(self, 'pixel'):
                self.types.setCurrentWidget(self.pixel)
            else:
                print("stackedWidget or Dashboard not found in the UI file")
        except Exception as e:
            print(e)

    def prev_item3(self):
        try:
            if hasattr(self, 'types') and hasattr(self, 'pixel'):
                self.types.setCurrentWidget(self.pixel)
            else:
                print("stackedWidget or Dashboard not found in the UI file")
        except Exception as e:
            print(e)

    def next_item3(self):
        try:
            if hasattr(self, 'types') and hasattr(self, 'samsun'):
                self.types.setCurrentWidget(self.samsun)
            else:
                print("stackedWidget or Dashboard not found in the UI file")
        except Exception as e:
            print(e)

    def pones(self):
        if hasattr(self, 'main') and hasattr(self, 'phones'):
            self.main.setCurrentWidget(self.phones)
        else:
            print("stackedWidget or Dashboard not found in the UI file")
        self.startat()

    def startat(self):
        try:
            if hasattr(self, 'types') and hasattr(self, 'samsun'):
                self.types.setCurrentWidget(self.samsun)
            else:
                print("stackedWidget or Dashboard not found in the UI file")
        except Exception as e:
            print(e)
            self.setui()

    def setui(self):
        try:
            self.addicon.setPixmap(
                QtGui.QPixmap("../icons/angle-double-right.png"))
            self.ree.setPixmap(
                QtGui.QPixmap("../icons/angle-double-right.png"))
            icon5 = QIcon("../icons/left.png")
            self.back.setIcon(icon5)
            icon5 = QIcon("../icons/left.png")
            self.back_3.setIcon(icon5)
            icon6 = QIcon("../icons/shopping-cart.png")
            self.cartbox.setIcon(icon6)
            icon6 = QIcon("../icons/shopping-cart.png")
            self.cartbox_2.setIcon(icon6)
            icon6 = QIcon("../icons/shopping-cart.png")
            self.cartbox_4.setIcon(icon6)
            icon9 = QIcon("../icons/left.png")
            self.previtem.setIcon(icon9)
            icon8 = QIcon("../icons/right.png")
            self.nextitem.setIcon(icon8)
            icon9 = QIcon("../icons/left.png")
            self.previtem_2.setIcon(icon9)
            icon8 = QIcon("../icons/right.png")
            self.nextitem_2.setIcon(icon8)
            icon9 = QIcon("../icons/left.png")
            self.previtem_3.setIcon(icon9)
            icon8 = QIcon("../icons/right.png")
            self.nextitem_3.setIcon(icon8)
            icon = QIcon("../icons/square-plus.png")
            self.quanadd.setIcon(icon)
            icon2 = QIcon("../icons/square-minus.png")
            self.quanmin.setIcon(icon2)
            icon = QIcon("../icons/square-plus.png")
            self.rerer.setIcon(icon)
            icon2 = QIcon("../icons/square-minus.png")
            self.uii.setIcon(icon2)
            icon = QIcon("../icons/square-plus.png")
            self.tensor.setIcon(icon)
            icon2 = QIcon("../icons/square-minus.png")
            self.opp.setIcon(icon2)
            self.sam1.setPixmap(
                QtGui.QPixmap("../icons/s1.jpg"))
            self.sam2.setPixmap(
                QtGui.QPixmap("../icons/s2.jpg"))
            self.sam3.setPixmap(
                QtGui.QPixmap("../icons/s3.jpg"))
            self.sam4.setPixmap(
                QtGui.QPixmap("../icons/s4.jpg"))
            self.i11.setPixmap(
                QtGui.QPixmap("../icons/ip1.jpg"))
            self.i2.setPixmap(
                QtGui.QPixmap("../icons/ip2.jpg"))
            self.i3.setPixmap(
                QtGui.QPixmap("../icons/ip3.jpg"))
            self.i4.setPixmap(
                QtGui.QPixmap("../icons/ip4.jpg"))
            self.label_48.setPixmap(
                QtGui.QPixmap("../icons/p1.jpg"))
        except Exception as e:
            print(e)

    def addtoquan(self):
        global samquan
        try:
            samquan = (samquan + 1)
        except Exception as e:
            print(e)
        self.actualquan_2.setText(str(samquan))

    def removequan(self):
        global samquan
        if samquan > 1:
            samquan = samquan - 1
        else:
            samquan = 1
        self.actualquan_2.setText(str(samquan))

    def addtoquan2(self):
        global pquan
        try:
            pquan = (pquan + 1)
        except Exception as e:
            print(e)
        self.quanbox.setText(str(pquan))

    def removequan2(self):
        global pquan
        if pquan > 1:
            pquan = pquan - 1
        else:
            pquan = 1
        self.quanbox.setText(str(pquan))

    def addtoquan3(self):
        global ipquan
        try:
            ipquan = (ipquan + 1)
        except Exception as e:
            print(e)
        self.actualquan.setText(str(ipquan))

    def removequan3(self):
        global ipquan
        if ipquan > 1:
            ipquan = ipquan - 1
        else:
            ipquan = 1
        self.actualquan.setText(str(ipquan))

    def cart__p(self):
        global pquan
        price = "1,050,000"
        pquantity = pquan
        itemname = "Google Pixel 8 Pro 5G"
        image_path = "../icons/p1.jpg"
        selected_color = self.pcolor.currentText()
        if selected_color == "Select Color":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Invalid Selection")
            msg.setText("Please select a color.")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
        else:
            self.cart_items.append((itemname, pquantity, selected_color, price, image_path))
            msg_box = QMessageBox(self)
            msg_box.setText("Do You Want to View Your Cart?")
            msg_box.setWindowTitle('Pixel Added!')
            msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            msg_box.setDefaultButton(QMessageBox.No)
            reply = msg_box.exec_()
            if reply == QMessageBox.Yes:
                self.load_cart()
            self.activecart_2.show()
            self.outt.show()


    def cart__(self):
        global carttt
        global samquan
        price = "1,998,000"
        squantity = samquan
        print(type(samquan))
        itemname = "Samsung S23 Ultra"
        image_path = "../icons/s1.jpg"
        selected_color = self.colorcombo.currentText()
        if selected_color == "Select Color":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Invalid Selection")
            msg.setText("Please select a valid color.")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
        else:
            self.cart_items.append((itemname, squantity, selected_color, price, image_path))
            msg_box = QMessageBox(self)
            msg_box.setText("Do You Want to View Your Cart?")
            msg_box.setWindowTitle('Samsung Added!')
            msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            msg_box.setDefaultButton(QMessageBox.No)
            reply = msg_box.exec_()
            if reply == QMessageBox.Yes:
                self.load_cart()
            self.activecart.show()
            self.outt.show()

    def cart__ip(self):
        global ipquan
        price = "1,997,999"
        ipquantity = ipquan
        itemname = "Apple iPhone 15 Pro Max"
        image_path = "../icons/ip1.jpg"
        selected_color = self.comboBox.currentText()
        if selected_color == "Select Color":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Invalid Selection")
            msg.setText("Please select a valid color.")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
        else:
            self.cart_items.append((itemname, ipquantity, selected_color, price, image_path))
            msg_box = QMessageBox(self)
            msg_box.setText("Do You Want to View Your Cart?")
            msg_box.setWindowTitle('iPhone 15 Added!')
            msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            msg_box.setDefaultButton(QMessageBox.No)
            reply = msg_box.exec_()
            if reply == QMessageBox.Yes:
                self.load_cart()
            self.activecart_4.show()
            self.outt.show()


    def load_cart(self):
        if hasattr(self, 'main') and hasattr(self, 'cart'):
            self.main.setCurrentWidget(self.cart)
        else:
            print("stackedWidget or cart not found in the UI file")
        self.settable()
        self.cart_table.setColumnCount(5)
        self.cart_table.setHorizontalHeaderLabels(["Image", "Item Name", "Quantity", "Color", "Price"])
        self.cart_table.setRowCount(0)
        print("Current Cart Items:", self.cart_items)
        row_height = 120
        for row_number, (item_name, quantity, color, price, image_path) in enumerate(self.cart_items):
            self.cart_table.insertRow(row_number)
            self.cart_table.setRowHeight(row_number, row_height)
            if image_path and os.path.isfile(image_path):
                pixmap = QPixmap(image_path)
                pixmap = pixmap.scaled(900, 900, aspectRatioMode=1)  # Resize to 100x100 pixels (adjust as needed)
                icon = QIcon(pixmap)
                image_item = QTableWidgetItem()
                image_item.setIcon(icon)
                self.cart_table.setItem(row_number, 0, image_item)
            else:
                print(f"Image path invalid or file does not exist: {image_path}")
                self.cart_table.setItem(row_number, 0, QTableWidgetItem("No Image"))
            self.cart_table.setItem(row_number, 1, QTableWidgetItem(item_name))
            self.cart_table.setItem(row_number, 2, QTableWidgetItem(str(quantity)))
            self.cart_table.setItem(row_number, 3, QTableWidgetItem(color))
            self.cart_table.setItem(row_number, 4, QTableWidgetItem(price))
            self.calculate_total()

    def settable(self):
        self.cart_table.setColumnWidth(0, 200)
        self.cart_table.setColumnWidth(1, 400)
        self.cart_table.setColumnWidth(2, 80)
        self.cart_table.setColumnWidth(3, 200)
        self.cart_table.setColumnWidth(4, 150)
        self.cart_table.setEditTriggers(QTableWidget.NoEditTriggers)

    def calculate_total(self):
        global totall
        # Initialize total
        total = 0.0

        # Iterate over cart items and sum up the total
        for item_name, quantity, color, price, image_path in self.cart_items:
            try:
                # Convert price to float and calculate total
                numeric_price = float(price.replace(',', ''))  # Remove any existing commas
                total += numeric_price * int(quantity)
            except ValueError:
                print(f"Invalid price or quantity for item {item_name}. Skipping.")

        formatted_total = f"{total:,.2f}"
        totall = formatted_total

        self.total.setText(f"Total: ₦{formatted_total}")

        return total

    def clear_cart(self):
        self.cart_items.clear()
        self.update_cart_ui()
        if hasattr(self, 'main') and hasattr(self, 'inventory'):
            self.main.setCurrentWidget(self.inventory)
        else:
            print("stackedWidget or Dashboard not found in the UI file")

    def update_cart_ui(self):
        self.cart_table.setRowCount(0)
        self.total.setText("Total: ₦0.00")

    def returnome(self):
        if hasattr(self, 'main') and hasattr(self, 'inventory'):
            self.main.setCurrentWidget(self.inventory)
        else:
            print("stackedWidget or Dashboard not found in the UI file")

    def checkout(self):
        payment_dialog = PaymentDialog(self)  # Pass the CartManager instance to PaymentDialog
        if payment_dialog.exec_() == QDialog.Accepted:
            self.payment_success()
        else:
            self.payment_failure()

    def payment_success(self):
        self.cart_items.clear()

    def payment_failure(self):
        pass

class PaymentDialog(QDialog):
    def __init__(self, cart_manager):
        super().__init__()
        self.cart_manager = cart_manager
        self.setWindowTitle("Payment Details")

        layout = QVBoxLayout()
        self.card_number_label = QLabel("Card Number:")
        self.card_number_input = QLineEdit()
        self.card_number_input.setMaxLength(16)
        layout.addWidget(self.card_number_label)
        layout.addWidget(self.card_number_input)
        self.expiry_date_label = QLabel("Expiry Date (MMYY):")
        self.expiry_date_input = QLineEdit()
        self.expiry_date_input.setMaxLength(4)
        self.expiry_date_input.setValidator(QIntValidator(0, 9999, self))
        layout.addWidget(self.expiry_date_label)
        layout.addWidget(self.expiry_date_input)
        self.cvv_label = QLabel("CVV:")
        self.cvv_input = QLineEdit()
        self.cvv_input.setMaxLength(3)
        self.cvv_input.setValidator(QIntValidator(0, 999, self))
        layout.addWidget(self.cvv_label)
        layout.addWidget(self.cvv_input)
        self.pay_button = QPushButton("Pay Now")
        self.pay_button.clicked.connect(self.process_payment)
        layout.addWidget(self.pay_button)
        self.setLayout(layout)

    def process_payment(self):
        try:
            card_number = self.card_number_input.text()
            expiry_date = self.expiry_date_input.text()
            cvv = self.cvv_input.text()

            if not card_number or not expiry_date or not cvv:
                QMessageBox.warning(self, "Invalid Input", "Please enter all the required details.")
                return
            payment_successful = self.simulate_payment(card_number, expiry_date, cvv)
            if payment_successful:
                self.payment_success()
        except Exception as e:
            print(f"Payment processing error: {e}")

    def payment_success(self):
        global totall
        amount = totall
        amount = amount.replace(',', '')
        amount = float(amount)

        QMessageBox.information(self, 'Payment Successful', f'Payment of ₦{amount:,.2f} was successful!')
        self.cart_manager.clear_cart()
        self.close()
    def simulate_payment(self, card_number, expiry_date, cvv):
        return True


class loginDialog(QDialog):
    def __init__(self):
        super(loginDialog, self).__init__()
        ui_path = "../ui/main.ui"
        uic.loadUi(ui_path, self)
        self.setWindowTitle('Login')
        self.logscreen()

    def logscreen(self):
        if hasattr(self, 'stackedWidget') and hasattr(self, 'login'):
            self.stackedWidget.setCurrentWidget(self.login)
        else:
            print("stackedWidget or Dashboard not found in the UI file")
        self.start.clicked.connect(self.logvalid)
        self.createacc.clicked.connect(self.reswitt)

    def reswitt(self):
        try:
            if hasattr(self, 'stackedWidget') and hasattr(self, 'acccreate'):
                self.stackedWidget.setCurrentWidget(self.acccreate)
            else:
                print("stackedWidget or Dashboard not found in the UI file")
            self.validate.clicked.connect(self.accountcreate)
            name_regex = QRegExp("[a-zA-Z]+")
            name_validator = QRegExpValidator(name_regex)
            self.f_name.setValidator(name_validator)
            self.l_name.setValidator(name_validator)
            int_validator = QIntValidator()
            int_validator.setRange(0, 2147483647)
            self.pnumber.setValidator(int_validator)
        except Exception as e:
            print(e)

    def accountcreate(self):
        try:
            fname = self.f_name.text()
            lname = self.l_name.text()
            email = self.email_.text()
            sex = self.sexcombo.currentText()
            email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

            reset_style = """QLineEdit{
                                background-color: transparent;
                                border-radius: 10px;
                                border: 1px solid rgb(95, 95, 95);
                                padding-left: 10px;}
                             QLineEdit:hover{
                                border: 2px solid rgb(95, 95, 95);
                             }"""

            if not fname:
                self.f_name.setStyleSheet("border: 0.5px solid red; padding-left: 10px; color: rgb(0, 0, 0);")
                self.fnameerror.setText("First name must not be empty")
                QTimer.singleShot(2000, lambda: self.fnameerror.setText(""))
                QTimer.singleShot(2000, lambda: self.f_name.setStyleSheet(reset_style))
                return False

            # Validate Last Name
            if not lname:
                self.l_name.setStyleSheet("border: 0.5px solid red; padding-left: 10px; color: rgb(0, 0, 0);")
                self.lnameerror.setText("Last name must not be empty")
                QTimer.singleShot(2000, lambda: self.lnameerror.setText(""))
                QTimer.singleShot(2000, lambda: self.l_name.setStyleSheet(reset_style))
                return False

            # Validate Email
            if not email:
                self.email_.setStyleSheet("border: 0.5px solid red; padding-left: 10px; color: rgb(0, 0, 0);")
                self.emailerror.setText("Email must not be empty")
                QTimer.singleShot(2000, lambda: self.emailerror.setText(""))
                QTimer.singleShot(2000, lambda: self.email_.setStyleSheet(reset_style))
                return False

            if not re.match(email_regex, email):
                self.email_.setStyleSheet("border: 0.5px solid red; padding-left: 10px; color: rgb(0, 0, 0);")
                self.emailerror.setText("Invalid email format")
                QTimer.singleShot(2000, lambda: self.emailerror.setText(""))
                QTimer.singleShot(2000, lambda: self.email_.setStyleSheet(reset_style))
                return False

            pnumber = self.pnumber.text()
            phone_regex = r'^\+?\d{10,15}$'
            if not pnumber:
                self.pnumber.setStyleSheet("border: 0.5px solid red; padding-left: 10px; color: rgb(0, 0, 0);")
                self.pnumbererror.setText("Phone number must not be empty")
                QTimer.singleShot(2000, lambda: self.pnumbererror.setText(""))
                QTimer.singleShot(2000, lambda: self.pnumber.setStyleSheet(reset_style))
                return False

            if not re.match(phone_regex, pnumber):
                self.pnumber.setStyleSheet("border: 0.5px solid red; padding-left: 10px; color: rgb(0, 0, 0);")
                self.pnumbererror.setText("Invalid phone number format")
                QTimer.singleShot(2000, lambda: self.pnumbererror.setText(""))
                QTimer.singleShot(2000, lambda: self.pnumber.setStyleSheet(reset_style))
                return False
            if not re.match(phone_regex, pnumber):
                self.pnumber.setStyleSheet("border: 0.5px solid red; padding-left: 10px; color: rgb(0, 0, 0);")
                self.pnumbererror.setText("Invalid phone number format")
                QTimer.singleShot(2000, lambda: self.pnumbererror.setText(""))
                return False

            if sex == "Select One":
                self.sexerror.setText("Please select a valid sex option")
                QTimer.singleShot(2000, lambda: self.sexerror.setText(""))
                return False

            path = "../db/userdata.db"
            conn = sqlite3.connect(path)
            local = conn.cursor()
            local.execute('''
                                    CREATE TABLE IF NOT EXISTS userdata(
                                        First_Name TEXT,
                                        Last_Name TEXT,
                                        Username TEXT PRIMARY KEY,
                                        Password TEXT,
                                        Phone_Number TEXT,
                                        Email TEXT,
                                        Gender TEXT,
                                        D_O_B TEXT
                                    )
                                ''')
            conn.close()
        except Exception as e:
            print(e)
        self.createuser()

    def createuser(self):
        global userr
        fname = self.f_name.text()
        lname = self.l_name.text()
        email = self.email_.text()
        sex = self.sexcombo.currentText()
        pnumber = self.pnumber.text()
        selected_date = self.dateEdit.date()
        date_str = selected_date.toString("yyyy-MM-dd")
        try:
            path2 = "../db/userdata.db"
            conn = sqlite3.connect(path2)
            local = conn.cursor()
            local.execute('''
                    INSERT INTO userdata (First_Name, Last_Name, Phone_Number, Email, 
                    Gender, D_O_B)
                    VALUES (?, ?, ?, ?, ?, ?);
                ''', (fname, lname, pnumber, email, sex, date_str))
            self.nextstep()
            userr = fname
            conn.commit()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        finally:
            if conn:
                conn.close()

    def nextstep(self):
        if hasattr(self, 'stackedWidget') and hasattr(self, 'create2'):
            self.stackedWidget.setCurrentWidget(self.create2)
        else:
            print("stackedWidget or Dashboard not found in the UI file")
        self.doneee.clicked.connect(self.readyup)

    def readyup(self):

        usernamee = self.username.text()
        passkey = self.passkey.text()
        confirmpass = self.confirmpasskey.text()
        username_regex = r'^[a-zA-Z0-9]{5,15}$'
        if not usernamee:
            self.username.setStyleSheet("border: 0.5px solid red; padding-left: 10px; color: rgb(0, 0, 0);")
            self.usernameerror.setText("Username must not be empty")
            QTimer.singleShot(2000, lambda: self.usernameerror.setText(""))
            return False
        if not re.match(username_regex, usernamee):
            self.username.setStyleSheet("border: 0.5px solid red; padding-left: 10px; color: rgb(0, 0, 0);")
            self.usernameerror.setText("Username must be alphanumeric and 5-15 characters long")
            QTimer.singleShot(2000, lambda: self.usernameerror.setText(""))
            return False
        if not passkey or len(passkey) < 6:
            self.passkey.setStyleSheet("border: 0.5px solid red; padding-left: 10px; color: rgb(0, 0, 0);")
            self.passkeyerror.setText("Password must be at least 6 characters long")
            QTimer.singleShot(2000, lambda: self.passkeyerror.setText(""))
            return False
        if passkey != confirmpass:
            self.confirmpasskey.setStyleSheet("border: 0.5px solid red; padding-left: 10px; color: rgb(0, 0, 0);")
            self.confirmpasserror.setText("Passwords do not match")
            QTimer.singleShot(2000, lambda: self.confirmpasserror.setText(""))
            return False
        self.confirm()

    def confirm(self):
        global userr
        usernamee = self.username.text()
        passkey = self.passkey.text()
        path2 = "../db/userdata.db"
        conn = sqlite3.connect(path2)
        local = conn.cursor()
        local.execute('''
                            UPDATE userdata
                            SET Username = ?, Password = ?
                            WHERE First_Name = ?;
                        ''', (usernamee, passkey, userr))
        conn.commit()
        self.logscreen()


    def logvalid(self):
        user = self.user.text()
        passkey = self.password.text()
        try:
            path = "../db/userdata.db"
            conn = sqlite3.connect(path)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM userdata WHERE Username = ? AND Password = ?", (user, passkey))
            result = cursor.fetchone()
            if result:
                self.yes()
            else:
                self.no()
            conn.close()
        except Exception as e:
            print(e)

    def no(self):
        self.label.setText("Login failed! Incorrect username or password")
        QTimer.singleShot(2000, lambda: self.label.setText(""))

    def yes(self):
        user = self.user.text()
        global user_name_local
        user_name_local = user
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SoMain()
    window.show()
    sys.exit(app.exec_())

