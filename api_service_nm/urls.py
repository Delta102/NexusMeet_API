"""
URL configuration for api_service_nm project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from api.views import *
from api_events.views import *
from api_entrys.views import *
from django.conf import settings
from django.conf.urls.static import static

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls)
    ,
    # PATH PARA EVENTS
    path('events/', get_all_events, name='event-list'),
    path('event/<int:event_id>', get_event_by_id, name='event'),
    path('events/create/', create_event, name='create-event'),
    path('update-events/', update_event, name='update-event'),
    path('delete-events/<int:event_id>', delete_event, name='delete-events'),
    path('events-by-user/<int:user_id>', get_all_events_by_user, name='events-by-user'),
    
    # PATH PARA ENTRYS
    path('entrys/create/', create_entry, name='create-entry'),
    path('qrvalue/', qr_scanned, name='qr_value'),
    path('get-assitants/<int:event_id>', get_assistant, name='get_assistant'),
    path('entrys/get-entrys-by-user/<int:user_id>', get_entrys_by_user, name = 'entrys-by-user'),
    path('get-assists-by-user/<int:user_id>', get_assists, name = 'assists-by-user'),
    
    # PATH PARA USERS
    path('create-user/', create_user_promotor, name='create_user_promotor'),
    path('update-user/<int:user_id>', update_user, name='update_user'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    #path('user/aff-attenee/<int:event_id>/<int:user_id>/', add_attendee(), name='add-attendee'),
    path('login/', login_view, name='login_view'),
    path('logout/', logout_view, name='logout_view'),
    path('get-current-user/', get_current_user, name='get_current_user'),
    path('get-user/<int:user_id>', get_user_by_id, name='get_user_by_id'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
