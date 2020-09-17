from django.db import models

class User(models.Model):
    userid = models.CharField(max_length = 50)
    password = models.CharField(max_length = 100)
    user_name = models.CharField(max_length = 50)
    address = models.CharField(max_length = 100)
    telephone = models.IntegerField()
    phonenumber = models.IntegerField()
    email = models.CharField(max_length = 100)
    sex = models.CharField(max_length=1, choices=(('M', '남자'), ('F', '여자')))
    birthday = models.DateField(max_length=1, choices=(('S', '양력'), ('L', '음력')), null=True)
    area = [
        ('1', '경기'),
        ('2', '서울'),
        ('3', '인천'),
        ('4', '강원'),
        ('5', '충남'),
        ('6', '충북'),
        ('7', '대전'),
        ('8', '경북'),
        ('9', '경남'),
        ('10', '대구'),
        ('11', '부산'),
        ('12', '울산'),
        ('13', '전북'),
        ('14', '전남'),
        ('15', '광주'),
        ('16', '제주'),
        ('17', '해외'),
    ]
    area = models.CharField(max_length=2, choices=area)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'user'
