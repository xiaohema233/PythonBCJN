# Generated by Django 2.2 on 2019-05-30 05:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now_add=True, verbose_name='更新时间')),
                ('is_delete', models.DateTimeField(auto_now_add=True, verbose_name='删除标记')),
                ('name', models.CharField(max_length=20, verbose_name='种类名称')),
            ],
            options={
                'verbose_name': '种类',
                'verbose_name_plural': '种类',
                'db_table': 'df_type',
            },
        ),
        migrations.CreateModel(
            name='TypeDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now_add=True, verbose_name='更新时间')),
                ('is_delete', models.DateTimeField(auto_now_add=True, verbose_name='删除标记')),
                ('name', models.CharField(max_length=20, verbose_name='具体名称')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ajax.Type', verbose_name='种类名称')),
            ],
            options={
                'verbose_name': '具体类型',
                'verbose_name_plural': '具体类型',
                'db_table': 'df_type_detail',
            },
        ),
    ]
