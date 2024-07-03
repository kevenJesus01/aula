from faker import Faker
import random

faker = Faker('pt_BR')

persona = {
    "nome": faker.name(),
    "Cidade": faker.city(),
    "data": faker.date_of_birth(),
    "idade": faker.random_int(18, 18)

}


print(persona)
