# Generated by Django 3.2.7 on 2021-10-05 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_auto_20211005_1212'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderlineitem',
            name='final_price',
            field=models.IntegerField(default=0),
        ),
    ]
