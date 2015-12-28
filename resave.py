#script to resave providers to set the latlng property of each provider.

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sheltr.settings')

import django
django.setup()

from app.models import Provider

providers = Provider.objects.all()

print("Resaving all providers...")

for provider in providers: 
	provider.save()


print("Complete.")