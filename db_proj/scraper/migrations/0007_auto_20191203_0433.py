# Generated by Django 2.2.1 on 2019-12-03 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0006_review_added_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='instructor',
            name='rating',
            field=models.DecimalField(decimal_places=2, default=5.0, max_digits=3),
        ),
        migrations.AddField(
            model_name='section',
            name='meeting_times',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
