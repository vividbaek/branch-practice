from random import randint
from random import choice

def get_luckies() -> list:
	return [randint(1,45) for _ in range(7)]


def get_luckies() -> list:
	return [choice(range(1,45+1)) for _ in range(7)]


if __name__=='__main__':
	print(get_luckies())
    print(get_choice())
