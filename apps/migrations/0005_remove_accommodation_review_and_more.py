# Generated by Django 5.1.3 on 2024-11-21 12:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0004_remove_accommodation_review_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accommodation',
            name='review',
        ),
        migrations.AlterField(
            model_name='accommodation',
            name='ranks',
            field=models.DecimalField(decimal_places=1, default=0.0, max_digits=3),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('content', models.TextField()),
                ('rating', models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('accommodation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='apps.accommodation')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='apps.user')),
            ],
        ),
    ]
