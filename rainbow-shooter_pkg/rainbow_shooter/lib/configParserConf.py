import ConfigParser
from sys import stdout
class pcm():
	def __init__(self, cpath):
		self.cpath = cpath
		self.config = ConfigParser.ConfigParser()
		#self.confpath = "colorchanger.ini"
		self.config.read(cpath)
	def get_key(self, category, key):
		return self.config.get(category, key)
	def set_key(self, category, key, value):
		self.config.set(category, key, value)
	def save(self):
		#self.config.write(stdout)
		self.confpathF = open(self.cpath, 'w+')
		self.config.write(self.confpathF)
def main():
	cm = pcm()
	print (cm.get_key("timer", "pd_default_timer"))
	cm.set_key("timer", "pd_default_timer", "6")
	print (cm.get_key("timer", "pd_default_timer"))
	cm.save()
#if __name__ == '__main__': main()