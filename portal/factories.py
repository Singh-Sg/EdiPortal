import random
import factory
from faker import Faker
from factory.fuzzy import BaseFuzzyAttribute
from .models import InfraVltgDetail
fake = Faker()


class InfraVltgDetailFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = InfraVltgDetail

    asof = fake.past_datetime(start_date="-30d", tzinfo=None)
    username = factory.Faker('sentence', nb_words=1)
    environment= factory.Faker('sentence', nb_words=1)
    username= factory.Faker('sentence', nb_words=1)
    vltg_identity = factory.Faker('sentence', nb_words=1)
    cvproduct = factory.Faker('sentence', nb_words=1)
    cvapi = factory.Faker('sentence', nb_words=1)
    srcip = factory.Faker('sentence', nb_words=1)
    typeofapi = factory.Faker('sentence', nb_words=1)
    hostname = factory.Faker('sentence', nb_words=1)
    create_dt = fake.past_datetime(start_date="-30d", tzinfo=None)

