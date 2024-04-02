from jose import jwt
from django.conf import settings

def extract_roles_from_jwt(request):
    """Extract roles from JWT token."""
    auth_header = request.headers.get('Authorization')
    if not auth_header:
        return []

    token = auth_header.split()[1]
    try:
        # Decode JWT token. Use Keycloak's public key here, replacing 'your-public-key'
        decoded_token = jwt.decode(token, 'MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAzi9IfixgT1/tmeSUnLQ9KDyDAAAFIKkSHRthiGjmtHqRK7KeffU3oQ+SmepLkndine8yhxHf4cFziJt3Rrlh82CXzenQ2zBdqLsxAAkzFHJtLuQJ5fgnr1NCAF4PHBzG6XFR2kaHh8WBPkO+R/y/1qsMm32iGvhaDb0IYcmxM3VzggA4U4LbQ+UECM/uaIXejIZaBuomjzKYlD5ekKCPEzWrUrYx96TTu35I8FwiJkzkjuYkcP886WxpzW04mTjGGVQwPXWz6NawSNm75XIpC77TNBL060KvwNLh1mupHnGRaTescX6CFZSFMJMP7tq3EPjAaKebTAuyrBV+G8dlDQIDAQAB', algorithms=['RS256'])
        # Extract roles. Adjust this based on how roles are stored in your JWT
        roles = decoded_token.get('realm_access', {}).get('roles', [])
        return roles
    except jwt.JWTError:
        return []
