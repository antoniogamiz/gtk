#!/usr/bin/python
# -*- coding: utf-8 -*-

import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk

class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Hello World")

        self.button = Gtk.Button(label="Click here")
        #Esta función devuelve un número asociado a la callback, que sirve para desconectarla 'widget.disconnect(handler_id)' o 'widget.disconnect_by_func(callback)'
        self.button.connect("clicked", self.on_button_clicked)
        self.add(self.button)

    def on_button_clicked(self, window):
        print "Hello World"
        widget = Gtk.Box()
        #Para ver las funciones de un widget.
        print dir(widget.props)

win = MyWindow()
win.connect("delete-event",Gtk.main_quit)
win.show_all()
Gtk.main()