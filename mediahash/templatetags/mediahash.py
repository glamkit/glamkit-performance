import md5

from django import template

register = template.Library()

@register.simple_tag
def mediahash(name):
	return dohash(name)

def dohash(name):
	from django.conf import settings
	if settings.DEBUG:
		return "%s/%s" % (settings.MEDIA_URL, name)
	else:
		try:
			from django.conf import settings
		except ImportError:
			return ''
		m = md5.new()
		m.update(name)
		h = m.hexdigest()
		number = int(h, 16) % settings.MEDIA_HASH_RANGE + 1
		return "%s/%s" % (settings.MEDIA_HASH_URL % number, name)
