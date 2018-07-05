class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y


    def __repr__(self):
        return "Я - точка: координата_x {} координата_y {}".format(self.__x, self.__y)
    @property
    def x(self):
        return self.__x
    @property
    def y(self):
        return self.__y

    @x.setter
    def x(self, n):
        if isinstance(n, int):
            self.__x = n
        else:
            return "Coordinats must be numbers"

    @y.setter
    def y(self, n):
        if isinstance(n, int):
            self.__y = n
        else:
            return "Coordinats must be numbers"

    def move_to(self, x, y):
        self.x = x
        self.y = y

    def move_by(self, x, y):
        self.x += x
        self.y += y

    # def get_x(self):
    #     return self.__x
    #
    # def get_y(self):
    #     return self.__y
    #
    # def set_x(self, n):
    #     self.__x = n
    #
    # def set_y(self, n):
    #     self.__y = n
    #
    # x = property(get_x, set_x)
    # y=property(get_y, set_y)
    #
    # def move_to(self, x, y):
    #     self.set_x(x)
    #     self.set_y(y)
    #
    # def move_by(self, x, y):
    #     self.set_x(self.__x + x)
    #     self.set_y(self.__y + y)


point = Point(20, 20)
point.move_to(30, "30")
#point.y = 60
#point.x = 60
#print(point.y)
print(point)