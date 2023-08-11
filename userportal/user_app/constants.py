# CUSTOM ERROR CODES

errors = {

    'MISSING_FIELD':{
        'code':40001,
        'message':'Some required fields are missing'
    },
    'INVALID_PASSWORD_FORMAT':{
        'code':40002,
        'message':'Password must contain one uppercase, one lowercase, one special character, one digit and length should be 8'
    },
    'INVALID_EMAIL_FORMAT':{
        'code':40003,
        'message':'Email format is invalid'
    },
    'INVALID_MOBILE_FORMAT':{
        'code':40004,
        'message':'Mobile number must contain only digits and should be of length 10'
    },
    'PASSWORD_INCORRECT':{
        'code':40005,
        'message':'Password is incorrect'
    },
    'EMAIL_DOES_NOT_EXIST':{
        'code':40006,
        'message':'Email does not exist, please register'
    },
    'MODEL_VALIDATION_ERROR':{
        'code':40007
    }
}

# RESPONSE FORMAT FOR SUCCESS

# {
#     "success":True,
#     "response_code":"",
#     "message":"",
#     "data":{}
# }

# # RESPONSE FORMAT FOR FAILURE
# {
#     "success":False,
#     "response_code":"",
#     "error":{
#         "code":"",
#         "message":"",
#         "fields":[]
#     }
# }

'''
{
    "type": "failure",
    "error": {
        "mobile": [
            "Ensure this field has no more than 10 characters."
        ]
    }
}

# object level or field level validation
{
    "type": "failure",
    "error": {
        "non_field_errors": [
            "mobile number is invalid"
        ]
    }
}

# model level validation
{
    "type": "failure",
    "error": {
        "email": [
            "user with this email already exists."
        ],
        "mobile": [
            "user with this mobile already exists."
        ],
        "username": [
            "user with this username already exists."
        ]
    }
}

# when incomplete details supplied
{
    "type": "failure",
    "error": {
        "email": [
            "This field is required."
        ],
        "password": [
            "This field is required."
        ]
    }
}
'''
