# Generated by Django 5.1.3 on 2024-12-06 06:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("myweb", "0006_remove_orderdetail_id_alter_orderdetail_order_id_and_more"),
    ]

    operations = [
        migrations.DeleteModel(
            name="OrderDetail",
        ),
    ]