
from django.core import serializers

def save_user(request, user1):
    obj = serializers.serialize('json', [ user1, ])
    request.session['user1'] = obj

def get_user(request):
    obj = request.session.get('user1')
    if obj:
        user = list(serializers.deserialize('json',obj))
        return user[0].object
    else:
        return None
