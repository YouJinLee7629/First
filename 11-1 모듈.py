import theater_module
theater_module.price(3) # 3명 가격
theater_module.price_morning(4) # 4명 조조 할인 가격
theater_module.price_soldier(1) # 1명 군인 할인 가격

import theater_module as mv # mv 로 줄이기
mv.price(3)
mv.price_morning(4)
mv.price_soldier(1)

from theater_module import *
# from random ipmort *
price(3)
price_morning(4)
price_soldier(1)

from theater_module import price, price_morning
price(5)
price_morning(3)
price_soldier(2) # 오류가 남

from theater_module import price_soldier as price
price(5)