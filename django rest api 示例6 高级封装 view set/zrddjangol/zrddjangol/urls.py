from django.conf.urls import url, include
from django.contrib import admin

from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^doc_u/', schema_view),
    url(r'^', include('o.urls', )),
    url(r'^api/', include('restapi.urls', namespace='res')),

]
