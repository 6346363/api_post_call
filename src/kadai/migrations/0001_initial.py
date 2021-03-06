# Generated by Django 2.0.4 on 2021-03-03 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ai_analysis_log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_path', models.CharField(default='', max_length=255)),
                ('success', models.CharField(default='', max_length=255)),
                ('message', models.CharField(default='', max_length=255)),
                ('class_value', models.IntegerField(db_column='class')),
                ('confidence', models.DecimalField(decimal_places=4,  max_digits=5)),
                ('request_timestamp', models.PositiveIntegerField()),
                ('response_timestamp', models.PositiveIntegerField()),
            ],
        ),
    ]
