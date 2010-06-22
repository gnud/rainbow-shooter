#!/usr/bin/python
# -*- coding: utf-8 -*-

# Pygtk modules
from gtk import Window, glade, Builder
from gtk import ENTRY_ICON_PRIMARY, ENTRY_ICON_SECONDARY
from gtk import main as Main, main_quit
from gtk.gdk import pixbuf_new_from_file
# Python built-in stuff
#from random import randint, randrange
from os.path import splitext
# The rainbow_shooter modules
from lib.periodictable import periodictable
from lib.uicontrol.newrow import new_row_UIcontrol
from lib.uicontrol.prefdialog import pref_UIcontrol
from lib.uicontrol.playbackui import playerui
from lib.parman import paramanager
from lib.confman import confmanager
from lib.resman import resourceman

""" Program which plays colors in a color player."""
class rshooterGui (Window):
	"""Constructs each widget and loads any managers."""
	def start_builder(self):
		self.resourceman = resourceman("rainbow_shooter.share")
		#self.configuration = confmanager()
		self.configuration = confmanager(True) # Debug version
		self.parman = paramanager(self.configuration)


		#gladefile = "share/rainbow_shooter.xml"
		gladefile = self.resourceman.get_xml_file_path("rainbow_shooter")
		self.builder = Builder()
		self.builder.add_from_file(gladefile)

		# Add row dialog UI elements
		self.color_list = self.builder.get_object("color_lst")
		self.time = self.builder.get_object("time")
		self.color_btn = self.builder.get_object("color_btn")

		# Preference dialog objects
		self.preference_dialog = self.builder.get_object("preference_dialog")
		self.timer_adjustment = self.builder.get_object("timer_adjustment")
		self.default_adjustment = self.builder.get_object("default_adjustment")
		self.minimum_adjustment = self.builder.get_object("minimum_adjustment")
		self.maximum_adjustment = self.builder.get_object("maximum_adjustment")
		self.pd_libpath = self.builder.get_object("pd_libpath")
		# The table UI controls.
		self.pt_model = periodictable(self.color_list)
		# New row appender UI controls.
		newrowuictrl = new_row_UIcontrol(self.pt_model, self.color_list, self.color_btn, self.time, self.timer_adjustment, self.configuration)
		# Preference dialog UI controls.
		prefuictrl = pref_UIcontrol(self.preference_dialog, self.configuration,
		self.default_adjustment, self.minimum_adjustment, self.maximum_adjustment,
		self.update_defaults)
		# Playback dialog UI controls.
		playback_ui = playerui(self.pt_model, self.resourceman)
		# Builder signals
		dic = {
		"options_clicked_cb" : prefuictrl.options_clicked_cb,
		"cancel_clicked_cb" : prefuictrl.cancel_clicked_cb,
		"pd_ok_clicked_cb" : prefuictrl.pd_ok_clicked_cb,
		"pd_cancel_clicked_cb" : prefuictrl.pd_cancel_clicked_cb,
		"time_icon_press_cb" : newrowuictrl.time_icon_press_cb,
		"add_clicked_cb"	: newrowuictrl.add_clicked_cb,
		"remove_clicked_cb"	: self.pt_model.remove_clicked_cb,
		"play_clicked_cb"	: playback_ui.play_clicked_cb,
		"destroy"			: self.destroy
		}
		self.builder.connect_signals(dic)
		self.start_defaults()
	"""Based on the loaded configuration set the values in the UI widgets
	This action is made only once per start."""
	def start_defaults(self):
		self.default_adjustment.set_value(self.configuration.get_default_timer())
		print(type(self.configuration.get_min_range()))
		self.minimum_adjustment.set_value(self.configuration.get_min_range())
		self.maximum_adjustment.set_value(self.configuration.get_max_range())
		self.update_defaults()
	"""Sets new values in the UI widgets."""
	def update_defaults(self):
		self.timer_adjustment.set_value(self.default_adjustment.get_value())
		self.timer_adjustment.set_lower(self.minimum_adjustment.get_value())
		self.timer_adjustment.set_upper(self.maximum_adjustment.get_value())
	#"""Sets dynamically the default values of the widgets."""
#	def update_live_conf(self):
#		self.default_adjustment.set_value(self.configuration.get_default_timer())
#		self.minimum_adjustment.set_value(self.configuration.get_min_range())
#		self.maximum_adjustment.set_value(self.configuration.get_max_range())
	def __init__(self):
		super(rshooterGui, self).__init__()
		self.start_builder()
		# Preparing the artwork
		win_icon = pixbuf_new_from_file("/home/gnu_d/Desktop/active_programs/olivers_colors/rainbow-shooter/rainbow_shooter/share/icons/rainbow_shooter.svg")
		win_icon = pixbuf_new_from_file(self.resourceman.get_images_file_path("rainbow_shooter", "svg"))

		self = self.builder.get_object("window1")
		# Setting the window icon.
		self.set_icon(win_icon)

		self.show_all()
	"""Exits from the program."""
	def destroy(self, widget):
		main_quit()

def main ():
	p = rshooterGui()
	Main()
if __name__ == "__main__": main()
