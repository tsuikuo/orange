# Generated by Django 2.1.4 on 2019-01-08 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('code', models.CharField(db_index=True, max_length=6, primary_key=True, serialize=False)),
                ('policy', models.CharField(max_length=4)),
                ('comments', models.TextField()),
                ('createDay', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('code', models.CharField(db_index=True, max_length=6, primary_key=True, serialize=False)),
                ('createDay', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('code', models.CharField(db_index=True, max_length=6, primary_key=True, serialize=False)),
                ('priceToSell', models.FloatField()),
                ('priceToStop', models.FloatField()),
                ('createDay', models.DateField()),
            ],
        ),
    ]