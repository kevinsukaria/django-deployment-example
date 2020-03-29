import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_Django.settings')

import django

django.setup()

from third_app.models import Users
from faker import Faker

fakegen = Faker()

def populate(N=5):
    for entry in range(N):
        fn = fakegen.name().split()[0]
        ln = fakegen.name().split()[1]
        em = fakegen.email()

        Users.objects.get_or_create(first_name=fn, last_name=ln, email=em)

if __name__ == '__main__':
    print('populating script !')
    populate(20)
    print('populating complete')
