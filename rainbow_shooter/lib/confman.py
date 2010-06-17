#!/usr/bin/python
# -*- coding: utf-8 -*-
from os import environ
from os.path import join
from os.path import exists
from configParserConf import pcm

""" Configuration manager that (will) support several backends."""
class confmanager():
	def loadconf(self):
		#self.installed = int(cm.get_key("installation", "installed")
		self.pd_default_timer = int(self.cm.get_key("timer", "pd_default_timer"))
		self.pd_min_range = int(self.cm.get_key("timer", "pd_min_range"))
		self.pd_max_range = int(self.cm.get_key("timer", "pd_max_range"))
		self.pd_libpath = str(self.cm.get_key("library", "pd_libpath"))
	def __init__ (self, DEBUG=False):
		self.DEBUG = DEBUG
		confName = "rainbow_shooter.ini"

		self.confman = join(environ.get("HOME"), ".rainbowshooter/", confName)
		#print(exists(self.confman))
		#print(self.confman)
		self.cm = pcm (self.confman)
		# the hardcoded path of the conf file (dev version)
		#self.confman = confName
		#self.nodes = {}

		self.installed = 0					# Whether the conf files are there
		self.pd_default_timer = 5			# Hardcoded for any case :D
		self.pd_min_range = 1				# Hardcoded for any case :D
		self.pd_max_range = 60				# Hardcoded for any case :D
		self.pd_libpath = ".colorchanger"	# Hardcoded for any case :D

		self.loadconf() # Fill the values from the conf
	def get_isInstalled(self):
		return self.pd_default_timer
	def get_default_timer(self):
		if (self.DEBUG): print("::Getting default timer, which is: %s. ::"%self.pd_default_timer)
		return self.pd_default_timer
	def get_min_range(self):
		if (self.DEBUG): print("::Getting minimum range, which is: %s. ::"%self.pd_min_range)
		return self.pd_min_range
	def get_max_range(self):
		if (self.DEBUG): print("::Getting maximum range, which is: %s. ::"%self.pd_max_range)
		return self.pd_max_range
	def get_libpath (self):
		return self.pd_libpath
	def set_isInstalled(self, value):
		self.pd_default_timer = value
	def set_default_timer(self, value):
		if (self.DEBUG): print("::writting default timer, which is: %s. ::"%value)
		self.pd_default_timer = value
		self.cm.set_key("timer", "pd_default_timer", value)
	def set_min_range(self, value):
		if (self.DEBUG): print("::writting minimum range, which is: %s. ::"%value)
		self.pd_min_range = value
		self.cm.set_key("timer", "pd_min_range", value)
	def set_max_range(self, value):
		if (self.DEBUG): print("::writting maximum range, which is: %s. ::"%value)
		self.pd_max_range  = value
		self.cm.set_key("timer", "pd_max_range", value)
	def set_libpath (self, value):
		self.pd_libpath  = value
		self.cm.set_key("library", "pd_libpath", value)
	def update_all(self, value1, value2, value3, value4):
		self.set_default_timer(int(value1))
		self.set_min_range(int(value2))
		self.set_max_range(int(value3))
		self.set_libpath(value4)
		self.saveConf()
	def saveConf(self):
		self.cm.save()
#def main ():
#	s = confmanager()
#if __name__ == "__main__": main()
