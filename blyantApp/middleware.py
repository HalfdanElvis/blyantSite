class MobileDetectionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user_agent = request.META.get('HTTP_USER_AGENT', '').lower()
        request.is_mobile = "mobile" in user_agent
        return self.get_response(request)
