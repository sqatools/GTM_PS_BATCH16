# install faker module with below command
# pip install faker

from faker import Faker

fk = Faker()

for i in range(1, 10):
    print(i)
    print(fk.first_name())
    print(fk.last_name())
    print(fk.email())
    print("__"*10)
