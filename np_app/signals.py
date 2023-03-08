from NewsPortal.np_app.tasks import send_notifications
from .models import PostCategory
from django.db.models.signals import m2m_changed
from django.dispatch import receiver




@receiver(m2m_changed, sender=PostCategory)
def notify_post(sender, instance, **kwargs):
    if kwargs['action'] == 'post_add':
        categories = instance.category.all()
        subscribers = []

        for cat in categories:
            subscribers += cat.subscribers.all()
        subscribers = [s.email for s in subscribers]

        send_notifications(instance.preview(), instance.pk, instance.header_post, subscribers)