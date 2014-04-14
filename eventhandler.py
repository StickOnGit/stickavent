class Satellite(dict):
	"""Coordinates the message passing between
	ListenObj instances.
	
	At present the goal is to never have to think about
	this, so it is basically setup to durdle in the background.
	"""
	def __init__(self, *args, **kwargs):
		super(Satellite, self).__init__(*args, **kwargs)
		
	def __setitem__(self, k, v):
		if k in self:
			self[k].append(v)
		else:
			super(Satellite, self).__setitem__(k, [v])
			
	def __repr__(self):
		msgs = ""
		for k, v in self.iteritems():
			msgs += "\n(Message: {}, Listeners: {})\n".format(k, len(v))
		return "Satellite({})".format(msgs)
	
	def _tell(self, msg, *args, **kwargs):
		if msg in self:
			for listener in self[msg]:
				listener._got_msg(msg, *args, **kwargs)
				
	def _add_listener(self, listener, msg):
		if msg in self:
			self[msg].append(listener)
		else:
			self[msg] = listener
	
	def _rm_listener(self, listener, msg):
		if msg in self:
			if listener in self[msg]:
				self[msg].remove(listener)
				
_handler = Satellite()
