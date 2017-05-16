from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'TableCharts.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^app/','app.views.index',name='index'),
    url(r'^charts/','app.views.charts',name='charts'),
    url(r'^accounts/',include('registration.backends.default.urls')),
    url(r'^admin/', include(admin.site.urls)),

]
