# 예외 처리
try:
    print("나누기 전용 계산기")
    # num1 = int(input("첫 번째 숫자 입력: "))
    # num2 = int(input("두 번째 숫자 입력: "))
    # print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("에러!값 입력이 잘못됨.")
except ZeroDivisionError as err:
    print(err)
except Exception as err:
    print("알 수 없는 오류")
    print(err)
print("----------------")
# 에러 발생시키기 throw exception
try:
    raise Exception("errrr")
except Exception as err:
    print(err)
print("----------------")


# 사용자 정의 에러
class CustomError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


try:
    raise CustomError("custom error")
except CustomError as err:
    print(err)

print("----------------")
# Finally
try:
    raise Exception
except:
    print("err")
finally:
    print("finally")

print("----------------")

