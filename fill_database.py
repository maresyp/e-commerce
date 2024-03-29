import os
from pathlib import Path

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'e_commerce.settings')
django.setup()

from django.contrib.auth.models import User
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
            product, created = Product.objects.get_or_create(
                name=product_name,
                defaults={
                    'description': product_description,
                    'category': sub_cat,
                    'price': 89 + 2*i,
                    'quantity': 123 - 2*i,
                    'product_image': str(Path(f'shop/images/Ball_{i}.jpg')),
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
                'product_image': str(Path('shop/images/Ball_white.jpg')),
            },
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
                    'product_image': str(Path(f'shop/images/Ball_{color}.jpg')),
                },
            )
            if created:
                print(f"Produkt '{product_name}' został utworzony.")
            else:
                print(f"Produkt '{product_name}' już istnieje.")
        except Exception as e:
            print(f"Nie można utworzyć produktu '{product_name}': {e}")

def create_snooker_sticks():
    main_cat, _ = MainCategory.objects.get_or_create(name='Kije')
    sub_cat, _ = SubCategory.objects.get_or_create(name='Kije snookerowe', mainCategory=main_cat)

    product_name = 'Kij Snookerowy'
    product_description = 'Kij snookerowy, zapewniający precyzję i trwałość.'

    try:
        product, created = Product.objects.get_or_create(
            name=product_name,
            defaults={
                'description': product_description,
                'category': sub_cat,
                'price': 325,
                'quantity': 123,
                'product_image': str(Path('shop/images/Kij_snooker.png')),
            },
        )
        if created:
            print(f"Produkt '{product_name}' został utworzony.")
        else:
            print(f"Produkt '{product_name}' już istnieje.")
    except Exception as e:
        print(f"Nie można utworzyć produktu '{product_name}': {e}")

def create_biliard_sticks():
    main_cat, _ = MainCategory.objects.get_or_create(name='Kije')
    sub_cat, _ = SubCategory.objects.get_or_create(name='Kije bilardowe pool', mainCategory=main_cat)

    product_name = 'Kij Bilardowy'
    product_description = 'Kij bilardowy, zapewniający precyzję i trwałość.'

    try:
        product, created = Product.objects.get_or_create(
            name=product_name,
            defaults={
                'description': product_description,
                'category': sub_cat,
                'price': 420,
                'quantity': 123,
                'product_image': str(Path('shop/images/Kij_bilardowy.jpg')),
            },
        )
        if created:
            print(f"Produkt '{product_name}' został utworzony.")
        else:
            print(f"Produkt '{product_name}' już istnieje.")
    except Exception as e:
        print(f"Nie można utworzyć produktu '{product_name}': {e}")

def create_snooker_triangle():
    main_cat, _ = MainCategory.objects.get_or_create(name='Trójkąty')
    sub_cat, _ = SubCategory.objects.get_or_create(name='Snookerowe', mainCategory=main_cat)

    product_name = 'Trójkąt snooker'
    product_description = 'Trójkąt snookerowy, zapewniający precyzję i trwałość.'

    try:
        product, created = Product.objects.get_or_create(
            name=product_name,
            defaults={
                'description': product_description,
                'category': sub_cat,
                'price': 25,
                'quantity': 123,
                'product_image': str(Path('shop/images/snooker_triangle.jpg')),
            },
        )
        if created:
            print(f"Produkt '{product_name}' został utworzony.")
        else:
            print(f"Produkt '{product_name}' już istnieje.")
    except Exception as e:
        print(f"Nie można utworzyć produktu '{product_name}': {e}")

def create_billiard_triangle():
    main_cat, _ = MainCategory.objects.get_or_create(name='Trójkąty')
    sub_cat, _ = SubCategory.objects.get_or_create(name='Pool', mainCategory=main_cat)

    product_name = 'Trójkąt pool'
    product_description = 'Trójkąt bilardowy, zapewniający precyzję i trwałość.'

    try:
        product, created = Product.objects.get_or_create(
            name=product_name,
            defaults={
                'description': product_description,
                'category': sub_cat,
                'price': 25,
                'quantity': 123,
                'product_image': str(Path('shop/images/billiard_triangle.jpg')),
            },
        )
        if created:
            print(f"Produkt '{product_name}' został utworzony.")
        else:
            print(f"Produkt '{product_name}' już istnieje.")
    except Exception as e:
        print(f"Nie można utworzyć produktu '{product_name}': {e}")

def create_billiard_table():
    main_cat, _ = MainCategory.objects.get_or_create(name='Stoły bilardowe')
    sub_cat, _ = SubCategory.objects.get_or_create(name='Stoły bilardowe pool', mainCategory=main_cat)

    product_name = 'Stół Pool'
    product_description = 'Stół bilardowy, zapewniający precyzję i trwałość.'

    try:
        product, created = Product.objects.get_or_create(
            name=product_name,
            defaults={
                'description': product_description,
                'category': sub_cat,
                'price': 2500,
                'quantity': 123,
                'product_image': str(Path('shop/images/pool_table.jpg')),
            },
        )
        if created:
            print(f"Produkt '{product_name}' został utworzony.")
        else:
            print(f"Produkt '{product_name}' już istnieje.")
    except Exception as e:
        print(f"Nie można utworzyć produktu '{product_name}': {e}")

def create_snooker_table():
    main_cat, _ = MainCategory.objects.get_or_create(name='Stoły bilardowe')
    sub_cat, _ = SubCategory.objects.get_or_create(name='Stoły do snookera', mainCategory=main_cat)

    product_name = 'Stół snooker'
    product_description = 'Stół snookerowy, zapewniający precyzję i trwałość.'

    try:
        product, created = Product.objects.get_or_create(
            name=product_name,
            defaults={
                'description': product_description,
                'category': sub_cat,
                'price': 2500,
                'quantity': 123,
                'product_image': str(Path('shop/images/snooker_table.jpg')),
            },
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
    create_snooker_sticks()
    create_biliard_sticks()
    create_snooker_triangle()
    create_billiard_triangle()
    create_snooker_table()
    create_billiard_table()