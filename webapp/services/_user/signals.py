# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from serializers._profile import UserProfileCreateSerializer
#
# from _user.models import User
#
#
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         serializer = UserProfileCreateSerializer(data=instance)
#
#         if serializer.is_valid():
#             print("saving it is valid")
#             serializer.save()
#         else:
#             print(serializer.errors)
#     pass
