import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sheltr.settings')

import django
django.setup()

from app.models import Category, Provider

def testPopulate():

    health=add_category('Health Services')
    legal=add_category('Legal Services')
    housing=add_category('Housing')
    All=add_category('All')

    add_provider(
        category=health,
        provider_name='Example Location',
        location_name='Baltimore Office of Stuff',
        website='www.google.com',
        address1='123 Fake Street',
        address2='',
        city='Baltimore',
        state='Maryland',
        zipcode='21218',
        contact='admin@example.com',
        phone='1-800-301-1234',
        hours='9-5',
        )

    add_provider(
        category=legal,
        provider_name='Legal Place Co',
        location_name='Walmart',
        website='www.legalzoom.com',
        address1='128 Fake Street',
        address2='',
        city='Baltimore',
        state='Maryland',
        zipcode='21216',
        contact='admin@legal.com',
        phone='1-800-240-5069',
        hours='9-5',
        )
    add_provider(
    	category=housing,
    	provider_name='Houses.com',
        location_name='Internet',
        website='www.houses.com',
        address1='Online',
        address2='',
        city='Baltimore',
        state='Maryland',
        zipcode='21701',
        contact='house@houses.com',
        phone='1-800-HOUSE',
        hours='9-5',
        )

    add_provider(
        category=All,
        provider_name='sheltr.org',
        location_name='Internet',
        website='www.sheltr.org',
        address1='Online',
        address2='',
        city='Baltimore',
        state='Maryland',
        zipcode='21218',
        contact='info@sheltr.com',
        phone='N/A',
        hours='24/7',
        )

    add_provider(
        category=All,
        provider_name='MD211',
        location_name='Maryland 211',
        website='www.md211.gov',
        address1='Online',
        address2='',
        city='Baltimore',
        state='Maryland',
        zipcode='21218',
        contact='211',
        phone='211',
        hours='24/7',
        )

    for c in Category.objects.all():
        for p in Provider.objects.filter(category=c):
            print (str(c), " - ", str(p))


def add_provider(provider_name, location_name, website, address1, address2, city, state, zipcode, contact, phone,  hours, category):
    p = Provider.objects.create()
    p.provider_name=provider_name
    p.location_name=location_name
    p.website=website
    p.address1=address1
    p.address2=address2
    p.city=city
    p.state=state
    p.zipcode=zipcode
    p.contact=contact
    p.phone=phone
    p.hours=hours
    p.save()
    p.category=category
    p.save()
    return p

def add_category(name):
    c = Category.objects.get_or_create(name=name)[0]
    return c

# Start execution here!
if __name__ == '__main__':
    print ("")
    print ("Starting testing population script...")
    print ("")
    testPopulate()