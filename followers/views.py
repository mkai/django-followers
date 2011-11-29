from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from followers.models import UserLink
from followers.utils import (get_next, get_people_user_follows, 
                             get_people_following_user, get_mutual_followers)

FRIEND_FUNCTION_MAP = {
    'followers': get_people_following_user,
    'following': get_people_user_follows,
    'mutual': get_mutual_followers,
}


def friend_list(request, list_type, username):
    """
    Renders a list of friends, as returned by the function retrieved from the
    ``FRIEND_FUNCTION_MAP``, given the user specified by the username in the
    URL.
    
    """
    user = get_object_or_404(User, username=username)
    context = {
        'list_type': list_type,
        'friends': FRIEND_FUNCTION_MAP[list_type](user),
    }
    return render_to_response(
        'followers/friend_list.html',
        context,
        context_instance=RequestContext(request)
    )


@login_required
def follow(request, username):
    """
    Adds a "following" edge from the authenticated user to the user specified 
    by the username in the URL.
    
    """
    user = get_object_or_404(User, username=username)
    ul, created = UserLink.objects.get_or_create(from_user=request.user, 
        to_user=user)
    next = get_next(request)
    if next and next != request.path:
        # request.user.message_set.create(
        #     message=_('You are now following %s') % user.username)
        return HttpResponseRedirect(next)
    context = {
        'other_user': user,
        'created': created,
    }
    return render_to_response(
        'followers/followed.html',
        context,
        context_instance=RequestContext(request)
    )


@login_required
def unfollow(request, username):
    """
    Removes a "following" edge from the authenticated user to the user 
    specified by the username in the URL.
    
    """
    user = get_object_or_404(User, username=username)
    try:
        ul = UserLink.objects.get(from_user=request.user, to_user=user)
        ul.delete()
        deleted = True
    except UserLink.DoesNotExist:
        deleted = False
    next = get_next(request)
    if next and next != request.path:
        # request.user.message_set.create(
        #    message=_('You are no longer following %s') % user.username)

        return HttpResponseRedirect(next)
    context = {
        'other_user': user,
        'deleted': deleted,
    }
    return render_to_response(
        'followers/unfollowed.html',
        context,
        context_instance=RequestContext(request)
    )
