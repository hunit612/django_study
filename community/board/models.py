from django.db import models


class Board(models.Model):
    title = models.CharField(max_length=128, verbose_name='제목')
    contents = models.TextField(verbose_name='내용')
    writer = models.ForeignKey('user.User', on_delete=models.CASCADE, verbose_name='작성자')
    tags = models.ManyToManyField('tag.Tag', verbose_name='태그')
    registered_dttm = models.DateField(auto_now_add=True, verbose_name='등록시간')


    def __str__(self):
        return self.title

    class Meta:
        db_table = 'community_board'
        verbose_name = '게시글'
        verbose_name_plural = '커뮤니티 사용자'