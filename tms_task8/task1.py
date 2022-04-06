from dataclasses import dataclass
from datetime import date

@dataclass
class Company:
    name: str
    year_of_creation: int
    capitalization: str
    
    @staticmethod
    def len_of_name(name):
        return len(name)
    
    @classmethod
    def age(cls, year_of_creation):
        return date.today().year - year_of_creation

apple = Company('Apple', 1976, '$2.826 Trillion')
google = Company('Google', 1998, '$1.820 Trillion')
amazon = Company('Amazon', 1994, '$1.618 Trillion')

print(Company.len_of_name(apple.name))
print(Company.age(google.year_of_creation))