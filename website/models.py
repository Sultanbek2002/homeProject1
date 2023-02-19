from django.db import models
import uuid
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField


# Create your models here.
class Workers(models.Model):
    company_choice = (
        ('Баткен Stream', 'Баткен Stream'),
        ('Яндекс', 'Яндекс'),
        ('Байбол', 'Байбол'),
        ('Алга', 'Алга'),
        ('Бат такси', 'Бат такси'),
    )
    direction_choices = (
        ('BAT_BUJ', 'Баткен-Бужум'),
        ('BAT_SAM', 'Баткен-Самаркандек'),
        ('SAM_AT', 'Самаркандек-Ак-Татыр'),
        ('BAT_LEY', 'Баткен-Лейлек'),
        ('ISF_KAD', 'Исфана-Кадамжай'),
        ('KYZ_KAD', 'Кызыл_Кыя-Кадамжай'),
    )
    working_choi = (
        ('Понедельник', 'Понедельник'),
        ('Вторник', 'Вторник'),
        ('Среда', 'Среда'),
        ('Четверть', 'Четверть'),
        ('Пятница', 'Пятница'),
        ('Суббота', 'Суббота')
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), blank=False, editable=False, unique=False)
    name = models.CharField(max_length=300, null=True)
    last_name = models.CharField(max_length=300)
    age = models.IntegerField()
    company = models.CharField(max_length=100, choices=company_choice)
    transport = models.CharField(max_length=100)
    tr_number = models.CharField(max_length=20, default="xx xx xx x")
    direction = models.CharField(max_length=300, choices=direction_choices)
    places = models.IntegerField()
    working_days = MultiSelectField(max_length=400, choices=working_choi)
    description = RichTextField(max_length=500)
    url_instagram = models.URLField(blank=True)
    date_creat = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='photo/%Y/%m/%d', null=True)

    def __str__(self):
        return self.name + " " + self.last_name
