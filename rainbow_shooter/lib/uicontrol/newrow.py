# Pygtk modules
from gtk import Window, glade, Builder
from gtk import ENTRY_ICON_PRIMARY, ENTRY_ICON_SECONDARY
from gtk import main as Main, main_quit
# Python built-in stuff
from random import randint, randrange
class new_row_UIcontrol():
	def __init__ (self, pt_model, table, color_btn, time, timer_adjustment, configuration):
		self.pt_model = pt_model
		self.table = table
		self.color_btn = color_btn
		self.time = time
		self.timer_adjustment = timer_adjustment
		self.configuration = configuration
	def add_clicked_cb(self, widget):
		self.pt_model.append((self.color_btn.get_color(), self.time.get_value(),True))
		cmap = self.color_btn.get_colormap()
		self.color_btn.set_color(self.random_color(cmap))
	def random_color(self, map):
		red = randint(0, 65535)
		green = randint(0, 65535)
		blue = randint(0, 65535)
		return map.alloc_color(red, green, blue)
	def time_icon_press_cb(self, widget, icon, event):
		if icon == ENTRY_ICON_SECONDARY:
			self.timer_adjustment.set_value(self.configuration.get_default_timer())
		elif icon == ENTRY_ICON_PRIMARY:
			self.timer_adjustment.set_value(randrange(self.configuration.get_min_range(), self.configuration.get_max_range()))