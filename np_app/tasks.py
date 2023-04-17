from datetime import datetime

from .models import Post, Category
from django.conf import settings
from celery import shared_task
import time

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


@shared_task
def send_notifications(preview, pk, header_post, subscribers):
    html_content = render_to_string('appointment_created.html',
                                    {
                                        'text_post': preview,
                                        'link': f'{settings.SITE_URL}/news/{pk}'
                                    })
    msg = EmailMultiAlternatives(
        subject=header_post,
        body='',
        from_email='rudeigos1995@yandex.ru',
        to=subscribers,
    )
    msg.attach_alternative(html_content, 'text/html')
    msg.send()


@shared_task
def weekly_notifications():
    today = datetime.datetime.now()
    last_week = today - datetime.timedelta(days=7)
    posts = Post.objects.filter(time_create_post__gte=last_week)
    categories = set(posts.values_list('category__genre', flat=True))
    subscribers = set(
        Category.objects.filter(genre__in=categories).values_list('subscribers__email', flat=True))


    html_content = render_to_string(
        'daily_post.html',
        {
            'link': settings.SITE_URL,
            'posts': posts,
        }
    )
    msg = EmailMultiAlternatives(
        subject='Статьи за неделю',
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers,
)

    msg.attach_alternative(html_content, 'text/html')
    msg.send()
    print("отправлено")
