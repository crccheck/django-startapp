from django.conf.urls import include, url
from django.http import HttpResponse
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()


def favicon(request):
    """Hack to keep logs from filling with favicon.ico requests."""
    image_data = open("example_project/static/favicon.ico", "rb").read()
    return HttpResponse(image_data, mimetype="image/x-icon")


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^', include('{{ project_name }}.urls',
        namespace='{{ project_name }}', app_name='{{ project_name }}')),

    # HACK patterns
    url(r'^favicon.ico$', favicon),
    url(r'^robots.txt$', TemplateView.as_view(
        content_type='text/plain', template_name='robots.txt')),
]
