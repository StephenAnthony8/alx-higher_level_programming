#!/usr/bin/python3
"""
    1-my_list - Description on module "1-my_list"
"""


class MyList(list):
    """
        MyList - Class that inherits from the properties of class list
    """
    def print_sorted(self, key=None, reverse=False):
        """
            print_sorted - sorts object depending on the parameters given
            @self: object
            @key: sorting parameter dependent on soritng preference
            @reverse: sorts object in ascending or descending if True
        """
        new_list = self.copy()
        new_list.sort(key=key, reverse=reverse)
        print(new_list)
        del new_list
