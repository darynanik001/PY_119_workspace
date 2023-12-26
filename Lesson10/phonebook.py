import json


def search_user_by_value(user_value: str, records: list) -> dict:
    """Searches for an entry by specified field and returns first found"""
    for record in records:
        for value in record.values():
            if user_value == value:
                return record
    print(f"User with value {user_value} was not found.")
    return {}


def add_entry(file_path: str, records: list, new_entry: dict) -> None:
    """Adds new entry"""
    records.append(new_entry)
    print(f"Record {new_entry} was added.")
    with open(file_path, "w") as f:
        f.writelines(json.dumps(records))


def delete_record_by_phone(file_path: str, records: list, phone_number: str) -> None:
    """Deletes entry found by phone number"""
    record = search_user_by_value(phone_number, records)
    records.remove(record)
    print(f"Record: {record} was removed.")

    with open(file_path, "w") as f:
        f.writelines(json.dumps(records))


def update_record(file_path: str, records: list, phone_number: str, what_to_update: str, new_value: str) -> None:
    """Updates entry found by phone number"""
    record = search_user_by_value(phone_number, records)
    if record.get(what_to_update):
        record[what_to_update] = new_value
        print(f"Updated record: {record}")
    else:
        print(f"Record does not have such option {what_to_update}."
              f"You can only update these fields: first_name, last_name, full_name, phone and city ")

    with open(file_path, "w") as f:
        f.writelines(json.dumps(records))


if __name__ == "__main__":
    file_path = input("Enter path to json data\n")

    while True:
        records = []

        with open(file_path) as f:
            option = input("Please select an option. Available options: search, add, delete, update, exit\n")
            records.extend(json.loads(f.read()))

            if option == "exit":
                break

            if option == "search":
                search_by = input("Specify field value you want to search by (first_name, last_name, full_name, "
                                  "phone, city)\n")

                search_user_by_value(search_by, records)
            if option == "delete":
                phone_number = input("Enter entry phone number\n")
                delete_record_by_phone(file_path, records, phone_number)

            if option == "update":
                phone_number = input("Enter entry phone number\n")
                what_to_update = input("Specify field you want to update: ")
                new_value = input("Set new value: ")
                update_record(file_path, records, phone_number, what_to_update, new_value)

            if option == "add":
                print("To create new entry you need to input first name, last name, full name, phone and city\n")
                first_name = input("Enter first name: ")
                last_name = input("Enter last name: ")
                full_name = input("Enter full name: ")
                phone = input("Enter phone number: ")
                city = input("Enter city: ")

                entry = {
                    "first_name": first_name,
                    "last_name": last_name,
                    "full_name": full_name,
                    "phone": phone,
                    "city": city
                }

                add_entry(file_path, records, entry)
