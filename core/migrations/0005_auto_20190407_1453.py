# Generated by Django 2.2 on 2019-04-07 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20190407_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programhighlights',
            name='avg_salary',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]