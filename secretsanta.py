import random
import base64
import yaml


class Person():
    def __init__(self, name, household):
        self.name = name
        self.household = set(household)
        self.assignment = None
    
    def __repr__(self):
        return self.name


def random_assign(households):
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
            person.url = encrypt_assignment(person)
            remaining.remove(assignment)
    except IndexError:
        return random_assign(households)
    return people


def encrypt_assignment(person):
    otp = random.randbytes(16)
    pt = int.to_bytes(len(person.assignment), 1, "big") + person.assignment.encode() + random.randbytes(15 - len(person.assignment))
    msg = base64.urlsafe_b64encode(bytearray([c1 ^ c2 for c1, c2 in zip(pt, otp)]) + otp)
    return f"file:///home/pete/secretsanta/index.html?name={person.name}&msg={msg.decode()}"


with open("households.yaml") as f:
    households = yaml.safe_load(f.read())
people = random_assign(households)
for name in people:
    print(people[name].url)
    # print(f"name: {name}, assignment: {people[name].assignment}")
