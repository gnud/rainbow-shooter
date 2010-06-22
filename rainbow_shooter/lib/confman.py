#!/usr/bin/python
# -*- coding: utf-8 -*-
from os import environ
from os import getenv
from os.path import expanduser
from os.path import join
from os.path import exists
from configParserConf import pcm

""" Configuration manager that (will) support several backends."""
class confmanager():
	def convertType(self, value, ttype):
		import __builtin__
		print("""
convertType:
=================================
ttype is %s, and it of type %s.
value is %s, and it of type %s.
---------------------------------""" %(ttype[0], type(ttype), value, type(value)))
		value = getattr(__builtin__, ttype)(value)
		print (value)
		return value
	def loadconf(self, loadwhat):
		print(loadwhat)
		confvalues=[["timer", "pd_default_timer", "int"], ["timer", "pd_min_range", "int"],
		["timer", "pd_max_range", "int"], ["library", "pd_libpath", "str"], ]

		for cval in confvalues:
			try:
				if cval[1] in loadwhat:
					#print(type(cval[1]))
					#print((cval[1]))
					#print(type(cval[2]))
					#print((cval))
					print("""
One config type:
=================================
Cval[0] is %s, and it of type %s.
Cval[1] is %s, and it of type %s.
Cval[2] is %s, and it of type %s.
---------------------------------
					""" %(cval[0], type(cval[0]), cval[1], type(cval[1]), cval[2], type(cval[2]))
					)
					keyvalue = self.cm.get_key(cval[0], cval[1])
					print("""KeyValue is %s, and it's of type %s.""" %(keyvalue, type(keyvalue)))
					value = self.convertType(keyvalue, cval[2])
					print("""Value is %s, and it's of type %s.""" %(value, type(value)))
					if (self.DEBUG): print("::Setting values %s from %s, %s is of type: %s. ::"%(value, cval[0], cval[1], type(value) ) )
					# set key in here with the value of the get from the conf
					setattr (self, cval[1], value)


			except KeyError: print("Key: %s doesn't exist'"%cval[1])

		#self.installed = int(cm.get_key("installation", "installed")
		#self.pd_default_timer = int(self.cm.get_key("timer", "pd_default_timer"))
		#self.pd_min_range = int(self.cm.get_key("timer", "pd_min_range"))
		#self.pd_max_range = int(self.cm.get_key("timer", "pd_max_range"))
		#self.pd_libpath = str(self.cm.get_key("library", "pd_libpath"))
	def __init__ (self, DEBUG=False):
		self.DEBUG = DEBUG
		confName = "rainbow_shooter.ini"
		confNameDIR = ".rainbowshooter"
		confNamePATH = ".rainbowshooter"

		self.confman = join(expanduser("~"), ".rainbowshooter", confName)
		#self.confman = join(environ.get("HOME"), ".rainbowshooter/", confName)
		#print(exists(self.confman))
		#print(self.confman)
		self.cm = pcm (self.confman)
		# the hardcoded path of the conf file (dev version)
		#self.confman = confName

		self.installed = 0					# Whether the conf files are there
		self.pd_default_timer = 5			# Hardcoded for any case :D
		self.pd_min_range = 1				# Hardcoded for any case :D
		self.pd_max_range = 50				# Hardcoded for any case :D
		self.pd_libpath = ".colorchanger"	# Hardcoded for any case :D


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
	def set_from_args (self, value_dic):
		argsnloaded=True
		argsnloadedD = []
		try:
			self.set_default_timer(int(value_dic["pd_default_timer"]))
		except KeyError: argsnloadedD["pd_default_timer"]
		try:
			self.set_min_range(int(value_dic["pd_min_range"]))
		except KeyError: argsnloadedD.append("pd_min_range")
		try:
			self.set_max_range(int(value_dic["pd_max_range"]))
		except KeyError: argsnloadedD.append("pd_max_range")
		try:
			self.set_libpath(str(value_dic["pd_set_libpath"]))
		except KeyError: argsnloadedD.append("pd_set_libpath")


		#if not argsnloaded: self.loadconf() # Fill the values from the conf
		#else: print("yeaaa")
		self.loadconf(argsnloadedD)

	def update_all(self, set_default_timer, set_min_range, set_max_range, set_libpath):
		self.set_default_timer(int(set_default_timer))
		self.set_min_range(int(set_min_range))
		self.set_max_range(int(set_max_range))
		self.set_libpath(set_libpath)
		self.saveConf()
	def saveConf(self):
		self.cm.save()
#def main ():
#	s = confmanager()
#if __name__ == "__main__": main()
