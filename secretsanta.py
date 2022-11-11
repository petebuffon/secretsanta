"""Generate secret santa assignments."""

import base64
import random
import sys
import yaml


class Person():
    """Person with name, household, and assignment."""
    def __init__(self, name, household):
        self.name = name
        self.household = set(household)
        self.assignment = None

    def __repr__(self):
        return self.name


def encrypt_assignment(person, baseurl):
    """Encrypt assignment using one-time-pad."""
    otp = random.randbytes(16)
    padding = random.randbytes(15 - len(person.assignment))
    name_len = int.to_bytes(len(person.assignment), 1, "big")
    plaintext =  name_len + person.assignment.encode() + padding
    msg = base64.urlsafe_b64encode(bytearray([c1 ^ c2 for c1, c2 in zip(plaintext, otp)]) + otp)
    return f"{baseurl}?name={person.name}&msg={msg.decode()}"


def random_assign(households, baseurl):
    """Make assignments randomly."""
    people = {}
    names = []
    for household in households:
        for name in household:
            names.append(name)
            people[name] = Person(name, household)
    random.shuffle(names)
    remaining = set(names)
    try:
        for name in names:
            person = people[name]
            assignment = random.choice(list(remaining - person.household))
            person.assignment = assignment
            person.url = encrypt_assignment(person, baseurl)
            remaining.remove(assignment)
    except IndexError:
        return random_assign(households, baseurl)
    return people


def main():
    """Main function."""
    if len(sys.argv) != 3 or sys.argv[1] == "-help" or sys.argv[1] == "--help":
        sys.exit("usage: python secretsanta.py [households.yaml] [baseurl]")
    with open(sys.argv[1], encoding="utf8") as file:
        households = yaml.safe_load(file.read())
    people = random_assign(households, sys.argv[2])
    for name in people:
        print(people[name].url)


if __name__ == "__main__":
    main()
