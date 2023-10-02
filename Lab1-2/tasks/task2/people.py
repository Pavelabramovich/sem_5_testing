from main_decorator import main


def parse_age(age):
    try:
        age = int(age)
    except ValueError as error:
        raise ValueError("Age must be positive integer number") from error
    else:
        if age <= 0:
            raise ValueError("Age must be positive integer number")
        else:
            return age


@main
def main():
    people = []

    while human_str := input():
        try:
            name, surname, age = human_str.split()
        except ValueError as error:
            raise ValueError("You need enter name, surname and age for every human.") from error

        age = parse_age(age)
        people.append((name, age, surname))

    for human in people:
        print("%s %d %s" % human)

    print(min(people, key=lambda human: human[1])[1])
    print(max(people, key=lambda human: human[1])[1])

    print(sum(age for _, age, _ in people) / len(people))
