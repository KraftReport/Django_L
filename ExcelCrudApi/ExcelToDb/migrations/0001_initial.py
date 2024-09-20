# Generated by Django 5.1.1 on 2024-09-20 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_id', models.IntegerField()),
                ('user_name', models.CharField(max_length=100)),
                ('upload_time', models.DateTimeField()),
                ('receive_time', models.DateTimeField()),
                ('description', models.CharField(max_length=500)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
