# Generated by Django 2.0.4 on 2021-03-09 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kadai', '0002_auto_20210308_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ai_analysis_log',
            name='image_path',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='ai_analysis_log',
            name='message',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='ai_analysis_log',
            name='success',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]