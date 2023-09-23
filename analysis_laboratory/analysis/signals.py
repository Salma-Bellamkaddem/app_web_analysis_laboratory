from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth.models import Group


from .models import Laborantins

def laborantins_profile(sender, instance, created, **kwargs):
	if created:
		group = Group.objects.get(name='laborantins')
		instance.groups.add(group)
		Laborantins.objects.create(
			user=instance,
			name=instance.username,
			)
		print('Profile created!')

post_save.connect(laborantins_profile, sender=User)