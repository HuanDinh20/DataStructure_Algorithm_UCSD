import sys

def get_change(money):
    #write your code here
    return money // 10 + (money % 10) // 5 + money % 5

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))