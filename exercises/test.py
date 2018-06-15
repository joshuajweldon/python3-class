class Test:
    test = 10

    def __init__(self):
        self.test = 20

    @staticmethod
    def tester():
        pass

    @classmethod
    def testable(cls):
        pass

    @property
    def test(self):
        return self.test

    @test.setter
    def test(self, test):
        self.test = test

    def testing(self):
        print(Test.test)
        print(self.test)

