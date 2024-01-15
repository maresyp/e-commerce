import os
from pathlib import Path

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'e_commerce.settings')
django.setup()

from django.contrib.auth.models import User
from django.core.files import File
from shop.models import MainCategory, Product, SubCategory


def create_categories():
    categories = {
        'Kije': ['Kije snookerowe', 'Kije bilardowe pool'],
        'Bile': ['Snookerowe', 'Pool'],
        'Trójkąty': ['Snookerowe', 'Pool'],
        'Stoły bilardowe': ['Stoły do snookera', 'Stoły bilardowe pool'],
    }

    for main_cat, sub_cats in categories.items():
        main_cat_obj, created = MainCategory.objects.get_or_create(name=main_cat)
        for sub_cat in sub_cats:
            SubCategory.objects.get_or_create(name=sub_cat, mainCategory=main_cat_obj)
        print(f"Kategoria główna '{main_cat}' oraz podkategorie zostały utworzone.")

def create_users() -> None:
    # Tworzenie superusera
    try:
        User.objects.create_superuser('admin', 'admin@email.com', 'admin')
        print("Superuser 'admin' został utworzony.")
    except Exception as e:
        print(f"Nie można utworzyć superusera 'admin': {e}")

    # Tworzenie zwykłego użytkownika
    try:
        user = User.objects.create_user('mirek', 'mirek@email.com', '3edcXSW@')
        user.first_name = 'Mirek'
        user.save()
        print("Użytkownik 'Mirek' został utworzony.")
    except Exception as e:
        print(f"Nie można utworzyć użytkownika 'Mirek': {e}")

def create_pool_balls():
    # Znajdowanie lub tworzenie podkategorii "Pool" w kategorii "Bile"
    main_cat, _ = MainCategory.objects.get_or_create(name='Bile')
    sub_cat, _ = SubCategory.objects.get_or_create(name='Pool', mainCategory=main_cat)

    # Tworzenie bil - pool
    for i in range(1, 16):
        product_name = f'Bila nr {i}'
        product_description = f'Bila numer {i} do gry w pool, zapewniająca precyzję i trwałość.'

        try:
            with Path(f'static/images/shop/images/Ball_{i}.jpg').open('rb') as file:
                product, created = Product.objects.get_or_create(
                    name=product_name,
                    defaults={
                        'description': product_description,
                        'category': sub_cat,
                        'price': 89 + 2*i,
                        'quantity': 123 - 2*i,
                        'product_image': File(file),
                    },
            )
            if created:
                print(f"Produkt '{product_name}' został utworzony.")
            else:
                print(f"Produkt '{product_name}' już istnieje.")
        except Exception as e:
            print(f"Nie można utworzyć produktu '{product_name}': {e}")

    # Generowanie białej bili
    product_name = f'Bila biała'
    product_description = f'Bila biała do gry w pool, zapewniająca precyzję i trwałość.'
    try:
        product, created = Product.objects.get_or_create(
            name=product_name,
            defaults={
                'description': product_description,
                'category': sub_cat,
                'price': 199,
                'quantity': 4,
                'product_image': f'D:\Repositories\e-commerce\static\images\shop\images\Ball_white.jpg'
            }
        )
        if created:
            print(f"Produkt '{product_name}' został utworzony.")
        else:
            print(f"Produkt '{product_name}' już istnieje.")
    except Exception as e:
        print(f"Nie można utworzyć produktu '{product_name}': {e}")

def create_snooker_balls():
    # Lista kolorów bil snookera
    snooker_colors = ['red', 'yellow', 'green', 'brown', 'blue', 'pink', 'black']

    # Znajdowanie lub tworzenie podkategorii "Snooker" w kategorii "Bile"
    main_cat, _ = MainCategory.objects.get_or_create(name='Bile')
    sub_cat, _ = SubCategory.objects.get_or_create(name='Snookerowe', mainCategory=main_cat)

    # Tworzenie bil snookera
    for color in snooker_colors:
        product_name = f'Ball_{color}'
        product_description = f'Bila koloru {color} do gry w snookera, zapewniająca precyzję i trwałość.'

        try:
            product, created = Product.objects.get_or_create(
                name=product_name,
                defaults={
                    'description': product_description,
                    'category': sub_cat,
                    'price': 89,
                    'quantity': 123,
                    'product_image': f'D:\Repositories\e-commerce\static\images\shop\images\Ball_{color}.jpg'
                }
            )
            if created:
                print(f"Produkt '{product_name}' został utworzony.")
            else:
                print(f"Produkt '{product_name}' już istnieje.")
        except Exception as e:
            print(f"Nie można utworzyć produktu '{product_name}': {e}")


if __name__ == '__main__':
    create_users()
    create_categories()
    create_pool_balls()
    create_snooker_balls()
