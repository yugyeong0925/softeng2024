

def factorial(n):
    # 기저 조건: n이 0이면 1을 반환
    if n == 0:
        return 1
    # 재귀 호출: n × (n-1)!로 팩토리얼 계산
    else:
        return n * factorial(n - 1)



def main():
    num = int(input("팩토리얼 값을 구할 숫자를 입력하세요. => "))
    print(factorial(num))


if __name__ == "__main__":
    main() 
