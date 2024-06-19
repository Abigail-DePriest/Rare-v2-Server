from rarev2api.models import Users
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def check_user(request):
    '''Checks to see if User has Associated Users

    Method arguments:
      request -- The full HTTP request object
    '''
    uid = request.data['uid']

    # Use the built-in authenticate method to verify
    # authenticate returns the user object or None if no user is found
    users = Users.objects.filter(uid=uid).first()

    # If authentication was successful, respond with their token
    if users is not None:
        data = {
            'id': users.id,
            'uid': users.uid,
            'bio': users.bio
        }
        return Response(data)
    else:
        # Bad login details were provided. So we can't log the user in.
        data = { 'valid': False }
        return Response(data)


@api_view(['POST'])
def register_user(request):
    '''Handles the creation of a new Users for authentication

    Method arguments:
      request -- The full HTTP request object
    '''

    # Now save the user info in the rarev2api-users table
    users = Users.objects.create(
        bio=request.data['bio'],
        uid=request.data['uid']
    )

    # Return the users info to the client
    data = {
        'id': users.id,
        'uid': users.uid,
        'bio': users.bio
    }
    return Response(data)