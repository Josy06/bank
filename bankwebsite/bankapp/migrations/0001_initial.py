# Generated by Django 4.1.3 on 2022-12-03 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=300)),
                ('Img', models.ImageField(upload_to='photo')),
                ('Role', models.TextField()),
            ],
        ),
    ]
