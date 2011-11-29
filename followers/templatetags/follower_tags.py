from django import template
from followers import utils

register = template.Library()


@register.assignment_tag
def get_people_user_follows(user):
    return utils.get_people_user_follows(user)


@register.assignment_tag
def get_people_following_user(user):
    return utils.get_people_following_user(user)


@register.assignment_tag
def get_mutual_followers(user):
    return utils.get_mutual_followers(user)
