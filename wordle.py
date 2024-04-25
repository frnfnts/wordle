import itertools


def main():
    letters = "norti"
    not_at = ["n", "o", "r", "tn", "t"]
    p = itertools.permutations(letters, 5)
    for i in p:
        ng = False
        for at, ii in enumerate(i):
            if ii in not_at[at]:
                ng = True
                break
        if not ng:
            print("".join(i))


if __name__ == "__main__":
    main()
