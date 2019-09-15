#°´Ðò´òÓ¡
#2019-08-16 00:31:03

from threading import Lock, Condition
class Foo:
    def __init__(self):
        self.cv = Condition()
        self.num = 0

    def first(self, printFirst: 'Callable[[], None]') -> None:
        with self.cv:
            while self.num != 0:
                self.cv.wait()
            printFirst()
            self.num += 1
            self.cv.notify_all()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        with self.cv:
            while self.num != 1:
                self.cv.wait()
            printSecond()
            self.num += 1
            self.cv.notify_all()

    def third(self, printThird: 'Callable[[], None]') -> None:
        with self.cv:
            while self.num != 2:
                self.cv.wait()
            printThird()
