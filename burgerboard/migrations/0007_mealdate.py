# Generated by Django 2.2.2 on 2019-06-06 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('burgerboard', '0006_auto_20190606_1428'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mealdate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('next_meal', models.DateTimeField(verbose_name='next meal date')),
            ],
        ),
    ]
