from django.http import HttpResponse, JsonResponse


def hello_world_txt(request):
    if request.method == 'GET':
        return HttpResponse("Hello World", content_type="text/plain")


def hello_world_json(request):
    response = {"message": "Hello World"}
    if request.method == 'GET':
        return JsonResponse(response, content_type="application/json")
