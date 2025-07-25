from django.dispatch import receiver
from blog.models import News,Author
from django.db.models.signals import pre_delete,pre_save,post_delete,post_save

@receiver(pre_save,sender=News)
def create_news(sender,instance,**kwargs):
    instance.first_name="from signal"

@receiver(post_save,sender=News)
def create_news(sender,instance,created,**kwargs):
    if created:
        Author.objects.create(name=instance.first_name+" "+instance.last_name, email=instance.email)

@receiver(pre_delete, sender=News)
def before_delete_log(sender, instance, **kwargs):
   print("jinncnnnnvnbwnvivnrnnvnwnvnkw")
