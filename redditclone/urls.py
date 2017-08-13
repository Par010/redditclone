
from django.conf.urls import url, include
from django.contrib import admin
import accounts.views
import posts.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^posts/', include('posts.urls')),
    url(r'^$', posts.views.home, name="home"),

]
