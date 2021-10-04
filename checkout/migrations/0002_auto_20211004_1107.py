# Generated by Django 3.2.7 on 2021-10-04 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='original_bag',
        ),
        migrations.RemoveField(
            model_name='order',
            name='stripe_pid',
        ),
        migrations.AlterField(
            model_name='orderlineitem',
            name='artwork_colour',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='orderlineitem',
            name='artwork_request',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='orderlineitem',
            name='product_text_content',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
    ]
