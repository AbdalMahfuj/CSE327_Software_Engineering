# Generated by Django 3.2.6 on 2021-09-13 02:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('class', '0005_alter_readingreview_comtime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='class_code',
            field=models.CharField(default='R2ZaOKWA', max_length=120),
        ),
        migrations.AlterField(
            model_name='material',
            name='dueTime',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]
