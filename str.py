"""This module provides utility functions basic string manipulations"""
import sys
import pyperclip
from termcolor import colored


def to_lower_case(string):
    """Returns string in lowercase"""
    return string.lower().strip()


def to_upper_case(string):
    """Returns string in uppercase"""
    return string.upper().strip()


def to_title_case(string):
    """Returns string in titlecase"""
    return string.title().strip()


def to_capital_case(string):
    """Returns string in capitalcase"""
    return string.capitalize().strip()


def print_help():
    """Print help options"""
    print(colored("Usage:", "green"))
    print(colored("  Provide a string.", "white"))
    print(colored("  Provide a flag option.", "white"))
    print(colored("Flag Options:", "green"))
    print(colored("  -l, --lower-case", "white"))
    print(colored("  -u, --upper-case", "white"))
    print(colored("  -t, --title-case", "white"))
    print(colored("  -c, --capital-case", "white"))


def operation(string, flag):
    """Determine what operation is being used based on flag provided"""
    if flag in ["-l", "--lower-case"]:
        return to_lower_case(string)
    if flag in ["-u", "--upper-case"]:
        return to_upper_case(string)
    if flag in ["-t", "--title-case"]:
        return to_title_case(string)
    if flag in ["-c", "--capital-case"]:
        return to_capital_case(string)

    print(colored("\nInvalid flag option.\n", "red"))

    print_help()
    sys.exit(1)


def main(args):
    """Entry function for program"""
    if len(args) < 3:
        print_help()
        sys.exit(0)

    string = args[-2]
    flag = args[-1]
    result = operation(string, flag)
    print(f"{colored(result, 'yellow')} copied to the clipboard.")
    pyperclip.copy(result)


if __name__ == "__main__":
    main(sys.argv)
