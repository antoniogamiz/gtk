#!/usr/bin/python3
#-*- coding: utf-8 -*-

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

import os
os.system("clear")

class Handler:
    builder=None
    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file("main.glade")
        self.handlers = {
                        "on_main_destroy" : Gtk.main_quit,
                        "on_add_clicked" : self.on_add_clicked
                        }
        self.builder.connect_signals(self.handlers)
        self.window = self.builder.get_object("main")
        self.treeView = self.builder.get_object("treeView")
        self.add_button = self.builder.get_object("add")
        self.model = Gtk.ListStore(str)
        self.model.append(["Benjamin"])
        self.model.append(["Charles"])
        self.model.append(["alfred"])
        self.model.append(["Alfred"])
        self.model.append(["David"])
        self.model.append(["charles"])
        self.model.append(["david"])
        self.model.append(["benjamin"])

        self.treeView.set_model(self.model)

        cellRenderer = Gtk.CellRendererText()
        column = Gtk.TreeViewColumn("Title", cellRenderer, text=0)
        self.treeView.append_column(column)

        self.window.show_all()
        self.window.resize(300,300)
    def on_add_clicked(self, button):
        self.model.append(["FUNCIONA JAJAJAJJA"])

def main():
    window = Handler()
    Gtk.main()
    return 0

if __name__ == '__main__':
    main()