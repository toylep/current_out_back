# Generated by Django 5.0.2 on 2024-04-15 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='practice',
            name='name',
            field=models.CharField(db_collation='utf8mb3_general_ci', max_length=255, null=True),
        ),
    ]