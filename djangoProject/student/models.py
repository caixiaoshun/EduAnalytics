from django.db import models


# Create your models here.
class Student(models.Model):
    # 学号字段，使用CharField类型，最大长度为20，不允许为空
    # 学号通常是唯一的，因此设置unique=True
    student_id = models.CharField(max_length=20, unique=True, verbose_name='学号')

    # 姓名字段，使用CharField类型，最大长度为50，不允许为空
    name = models.CharField(max_length=50, verbose_name='姓名')

    # 性别字段，使用CharField类型，最大长度为10，允许为空
    # 通常性别字段存储'男'或'女'，因此设置choices参数为性别选项
    gender = models.CharField(
        max_length=10,
        blank=True,
        choices=[('男', '男'), ('女', '女')],
        verbose_name='性别'
    )

    # 所在班级字段，使用CharField类型，最大长度为50，允许为空
    class_name = models.CharField(max_length=50, blank=True, verbose_name='所在班级')

    def __str__(self):
        # 定义模型的字符串表示，通常返回一个可读的字符串
        return (f"姓名：{self.name}, 学号：{self.student_id}, 性别：{self.gender}, 所在班级：{self.class_name}"
                ).strip()

    class Meta:
        # 模型的元数据
        # 设置表名为'student'
        db_table = 'student'
        # 可以添加其他元数据选项，如ordering, verbose_name等
