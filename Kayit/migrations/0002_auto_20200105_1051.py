# Generated by Django 3.0.2 on 2020-01-05 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Kayit', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='kayitmodel',
            name='eposta',
            field=models.EmailField(default='aa@a.com', max_length=254),
        ),
        migrations.AddField(
            model_name='kayitmodel',
            name='telefon',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='kayitmodel',
            name='tcKimlikNo',
            field=models.BigIntegerField(default=0),
        ),
    ]
