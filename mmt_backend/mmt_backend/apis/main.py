from rest_framework.decorators import api_view
import json
from models.user import User
from django.http import JsonResponse
from copy import deepcopy


# @api_view(['POST'])
@api_view(['POST', 'OPTIONS'])
def login_user(request):
    return_response = {'success': True, 'error': ""}
    status_code = 200
    try:
        body = request.data
        temp = User.objects.filter(email=body['email'], password=body['password']).values("name", "email", "gender")
        if temp:
            return_response['data'] = deepcopy(temp[0])
        else:
            return_response['success'] = False
            return_response['error'] = "User Not Exist"
    except Exception as ex:
        return_response['success'] = False
        return_response["error"] = str(ex)

    print(return_response)
    response = JsonResponse(return_response, status=status_code)

#     return JsonResponse(return_response,header={'Access-Control-Allow-Origin' : 'http://localhost:3000',
#                                                   'Access-Control-Allow-Credentials' : 'true',
# 'Access-Control-Allow-Methods' : 'GET, POST, OPTIONS',
# 'Access-Control-Allow-Headers' : 'Origin, Content-Type, Accept'} ,status=status_code)
    response['Access-Control-Allow-Origin'] = 'http://localhost:3000'
    response['Access-Control-Allow-Headers'] = 'Origin, Content-Type, Accept'
    return response

@api_view(['POST', 'OPTIONS'])
def register_user(request):
    return_response = {"success": True, "message": "User Successfully Registered"}
    try:
        body = json.loads(request.body)
        temp = User.objects.filter(email=body['email']).values("name", "email", "gender")
        if temp:
            return_response = {"success": False, "message": "Email already exists"}
        else:
            temp = User.objects.create(**body)
            temp.save()
    except Exception as ex:
        return_response = {"success": True, "message": "Error In User Registeration"}
    response =  JsonResponse(return_response, status=200)
    response['Access-Control-Allow-Origin'] = 'http://localhost:3000'
    response['Access-Control-Allow-Headers'] = 'Origin, Content-Type, Accept'

    return response