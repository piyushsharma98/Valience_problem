from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'myProject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'myProject.views.index'),
    url(r'^admin/', include(admin.site.urls)),
]
