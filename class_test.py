#encoding=utf-8

class Animal(object):
    # """docstring for ."构造函数""
    def __init__(self, name,age):
        self.name = name
        self.age = age;

    # def __init__(self):
    #     pass

    def eat(self,arg):
        print(self,"......")
        print("eating .........",arg)

    def run(self):
        print("running .........",self)


class Bird(Animal):
    def fly(self):
        print("flying......")


class Cat(Animal):
    def zhulaoshu(self):
        print("zhulaoshu........")

class Owl(Bird,Cat):
    """docstring for ."""
    def __init__(self,name,age,color):
        super(Owl, self).__init__(name,age)
        # self.name = name
        # self.age = age;
        self.color = color

    def nosleep(self):
        print("no sleeping ......")





# owlA = Owl("owlsss",10,"red")
# print(owlA.name)
# owlA.run()
# owlA.fly()
# owlA.zhulaoshu()
# owlA.nosleep()





class User(object):
    def __init__(self,id):
        self.id = id
    def post(self,title,content):
        print("title:",title)
        print("content:",content)


user = User(100)
print(user.id)
user.post("biaoti A","content contetn")





# birdA = Bird("wangwu",100)
# print(birdA.name)
# birdA.run()
# birdA.fly()
#
#
# animalA = Animal("liuliu",10)
# print(animalA.name)
# animalA.run()
# # animalA.fly()
#
#
# catA = Cat("777787",100)
# print(catA.name)
# catA.run()
# catA.zhulaoshu()
# # catA.fly()



#
#
#
# a = Animal("zhangsan",23)
# a.height = 100;
# print(a.name)
# print(a.age)
# a.eat("aaa")
# a.run()
#
#
#
# b = Animal("lisi",24)
# b.fat = True
# print(b.name)
# print(b.age)
# print(b.fat)
# b.eat("ssss=====")
#
# b = Animal()
#
# print a
# print b
# # print Animal
#
# a.eat("aaaaa")
# eat(a,"aaaaa")
# b.eat("nbbbbbb")
#
#
# a.run()
# b.run()
#
# run(a)
#
# c = Animal()
# a.run()
