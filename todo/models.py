from django.db import models

# Create your models here.


class Task(models.Model):
    title = models.CharField("タスク", max_length=50,blank=False)
    description = models.TextField("説明", blank=True)

    class Meta:
        # DBテーブル名
        db_table = "task"
        # DBテーブル名の単数形'/admin'等に表示されるもの
        verbose_name = "task"
        # DBテーブル名の複数形'/admin'等に表示されるもの
        verbose_name_plural = "tasks"
