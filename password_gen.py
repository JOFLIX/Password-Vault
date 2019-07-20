# #!/usr/bin/env python3

# """Password generator using Python 3.6 features."""

# # import secrets

import random
import string
import sys

class Gen

def password(length):
    """Generate a random password."""
    alphabet = string.ascii_letters + string.digits
    while True:
        pw = ''.join(random.choice(alphabet) for i in range(length))
        if (any(c.islower() for c in pw)
                and any(c.isupper() for c in pw)
                and any(c.isdigit() for c in pw)):
            break
    return(pw)


def main():
    "Print a random password."""
    try:
        length = int(sys.argv[1])
    except (IndexError, ValueError):
        length = 16
    if length < 3:
        print("Length {} is too short".format(length))
        sys.exit(1)
    print(password(length))


if __name__ == '__main__':
    main()
