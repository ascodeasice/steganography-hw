import random
import re

from utils import get_random_char, remove_if_in


def encode(cleartext):
    result = ""

    commas = ["，", "、"]
    endings = ["。", "！", "？"]

    for char in cleartext:
        MIN_SENTENCE_SIZE = 10
        MAX_SENTENCE_SIZE = 100
        SENTENCE_SIZE = random.randint(MIN_SENTENCE_SIZE, MAX_SENTENCE_SIZE)

        MIN_COMMA_COUNT = max(0, MIN_SENTENCE_SIZE // 3 - 1)
        # make sure no consecutive comma
        MAX_COMMA_COUNT = max(0, SENTENCE_SIZE // 3 - 2)
        comma_count = random.randint(MIN_COMMA_COUNT, MAX_COMMA_COUNT)

        char_position = comma_count

        # encoding comma
        if char in commas:
            char_position += 1

        sentence_chars = [get_random_char() for _ in range(SENTENCE_SIZE)]
        sentence_chars[char_position] = char

        #  skip start, end, and character position
        valid_comma_position = list(range(1, char_position)) + list(
            range(char_position + 1, SENTENCE_SIZE - 1)
        )

        # insert comma
        for _ in range(comma_count):
            position = random.choice(valid_comma_position)
            # plus i because there are commas before it
            sentence_chars[position] = random.choice(commas)

            # mark left and right of comma as invalid, to prevent consecutive comma
            valid_comma_position = remove_if_in(
                valid_comma_position, [position - 1, position, position + 1]
            )

        sentence_str = "".join(sentence_chars)
        result += sentence_str

        result += random.choice(endings)

    return result


def decode(ciphertext):
    commas = ["，", "、"]
    pattern = "[。？！]"
    sentences = re.split(pattern, ciphertext)

    result = ""
    for sentence in sentences:
        if len(sentence) == 0:
            continue
        comma_count = 0
        for char in sentence:
            if char in commas:
                comma_count += 1
        result += sentence[comma_count]

    return result
