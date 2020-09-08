# from django.contrib.auth.models import User
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from asgiref.sync import async_to_sync
# from channels.layers import get_channel_layer

# def announce_user(sender, **kwargs):
#     if kwargs['created']:
#         print("new user has been created")

# post_save

# @receiver(post_save, sender=User)
# def announce_new_user(sender, instance, created, **kwargs):
#     if created:
        # print("New user created")
        # channel_layer = get_channel_layer()
        # async_to_sync(channel_layer.group_send)(
        #     "api",
        #     {
        #         'type': 'send_message',
        #         'message': 'A new user has been created'
        #     }
        # )