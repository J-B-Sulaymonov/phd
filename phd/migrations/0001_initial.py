# Generated by Django 5.0.4 on 2024-04-08 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shakil_yasovchi_qushimchalar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=1000)),
            ],
            options={
                'verbose_name': "Shakil yasovchi qo'shimchalar",
                'verbose_name_plural': "Shakil yasovchi qo'shimchalar",
            },
        ),
        migrations.CreateModel(
            name='Suz_uzgartiruvchilar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=1000)),
            ],
            options={
                'verbose_name': "So'z o'zgartiruvchilar",
                'verbose_name_plural': "So'z o'zgartiruvchilar",
            },
        ),
        migrations.CreateModel(
            name='Suzlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=1000)),
            ],
            options={
                'verbose_name': "So'zlar",
                'verbose_name_plural': "So'zlar",
            },
        ),
        migrations.CreateModel(
            name='UZB_affiks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=1000)),
            ],
            options={
                'verbose_name': "O'zb affiks",
                'verbose_name_plural': "O'zb affiks",
            },
        ),
    ]
