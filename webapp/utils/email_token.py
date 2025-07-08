from django.core import signing


def generate_verification_token(user):
    return signing.dumps({"user_email": user.email})


def decode_verification_token(token, max_age=60 * 60 * 24):  # 1 day
    return signing.loads(token, max_age=max_age)
