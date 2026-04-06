# install faker module with below command
# pip install faker
from faker import Faker

fk = Faker()

for i in range(1, 10):
    print(i)
    print("first_name :", fk.first_name())
    print("last name :", fk.last_name())
    print("email :", fk.email())
    print("_"*20)