from odd_even import is_even



def main():
    total = 0

    # for i in range (1, 101):
    #     if is_even(i):
    #         total += i
    # print(f"1부터 100까지 짝수의 합은 {total}입니다.")


    even_100 = [i for i in range(1, 100) if is_even(i)]
    total = 0
    for i in even_100:
        total += 1
    print(f"1부터 100까지 짝수의 합은 {total}입니다.")




if __name__ == "__main__":
    main()