from os.path import splitext
from pkg_resources import resource_listdir, resource_filename
class resourceman():
	def __init__(self, reslocation):
		self.location = reslocation
		self.resources = resource_listdir(self.location, '')
		self.xml()
		self.videos()
		self.images()

		#rld = resource_listdir('rainbow_shooter.share.ui', '')

	def xml(self):
		self.xml_dict_res = dict([(splitext(r)[0],resource_filename("rainbow_shooter.share.ui", r) ) for r in self.resources if "xml" in r])
		#print (self.xml_dict_res.keys())
		#print (self.xml_dict_res.values())
	def get_xml_file_path(self, resource):
		#print (self.xml_dict_res[resource])
		return self.xml_dict_res[resource]
	def sounds(self):pass
	def videos(self):pass
	def images(self):pass