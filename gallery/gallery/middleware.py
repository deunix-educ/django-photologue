'''
Created on 3 avr. 2024

@author: denis
'''
import re
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.utils.deprecation import MiddlewareMixin
from django.utils.http import url_has_allowed_host_and_scheme


EXEMPT_URLS = [re.compile(settings.LOGIN_URL.lstrip('/'))]
if hasattr(settings, 'LOGIN_EXEMPT_URLS'):
    EXEMPT_URLS += [re.compile(url) for url in settings.LOGIN_EXEMPT_URLS]


class LoginRequiredMiddleware(MiddlewareMixin):

    def process_request(self, request):
        assert hasattr(request, 'user'), "The Login Required Middleware"
        if not request.user.is_authenticated:
            path = request.path_info.lstrip('/')
            if not any(m.match(path) for m in EXEMPT_URLS):
                redirect_to = settings.LOGIN_URL
                # 'next' variable to support redirection to attempted page after login
                if len(path) > 0 and url_has_allowed_host_and_scheme(
                    url=request.path_info, allowed_hosts=request.get_host()):
                    redirect_to = f"{settings.LOGIN_URL}?next={request.path_info}"

                return HttpResponseRedirect(redirect_to)


class QuotasMiddleware(MiddlewareMixin):

    html = f"""
<html>
    <head>
        <title>hmml error 423</title>
    </head>
    <body style="margin:6em auto; text-align:center;">
        <h1>Sorry you are blocked</h1>
        <h3 style="margin:4em;">Media quota of {settings.MEDIA_QUOTA:.3f} Go reached.</h3>
        <h5 style="margin:2em;">Please contact the site administrator.</h5>
    </body>
</html>
"""
    def process_request(self, request):
        root_directory = settings.BASE_DIR / 'media'
        size = sum(f.stat().st_size for f in root_directory.glob('**/*') if f.is_file())
        size = size/12024/1024/1024
        rate = size/settings.MEDIA_QUOTA*100
        if rate > 95 and rate <100:
            messages.error(request, f"Attention le quota proche: {rate:.3f}% de {size:.3f} Go. Supprimer des photos",  extra_tags='w3-text-orange')
        elif size > settings.MEDIA_QUOTA:
            return HttpResponse(self.html, status=423)
        return None


