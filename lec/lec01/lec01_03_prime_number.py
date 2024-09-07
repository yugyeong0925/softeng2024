

def is_prime(n: int):
    #n이 음수이면 소수가 아님
    if n <= 1:
        #False=소수가 아님
        return False
    
    for i in range(2, n):
        #입력한 숫자를 2부터 입력한 숫자까지 나눠서 나머지가 0이 되는 것이 있으면 소수임
        if n % i == 0:
            #소수가 아님
            return False

    #소수임    #들여쓰기나 위에 안 붙여서 써도 되나? 이렇게 하면 무조건 트루만 리턴되는 거 아닌가?
    return True


def main():
    num = int(input("소수인지 확인할 숫자를 입력하세요. -> "))

    if is_prime(num):
        print(f"{num}은 소수입니다.")

    else:
        print(f"{num}은 소수가 아닙니다.")


if __name__ == "__main__":
    main()

