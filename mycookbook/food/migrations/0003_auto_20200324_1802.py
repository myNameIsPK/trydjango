# Generated by Django 3.0.4 on 2020-03-24 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_auto_20200324_1801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='food',
            name='materials',
            field=models.TextField(),
        ),
    ]
