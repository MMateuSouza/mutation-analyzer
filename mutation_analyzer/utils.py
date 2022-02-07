from django.http import JsonResponse

import json


def json_response(data, status, charset="utf-8"):
    return JsonResponse(data=data, status=status, charset=charset)


def json_serializer(body):
    return json.loads(body if body else b"{}")
