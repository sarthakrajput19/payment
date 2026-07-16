from faker import Faker

fake = Faker()

print("Email:", fake.email())
print("Country:", fake.country())
print("Name:", fake.name())
print("Text:", fake.text())
print("Latitude:", fake.latitude())
print("Longitude:", fake.longitude())
print("Website:", fake.url())
