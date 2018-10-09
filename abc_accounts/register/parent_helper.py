credit_card = 378750082492053
cc_code = 4882


def save_survey(host):
    return {
        "answer17": "null",
        "answer18": "",
        "page": f"https%3A%2F%2F{host}%2Fhtml5%2Fregpath%2Fsurvey",
        "action": "savesurvey"
    }


def save_parent(first_name, last_name, user_id):
    return {
        "action": "saveparent",
        "username": first_name,
        "lastname": last_name,
        "gender": "F",
        "avatar": "/av/puppy.jpg",
        "userid": user_id,
    }


def save_child(name, gender, level):
    return {
        "action": "savechild",
        "fields": (
            "username,gender,birthdate,teacher,pathlevel,"
            "childrelation,relativeFirstName,relativeLastName,"
            "relativeEmail,relativeRelationship,guardian"
        ),
        "username": name,
        "gender": gender,
        "pathlevel": level,
        "birthdate": "2017-2-01",
        "teacher": 0,
        "childrelation": 12,
        "relativeFirstName": "",
        "relativeLastName": "",
        "relativeEmail": "",
        "relativeRelationship": 0,
        "guardian": "Yes",
        "userid": 0,
    }


def save2():
    return {
        "action": "save2",
        "area": "page6",
        "skus": "90602,90401,51900,54600,95305,95501,106006,92205,96404",
    }


def save_avatar(avatar, child_id):
    return {
        "action": "avatar_change",
        "av": f"av/premade/{avatar}",
        "userid": child_id,
    }


def confirm_child(child_id):
    return {
        "action": "confirm_child",
        "userid": child_id,
    }


def get_form_auth(auth_id):
    return {
        "service_action": "get_form_auth_code",
        "form_auth_id": auth_id,
    }


def process_subscription(email, password, form_auth, form_code):
    return {
        "email": email,
        "confirmEmail": email,
        "password": password,
        "confirmPassword": password,
        "cardName": "Test Automation",
        "cardNumber": credit_card,
        "cardExpMonth": "07",
        "cardExpYear": "2020",
        "postFromWelcomeBack": "0",
        "securityCode": cc_code,
        "cardZip": "91206",
        "phone": "",
        "agree": "yes",
        "paymentMethod": "1",
        "productId": product_id,
        "amazonBillingAgreementId": "",
        "action": "process",
        "form_auth_id": form_auth,
        "form_auth_code": form_code,
    }


def subscription_prospect(email, password, form_id, form_code):
    account_info = {
        "email": email,
        "password": password,
        "phone": "",
    }
    credentials = {
        "card_number": credit_card,
        "card_cvv": cc_code,
        "card_name": "AC TEST",
        "card_exp_date": "202006",
        "card_zip": "91206",
        "is_valid_zip": True,
    }
    authorization = {"id": form_id, "code": form_code}
    subscription_info = {
        "subscriptionOption": "monthly",
        "subscriberStatus": "new",
        "trackingPixelStatus": "new",
    }
    return [
        account_info,
        "8946f006fa9f0e8677f950f82fabf289",
        "PAYMENTECH",
        credentials,
        authorization,
        subscription_info,
    ]
