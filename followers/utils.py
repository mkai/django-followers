from django.contrib.auth.models import User
from followers.models import UserLink


def get_next(request):
    """
    1. If there is a variable named ``next`` in the *POST* parameters, the
    view will redirect to that variable's value.
    2. If there is a variable named ``next`` in the *GET* parameters, the 
    view will redirect to that variable's value.
    3. If Django can determine the previous page from the HTTP headers, the 
    view will redirect to that previous page.
    
    """
    return request.POST.get('next', request.GET.get('next', 
        request.META.get('HTTP_REFERER', None)))


def get_people_user_follows(user):
    """
    Returns a ``QuerySet`` representing the users that the given user follows.
    
    """
    ul = UserLink.objects.filter(from_user=user).values_list('to_user', 
        flat=True)
    return User.objects.filter(id__in=ul)


def get_people_following_user(user):
    """
    Returns a ``QuerySet`` representing the users that follow the given user.
    
    """
    ul = UserLink.objects.filter(to_user=user).values_list('from_user', 
        flat=True)
    return User.objects.filter(id__in=ul)


def get_mutual_followers(user):
    """
    Returns a ``QuerySet`` representing the users that the given user follows,
    who also follow the given user back.
    
    """
    follows = UserLink.objects.filter(from_user=user).values_list('to_user',
        flat=True)
    following = UserLink.objects.filter(to_user=user).values_list('from_user',
        flat=True)
    return User.objects.filter(
        id__in=set(follows).intersection(set(following)))
