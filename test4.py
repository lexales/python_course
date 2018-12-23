import random

def random_alpha(string_in):
    str_out = ''
    for word in string_in:
        str_middle = word[1:len(word) - 1]
        str_out +=word[0] + ''.join(random.sample(str_middle, len(str_middle))) + word[len(word) - 1] + ' '
    return str_out


if __name__ == "__main__":
    print(random_alpha(input().split()))