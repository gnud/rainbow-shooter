import gtk
import gtk.glade
import gobject
from types import StringType
from slideshow import slideshow
#from rainbow_shooter.lib.resman import resourceman
class colorplayer (gtk.Window):
	def fix_color(self, color):
		if type(color) == StringType:
			return gtk.gdk.color_parse(color)
		else:
			return color
	# Removes every gobject timer
	def stop_timers(self):
		for t in self.timer_ids:
			gobject.source_remove(t)
	def playcolor(self, param):
		s = slideshow(self.fix_color(param[0][0]),
			#param[0][1], self, self.playNextColor, self.whereColor, len(self.colors), self.debug_lb, self.debug_lb1, True)
			param[0][1], self, self.playNextColor, self.whereColor, len(self.colors), self.debug_lb, self.debug_lb1)
		# Appends the id of every new timer in a list
		self.timer_ids.append(gobject.timeout_add(1000, s.update_clock))
	def playNextColor(self):
		self.whereColor +=1
		self.playcolor([self.colors[self.whereColor], self.time])
	def __init__(self, colors, resman):
		super(colorplayer, self).__init__()
		self.timer_ids =[]
		self.end = False
		#self.gladefile = "share/colorplayer_win.xml"
		self.gladefile = resman.get_xml_file_path("colorplayer_win")


		dic = {
			"destroy"	:	self.destroy,
			"stop_show" : self.stop_show,
			"end_show_press" : self.end_show_press
		}

		builder = gtk.Builder()
		builder.add_from_file(self.gladefile)
		builder.connect_signals(dic)
		self.background = builder.get_object("background")
		self.debug_box = builder.get_object("debug_box")
		self.debug_lb = builder.get_object("debug_lb")
		self.debug_lb1 = builder.get_object("debug_lb1")
		self.label = builder.get_object("label")
		self.whereColor = 0
		self.colors = colors

		self.time = 5
		self.playcolor([self.colors[self.whereColor], self.time, self.whereColor, len(self.colors)])

		self.win = builder.get_object("window1")
		self.win.show_all()
		self.win.fullscreen()
	def end_show(self):
		self.background.modify_bg(gtk.STATE_NORMAL, gtk.gdk.color_parse("black"))
		self.label.modify_fg(gtk.STATE_NORMAL, gtk.gdk.color_parse("white"))
		self.label.set_text("End show")
		self.end = True
	def stop_player(self):
		self.stop_timers()
		self.win.destroy()
	def stop_show(self, widget, event):
		#print(event.keyval)
		# if the end show is raised let any key stop the player
		if self.end:
			if event.keyval:
				self.stop_player()
		# else if the user wants to stop it early, use the key from
		# the settings.
		elif event.keyval == 65307:
			self.stop_player()

	def end_show_press(self, widget, event):
		print(event.keyval)
		if event.keyval == 65307:
			self.stop_player()
	def destroy(self, widget):
		self.stop_player()
def test ():
	colors = [["red", 5], ["blue", 3], ["green", 4]]
	p = colorplayer(colors)

	gtk.main()
#test()
