#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys

    state = True
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError) as exc:
        print("Exception: " + str(exc), file=sys.stderr)
        state = False
    return state
