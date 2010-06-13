#!/usr/bin/python
# -*- coding: utf-8 -*-

import gtk
import gtk.glade
import gobject
import pango
import random
from cbtn2 import *
from colorplayer import colorplayer
from confmanager1 import confmanager

class prozor (gtk.Window):
	def options_clicked_cb(self, widget):
		self.prefference_dialog.show()
	def play_clicked_cb(self, widget):
		if self.isModelEmpty():
			colors = []
			for c in self.color_list_model:
				#print (type(c[0]))
				#print(c[0], c[1])
				if (c[2]):
					colors.append([c[0], c[1]])
			p = colorplayer(colors)
	def isModelEmpty(self):
		if len(self.color_list_model): return True
		else: return False
	def remove_clicked_cb(self, widget):
		sel = self.color_list.get_selection().get_selected()[1]
		print(type(sel))
		if self.isModelEmpty() and sel:
			self.color_list_model.remove(sel)
	def add_clicked_cb(self, widget):
		self.color_list_model.append((self.color_btn.get_color(), self.time.get_value(),True))
		cmap = self.color_btn.get_colormap()
		self.color_btn.set_color(self.random_color(cmap))
	def pd_ok_clicked_cb(self, widget):
		self.configuration.update_all(self.default_adjustment.get_value(), self.minimum_adjustment.get_value(), self.maximum_adjustment.get_value(), ".colorchange")
		self.update_defaults()
		self.prefference_dialog.hide()
	def pd_cancel_clicked_cb(self, widget):
		self.prefference_dialog.hide()
	def cancel_clicked_cb(self, widget):
		self.destroy(None)
	def toggled_callback(self, cell, path, model=None, col_num=0):
		iter = model.get_iter(path)
		model[iter][2] = not cell.get_active()
	def on_color_set(self, cell, path, color):
		#print ls[path][0]
		self.color_list_model[path][0] = color
		#print color
		#print ls[path][0]
	def on_edit(self, cell, path, t):
		self.color_list_model[path][1] = int(t)
	#def random_color(color='#'):
	def random_color(self, map):
		red = random.randint(0, 65535)
		green = random.randint(0, 65535)
		blue = random.randint(0, 65535)
		return map.alloc_color(red, green, blue)
	def update_live_conf(self):
		self.default_adjustment.set_value(self.configuration.get_default_timer())
		self.minimum_adjustment.set_value(self.configuration.get_min_range())
		self.maximum_adjustment.set_value(self.configuration.get_max_range())
	def start_builder(self):
		dic = {
		"options_clicked_cb" : self.options_clicked_cb,
		"time_icon_press_cb" : self.time_icon_press_cb,
		"play_clicked_cb"	: self.play_clicked_cb,
		"remove_clicked_cb"	: self.remove_clicked_cb,
		"add_clicked_cb"	: self.add_clicked_cb,
		"cancel_clicked_cb" : self.cancel_clicked_cb,
		"pd_ok_clicked_cb" : self.pd_ok_clicked_cb,
		"pd_cancel_clicked_cb" : self.pd_cancel_clicked_cb,
		"destroy"			: self.destroy
		}
		gladefile = "boimenuvach.xml"
		self.builder = gtk.Builder()
		self.builder.add_from_file(gladefile)
		self.builder.connect_signals(dic)

		#self.csd = self.builder.get_object("csd")
		#self.color_list_model = self.builder.get_object("liststore1")
		self.color_list = self.builder.get_object("color_lst")
		self.time = self.builder.get_object("time")
		self.color_btn = self.builder.get_object("color_btn")
		# Prefference_dialog objects
		self.prefference_dialog = self.builder.get_object("prefference_dialog")
		self.timer_adjustment = self.builder.get_object("timer_adjustment")
		self.default_adjustment = self.builder.get_object("default_adjustment")
		self.minimum_adjustment = self.builder.get_object("minimum_adjustment")
		self.maximum_adjustment = self.builder.get_object("maximum_adjustment")
		self.pd_libpath = self.builder.get_object("pd_libpath")
		self.start_defaults()
		#self.pd_default_timer = builder.get_object("pd_default_timer")
	def table(self):
		self.color_list_model = gtk.ListStore(gtk.gdk.Color, int, bool)

		font = pango.FontDescription('utopia bold 12')

		cell1 = CellRendererColor()
		cell1.connect('color-set', self.on_color_set)

		cell2 = gtk.CellRendererSpin()
		cell2.set_property('editable', True)
		self.adjustment = gtk.Adjustment(0, 0, 100, 1)
		cell2.set_property("adjustment", self.adjustment)
		cell2.set_property('font-desc', font)
		cell2.connect("edited", self.on_edit)
		col2 = gtk.TreeViewColumn('Времетраење[с]', cell2, text=1)


		cell3 = gtk.CellRendererToggle()
		cell3.connect('toggled', self.toggled_callback, self.color_list_model, 1)
		col3 = gtk.TreeViewColumn('Играјго', cell3, active=2, activatable=1)
		#cell3.set_property('activatable', True)

		self.color_list.set_model(self.color_list_model)

		self.color_list.insert_column_with_attributes(-1, 'Боја', cell1, color=0)
		self.color_list.append_column(col2)
		self.color_list.append_column(col3)
		self.color_list.show_all()
	def start_defaults(self):
		self.default_adjustment.set_value(self.configuration.get_default_timer())
		self.minimum_adjustment.set_value(self.configuration.get_min_range())
		self.maximum_adjustment.set_value(self.configuration.get_max_range())
		self.update_defaults()
	def update_defaults(self):
		self.timer_adjustment.set_value(self.default_adjustment.get_value())
		self.timer_adjustment.set_lower(self.minimum_adjustment.get_value())
		self.timer_adjustment.set_upper(self.maximum_adjustment.get_value())
	def __init__(self):
		super(prozor, self).__init__()
		self.configuration = confmanager()
		self.start_builder()

		self.table()
		self = self.builder.get_object("window1")
		self.show_all()

	def time_icon_press_cb(self, widget, icon, event):
		if icon == gtk.ENTRY_ICON_SECONDARY:
			self.timer_adjustment.set_value(self.configuration.get_default_timer())
		elif icon == gtk.ENTRY_ICON_PRIMARY:
			self.timer_adjustment.set_value(random.randrange(self.configuration.get_min_range(), self.configuration.get_max_range()))
	def destroy(self, widget):
		gtk.main_quit()


def main ():
	p = prozor()
	gtk.main()
if __name__ == "__main__": main()
