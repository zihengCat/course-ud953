import my_vector as v
if __name__ == '__main__':
    my_v = v.Vector([8.218, -9.341])
    my_w = v.Vector([-1.129, 2.111])
    print(my_v.plus(my_w))
    #-----------------------
    my_v = v.Vector([7.119, 8.215])
    my_w = v.Vector([-8.223, 0.878])
    print(my_v.minus(my_w))
    #-----------------------
    my_v = v.Vector([1.671, -1.012, -0.318])
    my_c = 7.41
    print(my_v.scalar_mul(my_c))

