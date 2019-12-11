# Generated by Django 3.0 on 2019-12-11 14:50

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
                ('category', models.IntegerField(choices=[(0, 'Unexpected'), (1, 'Car'), (7, 'House'), (5, 'Family'), (4, 'Technologies'), (6, 'Education'), (3, 'Hobbies'), (2, 'Shopping')], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Funds',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sum_of_founds', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField()),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('birthday', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('value', models.FloatField()),
                ('sender', models.CharField(max_length=50)),
                ('category', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='makarena.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('value', models.FloatField()),
                ('recipient', models.CharField(max_length=50)),
                ('category', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='makarena.Category')),
            ],
        ),
    ]
