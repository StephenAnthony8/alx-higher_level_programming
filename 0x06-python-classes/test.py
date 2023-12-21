def create_adder(x):
    def adder(y):
        return x+y
 
    return adder
 
add_15 = create_adder(15)
 
print(add_15(10))


def sum_xy(z):
    def sum_yx(a):
        return(z + a)
    b = sum_yx(15)
    return(b)

print(sum_xy(10))