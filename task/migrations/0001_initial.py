# Generated by Django 5.0.6 on 2024-06-02 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_title', models.CharField(max_length=100)),
                ('task_discription', models.TextField()),
                ('is_completed', models.BooleanField(default=False)),
                ('task_assign_date', models.DateField()),
                ('category', models.ManyToManyField(to='category.categorymodel')),
            ],
        ),
    ]
