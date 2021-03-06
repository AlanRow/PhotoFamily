# Generated by Django 3.0.2 on 2020-01-11 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('patronimyc', models.CharField(max_length=50, null=True)),
                ('sex', models.CharField(choices=[('m', 'Man'), ('w', 'Woman')], max_length=1)),
                ('birth', models.DateField(null=True)),
                ('birthplace', models.CharField(max_length=100, null=True)),
                ('spec', models.CharField(max_length=100, null=True)),
                ('bio', models.TextField(null=True)),
            ],
        ),
    ]
