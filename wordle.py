import itertools


def main():
    letters = ""
    not_at = ["", "", "", "", ""]
    exact_at = ["", "", "", "", ""]
    may_use = ""

    vague_count = letters.count("-")
    p = itertools.permutations(letters, 5)
    memo = set()
    for word in p:
        ng = False
        for at, letter in enumerate(word):
            if letter in not_at[at]:
                ng = True
                break
            if exact_at[at] and letter != exact_at[at]:
                ng = True
                break
        if ng:
            continue

        pp = itertools.product(may_use, repeat=vague_count)
        for may_use_letters in pp:
            concrete_word = "".join(word)
            for letter in may_use_letters:
                concrete_word = concrete_word.replace("-", letter, 1)
            if concrete_word not in memo:
                memo.add(concrete_word)
                print(concrete_word)


if __name__ == "__main__":
    main()
