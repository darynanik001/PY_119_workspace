

def generate_words_occurrences_map(string: str):
    """Task 1
       Make a program that has some sentence (a string) on input and returns a dict containing all unique words as keys
       and the number of occurrences as values. """
    words_occurrences_map = dict()
    words = string.split(', ')

    for word in words:
        if word not in words_occurrences_map.get(word):
            words_occurrences_map[word] = 0
        words_occurrences_map[word] += 1

    return words_occurrences_map


def get_total_stock_price(stock: dict, prices: dict):
    """Task 2
    Compute the total price of the stock where the total price is the sum of the price of an item multiplied by the
    quantity of this exact item. The code has to return the dictionary with the sums of the prices by the goods types"""
    total_prices_per_good = dict()

    for good in stock.keys():
        total_prices_per_good[good] = stock[good]*prices[good]

    return total_prices_per_good


def generate_list_of_tuples():
    """Task 3
    Use a list comprehension to make a list containing
    tuples (i, j) where 'i' goes from 1 to 10 and 'j' is corresponding to 'i' squared."""
    return [(i, i**i) for i in range(1, 11)]


def generate_weekday_number_map():
    """Task 4
       Створити лист із днями тижня. В один рядок (ну або як завжди) створити словник виду: {1: "Monday", 2:...
       Також в один рядок або як вдасться створити зворотний словник {"Monday": 1,"""
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    numbers = [1, 2, 3, 4, 5, 6, 7]
    return dict(zip(numbers, weekdays)), dict(zip(weekdays, numbers))


if __name__ == '__main__':
    print(generate_words_occurrences_map("Ukraine, Poland, England, Norway, Switzerland, Poland, Norway, Ukraine, "
                                         "Denmark, Ukraine, England"))

    stock = {
        "banana": 6,
        "apple": 0,
        "orange": 32,
        "pear": 15
    }
    prices = {
        "banana": 4,
        "apple": 2,
        "orange": 1.5,
        "pear": 3
    }
    print(f"Total stock prices: {get_total_stock_price(stock, prices)}")
    print(f"List of tuples (i,j) where j = i^2: {generate_list_of_tuples()}")
    weekday_number_map, weekday_number_map_reversed = generate_weekday_number_map()
    print(f"Number to weekday: {weekday_number_map}\nWeekday to number: {weekday_number_map_reversed}")