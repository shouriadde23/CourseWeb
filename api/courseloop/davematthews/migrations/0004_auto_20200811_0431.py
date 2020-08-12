# Generated by Django 3.1 on 2020-08-11 04:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('davematthews', '0003_auto_20200810_2250'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='frq',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='davematthews.frqassignment'),
        ),
        migrations.AddField(
            model_name='submission',
            name='ws',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='davematthews.wsassignment'),
        ),
    ]
