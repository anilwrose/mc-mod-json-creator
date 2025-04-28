#
# Copyright (C) 2025  anilwrose
#
# This file may be used under the terms of the GNU General Public License
# version 3.0 as published by the Free Software Foundation and appearing in
# the file LICENSE included in the packaging of this file.  Please review the
# following information to ensure the GNU General Public License version 3.0
# requirements will be met: http://www.gnu.org/copyleft/gpl.html.
#
# If you do not wish to use this file under the terms of the GPL version 3.0
# then you may purchase a commercial license.  For more information contact
# https://github.com/anilwrose.
#
# This file is provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE
# WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.

import json
import os
import sys
from time import sleep
from string import ascii_letters, digits
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow
from untitled import Ui_MainWindow
import ctypes

ALLOWED = list(ascii_letters + digits + "-_")
class mc_json_creator:
    def __init__(self, jsontype, modname, itemname, folderpath):
        self.jsontype = jsontype #blockstates-items-modelsblock-modelsitem
        self.modname = modname
        self.itemname = itemname
        self.folderpath = folderpath

        if self.jsontype == "blockstates":
            mc_json_creator.blockstates(self)
        elif self.jsontype == "items":
            mc_json_creator.items(self)
        elif self.jsontype == "modelsblock":
            mc_json_creator.modelsblock(self)
        elif self.jsontype == "modelsitem":
            mc_json_creator.modelsitem(self)
        else:
            raise ValueError(f"invalid json type: {self.jsontype}")


    def blockstates(self): # Fonksiyon blockstates için json oluşturuyor.
        blockstates = {
                      "variants": {
                        "": {
                          "model": f"{self.modname}:blocks/{self.itemname}"
                        }
                      }
                    }

        if len(self.folderpath)==0:
            try:
                os.makedirs("blockstates")
            except Exception as e:
                #ctypes.windll.user32.MessageBoxW(0, f"An error occurred: {e}", "Error", 1)
                pass
            with open("blockstates/"+self.itemname+".json", "w", encoding="utf-8") as file: #json oluşturma
                json.dump(blockstates, file, ensure_ascii=False, indent=2)  # indent satırları alt alta yazar
            ctypes.windll.user32.MessageBoxW(0, f"blockstates/{self.itemname}.json created successfully.", "Info", 1)
        elif os.path.isdir(self.folderpath)==True:
            try:
                os.makedirs(self.folderpath+"/"+"blockstates")
            except Exception as e:
                #ctypes.windll.user32.MessageBoxW(0, f"An error occurred: {e}", "Error", 1)
                pass
            with open(self.folderpath+"/"+"blockstates/"+self.itemname+".json", "w", encoding="utf-8") as file:
                json.dump(blockstates, file, ensure_ascii=False, indent=2)
            ctypes.windll.user32.MessageBoxW(0, f"{self.folderpath}/blockstates/{self.itemname}.json created successfully.", "Info", 1)
        elif os.path.isdir(self.folderpath)==False:
            print(f"invalid path: {self.folderpath}")
            return ctypes.windll.user32.MessageBoxW(0, f"invalid path: {self.folderpath}", "Error", 1)
        else:
            print(f"invalid path: {self.folderpath}")
            return ctypes.windll.user32.MessageBoxW(0, f"invalid path: {self.folderpath}", "Error", 1)

    def items(self): # Fonksiyon items için json oluşturuyor.
        items = {
                  "model": {
                    "type": "minecraft:model",
                    "model": f"{self.modname}:item/{self.itemname}"
                  }
                }

        if len(self.folderpath) == 0:
            try:
                os.makedirs("items")
            except Exception as e:
                #ctypes.windll.user32.MessageBoxW(0, f"An error occurred: {e}", "Error", 1)
                pass
            with open("items/" + self.itemname + ".json", "w", encoding="utf-8") as file:
                json.dump(items, file, ensure_ascii=False, indent=2)
            ctypes.windll.user32.MessageBoxW(0, f"items/{self.itemname}.json created successfully.", "Info", 1)
        elif os.path.isdir(self.folderpath) == True:
            try:
                os.makedirs(self.folderpath + "/" + "items")
            except Exception as e:
                #ctypes.windll.user32.MessageBoxW(0, f"An error occurred: {e}", "Error", 1)
                pass
            with open(self.folderpath + "/" + "items/" + self.itemname + ".json", "w", encoding="utf-8") as file:
                json.dump(items, file, ensure_ascii=False, indent=2)
            ctypes.windll.user32.MessageBoxW(0, f"{self.folderpath}/items/{self.itemname}.json created successfully.", "Info", 1)
        elif os.path.isdir(self.folderpath) == False:
            print(f"invalid path: {self.folderpath}")
            return ctypes.windll.user32.MessageBoxW(0, f"invalid path: {self.folderpath}", "Error", 1)
        else:
            print(f"invalid path: {self.folderpath}")
            return ctypes.windll.user32.MessageBoxW(0, f"invalid path: {self.folderpath}", "Error", 1)

    def modelsblock(self): # Fonksiyon models block için json oluşturuyor. Aynı zamanda item olarak tanımlıyor ek olarak models/item kullanmaya gerek yoktur.
        modelsblock = {
                      "parent": "minecraft:block/cube_all",
                      "textures": {
                        "all": f"{self.modname}:block/{self.itemname}"
                      }
                    }

        if len(self.folderpath) == 0:
            try:
                os.makedirs("models/block")
                os.makedirs("models/item")
            except Exception as e:
                #ctypes.windll.user32.MessageBoxW(0, f"An error occurred: {e}", "Error", 1)
                pass
            with open("models/block/" + self.itemname + ".json", "w", encoding="utf-8") as file:
                json.dump(modelsblock, file, ensure_ascii=False, indent=2)
            with open("models/item/" + self.itemname + ".json", "w", encoding="utf-8") as file:
                json.dump(modelsblock, file, ensure_ascii=False, indent=2)
            ctypes.windll.user32.MessageBoxW(0, f"models/block/{self.itemname}.json created successfully.", "Info", 1)
            ctypes.windll.user32.MessageBoxW(0, f"models/item/{self.itemname}.json created successfully.", "Info", 1)
        elif os.path.isdir(self.folderpath) == True:
            try:
                os.makedirs(self.folderpath + "/" + "models/block")
                os.makedirs(self.folderpath + "/" + "models/item")
            except Exception as e:
                #ctypes.windll.user32.MessageBoxW(0, f"An error occurred: {e}", "Error", 1)
                pass
            with open(self.folderpath + "/" + "models/block/" + self.itemname + ".json", "w", encoding="utf-8") as file:
                json.dump(modelsblock, file, ensure_ascii=False, indent=2)
            with open(self.folderpath + "/" + "models/item/" + self.itemname + ".json", "w", encoding="utf-8") as file:
                json.dump(modelsblock, file, ensure_ascii=False, indent=2)
            ctypes.windll.user32.MessageBoxW(0, f"{self.folderpath}/models/block/{self.itemname}.json created successfully.","Info", 1)
            ctypes.windll.user32.MessageBoxW(0, f"{self.folderpath}/models/item/{self.itemname} .json created successfully.","Info", 1)
        elif os.path.isdir(self.folderpath) == False:
            print(f"invalid path: {self.folderpath}")
            return ctypes.windll.user32.MessageBoxW(0, f"invalid path: {self.folderpath}", "Error", 1)
        else:
            print(f"invalid path: {self.folderpath}")
            return ctypes.windll.user32.MessageBoxW(0, f"invalid path: {self.folderpath}", "Error", 1)


    def modelsitem(self):# Fonksiyon models item için json oluşturuyor.
        modelsitem = {
                      "parent": "minecraft:item/generated",
                      "textures": {
                        "layer0": f"{self.modname}:item/{self.itemname}"
                      }
                    }

        if len(self.folderpath) == 0:
            try:
                os.makedirs("models/item")
            except Exception as e:
                #ctypes.windll.user32.MessageBoxW(0, f"An error occurred: {e}", "Error", 1)
                pass
            with open("models/item/" + self.itemname + ".json", "w", encoding="utf-8") as file:
                json.dump(modelsitem, file, ensure_ascii=False, indent=2)
            ctypes.windll.user32.MessageBoxW(0, f"models/item/{self.itemname}.json created successfully.", "Info", 1)
        elif os.path.isdir(self.folderpath) == True:
            try:
                os.makedirs(self.folderpath + "/" + "models/item")
            except Exception as e:
                #ctypes.windll.user32.MessageBoxW(0, f"An error occurred: {e}", "Error", 1)
                pass
            with open(self.folderpath + "/" + "models/item/" + self.itemname + ".json", "w", encoding="utf-8") as file:
                json.dump(modelsitem, file, ensure_ascii=False, indent=2)
            ctypes.windll.user32.MessageBoxW(0, f"{self.folderpath}/models/item/{self.itemname}.json created successfully.", "Info", 1)
        elif os.path.isdir(self.folderpath) == False:
            print(f"invalid path: {self.folderpath}")
            return ctypes.windll.user32.MessageBoxW(0, f"invalid path: {self.folderpath}", "Error", 1)
        else:
            print(f"invalid path: {self.folderpath}")
            return ctypes.windll.user32.MessageBoxW(0, f"invalid path: {self.folderpath}", "Error", 1)

