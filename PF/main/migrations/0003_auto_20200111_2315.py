# Generated by Django 3.0.2 on 2020-01-11 18:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_man_marriage_woman'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('father', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Man')),
                ('mother', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Woman')),
            ],
        ),
        migrations.AddField(
            model_name='person',
            name='parents',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Parents'),
        ),
    ]
