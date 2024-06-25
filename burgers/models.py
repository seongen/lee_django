from django.db import models #django에서 모델을 가져옴

# Create your models here.
class Burger(models.Model): # burger 클래스 정의
    name = models.CharField(max_length=20) # 이름을 나타냄, 문자열을 받음
    price = models.IntegerField(default=0) # 가격을 나타냄 속성을 받아옴
    claories = models.IntegerField(default=0) # 칼로리 역시나 숫자를 받아옴

    # burger class에서 메서드를 추가! 모델 클래스의 인스턴스를 어떻게 나타낼지,,
    def __str__(self):
        return self.name