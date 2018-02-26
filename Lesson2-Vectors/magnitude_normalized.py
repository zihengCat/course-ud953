from my_vector import Vector

if __name__ == "__main__":
    my_v = Vector([0.221, 7.437])
    print(my_v.magnitude())
    my_v = Vector([8.813, -1.331, -6.247])
    print(my_v.magnitude())
    #--------------------------
    my_v = Vector([5.581, -2.136])
    print(my_v.normalized())
    my_v = Vector([1.996, 3.108, -4.554])
    print(my_v.normalized())

