from faker import Faker
import random

faker = Faker('pt_BR')

persona = {
    "nome": faker.name(),
    "data": faker.date_of_birth(),
    "idade": random.randint(18, 18)
}


print(persona)


