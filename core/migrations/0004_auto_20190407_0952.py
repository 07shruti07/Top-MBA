# Generated by Django 2.2 on 2019-04-07 09:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_university_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='university',
            name='program_highlights',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.ProgramHighlights'),
        ),
    ]
