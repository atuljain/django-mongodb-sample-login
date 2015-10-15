from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from router import mapping
from txauth import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
urlpatterns = patterns('',
    url(r'^$',views.MAIN,name="Home"),
    url(r'^login/$',views.login_a,name='Login'),
    url(r'^home/$',views.home,name='Home'),
    # url(r'^admin/', include(admin.site.urls)),
)
