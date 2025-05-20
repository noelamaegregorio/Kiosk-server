from django.shortcuts import render

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .print import generate_and_print_qr

@csrf_exempt
def print_qr_code(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            value = data.get('value')
            if not value:
                return JsonResponse({'error': 'Missing "value"'}, status=400)
            
            generate_and_print_qr(value)
            return JsonResponse({'status': 'QR code generated and sent to printer'})
        
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)

