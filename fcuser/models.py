from django.db import models

# Create your models here.

class Fcuser(models.Model):
    email = models.EmailField(verbose_name='이메일')
    password = models.CharField(max_length=64, verbose_name='비밀번호')
    register_date = models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')

    def __str__(self):
        return self.email

    # Meta클래스는 권한, 데이터베이스 이름, 단 복수 이름, 추상화, 순서 지정 등과 같은 모델에 대한 다양한 사항을 정의하는 데 사용할 수 있습니다.
    # https://www.delftstack.com/ko/howto/django/class-meta-in-django/
    class Meta:
        db_table = 'fcuser'
        verbose_name = '사용자'
        verbose_name_plural = '사용자'