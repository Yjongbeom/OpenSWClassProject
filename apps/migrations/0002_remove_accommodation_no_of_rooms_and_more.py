# Generated by Django 5.1.3 on 2024-11-21 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accommodation',
            name='no_of_rooms',
        ),
        migrations.RemoveField(
            model_name='accommodation',
            name='urls',
        ),
        migrations.AddField(
            model_name='accommodation',
            name='review',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='accommodation',
            name='review_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='accommodation',
            name='number',
            field=models.CharField(default='000-0000-0000', max_length=20),
        ),
    ]
