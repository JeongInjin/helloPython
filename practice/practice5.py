# 함수
def open_account():
    print("새로운 계좌 생성")


open_account()


# 파라미터, return
def deposit(balance, money):
    print("입금완료, 잔액은 {0}원 입니다.".format(balance + money))
    return balance + money


balance = 0
balance = deposit(balance, 1000)
balance = deposit(balance, 2000)
print(balance)
print("----------------")


# 기본값
def profile(name, age, main_lang):
    print("이름: {0}\t나이: {1}\t주 사용 언어: {2}" \
          .format(name, age, main_lang))


profile("가가가", 20, "파이썬")
profile("나나나", 25, "자바")


# default value
def profileDefault(name, age=17, main_lang="파이썬"):
    print("이름: {0}\t나이: {1}\t주 사용 언어: {2}" \
          .format(name, age, main_lang))


profileDefault("다다다")
profileDefault("라라라")

print("----------------")


# 키워드 값

def profileKeyword(name, age, main_lang):
    print(name, age, main_lang)


profileKeyword(name="가나다", age=22, main_lang="코틀린")
profileKeyword(age=23, main_lang="파이썬", name="마바사", )
print("----------------")


# 기변인자
def profileArgs1(name, age, lang1, lang2, lang3, lang4, lang5):
    print("이름: {0}\t나이: {1}\t".format(name, age), end=" ")
    print(lang1, lang2, lang3, lang4, lang5)


profileArgs1("가가가", 20, "Python", "Kotlin", "Java", "C", "C#")


def profileArgs2(name, age, *lang):
    print("이름: {0}\t나이: {1}\t".format(name, age), end=" ")
    for l in lang:
        print(l, end=" ")
    print()


profileArgs2("가가가", 20, "Python", "Kotlin", "Java", "C", "C#")

print("----------------")
# 지역변수, 전역변수
gun = 10


def checkpoint(soldiers):
    global gun
    gun = gun - soldiers
    print("[함수 내] 남은 총: {0}".format(format(gun)))


def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총: {0}".format(format(gun)))
    return gun


print("전체 총: {0}".format(gun))
# checkpoint(2)
gun = checkpoint_ret(gun, 2)
print("전체 총: {0}".format(gun))

print("----------------")
