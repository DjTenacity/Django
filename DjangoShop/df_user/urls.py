from django.conf.urls import url
from . import views
urlpatterns = [
    # user/register/
    url(r'^register/$',views.register),


]
