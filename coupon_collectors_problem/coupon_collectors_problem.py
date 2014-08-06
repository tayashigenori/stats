
def sum_inverse_n(n):
    sum = 0
    for i in range(1, n+1):
        sum += float(1) / float(i)
    return sum


def main():
    N = 100
    for n in range(N):
        hn = sum_inverse_n(n)
        print "%d,%f,%.1f" %(n, hn, n*hn)


if __name__ == '__main__':
    main()
