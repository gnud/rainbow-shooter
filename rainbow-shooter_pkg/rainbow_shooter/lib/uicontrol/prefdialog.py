class pref_UIcontrol():
	def __init__(self, prefference_dialog, configuration, default_adjustment, minimum_adjustment, maximum_adjustment, update_defaults):
		self.prefference_dialog = prefference_dialog
		self.configuration = configuration
		self.default_adjustment = default_adjustment
		self.minimum_adjustment = minimum_adjustment
		self.maximum_adjustment = maximum_adjustment
		self.update_defaults = update_defaults
	def options_clicked_cb(self, widget):
		self.prefference_dialog.show()
	def pd_ok_clicked_cb(self, widget):
		self.configuration.update_all(self.default_adjustment.get_value(), self.minimum_adjustment.get_value(), self.maximum_adjustment.get_value(), ".colorchange")
		self.update_defaults()
		self.prefference_dialog.hide()
	def pd_cancel_clicked_cb(self, widget):
		self.prefference_dialog.hide()
	def cancel_clicked_cb(self, widget):
		self.destroy(None)