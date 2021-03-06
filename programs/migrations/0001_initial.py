# Generated by Django 2.2 on 2021-04-05 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='enter category name', max_length=50, unique=True, verbose_name='Category')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='add the name', max_length=100, verbose_name='Course')),
                ('description', models.TextField(blank=True, help_text='add some description', verbose_name='Course description')),
                ('last_changed', models.DateTimeField(auto_now=True, verbose_name='Date of change')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Date of creation')),
                ('status', models.CharField(choices=[('d', 'course is in the draft'), ('w', 'course is working'), ('a', 'course is in the archive')], default='d', max_length=1, verbose_name='Status')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='programs.Category')),
            ],
            options={
                'verbose_name': 'Course',
                'verbose_name_plural': 'Courses',
                'ordering': ['-last_changed', 'name'],
            },
        ),
    ]
