#script to resave providers to set the latlng property of each provider.

import os
import time

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sheltr.settings')

import django
django.setup()

from app.models import Provider

providers = Provider.objects.all()

print("Resaving all providers...")

for provider in providers: 
	#Slow down because Google Maps API only allows max ~5 queries/sec for location data.
	time.sleep(0.2)
	provider.save()


print("Complete.")