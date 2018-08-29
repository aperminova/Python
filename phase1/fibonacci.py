def main():
    print(fib(20))
    print(fib(-5))
    print(fib(1))


def fib(n):
    if n <= 0:
        return "Please enter positive number to generate sequence"
    elif n == 1:
        return 0
    elif n > 1:
        fiblist = [0]
        a, b = 0, 1
        for i in range(n - 1):
            a, b = b, a + b
            fiblist.append(a)
        return fiblist


if __name__ == "__main__":
    main()
