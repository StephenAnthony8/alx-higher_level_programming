#!/usr/bin/python3

def multiple_returns(sentence):
    l_s = len(sentence)
    f_c = sentence[0] if sentence else "None"
    r_t = tuple([l_s, f_c])
    return (r_t)


if __name__ == "__main__":
    multiple_returns(sentence)
