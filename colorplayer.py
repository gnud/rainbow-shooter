#import threading
#import thread, time
import gtk
import gtk.glade
#import time
import gobject
from types import StringType
from slideshow import slideshow
#from generatortask import GeneratorTask

class colorplayer (gtk.Window):
	def fix_color(self, color):
		#print (type(color))
		#print("%s==%s"%(type(color), type(gtk.gdk.Color())))
		#if type(color) == "<type 'gtk.gdk.Color'>":
		if type(color) == StringType:
			return gtk.gdk.color_parse(color)
		else:
			return color
	def playcolor(self, param):
		s = slideshow(self.fix_color(param[0][0]),
		param[0][1], self, self.playNextColor, self.whereColor, len(self.colors), self.debug_lb, self.debug_lb1, True)
		timer_id = gobject.timeout_add(1000, s.update_clock)

	def playNextColor(self):
		self.whereColor +=1
		#self.playcolor([self.colors[self.whereColor], self.time, self.whereColor, self.colors])
		self.playcolor([self.colors[self.whereColor], self.time])
	def __init__(self, colors):
		super(colorplayer, self).__init__()
		self.gladefile = "colorplayer_win.xml"
		dic = {
			"destroy"			: self.destroy
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
		#self.colors = ["red", "blue", "green"]
		self.colors = colors

		self.time = 5
		self.playcolor([self.colors[self.whereColor], self.time, self.whereColor, len(self.colors)])

		self = builder.get_object("window1")
		self.show_all()
		self.fullscreen()
	def end_show(self):
		self.background.modify_bg(gtk.STATE_NORMAL, gtk.gdk.color_parse("black"))
		#self.parent.background1.modify_bg(gtk.STATE_NORMAL, gtk.gdk.color_parse("black"))
		#self.parent.background.modify_bg(gtk.STATE_PRELIGHT, gtk.gdk.color_parse("black"))
		self.label.modify_fg(gtk.STATE_NORMAL, gtk.gdk.color_parse("white"))
		#self.parent.background.modify_fg(gtk.STATE_ACTIVE, gtk.gdk.color_parse("black"))
		#self.background_chg.modify_bg(gtk.STATE_ACTIVE, gtk.gdk.color_parse("black"))
		#print(dir(self.parent.p))
		self.label.set_text("End show")
	def destroy(self, widget):
		self.hide()
def main ():
	colors = [["red", 5], ["blue", 3], ["green", 4]]
	p = colorplayer(colors)

	gtk.gdk.threads_enter()
	gtk.main()
	gtk.gdk.threads_leave()
#main()