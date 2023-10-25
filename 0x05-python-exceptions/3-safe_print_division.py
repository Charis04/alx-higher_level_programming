#!/usr/bin/python3

def safe_print_division(a, b):
    """Return the div of a by b."""
    try:
        div = a / b
    except (ZeroDivisionError):
        div = None
    finally:
        print("Inside result: {}".format(div))
        return (div)
