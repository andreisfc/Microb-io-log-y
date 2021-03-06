# Generated by Django 3.1.3 on 2020-12-04 02:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0004_auto_20201203_2134'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.AlterField(
            model_name='organism',
            name='slug',
            field=models.SlugField(unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='creationdate',
            field=models.DateTimeField(verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='post',
            name='organism',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='mainpage.organism'),
        ),
        migrations.AlterField(
            model_name='post',
            name='updatedate',
            field=models.DateTimeField(verbose_name='date updated'),
        ),
    ]
