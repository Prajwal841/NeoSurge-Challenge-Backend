from django.http import JsonResponse

def login_required(view_func):
    def wrapped_view(request, *args, **kwargs):
        if request.user is None:
            return JsonResponse({'error': 'Authentication required'}, status=403)
        return view_func(request, *args, **kwargs)
    return wrapped_view
