# Generated by Django 3.1.3 on 2020-12-03 21:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='organism',
            field=models.ForeignKey(default='na', on_delete=django.db.models.deletion.SET_DEFAULT, to='mainpage.organism'),
        ),
    ]