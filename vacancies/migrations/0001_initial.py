# Generated by Django 3.1.7 on 2021-04-12 09:32

from django.conf import settings
from django.db import migrations, models
import django.utils.timezone
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название компании')),
                ('location', models.CharField(max_length=50, verbose_name='География')),
                ('logo', models.ImageField(blank=True, default='company_images/default.png',
                                           upload_to='company_images', verbose_name='Логотип')),
                ('description', models.CharField(max_length=100, verbose_name='Информация о компании')),
                ('employee_count', models.IntegerField(verbose_name='Количество человек в компании')),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT,
                                               related_name='owner_of_company', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Specialty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=40)),
                ('title', models.CharField(max_length=50)),
                ('picture', models.ImageField(upload_to='speciality_images')),
            ],
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название вакансии')),
                ('skills', models.CharField(max_length=200, verbose_name='Требуемые навыки')),
                ('description', models.TextField(verbose_name='Описание вакансии')),
                ('salary_min', models.IntegerField(verbose_name='Зарплата от')),
                ('salary_max', models.IntegerField(verbose_name='Зарплата до')),
                ('published_at', models.DateField(default=django.utils.timezone.now)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                              related_name='vacancies', to='vacancies.company')),
                ('specialty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                                related_name='vacancies', to='vacancies.specialty',
                                                verbose_name='Специализация')),
            ],
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('surname', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('status', models.CharField(choices=[('NOT_LOOKING', 'Не ищу работу'),
                                                     ('CONSIDER', 'Рассматриваю предложения'),
                                                     ('LOOKING', 'Ищу работу')],
                                            max_length=24,
                                            verbose_name='Готовность к работе')),
                ('salary', models.IntegerField(verbose_name='Ожидаемое вознаграждение')),
                ('grade', models.CharField(choices=[('TRAINEE', 'Стажер'),
                                                    ('JUNIOR', 'Джуниор'),
                                                    ('MIDDLE', 'Миддл'),
                                                    ('SENIOR', 'Сеньор'),
                                                    ('LID', 'Лид')],
                                           max_length=24, verbose_name='Квалификация')),
                ('education', models.TextField(verbose_name='Образование')),
                ('experience', models.TextField(verbose_name='Опыт работы')),
                ('portfolio', models.URLField(verbose_name='Ссылка на партфолио')),
                ('specialty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                                related_name='resume',
                                                to='vacancies.specialty',
                                                verbose_name='Специализация')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT,
                                              related_name='resume', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('written_username', models.CharField(max_length=100, verbose_name='Имя')),
                ('written_phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='RU',
                                                                                 unique=True, verbose_name='Телефон')),
                ('written_cover_letter', models.TextField(verbose_name='Сопроводительное письмо')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                           related_name='applications', to=settings.AUTH_USER_MODEL)),
                ('vacancy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                              related_name='applications', to='vacancies.vacancy')),
            ],
        ),
    ]