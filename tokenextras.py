from authentication.serializers import AccountSerializer

def jwt_response_payload_handler(token, email=None, request=None):
    return {
        'token': token,
        'account': AccountSerializer(email, context={'request': request}).data
    }
