from django.http import JsonResponse
import json


def api_home(request, *args, **kwargs):
    body = request.body
    data = {}
    try:
        data = json.loads(body) # String json --> Python dict
    except:
        pass
    print(data)
    return JsonResponse({"messege": "Hi there"})
