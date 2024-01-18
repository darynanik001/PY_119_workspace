import re

PREFIX_PATTERN = re.compile(r"^[a-z0-9]+(?:[_.\-][a-z0-9]+)*$")
SUFFIX_PATTERN = re.compile(r'^[a-zA-Z0-9-]+\.[a-zA-Z0-9-]{2,}$')


class EmailValidator:

    def __init__(self, email):
        self.__validate(email)

    def __validate(self, email):
        prefix, suffix = email.split('@')

        if not PREFIX_PATTERN.match(prefix) or not SUFFIX_PATTERN.match(suffix):
            print("Invalid email.")
        else:
            print("Valid email.")


valid_emails = ["abc-d@mail.com", "abc.def@mail.com", "abc@mail.com",
                "abc_def@mail.com", "abc.def@mail.cc", "abc.def@mail-archive.com",
                "abc.def@mail.org", "abc.def@mail.com"]
invalid_emails = [
    "abc-@mail.com",
    "abc..def@mail.com",
    ".abc@mail.com",
    "abc#def@mail.com",
    "abc.def@mail.c",
    "abc.def@mail#archive.com",
    "abc.def@mail",
    "abc.def@mail..com"
]

if __name__ == '__main__':
    for email in valid_emails:
        EmailValidator(email)

    for email in invalid_emails:
        EmailValidator(email)
