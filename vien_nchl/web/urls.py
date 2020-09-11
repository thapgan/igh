from django.conf.urls import url

from vien_nchl.web.views import HomePage

urlpatterns = [
    url(regex=r'^$', view=HomePage.as_view(), name='home_page')
]
