#!/usr/bin/python3

def roman_to_int(roman_string):
    r_str = roman_string
    val = 0
    if (not isinstance(r_str, str) or (r_str is None)):
        return (val)
    r_numeral = {'I': 1,
                 'V': 5,
                 'X': 10,
                 'L': 50,
                 'C': 100,
                 'D': 500,
                 'M': 1000
                 }
    for i in range(0, len(r_str)):
        x = r_str[i]
        if x in r_numeral:
            p_v = r_numeral[x]
            if i > 0:
                if x in 'VX' and r_str[i - 1] == 'I':
                    p_v -= 2
                elif x in 'LC' and r_str[i - 1] == 'X':
                    p_v -= 20
                elif x in 'DM' and r_str[i - 1] == 'C':
                    p_v -= 200
            if i > 2:
                if x in ('VLD') and (r_str[i - 1] == x):
                    return (0)
            if i + 1 < len(r_str):
                if x in 'IV' and r_str[i + 1] in 'MDCL':
                    return (0)
                elif x in 'X' and r_str[i - 1] in 'MD':
                    return (0)
                if x in 'L' and r_str[i + 1] in 'CDM':
                    return (0)
            val += p_v
        else:
            return (0)
    return (val if val < 4000 else 0)
