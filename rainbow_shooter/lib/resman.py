from os.path import splitext
from pkg_resources import resource_listdir, resource_filename
class resourceman():
	def __init__(self, reslocation):
		self.location = reslocation
		self.resources = resource_listdir(self.location, '')
		self.xml()
		self.videos()
		self.images()
	"""
	lists all the xml files in ui.
	"""
	def xml(self):
		xml_res = resource_listdir("rainbow_shooter.share.ui", '')
		self.xml_dict_res = dict([(splitext(r)[0],resource_filename("rainbow_shooter.share.ui", r) ) for r in xml_res if "xml" in r])
	"""
	Returns an xml file from ui.
	"""
	def get_xml_file_path(self, resource):
		return self.xml_dict_res[resource]
	"""
	For future use ...
	"""
	def sounds(self):pass
	"""
	For future use ...
	"""
	def videos(self):pass
	"""
	Supported images: SVG and PNG.
	Why ? - Because I like it :D.
	"""
	def images(self):
		img_res = resource_listdir("rainbow_shooter.share.icons", '')
		self.images_dict_res = dict([(r,resource_filename("rainbow_shooter.share.icons", r) ) for r in img_res if "png" in r or "svg" in r ])
	"""
	Returns an image file from icons.
	"""
	def get_images_file_path(self, resource, ext):
		return self.images_dict_res[resource+"."+ext]