class Person:
    def __int__(self, first_name: str, last_name: str, age: int):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def talk(self) -> None:
        print(f"Hello, my name is {self.first_name} {self.last_name} and I'm {self.age} years old.")


class Dog:
    age_factor = 7

    def __init__(self, dog_age: int):
        self.dog_age = dog_age

    def human_age(self) -> int:
        return self.dog_age * self.age_factor


CHANNELS = ["BBC", "Discovery", "TV1000"]


class TVController:

    def __init__(self, channels: list):
        self.channels = channels
        self.size = len(channels)
        self.current_channel = None

    def exists(self, value: str | int):
        found = "No"
        if isinstance(value, str):
            if value in CHANNELS:
                found = "Yes"
        elif isinstance(value, int):
            if self.size > 0 and -1 < value < self.size:
                found = "Yes"

        return found

    def first_channel(self):
        if self.exists(0) == "Yes":
            return self.channels[0]
        return "Oops...First channel is temporarily unavailable."

    def last_channel(self):
        if self.exists(self.size - 1) == "Yes":
            return self.channels[-1]
        return "Oops...Last channel is temporarily unavailable."

    def turn_channel(self, n: int):
        if self.exists(n - 1) == "Yes":
            self.current_channel = self.channels[n - 1]
            return self.channels[n - 1]
        return f"{n} channel does not exists." if n < 0 else f"Oops... {n} channel is temporarily unavailable."

    def current_channel(self):
        return self.current_channel

    def next_channel(self):
        if self.current_channel:
            if self.exists(self.channels.index(self.current_channel) + 1) == "Yes":
                self.current_channel = self.channels[self.channels.index(self.current_channel) + 1]
            else:
                self.current_channel = self.first_channel()
        return self.current_channel

    def previous_channel(self):
        if self.current_channel:
            if self.exists(self.channels.index(self.current_channel) - 1) == "Yes":
                self.current_channel = self.channels[self.channels.index(self.current_channel) - 1]
            else:
                self.current_channel = self.last_channel()
        return self.current_channel


if __name__ == "__main__":
    tv_controller = TVController(CHANNELS)
    # print(tv_controller.exists(-32))
    # print(tv_controller.last_channel())
    tv_controller.turn_channel(1)
    print(tv_controller.current_channel)
    print("next")
    print(tv_controller.next_channel())
    print(tv_controller.next_channel())
    print("previous")
    print(tv_controller.previous_channel())
    print(tv_controller.previous_channel())
    print(tv_controller.previous_channel())
    print(tv_controller.previous_channel())
    print(tv_controller.previous_channel())
