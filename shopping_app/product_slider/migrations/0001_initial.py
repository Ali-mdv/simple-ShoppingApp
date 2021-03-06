# Generated by Django 3.2.7 on 2021-09-25 17:37

from django.db import migrations, models
import extentions.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='عنوان')),
                ('link', models.URLField(max_length=50, verbose_name='لینک')),
                ('description', models.TextField(max_length=50, verbose_name='توضیحات')),
                ('image', models.ImageField(upload_to=extentions.utils.change_name, verbose_name='عکس')),
            ],
            options={
                'verbose_name': 'اسلاید',
                'verbose_name_plural': 'اسلاید',
            },
        ),
    ]
