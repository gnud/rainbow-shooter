# -*- coding: UTF-8 -*-

# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
#
# Authors: Quinn Storm (quinn@beryl-project.org)
#          Patrick Niklaus (marex@opencompositing.org)
#          Guillaume Seguin (guillaume@segu.in)
#          Christopher Williams (christopherw@verizon.net)
# Copyright (C) 2007 Quinn Storm

import gobject, gtk, cairo

class CellRendererColor(gtk.GenericCellRenderer):

	__gsignals__ = {
		'color-set': (gobject.SIGNAL_RUN_FIRST, gobject.TYPE_NONE,
			(gobject.TYPE_STRING,gtk.gdk.Color))
	}

	__gproperties__ = {
		'color': (gtk.gdk.Color,
				'color',
				'The color',
				gobject.PARAM_READWRITE)
	}


	_color = gtk.gdk.Color()

	def __init__(self):
		gtk.GenericCellRenderer.__init__(self)
		self.set_property('mode',gtk.CELL_RENDERER_MODE_ACTIVATABLE)

	def do_set_property(self, property, value):
		if property.name == 'color':
			self._color = value

	def do_get_property(self, property):
		if property.name == 'color':
			return self._color

	def on_get_size(self, widget, cell_area):
		xpad = self.get_property('xpad')
		ypad = self.get_property('ypad')
		width = xpad + 20
		height = ypad + 20
		xoffset = xpad
		yoffset = ypad

		if cell_area:
			xoffset += cell_area.x
			yoffset += cell_area.y

		return (xoffset, yoffset, width, height)

	def on_render(self, window, widget, background_area, cell_area, expose_area, flags):
		cr = window.cairo_create()

		cr.rectangle(cell_area.x, cell_area.y, cell_area.width, cell_area.height)
		cr.clip_preserve()

		cr.set_source_color(self._color)
		cr.fill()
		#print self._color

	def do_activate(self, event, widget, path, background_area, cell_area, flags):
		dialog = gtk.ColorSelectionDialog('Select color')
		response = dialog.run()
		if response == gtk.RESPONSE_OK:
			color = dialog.get_color_selection().get_current_color()
			dialog.hide()
			self.emit('color-set', path, color)
		elif response == gtk.RESPONSE_CANCEL:
			print ("Get out of my dialog :D.")
			dialog.hide()