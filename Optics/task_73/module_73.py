import Uncertainty as un

v = [344, 343.33, 354.375, 352, 359.375]

print("u(y) = {}\nU(y)= {}".format(un.ux(v),un.ux(v) * 3))