import itertools


ALL_LETTERS = list("abcdefghijklmnopqrstuvwxyz")


def main():
    not_at = ["", "", "", "", ""]
    exact_at = ["", "", "", "", ""]
    use = ""
    not_use = ""
    may_use = ""

    if not may_use:
        may_use = ALL_LETTERS
        for letter in not_use:
            may_use.remove(letter)

    vague_count = 5 - sum([1 for x in exact_at if x])
    memo = set()
    pp = itertools.product(may_use, repeat=vague_count)
    for may_use_letters in pp:
        # use が指定されている場合、その文字が含まれていないものはスキップ
        if use and not any([x in use for x in may_use_letters]):
            continue

        concrete_word = "".join(map(lambda x: x if x else "-", exact_at))
        for letter in may_use_letters:
            concrete_word = concrete_word.replace("-", letter, 1)

        # not_at が指定されている場合、その文字が含まれているものはスキップ
        ng = False
        for letter, not_at_letters in zip(concrete_word, not_at):
            if not_at_letters and letter in not_at_letters:
                ng = True
                break
        if ng:
            continue

        # 出力
        if concrete_word not in memo:
            memo.add(concrete_word)
            print(concrete_word)


if __name__ == "__main__":
    main()
