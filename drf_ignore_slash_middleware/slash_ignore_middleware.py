

class SlashIgnoreMiddleware(object):
	"""
	Removes trailing slash in path if any.
	"""
	def __init__(self, get_response):
		self.get_response = get_response

	def __call__(self, request):
		if request.path[-1] == '/':
			request.path = request.path_info = request.path[:-1]
		return self.get_response(request)