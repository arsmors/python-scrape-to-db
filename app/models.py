from django.db import models
from django.db.models.signals import pre_save, post_save
from app.utils import unique_slug_generator


# Create your models here.

class Headline(models.Model):
    instrument = models.CharField(max_length=1000)
    price = models.TextField()
    change = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.instrument

    @property
    def name(self):
        return self.instrument


def rl_pre_save_receiver(sender, instance, *args, **kwargs):
    # print('saving..')
    # print(instance.timestamp)
    if not instance.slug:
        # instance.title="another title"
        instance.slug = unique_slug_generator(instance)


# def rl_post_save_receiver(sender, instance, created, *args, **kwargs):
# print('saved')
# print(instance.timestamp)
# if not instance.slug:
# instance.slug = unique_slug_generator(instance)
# instance.save()

pre_save.connect(rl_pre_save_receiver, sender=Headline)
# post_save.connect(rl_post_save_receiver, sender=Headline)
