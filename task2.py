from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        if not value:
            raise ValueError("Name cannot be empty")
        super().__init__(value)


class Phone(Field):
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Invalid phone number format")
        super().__init__(value)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        new_phone = Phone(phone)
        if new_phone not in self.phones:
            self.phones.append(new_phone)
            return "Phone added."
        else:
            return "Phone already exists."

    def remove_phone(self, phone):
        if removed := [p for p in self.phones if p.value == phone]:
            self.phones.remove(removed[0])
            return "Phone removed."
        else:
            return "Phone not found."

    def edit_phone(self, old_phone, new_phone):
        removed = self.remove_phone(old_phone)
        if removed != "Phone removed.":
            return removed
        added = self.add_phone(new_phone)
        return "Phone edited." if added == "Phone added." else added

    def find_phone(self, phone):
        found = [p.value for p in self.phones if p.value == phone]
        return found[0] if found else "Phone not found."

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {', '.join(str(p) for p in self.phones)}"


class AddressBook(UserDict):
    def __init__(self):
        self.data = {}

    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data[name] if name in self.data else f"Record {name} not found"

    def delete(self, name):
        if name in self.data:
            del self.data[name]
            return f"Record {name} deleted"
        return f"Record {name} not found"


if __name__ == "__main__":
    # Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane
    book.delete("Jane")
