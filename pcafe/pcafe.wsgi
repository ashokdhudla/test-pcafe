import os
import sys
sys.path = ['/var/www/pcafe'] + sys.path
print sys.path
os.environ['DJANGO_SETTINGS_MODULE'] = 'pcafe.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()


