from django.db import models

# Create your models here.

class Order(models.Model):
    fcuser = models.ForeignKey('fcuser.Fcuser', on_delete=models.CASCADE, verbose_name='사용자')
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE, verbose_name='상품')
    quantity = models.IntegerField(verbose_name='수량')
    register_date = models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')

    def __str__(self):
        return str(self.fcuser) + ' ' + str(self.product)

    # Meta클래스는 권한, 데이터베이스 이름, 단 복수 이름, 추상화, 순서 지정 등과 같은 모델에 대한 다양한 사항을 정의하는 데 사용할 수 있습니다.
    # https://www.delftstack.com/ko/howto/django/class-meta-in-django/
    class Meta:
        db_table = 'order'
        verbose_name = '주문'
        verbose_name_plural = '주문'