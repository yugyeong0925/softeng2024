from hw02_01_odd_even import is_even



def main():
    total = 0
    n = int(input("짝수의 합을 구할 범위의 마지막 숫자를 입력하세요. => "))

    for i in range (1, n+1):
        if is_even(i):
            total += i
    print(f"1부터 {n}까지 짝수의 합은 {total}입니다.")




if __name__ == "__main__":
    main()