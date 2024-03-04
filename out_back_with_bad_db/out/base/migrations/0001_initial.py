# Generated by Django 5.0.2 on 2024-03-04 05:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DivisionsInst',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, db_collation='utf8mb3_general_ci', max_length=255, null=True)),
            ],
            options={
                'db_table': 'divisions_inst',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, db_collation='utf8mb3_general_ci', max_length=255, null=True)),
            ],
            options={
                'db_table': 'faculty',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_namber', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Profiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, db_collation='utf8mb3_general_ci', max_length=255, null=True)),
            ],
            options={
                'db_table': 'profiles',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Streams',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, db_collation='utf8mb3_general_ci', max_length=255, null=True)),
                ('full_name', models.CharField(blank=True, db_collation='utf8mb3_general_ci', max_length=255, null=True)),
                ('code', models.CharField(blank=True, db_collation='utf8mb3_general_ci', max_length=255, null=True)),
                ('year', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'streams',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.IntegerField(blank=True, null=True)),
                ('stud_id', models.IntegerField(blank=True, null=True)),
                ('category', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'student',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='StudentOtchet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_ya', models.IntegerField(blank=True, null=True)),
                ('status', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'student_otchet',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='StudentPractic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme', models.CharField(blank=True, db_collation='utf8mb3_general_ci', max_length=255, null=True)),
                ('status', models.IntegerField(blank=True, null=True)),
                ('company_path', models.CharField(blank=True, db_collation='utf8mb3_general_ci', max_length=255, null=True)),
            ],
            options={
                'db_table': 'student_practic',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(blank=True, db_collation='utf8mb3_general_ci', max_length=255, null=True)),
                ('post', models.CharField(blank=True, db_collation='utf8mb3_general_ci', max_length=255, null=True)),
                ('work_load', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'teachers',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Templates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, db_collation='utf8mb3_general_ci', max_length=255, null=True)),
                ('decanat_check', models.IntegerField(blank=True, null=True)),
                ('comment', models.CharField(blank=True, db_collation='utf8mb3_general_ci', max_length=255, null=True)),
                ('date', models.CharField(blank=True, db_collation='utf8mb3_general_ci', max_length=255, null=True)),
            ],
            options={
                'db_table': 'templates',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Companies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, db_collation='utf8mb3_general_ci', max_length=255, null=True)),
            ],
            options={
                'db_table': 'companies',
            },
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, db_collation='utf8mb3_general_ci', max_length=255, null=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='base.companies')),
            ],
        ),
    ]
