import factory
from random import random
from apps.profiles.models import Profile
from apps.properties.models import Property
from django.db.models.signals import post_save
from faker import Factory as FakerFactory
from villaage.settings.base import AUTH_USER_MODEL

faker = FakerFactory.create()


@factory.django.mute_signals(post_save)
class PropertiesFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory("tests.factories.UserFactory")
    title = factory.LazyAttribute(lambda x: f"Sweet house")
    ref_code = factory.LazyAttribute(lambda x: faker.password(length=8, special_chars=False, digits=True, upper_case=True, lower_case=True))
    slug = factory.LazyAttribute(lambda x: f"sweet-house")
    description = factory.LazyAttribute(lambda x: faker.text(max_nb_chars=8))
    country = factory.LazyAttribute(lambda x: faker.country_code())
    city = factory.LazyAttribute(lambda x: faker.city())
    postal_code = factory.LazyAttribute(lambda x: faker.postcode())
    street_address = factory.LazyAttribute(lambda x: faker.street_address())
    price = factory.LazyAttribute(lambda x: faker.random_int(min=3, max=5))
    tax = factory.LazyAttribute(lambda x: 0.15)
    plot_area = factory.LazyAttribute(lambda x: 10)
    total_floors = factory.LazyAttribute(lambda x: faker.random_int(min=1, max=4))
    bedrooms = factory.LazyAttribute(lambda x: faker.random_int(min=1, max=4))
    bathrooms = factory.LazyAttribute(lambda x: faker.random_int(min=1, max=4))
    advert_type = factory.LazyAttribute(lambda x: f"FOR_SALE")
    property_type = factory.LazyAttribute(lambda x: f"FOR_SALE")
    cover_photo = factory.LazyAttribute(
        lambda x: faker.file_extension(category="image")
    )
    photo1 = factory.LazyAttribute(
        lambda x: faker.file_extension(category="image")
    )
    photo2 = factory.LazyAttribute(
        lambda x: faker.file_extension(category="image")
    )
    photo3 = factory.LazyAttribute(
        lambda x: faker.file_extension(category="image")
    )
    photo4 = factory.LazyAttribute(
        lambda x: faker.file_extension(category="image")
    )
    published_status = True
    views = factory.LazyAttribute(lambda x: faker.random_int(min=0, max=500))

    class Meta:
        model = Property


@factory.django.mute_signals(post_save)
class ProfileFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory("tests.factories.UserFactory")
    phone_number = factory.LazyAttribute(lambda x: faker.phone_number())
    about_me = factory.LazyAttribute(lambda x: faker.sentence(nb_words=5))
    license = factory.LazyAttribute(lambda x: faker.text(max_nb_chars=6))
    profile_photo = factory.LazyAttribute(
        lambda x: faker.file_extension(category="image")
    )
    gender = factory.LazyAttribute(lambda x: f"other")
    country = factory.LazyAttribute(lambda x: faker.country_code())
    city = factory.LazyAttribute(lambda x: faker.city())
    is_buyer = False
    is_seller = False
    is_agent = False
    top_agent = False
    rating = factory.LazyAttribute(lambda x: faker.random_int(min=1, max=5))
    num_reviews = factory.LazyAttribute(lambda x: faker.random_int(min=0, max=25))

    class Meta:
        model = Profile


@factory.django.mute_signals(post_save)
class UserFactory(factory.django.DjangoModelFactory):
    first_name = factory.LazyAttribute(lambda x: faker.first_name())
    last_name = factory.LazyAttribute(lambda x: faker.last_name())
    username = factory.LazyAttribute(lambda x: faker.first_name())
    email = factory.LazyAttribute(lambda x: f"klowamirali@gmail.com")
    password = factory.LazyAttribute(lambda x: faker.password())
    is_active = True
    is_staff = False

    class Meta:
        model = AUTH_USER_MODEL

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        manager = cls._get_manager(model_class)
        if "is_superuser" in kwargs:
            return manager.create_superuser(*args, **kwargs)
        else:
            return manager.create_user(*args, **kwargs)
