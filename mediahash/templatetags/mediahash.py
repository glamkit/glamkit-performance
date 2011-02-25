import md5

from django import template
from django.conf import settings

MEDIAHASH_INACTIVE = getattr(settings, 'MEDIAHASH_INACTIVE', settings.DEBUG)
register = template.Library()

@register.simple_tag
def mediahash(name):
	return dohash(name)

def dohash(name):
	if MEDIAHASH_ACTIVE:
		m.update(name)
		h = m.hexdigest()
		number = int(h, 16) % settings.MEDIA_HASH_RANGE + 1
		return "%s/%s" % (settings.MEDIA_HASH_URL % number, name)
	else:
		return "%s/%s" % (settings.MEDIA_URL, name)
