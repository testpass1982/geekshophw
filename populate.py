import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'geekshop.settings')

import django
django.setup()

#FAKE POP SCRIPT
import random
from mainapp.models import ProductCategory, Product, Manufacturer
from faker import Faker

fakegen = Faker()

categories = ['Mens', 'Womens']
manufacts = ['Adidas', 'RubbernLeather', 'Reebok', 'Nike', 'RubberInc', 'Shoesnboots']
def add_category():
    c = ProductCategory.objects.get_or_create(name=random.choice(categories))[0]
    c.save()
    return c

def add_manufacturer():
    m = Manufacturer.objects.get_or_create(name=random.choice(manufacts))[0]
    m.save()
    return m

def populate(N=5):
    for entry in range(N):
        #get the categorie or the entry
        cat = add_category()

        #get the manufacturer or create
        man = add_manufacturer()

        #create fake products
        fake_title = fakegen.word(ext_word_list=None)
        fake_size = fakegen.day_of_month()
        fake_added = fakegen.date()

        prod = Product.objects.get_or_create(category=cat, title=fake_title, manufacturer=man, size=fake_size, date_added=fake_added)[0]

if __name__ == '__main__':
    print('populating script')
    populate()
    print('populating complete')
