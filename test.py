def louti(n : int) -> int:
    if n <= 0:
        return -1
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        a : int = 2
        b : int = 3
        for _ in range(3, n):
            a, b = b, a+b
        return b

def main() -> None:
    n = int(input('input a num:'))
    print(louti(n))

if __name__ == '__main__':
    main()