#!/usr/bin/python
# -*- coding: utf-8 -*-

#Importamos el paquete Gtk y nos aseguramos que sea la versión 3.

import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk

#Creamos un objeto Ventana.
win = Gtk.Window()

#Asociamos la señal "delete-event" a la función Gtk.main_quit.
win.connect("delete-event",Gtk.main_quit)

#Hacemos display de la ventana.
win.show_all()

#Empezamos el loop de procesado de Gtk.
Gtk.main()