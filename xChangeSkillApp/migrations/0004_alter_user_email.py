# Generated by Django 3.2.7 on 2021-11-02 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xChangeSkillApp', '0003_alter_user_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='email'),
        ),
    ]
