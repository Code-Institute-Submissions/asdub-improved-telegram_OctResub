# Generated by Django 3.2.7 on 2021-10-05 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0005_alter_orderlineitem_final_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderlineitem',
            name='final_price',
            field=models.DecimalField(decimal_places=2, editable=False, max_digits=6, null=True),
        ),
    ]
