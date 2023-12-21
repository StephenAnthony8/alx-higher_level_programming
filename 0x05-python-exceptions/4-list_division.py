#!/usr/bin/python3

# list_division - divides elements of 2 lists
# my_list_1: numerator list
# my_list_2: denominator list
# list_length: index count
# Return: list containing div values
def list_division(my_list_1, my_list_2, list_length):
    n_list = []
    for i in range(0, list_length):
        try:
            result = (my_list_1[i] / my_list_2[i])
        except TypeError:
            result = 0
            print("{}".format("wrong type"))
        except ZeroDivisionError:
            result = 0
            print("{}".format("division by 0"))
        except IndexError:
            result = 0
            print("{}".format("out of range"))
        finally:
            n_list.append(result)
    return (n_list)
