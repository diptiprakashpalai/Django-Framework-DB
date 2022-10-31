# Generated by Django 4.1.1 on 2022-10-22 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyPage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author_nationality',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='is_bestselling',
            field=models.BooleanField(default=False),
        ),
    ]
