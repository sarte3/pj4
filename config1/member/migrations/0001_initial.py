# Generated by Django 3.1.5 on 2021-01-07 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('pw', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('hp', models.CharField(max_length=50)),
                ('regdate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]