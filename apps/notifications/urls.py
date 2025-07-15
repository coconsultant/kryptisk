from django.urls import path

from .views import (
    mark_all_notifications_as_read_view,
    mark_notification_as_read_view,
    notification_count_view,
    notification_list_view,
)

app_name = 'notifications'

urlpatterns = [
    path('count/', notification_count_view, name='count'),
    path('list/', notification_list_view, name='list'),
    path('mark-as-read/<int:notification_id>/', mark_notification_as_read_view, name='mark_as_read'),
    path('mark-all-as-read/', mark_all_notifications_as_read_view, name='mark_all_as_read'),
]
