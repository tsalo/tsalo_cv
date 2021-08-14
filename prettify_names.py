"""Prettify names in an author list"""


def prettify(names):
    names = names.split(", ")
    new_names = []
    for name in names:
        name_parts = name.split(" ")
        last_name = name_parts[-1]
        other_names = name_parts[:-1]
        initials = [n[0] for n in other_names]
        initials = [n + "." for n in initials]
        initials = " ".join(initials)
        new_name = last_name + ", " + initials
        new_names.append(new_name)

    new_names[-1] = "\\& " + new_names[-1]
    new_names = ", ".join(new_names)
    print(new_names)


if __name__ == "__main__":
    import sys

    prettify(sys.argv[1])
