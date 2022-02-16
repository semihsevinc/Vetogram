def get_authenticatestatus(request):
    if request.user.is_authenticated:
        no_msgs = True
    else:
        no_msgs = False
    return {
        'is_authenticated' : no_msgs
    }