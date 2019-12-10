from car_file import Car,ElectricCar
my_car = Car("奥迪", "A4", 2013)
my_car.this_year=2020            #方法1对象修改属性值-需要修改对象的属性时必须要通过对象来进行修改，并且修改属性不需要在定义对象时传进去，只需要的属性定义语句中添加类的默认属性和默认值
print(my_car.year)
print(my_car.detection())
your_car=Car("奔驰","c200",2012)
your_car.mod_this_year(2020)     #方法2使用方法定义来进行属性的修改，不需要返回return值，需要进行传入新的参数就可以
print(your_car.detection())
my_tesla=ElectricCar("Tesla","model-s",2017)
print(my_tesla.year)
my_tesla.this_year=2020
my_tesla.battery(100)
print(my_tesla.detection())


