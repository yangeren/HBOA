from _datetime import datetime
from module import OaDb, db


def save_db():
    b = datetime(2012, 3, 3, 10, 10, 10)
    print(b)
    print(type(b))
    t = datetime.fromtimestamp(1542380400000 / 1000)
    print(t)
    print(type(t))
    # t = datetime.fromtimestamp(1542380400000 / 1000).strftime("%Y-%m-%d %H:%M:%S.%f"),
    # print(t)
    a = OaDb(createTime=t)
    db.session.add(a)
    db.session.commit()


class TestRep(object):

    def __init__(self, obj):
        self.obj = obj

    def __enter__(self):
        print("this is entery")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("this is exit")

    def test_rep(self):
        print("test rep func")


class Celeius:
    def __init__(self, temp=0):
        self.set_temp(temp)

    def get_new_data(self):
        return (self.temp * 8) + 10

    def get_temp(self):
        return self._temp

    def set_temp(self, value):
        if value < -237:
            raise ValueError("adf")
        self._temp = value


if __name__ == '__main__':
    c = Celeius()
    c.get_temp()
    c.set_temp(100)
    m = c.get_new_data()
    print(c.__dict__)
    print(m)

