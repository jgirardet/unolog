import factory

fk = factory.Faker


class FacUnoUser(factory.django.DjangoModelFactory):
    class Meta:
        model = "unousers.UnoUser"

    username = fk('user_name')
    email = fk('email')
