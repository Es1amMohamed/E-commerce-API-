from django.http import JsonResponse



def error_view(request, exception):
    message = {"message": 'Path Not Found'}
    response = JsonResponse({"error": message})
    response.status_code = 404
    return response



def error_view2(request):
    message = {"message": 'Internal Server Error'}
    response = JsonResponse({"error": message})
    response.status_code = 500
    return response