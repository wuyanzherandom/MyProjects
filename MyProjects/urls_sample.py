"""myprojects URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.views.generic.base import RedirectView

from . import settings
from projects.animenet import admin_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^report/admin-sql/', admin_views.AdminSQL.as_view()),
]

if settings.SYSTEM_IS_DOWN:
    urlpatterns += [
        #url(r'^/*$', views.SystemUpgradeView.as_view()),
        url(r'^.*$', RedirectView.as_view(url="/")),
    ]

else:
    if 'projects.animenet' in settings.INSTALLED_APPS:
        urlpatterns += [
            url(r'^', include('projects.animenet.urls'))
        ]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    #url(r'^error$', views.ErrorView.as_view()),
    #url(r'^.*$', RedirectView.as_view(url="/error")),
]
