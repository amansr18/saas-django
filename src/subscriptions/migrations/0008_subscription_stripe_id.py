# Generated by Django 5.0.9 on 2024-09-17 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0007_usersubscription'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='stripe_id',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
