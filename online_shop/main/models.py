from email.mime import image

from django.db import models


# Create your models here.


class Product(models.Model):
    MOBILE = 'mobile'
    NOTEBOOK = 'notebook'
    PC = 'pc'
    ACC = 'accessories'

    Choice_Group = {
        (MOBILE, 'mobile'),
        (NOTEBOOK, 'notebook'),
        (PC, 'personalComputer'),
        (ACC, 'accessories'),
    }
    name = models.CharField('Имя товара', max_length=100)
    description = models.TextField('Описание товара')
    price = models.IntegerField('Цена товара')
    availability = models.BooleanField('В наличии', default=True)
    group = models.CharField('Группа', max_length=20, choices=Choice_Group, default=MOBILE)
    img = models.ImageField('Картинка', default='noimage.jpg', upload_to='product_image')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
