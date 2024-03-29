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


def operation(flag, string):
    """Determine what operation is being used based on flag provided"""
    if flag in ["-l", "--lower-case"]:
        return to_lower_case(string)
    if flag in ["-u", "--upper-case"]:
        return to_upper_case(string)
    if flag in ["-t", "--title-case"]:
        return to_title_case(string)
    if flag in ["-c", "--capital-case"]:
        return to_capital_case(string)
    if flag in ["-h", "--help"]:
        print_help()
        sys.exit(1)

    print(colored("\nInvalid flag option.\n", "red"))

    sys.exit(1)


def main(args):
    """Entry function for program"""
    if len(args) < 3:
        print_help()
        sys.exit(0)

    string = args[-1]
    flag = args[-2]
    result = operation(flag, string)
    print(f"{colored(result, 'yellow')} copied to the clipboard.")
    pyperclip.copy(result)


if __name__ == "__main__":
    main(sys.argv)
