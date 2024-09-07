
from hw02_03_prime_number import is_prime


def main():
    s = int(input("소수인 숫자를 찾을 범위의 시작 숫자를 쓰세요. => "))
    e = int(input("소수인 숫자를 찾을 범위의 마지막 숫자를 쓰세요. => "))

    primes = []
    for i in range(s, e+1):
        if is_prime(i):
            primes.append(i)
    print(f"{s}부터 {e} 사이에 있는 소수는 {primes}입니다.")



if __name__ == "__main__":
    main()