from dj_static import Cling

from .base import *

application = Cling(get_wsgi_application())