import itertools


def main():
    letters = "norti"
    not_at = ["n", "o", "r", "tn", "t"]
    exact_at = ["", "", "", "", ""]
    may_use = ""
    p = itertools.permutations(letters, 5)
    memo = set()
    for i in p:
        ng = False
        for at, ii in enumerate(i):
            if ii in not_at[at]:
                ng = True
                break
            if exact_at[at] and ii != exact_at[at]:
                ng = True
                break
        if not ng:
            word = "".join(i)
            x_count = word.count("-")
            for sub in itertools.combinations(may_use, x_count):
                replaced_word = word
                for s in sub:
                    replaced_word = replaced_word.replace("-", s, 1)
                if replaced_word not in memo:
                    memo.add(replaced_word)
                    print(replaced_word)


if __name__ == "__main__":
    main()
