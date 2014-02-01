from test1.bar import bar
from carburetor.word import generate


def foo():
    print "foo fighters"
    bar()
    print generate(10)

if __name__ == '__main__':
    foo()
