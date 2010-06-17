from rainbow_shooter.colorplayer import colorplayer

class playerui():
	def __init__ (self, pt_model, resourceman):
		self.pt_model = pt_model
		self.resourceman = resourceman
	"""When clicked it calls the color player."""
	def play_clicked_cb(self, widget):
		noChecked = True
		# Checks whether there are colors inside.
		if self.pt_model.isModelEmpty():
			colors = []
			for c in self.pt_model:
				# When column 3 is checked
				if (c[2]):
					noChecked = False
					colors.append([c[0], c[1]])
				# Otherwise we set noChecked True, meaning there is no
				# checked row.
				elif noChecked:
					noChecked = True
			# When noChecked is False means that there is atleast one
			# row checked.
			# And than it calls the player.
			if not noChecked:
				p = colorplayer(colors, self.resourceman)
			else:
				print(":: no checked ::")