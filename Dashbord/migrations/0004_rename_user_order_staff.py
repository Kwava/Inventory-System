# Generated by Django 5.1.1 on 2024-11-10 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Dashbord', '0003_alter_order_options_alter_product_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='user',
            new_name='staff',
        ),
    ]