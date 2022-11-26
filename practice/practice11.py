# 모듈

import theater_module

theater_module.price_morning(3)
theater_module.price_morning(4)
theater_module.price_soldier(5)
print("----------------")

import theater_module as mv

mv.price_morning(3)
mv.price_morning(4)
mv.price_soldier(5)
print("----------------")

from theater_module import *
price(3)
price_morning(4)
price_soldier(5)

print("----------------")

from theater_module import price, price_morning
price(5)
price_morning(7)

print("----------------")
from theater_module import price_soldier as sp
sp(5)


print("----------------")
# import 는 가장 뒤에는 모듈이나 패키지만 가능하다.(from import 는 가능)
# 패키지
# import trarvel.thailand
# trip_to = trarvel.thailand.ThailandPackage()
# trip_to.detail()
#
# from trarvel import vietnam
# trip_to2 = vietnam.VietnamPackage()
# trip_to2.detail()

# __all__
# __init__.py 에서 open 될 패키지명을 정의해 줘야한다. __all__
from trarvel import *
trip_to3 = vietnam.VietnamPackage()
trip_to3.detail()

print("----------------")
# 모듈 직접 실행
# __name__ 구문으로 지정할 수 있음 ThailandPackage 참조
print("----------------")

# 파일의 위치 파악?

import inspect
import random
print(inspect.getfile(random))
print(inspect.getfile(thailand))

