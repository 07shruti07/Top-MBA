# Generated by Django 2.2 on 2019-04-04 09:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProgramHighlights',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_month', models.CharField(max_length=50)),
                ('class_size', models.CharField(max_length=50)),
                ('avg_work_experience', models.CharField(max_length=50)),
                ('avg_student_age', models.CharField(max_length=50)),
                ('intl_students', models.CharField(max_length=50)),
                ('women_students', models.CharField(max_length=50)),
                ('avg_salary', models.CharField(max_length=50)),
                ('scholarship', models.CharField(max_length=50)),
                ('accreditations', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='university',
            name='more',
        ),
        migrations.AddField(
            model_name='university',
            name='program_highlights',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.ProgramHighlights'),
            preserve_default=False,
        ),
    ]
