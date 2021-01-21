from django.db import models

# 테이블 -> 하나의 클래스
# 테이블의 컬럼 -> 클레스의 변수
# 기본키 컬럼은 id로 자동 생성
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    
    # toString()
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    # 외래키 제약 설정
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text