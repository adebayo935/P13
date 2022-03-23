from django.contrib import admin
from django.urls import path

from lettings import views as let
from profiles import views as pro
from . import views


def trigger_error(request):
    division_by_zero = 1 / 0
    print(division_by_zero)


urlpatterns = [
    path('', views.index, name='index'),
    path('lettings/', let.index, name='lettings_index'),
    path('lettings/<int:letting_id>/', let.letting, name='letting'),
    path('profiles/', pro.index, name='profiles_index'),
    path('profiles/<str:username>/', pro.profile, name='profile'),
    path('admin/', admin.site.urls),
    path('sentry-debug/', trigger_error),
]
