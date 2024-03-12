import hashlib
from django.contrib import messages


class NotificationAndSignatureMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if 'notifications' in request.session:
            for level, message in request.session['notifications']:
                messages.add_message(request, level, message)
            del request.session['notifications']

        data_to_sign = "some_data_to_sign"
        signature = hashlib.sha256(data_to_sign.encode()).hexdigest()
        request.signature = signature

        response = self.get_response(request)
        return response