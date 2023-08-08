from django.http import JsonResponse
from django.contrib.auth.hashers import check_password,make_password
from rest_framework.views import APIView
from .models import User
from .serializers import UserSerializer

class LoginView(APIView):

    def post(self,request):
        
        # checking if request has the required data
        if request.data.get('email') is None or request.data.get('email').strip() == "":
            return JsonResponse({"type":"failure","error":"email is required"})
        
        if request.data.get('password') is None or request.data.get('password').strip() == "":
            return JsonResponse({"type":"failure","error":"password is required"})

        try:
        # checking if the data is in the correct format 
            serializer = UserSerializer(data=request.data,partial=True)
            if serializer.is_valid():

                found_user = User.objects.filter(email= request.data.get('email')).first()

                if found_user:
                    
                    if check_password(request.data.get('password'),found_user.password):
                        return JsonResponse({"type":"success","message":"login successful"})
                    
                    return JsonResponse({"type":"failure","error":"password didn't match"})
                
                return JsonResponse({"type":"failure","error":"email doesn't exist"})
            
            return JsonResponse({"type":"failure","error":serializer.errors})
            
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
                return JsonResponse({"type":"success","message":"successfully registered","user":serializer.data})
            else:
                return JsonResponse({"type":"failure","error":serializer.errors})

        except Exception as e:
            return JsonResponse({"exception":str(e)})

