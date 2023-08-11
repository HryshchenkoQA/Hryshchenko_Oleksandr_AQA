class Traffic_light:
    def __init__(self):
        self.__color = "Green"

    #def __str__(self):
    #    return F"Hi im traffic_light instance and my current color_status is {self.__color} "
    def __repr__(self):
        #return f"color is {self.__color}"
        return 'Traffic_light()'

    def __getattr__(self, item):
        return f"this is not {item} you are looking for"


traffic_light1 = Traffic_light()
print(traffic_light1)
# traffic_light2= eval(repr(traffic_light1))
# print(traffic_light1)
print(traffic_light1.height)
