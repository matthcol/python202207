from point import Point

def Run():
    print("Application Géométrie")
    a = Point(1, 1)
    b = Point(3, 8)
    print(f"Distance entre a et b : {a.distance(b)}" )

def fibonacci(n):
    a = 0
    b = 1
    yield a
    yield b
    for _ in range(0, n-1):
        a, b = b, a+b
        yield b


if __name__=="__main__":
    fibo5=fibonacci(5)
    print(fibo5)
    print(list(fibo5))
    Run()

if __name__!="__main__":
    print(__name__)
