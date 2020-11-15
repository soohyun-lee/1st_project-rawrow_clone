from user.models import User
from my_settings import SECRET_KEY, ALGORITHM
import jwt
import bcrypt
from django.http import JsonResponse

def login_decorator(func):
    def wrapper(self, request, *args, **kwargs):
        try:
            access_token = request.headers.get('Authorization', None)
            payload = jwt.decode(access_token, SECRET_KEY, algorithm=ALGORITHM) 
            user = User.objects.get(id=payload['userid'])      
            request.user = user.id
            print(access_token)                                         

        except jwt.exceptions.DecodeError:                                   
            return JsonResponse({'message' : 'INVALID_TOKEN'}, status=400)

        except User.DoesNotExist:                                         
            return JsonResponse({'message' : 'INVALID_USER'}, status=400)

        return func(self, request, *args, **kwargs)
        
    return wrapper
    print(access_token)                                         


#이게 받아온거 
# import jwt
# import json
# ​
# from django.http             import JsonResponse
# from django.core.exceptions  import ObjectDoesNotExist
# ​
# from .models                 import User
# from my_settings             import SECRET, ALGORITHM
# ​
# def is_user(func):
#     def wrapper(self, request, *args, **kwargs):
#         if "Authorization" not in request.headers:
#             return JsonResponse({'message':'INVALID_USER'}, status = 401)
# ​
#         token = request.headers.get('Authorization', None)
        
#         try:
#             payload      = jwt.decode(token, SECRET['secret'], algorithm = ALGORITHM)
#             user         = User.objects.get(id = payload['user_id'])
#             request.user = user
        
#         except jwt.DecodeError:
#             return JsonResponse({'message':'INVALID_TOKEN'}, status = 401) 
        
#         except User.DoesNotExist:
#             return JsonResponse({'message':'USER_NOT_EXIST'}, status = 401)
# ​
#         return func(self, request, *args, **kwargs)
#     return wrapper 





