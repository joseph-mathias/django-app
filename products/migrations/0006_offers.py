# Generated by Django 3.1.7 on 2021-04-17 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20210417_0626'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('offers', models.CharField(max_length=100)),
                ('details', models.CharField(max_length=100)),
                ('catergory', models.CharField(max_length=100)),
            ],
        ),
    ]
