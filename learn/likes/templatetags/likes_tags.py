from django import template
from django.contrib.contenttypes.models import ContentType
from ..models import Likecount, Likerecord


register = template.Library()

@register.simple_tag
def get_like_count(obj):
    content_type = ContentType.objects.get_for_model(obj)
    like_count, created = Likecount.objects.get_or_create(content_type=content_type, object_id=obj.id)
    return like_count.liked_num


@register.simple_tag(takes_context=True)
def get_like_status(context, obj):
    # user = request.session.get('user_name')
    content_type = ContentType.objects.get_for_model(obj)
    user = context['user']
    if not user.is_authenticated: #request.session.get('is_login', None):
        return ''
    if Likerecord.objects.filter(content_type=content_type, object_id=obj.id, user=user).exists():
        return 'active'
    else:
        return ''