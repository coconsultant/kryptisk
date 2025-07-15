from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST

from .models import Notification


@login_required
def notification_count_view(request):
    count = Notification.objects.filter(user=request.user, is_read=False).count()
    return JsonResponse({'count': count})


@login_required
def notification_list_view(request):
    notifications = Notification.objects.filter(user=request.user, is_read=False)
    data = [{
        'id': n.id,
        'message': n.message,
        'created_at': n.created_at.strftime('%b %d, %Y, %I:%M %p')
    } for n in notifications]
    return JsonResponse({'notifications': data})


@login_required
@require_POST
def mark_notification_as_read_view(request, notification_id):
    try:
        notification = Notification.objects.get(id=notification_id, user=request.user)
        notification.is_read = True
        notification.save()
        return JsonResponse({'status': 'success'})
    except Notification.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Notification not found'}, status=404)


@login_required
@require_POST
def mark_all_notifications_as_read_view(request):
    Notification.objects.filter(user=request.user, is_read=False).update(is_read=True)
    return JsonResponse({'status': 'success'})
