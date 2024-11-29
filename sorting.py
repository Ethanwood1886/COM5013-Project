# Library for random words

from faker import Faker

fake = Faker()

# Generate random words

small_list = [fake.word() for _ in range(100)]
large_list = [fake.word() for _ in range(1000)]

print(small_list)
print(large_list)