class Thread(QtCore.QThread):
    def run(self):
        QtCore.QThread.sleep(1)

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('Modding Minecraft Json Creator')
        self.initUI()

    def check_string(self, string): # fonksiyon dosya türünün bozulmaması için belirli karakterleri sınıyor
        if len(string) == 0:
            return 0
        else:
            for character in string:
                if character not in ALLOWED:
                    return 0

    def initUI(self):
        self.ui.statusbar.showMessage("2025 version 0.0.1")
        self.ui.cb_3.stateChanged.connect(self.check_cb_3)
        self.ui.cb_4.stateChanged.connect(self.check_cb_4)
        self.ui.btn_1.clicked.connect(self.btn_1_clicked)
        self.ui.btn_2.clicked.connect(self.btn_2_clicked)
        self.ui.btn_3.clicked.connect(self.btn_3_clicked)
        self.thread = Thread()
        self.thread.finished.connect(lambda: self.ui.btn_1.setEnabled(True))
        self.thread.finished.connect(lambda: self.ui.btn_2.setEnabled(True))
        self.thread.finished.connect(lambda: self.ui.btn_3.setEnabled(True))

    def check_cb_3(self): # checkbox checkable kontrol
        if self.ui.cb_3.isChecked():
            self.ui.cb_4.setCheckable(False)
        else:
            self.ui.cb_4.setCheckState(0)
            self.ui.cb_3.setCheckState(0)
            self.ui.cb_4.setCheckable(True)

    def check_cb_4(self):
        if self.ui.cb_4.isChecked():
            self.ui.cb_3.setCheckable(False)
        else:
            self.ui.cb_3.setCheckState(0)
            self.ui.cb_4.setCheckState(0)
            self.ui.cb_3.setCheckable(True)

    def btn_1_clicked(self):
        if not self.thread.isRunning():
            self.ui.btn_1.setEnabled(False)
            self.thread.start()
        cb_list = ((self.ui.cb_1.checkState()),
                   (self.ui.cb_2.checkState()),
                   (self.ui.cb_3.checkState()),
                   (self.ui.cb_4.checkState()))
        if (self.check_string(self.ui.line_2.text())==0 or self.check_string(self.ui.line_3.text())==0 or cb_list==(0, 0, 0, 0)):
            QMessageBox.critical(self, "ERROR", "The text is not compatible or checkbox is not checked.")
            pass
        else:
            if self.ui.cb_1.checkState()==2:
                mc_json_creator("blockstates", self.ui.line_2.text(), self.ui.line_3.text(), self.ui.line_4.text())
            if self.ui.cb_2.checkState()==2:
                mc_json_creator("items", self.ui.line_2.text(), self.ui.line_3.text(), self.ui.line_4.text())
            if self.ui.cb_3.checkState()==2:
                mc_json_creator("modelsblock", self.ui.line_2.text(), self.ui.line_3.text(), self.ui.line_4.text())
            if self.ui.cb_4.checkState()==2:
                mc_json_creator("modelsitem", self.ui.line_2.text(), self.ui.line_3.text(), self.ui.line_4.text())

    def btn_2_clicked(self):
        if not self.thread.isRunning():
            self.ui.btn_2.setEnabled(False)
            self.thread.start()
        folderpath = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Folder')
        self.ui.line_4.setText(folderpath)

    def btn_3_clicked(self):
        if not self.thread.isRunning():
            self.ui.btn_3.setEnabled(False)
            self.thread.start()
        self.ui.line_2.setText("")
        self.ui.line_3.setText("")
        self.ui.line_4.setText("")
        self.ui.cb_1.setCheckState(0)
        self.ui.cb_2.setCheckState(0)
        self.ui.cb_3.setCheckState(0)
        self.ui.cb_4.setCheckState(0)



if __name__=="__main__":
    app = QApplication(sys.argv)
    app.setStyle('Breeze')  #['Breeze', 'Oxygen', 'QtCurve', 'Windows', 'Fusion']
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())