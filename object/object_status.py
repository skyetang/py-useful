# coding:utf-8

# 1、书写一个父类
class AiyaFather(object):
    def talk(self):
        print('aiya的爸爸说了一句话')


# 2、书写一个子类，并且继承一个父类, 同一个talk函数，处理的结果确有不同，这就是多态
class AiyaBrother(AiyaFather):
    def run(self):
        print('aiya的哥哥在奔跑')

    def talk(self):
        print('aiay的哥哥在说话')

# 为什么要去多态?
# 为什么要去继承父类?
# 答案：为了使用已经写好的类中的函数，为了保留子类中某个和父类名称一样的函数功能，这时候，我们就用到了类的多态
# 可以帮助我们保留子类中的函数功能


class Aiya(AiyaFather):
    def talk(self):
        print('aiya也可以说自己的观点')


if __name__ == '__main__':
    aiya_brother = AiyaBrother()
    aiya_brother.talk()
    aiya_father = AiyaFather()
    aiya_father.talk()
    aiya = Aiya()
    aiya.talk()