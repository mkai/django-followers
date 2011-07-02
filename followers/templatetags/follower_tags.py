from django import template
from followers.utils import get_people_user_follows as _get_people_user_follows, get_people_following_user as _get_people_following_user, get_mutual_followers as _get_mutual_followers

register = template.Library()

@register.assignment_tag
def get_people_user_follows(user):
    return _get_people_user_follows(user)

@register.assignment_tag
def get_people_following_user(user):
    return _get_people_following_user(user)

@register.assignment_tag
def get_mutual_followers(user):
    return _get_mutual_followers(user)
