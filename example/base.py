import tornado.web
import sys
sys.path.append("..")
import session


class BaseHandler(tornado.web.RequestHandler):
	def __init__(self, *argc, **argkw):
		super(BaseHandler, self).__init__(*argc, **argkw)
		self.session = session.Session(self.application.session_manager, self)

	def get_current_user(self):
		return self.session.get("user_name")
