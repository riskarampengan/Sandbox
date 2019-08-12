"""
Riskacinta Anetta Rampengan
"""

MINIMUM_LENGTH = 4


def main():
    password = input("Enter password with minimum of {} characters: ".format(MINIMUM_LENGTH))
    while len(password) < MINIMUM_LENGTH:
        password = input("Enter password with minimum of {} characters: ".format(MINIMUM_LENGTH))
    print('*' * len(password))


main()