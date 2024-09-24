#
# encoding: utf-8
from django.conf import settings
from django.contrib.sites.models import Site

def params(request):
    site = Site.objects.filter(id=settings.SITE_ID).first()

    return {
        'APP_TITLE': settings.APP_TITLE,
        'APP_SUB_TITLE': settings.APP_SUB_TITLE,
        'SITE_NAME': f'{site.name}',
        'SITE_DOMAIN': f'{site.domain}',
    }
