#!/usr/bin/env python
import random
from abc import ABC, abstractmethod


class Taxes:
    INCOME_TAX = 0.18
    MILITARY_TAX = 0.018
    SINGLE_TAX = 0.5
    SINGLE_SOCIAL_CONTRIBUTION = 704  # uah


class SoftwareEngineer(ABC):
    @abstractmethod
    def __init__(self, personal_id, name, surname):
        self.personal_id, self.name, self.surname = personal_id, name, surname

    @abstractmethod
    def get_salary(self):
        pass

    @abstractmethod
    def get_taxes(self):
        pass

    def __repr__(self):
        return f"Id: {self.personal_id}; Surname: {self.surname};" \
               f" Salary: {self.get_salary()}; Taxes: {self.get_taxes()};"


class HourlyRateEmployee(SoftwareEngineer):
    def __init__(self, personal_id, name, surname, hourly_rate, hours_total=20.8 * 8):
        super().__init__(personal_id, name, surname)
        self.hourly_rate = hourly_rate
        self.hours_total = hours_total

    def get_salary(self):
        return int(self.hourly_rate * self.hours_total)

    def get_taxes(self):
        return round(self.get_salary() * (Taxes.INCOME_TAX + Taxes.MILITARY_TAX), 2)


class FixedRateEmployee(SoftwareEngineer):
    def __init__(self, personal_id, name, surname, month_fixed_rate):
        super().__init__(personal_id, name, surname)
        self.month_fixed_rate = month_fixed_rate

    def get_salary(self):
        return self.month_fixed_rate

    def get_taxes(self):
        return round(self.get_salary() * (Taxes.INCOME_TAX + Taxes.MILITARY_TAX), 2)


class HourlyRateEntrepreneur(SoftwareEngineer):
    def __init__(self, personal_id, name, surname, hourly_rate, hours_total):
        super().__init__(personal_id, name, surname)
        self.hourly_rate = hourly_rate
        self.hours_total = hours_total

    def get_salary(self):
        return int(self.hourly_rate * self.hours_total * 1.1)

    def get_taxes(self):
        return round(self.get_salary() * Taxes.SINGLE_TAX + Taxes.SINGLE_SOCIAL_CONTRIBUTION, 2)


class Freelancer(SoftwareEngineer):
    def __init__(self, personal_id, name, surname, code_line_price, code_lines_count):
        super().__init__(personal_id, name, surname)
        self.code_line_price = code_line_price
        self.code_lines_count = code_lines_count

    def get_salary(self):
        return int(self.code_line_price * self.code_lines_count)

    def get_taxes(self):
        return round(self.get_salary() * (Taxes.INCOME_TAX + Taxes.MILITARY_TAX)
                     + Taxes.SINGLE_SOCIAL_CONTRIBUTION, 2)


class SoftwareEngineerFactory:
    __NAMES = ('Lily', ' Bran', ' Berry', ' Ran', 'Eliza', ' Dusty')
    __SURNAMES = ('Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Miller')
    __engineer_id = 0

    @staticmethod
    def generate_random_one():
        SoftwareEngineerFactory.__engineer_id += 1
        class_type = random.randint(0, 3)
        if class_type == 0:
            return HourlyRateEmployee(
                SoftwareEngineerFactory.__engineer_id,
                random.choice(SoftwareEngineerFactory.__NAMES),
                random.choice(SoftwareEngineerFactory.__SURNAMES),
                random.randint(3, 25)
            )
        if class_type == 1:
            return FixedRateEmployee(
                SoftwareEngineerFactory.__engineer_id,
                random.choice(SoftwareEngineerFactory.__NAMES),
                random.choice(SoftwareEngineerFactory.__SURNAMES),
                random.randint(300, 7000)
            )
        if class_type == 2:
            return HourlyRateEntrepreneur(
                SoftwareEngineerFactory.__engineer_id,
                random.choice(SoftwareEngineerFactory.__NAMES),
                random.choice(SoftwareEngineerFactory.__SURNAMES),
                random.randint(3, 25),
                random.randint(20, 200)
            )
        if class_type == 3:
            return Freelancer(
                SoftwareEngineerFactory.__engineer_id,
                random.choice(SoftwareEngineerFactory.__NAMES),
                random.choice(SoftwareEngineerFactory.__SURNAMES),
                random.uniform(0.05, 0.15),
                random.randint(2000, 20000)
            )


def main():
    engineers = [SoftwareEngineerFactory.generate_random_one() for _ in range(20)]
    engineers.sort(key=lambda e: (-e.get_salary(), e.surname))
    for engineer in engineers:
        print(engineer)


if __name__ == '__main__':
    main()
