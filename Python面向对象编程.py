class Car():               #创建类时，一般需要把类的名称首字母大写，这也是定义类的一种规范方式
    """汽车使用的目前价值估计使用程序"""            #类的功能说明与描述程序语句
    def __init__(self, make, model, year):        #当创建类时，Python会自动运行该方法
                                                  #下划线是一种约定，避免Python默认的方法与普通的方法名称冲突
                                                  #self必不可少，并且必须位于其他形参
        self.make = make                          #独立属性传入-可以通过对象来进行访问的变量称为属性，进行对象属性的定义，一般需要将对象的独立属性定义出来
        self.model = model
        self.year = year
        self.this_year=2018                       #默认属性-类的属性修改,一般定义为默认值，不可以在定义对象时传入
    def mod_this_year(self,newyear):             #修改当前年份的第二种方法-定义类的函数来进行修改
        self.this_year=newyear
    def detection(self):                          #类的具体方法定义，在后续对于队形属性的使用时直接访问self即可进行
        duration = self.this_year - self.year
        price = 30 - 2 * duration
        long_time = "你的" + self.make + self.model + "到目前已经行驶了" + str(duration) + "年," + "目前价值为" + str(price) + "万元"
        return long_time
my_car=Car("奥迪","A4","2013")
print(my_car.year)
print(my_car.detection)
my_car = Car("奥迪", "A4", 2013)
my_car.this_year=2020            #方法1对象修改属性值-需要修改对象的属性时必须要通过对象来进行修改，并且修改属性不需要在定义对象时传进去，只需要的属性定义语句中添加类的默认属性和默认值
print(my_car.year)
print(my_car.detection())
your_car=Car("奔驰","c200",2012)
your_car.mod_this_year(2020)     #方法2使用方法定义来进行属性的修改，不需要返回return值，需要进行传入新的参数就可以
print(your_car.detection())
class ElectricCar(Car):
    def __init__(self,make,model,year):
        #使用super()函数可以直接将父类继承给子类
        super().__init__(make,model,year)    #使用super函数可以将子类和父类进行关联，让Python调用父类的方法————init__()
    def battery(self,capacity):
        self.capacity_num=capacity
        print("你选择的电池容量为：",self.capacity_num)
    def detection(self):          #在子类的定义中如果和父类的方法相同，则将进行覆盖。另外对于父类无法使用子类的定义方法，子类可以使用父类的所有方法
        duration = self.this_year - self.year
        price = 30 -  duration-(500/self.capacity_num)
        long_time = "你的" + self.make + self.model + "到目前已经行驶了" + str(duration) + "年," + "目前价值为" + str(price) + "万元"
        return long_time
my_tesla=ElectricCar("Tesla","model-s",2017)
print(my_tesla.year)
my_tesla.this_year=2020
my_tesla.battery(100)
print(my_tesla.detection())

#导入模块的四种方法：
from car_file import Car
from car_file import ElectricCar        #第一种方法
from car_file import Car,ElectricCar    #第二种方法
import car_file  # A.b                  #第三种方法
from car_file import*                   #第四种方法，并不推荐使用，将所有的类直接调用到*所处的位置，容易引起内存爆满，程序不稳定
