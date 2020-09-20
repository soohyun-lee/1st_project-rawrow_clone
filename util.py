import jwt
import json

from user.models import User
from django.http import JsonResponse

class LoginConfirm:

    def wrapper(self, request, *args, **kwargs):
        token = request.headers.get("Authorization", None)
        try:
            if token:
                token_payload = jwt.decode(token, SECRET_KEY, algorithm="HS256")
                user          = User.objects.get(name=token_payload['name'])
                request.user  = user


        return JsonResponse({'message':'NEED_LOGIN'},status=401)
        
        except jwt.ExpiredSignatureError:
            return JsonResponse({'message':'EXPIRED_TOKEN'}, status=401)
        
        except jwt.DecodeError:
            return JsonResponse({'message':'INVALID_USER'}, status=401)

        except User.DoesNotExist:
            return JsonResponse({'message':'INVALID_USER'}, status=401)
                
                return func(self,request, *args, **kwargs)

        return wrapper