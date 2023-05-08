# Sing Up
post => http://127.0.0.1:8000/api/account/sing-up/

required field: 

    {
        "email":"demomail@gmail.com",
        "password":"1234",
        "first_name":"Mossaddak",
        "last_name":"Hossain"
    }

# Account Verification
-)First:

    need to hit this url, user must need loged in. there is no need any field. after hit this user will get an otp through the email:

    post => http://127.0.0.1:8000/api/account/account-verify-code/

-)Second:

    then you have to hit the below link with the otp you got through the email 

    post => http://127.0.0.1:8000/api/account/verify/

    required field:

        {
            "otp":"12279"
        }

# Login
post => http://127.0.0.1:8000/api/account/login/

required fields:

    {
        "email":"10000mossaddak1@gmail.com",
        "password":"1234"
    }

# Profile Picture

post, get, delete, patch => http://127.0.0.1:8000/api/account/profile-picture/

required field: img

Note: Authentication Mandetory

# Profile 
post, patch => http://127.0.0.1:8000/api/account/profile/

required fields:

    {
        "id": 16,
        "username": "mossaddak1",
        "first_name": "Mossaddak",
        "last_name": "",
        "email": "demomail1@gmail.com"
    }

Note: Here have to pass "username" field for patching

# Image Procesing
post => http://127.0.0.1:8000/api/app/image-proccess/

get => http://127.0.0.1:8000/api/app/image-proccess/<id>/

required field: input(form data)

note: only super admin has permission of GET

# PDF to image
post => http://127.0.0.1:8000/api/app/pdf-proccess/

get => http://127.0.0.1:8000/api/app/pdf-proccess/<id>/

required field: input(form data)

note: only super admin has permission of GET

# Reset Password
post => http://127.0.0.1:8000/api/recovery-account/reset-password/

required field:
    {
        "email":"demomail1@gmail.com"
    }

# Reset password send token
post => http://127.0.0.1:8000/api/recovery-account/reset-password-send-token/

required field:

    {
        "password_reset_token":<here will be the token send by email>,
        "new_password":12345
    }



# How to create app password?
=)
    go to this link: https://myaccount.google.com/?hl=en_GB&utm_source=OGB&utm_medium=act

    then,

        security > 2 step verification > sing into your account > App passwords(it will get in bottom) > select app(other) > give a name > click generate


# Payment Method
api_key = 