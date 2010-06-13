import gtk
import time
import signal
import random
gtk.gdk.threads_init()
class slideshow:
#	def random_color(self):
#		map = gtk.Label().get_colormap()
#		red = random.randint(0, 65535)
#		green = random.randint(0, 65535)
#		blue = random.randint(0, 65535)
#		return map.alloc_color(red, green, blue)
	def __init__(self, color, time, parent, next, total, total_items, debug_lb, debug_lb1, DEBUG=False):
		#print("Work Work")
		self.timer_id = None
		self.seconds = 0
		self.color = color
		self.time = time
		self.total = total
		self.total_items = total_items
		self.debug_lb = debug_lb
		self.debug_lb1 = debug_lb1
		self.DEBUG = DEBUG
		if (self.DEBUG): print(self.total_items)
		#self.label = label
		self.parent = parent
		if (not self.DEBUG):
			self.parent.debug_box.hide()
		self.next = next
		self.isComplete = False
	def update_clock(self):
		#print("working")
		#self.background_chg.modify_bg(gtk.STATE_NORMAL, self.color)
		#self.parent.background.modify_bg(gtk.STATE_PRELIGHT, self.color)
		self.parent.background.modify_bg(gtk.STATE_NORMAL, self.color)
		if self.seconds < self.time:
			self.seconds = self.seconds + 1
			if (self.DEBUG):
				print (self.seconds, self.time)
				self.debug_lb.set_text(str(self.seconds) +":" + str(self.time))
		else:
			if self.total < self.total_items-1:
				if (self.DEBUG):
					till = "%s : %s" %(self.total+1, self.total_items-1)
					print(till)
					self.debug_lb1.set_text(till)
				self.next()
			else:
				self.parent.end_show()
			return False
		return True # run again in one second