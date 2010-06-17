#!/usr/bin/python
# -*- coding: utf-8 -*-

# The rainbow_shooter modules
from tree_color_button import CellRendererColor
# TreeView modules
from gtk import ListStore
from gtk import CellRendererSpin
from gtk import CellRendererToggle
from gtk import TreeViewColumn
from gtk import Adjustment
from gtk import main as Main
from gtk import main_quit
from gtk.gdk import Color
from pango import FontDescription
class periodictable(ListStore):
	def __init__(self, color_list):
		super(periodictable, self).__init__(Color, int, bool)
		self.color_list = color_list
		font = FontDescription('utopia bold 12')

		cell1 = CellRendererColor()
		cell1.connect('color-set', self.on_color_set)

		cell2 = CellRendererSpin()
		cell2.set_property('editable', True)
		self.adjustment = Adjustment(0, 0, 100, 1)
		cell2.set_property("adjustment", self.adjustment)
		cell2.set_property('font-desc', font)
		cell2.connect("edited", self.on_edit)
		col2 = TreeViewColumn('Времетраење[с]', cell2, text=1)


		cell3 = CellRendererToggle()
		#cell3.connect('toggled', self.toggled_callback, self.color_list_model, 1)
		cell3.connect('toggled', self.toggled_callback, self, 1)
		col3 = TreeViewColumn('Играјго', cell3, active=2, activatable=1)
		cell3.set_property('activatable', True)

		#self.color_list.set_model(self.color_list_model)
		self.color_list.set_model(self)

		self.color_list.insert_column_with_attributes(-1, 'Боја', cell1, color=0)
		self.color_list.append_column(col2)
		self.color_list.append_column(col3)
		self.color_list.show_all()
	def isModelEmpty(self):
		#if len(self.color_list_model): return True
		if len(self): return True
		else: return False
	def remove_clicked_cb(self, widget):
		sel = self.color_list.get_selection().get_selected()[1]
		#print(type(sel))
		if self.isModelEmpty() and sel:
			#self.color_list_model.remove(sel)
			self.remove(sel)
	def on_color_set(self, cell, path, color):
		#print ls[path][0]
		#self.color_list_model[path][0] = color
		self[path][0] = color
		#print color
		#print ls[path][0]
	def on_edit(self, cell, path, t):
		#self.color_list_model[path][1] = int(t)
		self[path][1] = int(t)
	def toggled_callback(self, cell, path, model=None, col_num=0):
		iter = model.get_iter(path)
		model[iter][2] = not cell.get_active()

def test():
	p = periodictable()
#test()