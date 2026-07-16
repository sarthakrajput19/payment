from faker import Faker
import csv

fake = Faker()

message = {
    "name": fake.name(),
    "address": fake.address(),
    "phone": fake.phone_number(),
    "zipcode": fake.zipcode(),
    "country": fake.country()
}

csv_file = "fake_data.csv"

with open(csv_file, mode="w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=message.keys())

    writer.writeheader()
    writer.writerow(message)

print(f"Data saved to {csv_file}")
