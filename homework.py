from typing import Any
from typing import List

class OurAwesomeException(Exception):
    pass

def is_two_object_has_same_value(first: Any, second: Any) -> bool:
    """
    If @first and @second has same value should return True
    In another case should return False
    """
    return first == second


#print(is_two_object_has_same_value([1, 3, 5], [1, 4, 5]))


def is_two_objects_has_same_type(first: Any, second: Any) -> bool:
    """
    If @first and @second has same type should return True
    In another case should return False
    """
    return type(first) == type(second)


#print(is_two_objects_has_same_type(1, 2))


def is_two_objects_is_the_same_objects(first: Any, second: Any) -> bool:
    """
    If @first and @second has same type should return True
    In another case should return False
    """
    first = first + first
    second = second + second
    return first is second


#print(is_two_objects_is_the_same_objects(1, 1.01))


def multiple_ints(first_value: int, second_value: int) -> int:
    """
    Should calculate product of all args.
    if first_value or second_value is not int should raise ValueError

    Raises:
        ValueError

    Params:
        first_value: value for multiply
        second_value
    Returns:
        Product of elements
    """
    if type(first_value) == type(second_value) == int:

        return first_value * second_value
    else:
        return "ValueError"


#print(multiple_ints(2.1, 5))


def multiple_ints_with_conversion(first_value: Any, second_value: Any) -> int:
    """
    If possible to convert arguments to int value - convert and multiply them.
    If it is impossible raise OurAwesomeException

    Args:
        first_value: number for multiply
        second_value: number for multiply

    Raises:
        OurAwesomeException

    Returns: multiple of two numbers.

    Examples:
        multiple_ints_with_conversion(6, 6)
        >>> 36
        multiple_ints_with_conversion(2, 2.0)
        >>> 4
        multiple_ints_with_conversion("12", 1)
        >>> 12
        try:
            multiple_ints_with_conversion("Hello", 2)
        except ValueError:
            print("Not valid input data")
        >>> "Not valid input data"
    """
    try:
        if type(first_value) != type(second_value):
            first_value = float(first_value)
            second_value = float(second_value)
            return (int(first_value * second_value))
    except ValueError:
        return "Not valid input data"


#print(multiple_ints_with_conversion("TWENTY", 11))


def is_word_in_text(word: str, text: str) -> bool:
    """
    If text contain word return True
    In another case return False.

    Args:
        word: Searchable substring
        text: Text for searching

    Examples:
        is_word_in_text("Hello", "Hello word")
        >>> True
        is_word_in_text("Glad", "Nice to meet you ")
        >>> False

    """
    return word in text


#print(is_word_in_text("Hello", "Hello word"))
# is_word_in_text("Glad", "Nice to meet you ")


def some_loop_exercise() -> list:
    """
    Use loop to create list that contain int values from 0 to 12 except 6 and 7
    """
    a = [i + 1 for i in range(n)]
    del a[5:7]

    return a


#print(some_loop_exercise(12))


def remove_from_list_all_negative_numbers(data: List[int]) -> list:
    """
    Use loops to solve this task.
    You could use data.remove(negative_number) to solve this issue.
    Also you could create new list with only positive numbers.
    Examples:
        remove_from_list_all_negative_numbers([1, 5, -7, 8, -1])
        >>> [1, 5, 8]
    """
    n = [i for i in n if i >= 0]
    return n


#print(remove_from_list_all_negative_numbers([1, -5, 12]))


def alphabet() -> dict:
    """
    Create dict which keys is alphabetic characters. And values their number in alphabet
    Notes You could see an implementaion of this one in test, but create another one
    Examples:
        alphabet()
        >>> {"a": 1, "b": 2 ...}
    """
    import string
    d = {x: y for x, y in zip(string.ascii_lowercase, range(1, 26))}
    return d


#print(alphabet())


def simple_sort(my_list):
    """
    Sort list of ints without using built-in methods.
    Examples:
        simple_sort([2, 9, 6, 7, 3, 2, 1])
        >>> [1, 2, 2, 3, 6, 7, 9]
    Returns:

    """
    n1 = -1
    for i in my_list:
        n1 += 1
    for i in my_list[:n1]:
        n = n1
        for j in my_list[:n1]:
            if my_list[n - 1] > my_list[n]:
                my_list[n - 1], my_list[n] = my_list[n], my_list[n - 1]
            n -= 1
    return my_list


#print(simple_sort([4, 3, 10, 22, 15, 44, 55, 22, 2, 13, 111, 2]))