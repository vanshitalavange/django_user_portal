from django.http import JsonResponse
from django.contrib.auth.hashers import check_password,make_password
from rest_framework.views import APIView
from .models import User
from .constants import errors
from .serializers import UserSerializer,LoginSerializer

class LoginView(APIView):

    def post(self,request):
        
        try:

            serializer = LoginSerializer(data=request.data)
           
            if serializer.is_valid():

                found_user = User.objects.filter(email= request.data.get('email')).first()

                if found_user:
                    
                    if check_password(request.data.get('password'),found_user.password):

                        response = {
                            "success":True,
                            "message":"login successful",
                            "response_code":200,
                            "data":{
                                "user":{
                                    "id":found_user.id,
                                    "username":found_user.username
                                }
                            }
                        }
                        return JsonResponse(response)
                    
                    else:

                        response = {
                            "success":False,
                            "message":errors.get('PASSWORD_INCORRECT')['message'],
                            "response_code":401,
                            "code": errors.get('PASSWORD_INCORRECT')['code']
                        }

                        return JsonResponse(response)
                
                response = {
                    "success":False,
                    "message":errors.get('EMAIL_DOES_NOT_EXIST')['message'],
                    "response_code":401,
                    "code": errors.get('EMAIL_DOES_NOT_EXIST')['code']
                }
                
                return JsonResponse(response)
            
            else:
                response = {
                    "success":False,
                    "response_code":401,
                    "code": '',
                    "message": '',
                }
                code = serializer.errors.get('code')
                print(serializer.errors)
                if code:
                    response['code'] = serializer.errors['code'][0]
                    response['message'] = serializer.errors['message'][0]
                else:
                    error_code = list(serializer.errors.values())[0][0].code
                    error_msg = list(serializer.errors.values())[0][0]

                    if error_code == 'required':
                        response['code'] = errors['MISSING_FIELD']['code']
                        response['message'] = errors['MISSING_FIELD']['message']

            
                    else:
                        response['code'] = errors['MODEL_VALIDATION_ERROR']['code']
                        response['message'] = error_msg
                    
    
                return JsonResponse(response)
            
        except Exception as e:
            return JsonResponse({"exception":e})



class RegistrationView(APIView):

    def post(self,request):

        try:    

            serializer = UserSerializer(data=request.data)

            if serializer.is_valid():
                hashed_pass = make_password(serializer.validated_data['password'])
                serializer.validated_data['password'] = hashed_pass
                serializer.save()
                response = {
                    "success":True,
                    "message":"user registered successfully",
                    "response_code":201,
                    "data": {
                        "user":{
                            "id":serializer.data.get('id'),
                            "username":serializer.data.get('username')
                        }
                    }
                }
                return JsonResponse(response)
            else:
                
                response = {
                    "success":False,
                    "response_code":401,
                    "code": '',
                    "message": '',
                }

                code = serializer.errors.get('code')
                print(serializer.errors)
                if code:
                    response['code'] = serializer.errors['code'][0]
                    response['message'] = serializer.errors['message'][0]
                else:
                    error_code = list(serializer.errors.values())[0][0].code
                    error_msg = list(serializer.errors.values())[0][0]

                    if error_code == 'required':
                        response['code'] = errors['MISSING_FIELD']['code']
                        response['message'] = errors['MISSING_FIELD']['message']

                    elif error_code == 'max_length':
                        response['code'] = errors['MODEL_VALIDATION_ERROR']['code']
                        response['message'] = "Must contain 10 digits only"

                    else:
                        response['code'] = errors['MODEL_VALIDATION_ERROR']['code']
                        response['message'] = error_msg
                    
    
                return JsonResponse(response)
        except Exception as e:
            return JsonResponse({"exception":str(e)})

