#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import csv
import json
import yaml
import codecs
import sys

from  PySide2 import QtWidgets, QtCore

#init関数を定義
class Jymaker(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Json Yaml fileMaker")

        self.build_ui()
        #SignalとSlotを設定
        self.connect_signal_slot()

    def callback_line_edit_editingFinished(self):
        file = self.line_edit.text()

        if not file.endswith(".csv"):
            return

        url = QtCore.QUrl(file)
        if url.isLocalFile():
            file = url.toLocalFile()
        
        if os.path.exists(file):
            self.line_edit.setText(file)

            json_list = self.load_csv(file)
            self.listwgt.clear()
            self.listwgt.addItems(json_list)

#Openボタンを押したときの挙動を設定
    def callback_file_dialog_button_clicked(self):
        file, filter_ = QtWidgets.QFileDialog.getOpenFileName(
            self, "Open CSV", "C:/Users/User/Documents/Jymaker/csv", "CSV (*.csv)"
        )

#csvファイルの中の情報を取り出す
#listWedgetに情報を入れていく
        if file:
            self.line_edit.setText(file)
            json_list = self.load_csv(file)
            self.listwgt.clear()
            self.listwgt.addItems(json_list)
#returnで返された、変数を受け取り表示させる。
           

#JSONボタンを押したときにの処理
    def callback_create_file_button_clicked(self):
        jsdata = []
        for row in range(self.listwgt.count()):
            item = self.listwgt.item(row)
            jsdata.append(item.text())

        filename = "C:/Users/User/Documents/Jymaker/json/sample.json"
        with open(filename, "w", encoding="utf_8") as f:
            json.dump(jsdata, f ,indent=4)

#メッセージボックス
        QtWidgets.QMessageBox.about(
            self,
            "json file was created.",
            "json file was created."
        )
       
#YAMLボタンを押したときにの処理
    def callback_create_yaml_button_clicked(self):
        yamldata = []
        for row in range(self.listwgt.count()):
            item = self.listwgt.item(row)
            yamldata.append(item.text())

        filename = "C:/Users/User/Documents/Jymaker/yml/sample.yml"
        with codecs.open(filename, 'w', 'utf-8') as f:
            yaml.dump(yamldata, f, encoding='utf-8', allow_unicode=True)

#メッセージボックス
        QtWidgets.QMessageBox.about(
            self,
            "Yaml file was created.",
            "Yaml file was created."
        )

    #パーツを作る関数の定義
    def build_ui(self):
        self.line_edit = QtWidgets.QLineEdit()
        self.file_dialog_button = QtWidgets.QPushButton("Open")
        self.line = QtWidgets.QFrame()
        self.line.setFrameStyle(QtWidgets.QFrame.HLine | QtWidgets.QFrame.Sunken)
        self.listwgt = QtWidgets.QListWidget()
        self.create_file_button = QtWidgets.QPushButton("JSON")
        self.create_yaml_button = QtWidgets.QPushButton("YAML")

     #GUIを表示させるためのレイアウト設置
        form_layout = QtWidgets.QFormLayout()
        form_layout.addRow("CSV File", self.line_edit)
        form_layout.addRow("", self.file_dialog_button )
        form_layout.addRow(self.line)
        form_layout.addRow("File", self.listwgt)
        form_layout.addRow(self.create_file_button)
        form_layout.addRow(self.create_yaml_button)
        self.setLayout(form_layout)

    #SignalとSlotを繋げる処理を行う関数
    def connect_signal_slot(self):
        self.line_edit.editingFinished.connect(self.callback_line_edit_editingFinished)
        self.file_dialog_button.clicked.connect(self.callback_file_dialog_button_clicked)
        self.create_file_button.clicked.connect(self.callback_create_file_button_clicked)
        self.create_yaml_button.clicked.connect(self.callback_create_yaml_button_clicked)

#csvファイルの内容をを読み込む。
# 読み込んだ内容をQListWidgetItemに返して表示させる。
    def load_csv(self, file):
        json_list =[]
        with open(file, "r", encoding="utf_8") as f:
            reader = csv.reader(f)
            for row in reader:
                json_list.append(",".join(row))

        return(json_list)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = Jymaker()
    win.show()
    sys.exit(app.exec_())


    
