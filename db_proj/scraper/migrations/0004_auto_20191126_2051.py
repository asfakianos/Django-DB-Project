# Generated by Django 2.2.1 on 2019-11-26 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0003_auto_20191126_2050'),
    ]

    operations = [
        migrations.AddField(
            model_name='instructor',
            name='case_id',
            field=models.CharField(default='DEFAULT', max_length=10, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='name',
            field=models.CharField(default='DEFAULT', max_length=30),
        ),
    ]