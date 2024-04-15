import pytest

#make a function that takes a string and returns a reversed copy

#make a function that takes a string and reverses it

#make a function that reverses a string




def reverse(strong: str) -> str:
    rev_string = ""
    count = 1
    index_count = 0
    while count <= len(strong):
        rev_string += strong[index_count - count]
        count += 1
    return rev_string


def test_reverse():




def main():
    print(reverse("hello"))



main()