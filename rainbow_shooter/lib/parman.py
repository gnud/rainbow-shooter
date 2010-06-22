from optparse import OptionParser
from os.path import isfile
from types import DictionaryType

class paramanager():
	def sepcsv(self, data):
		csv = dict([(i.split("=")[0], i.split("=")[1]) for i in data.split(",")])
		return csv
	def confsep(self, args):
		if len(args) == 1 and args == "n":
			return False
		else:
			print("is File %s:"%args)
			if isfile(args):
				print ("%s is file"%args)
				return args
			elif "," in args:
				#print(self.sepcsv(args))
				#return self.sepcsv(args)
				# Make a way to separate them into individual strings.
				#self.confman.update_all(self.sepcsv(args).values)
				dvalues = self.sepcsv(args)#.values()
				self.confman.set_from_args(dvalues)
		return False
	def isGetCVSOption(self, item, param):
		option = getattr(self.options, item)

		if option:
			if type(option) == DictionaryType:
				return option[param]
		else: return False
	def getConf(self, item, param):
		#eval (self.options.item[param])
		#print(self.args)
		#print(type(self.args))
		#a = getattr(self.options, item)
		#print("+%s+"% a[param])
		return getattr(self.options, item)[param]
	#def reparse(self, item):
	def confreparse(self, option, opt_str, value, parser):
		#setattr(self.options, item, self.parsemethods[item](getattr(self.options, item)))
		#print(dir(option))
		print(type(option))
		print((option))
		print((opt_str))
		print(type(value))

		parser.values.conf = self.parsemethods[opt_str](value)
	def qreparse(self, option, opt_str, value, parser):
		#setattr(self.options, item, self.parsemethods[item](getattr(self.options, item)))
		#print(dir(option))
		print(type(option))
		print((option))
		print((opt_str))
		print(type(value))
		parser.values.verbose = value

	def __init__(self, confman):
		self.confman = confman
		self.parsemethods = {"-c"or "--conf":self.confsep}
		self.argumentsdata = {}
		parser = OptionParser()
		chelp = """Use configuration file, possible options:
- n (using harcoded options)
-filename (loads the file instead of the users
configuration)
- CSV for each option,
e.g: "-c time=5,time_min"=1"""

		parser.add_option("-c", "--conf", dest="conf",
                  action="callback", callback=self.confreparse,
                  type="string", help=chelp)
		parser.add_option("-q", "--quiet",
						  dest="verbose", default=True,
						  help="don't print status messages to stdout", action="callback", callback=self.qreparse)
		parser.add_option("-v", "--version",
						  dest="version", default=True,
						  help="don't print status messages to stdout", action="callback", callback=self.qreparse)
		(self.options, self.args) = parser.parse_args()
		#if len(self.args) != 1:
		#	parser.error("wrong number of arguments")

		print(self.options)
			#for pm in self.parsemethods.keys():
			#	self.reparse(pm)
			#print(self.getConf("conf", "time_min"))
			#print(self.getConf("conf", "time_max"))

		#print(self.isGetCVSOption("conf", "time_max"))

#paramanager()