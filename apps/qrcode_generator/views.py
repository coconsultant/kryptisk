from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import qrcode
from io import BytesIO


def generate_qr(request):
    data = request.GET.get('data', '')
    
    if not data:
        return HttpResponse('Missing data parameter', status=400)
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    
    buffer = BytesIO()
    img.save(buffer, format='PNG')
    buffer.seek(0)
    
    return HttpResponse(buffer.getvalue(), content_type='image/png')
