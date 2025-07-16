from django.urls import path
from .views import generate_qr, vcard_qr_page, generate_vcard_qr_image

urlpatterns = [
    path('generate/', generate_qr, name='generate_qr'),
    path('vcard/', vcard_qr_page, name='vcard_qr_page'),
    path('vcard-image/<int:user_id>/', generate_vcard_qr_image, name='generate_vcard_qr_image'),
]
