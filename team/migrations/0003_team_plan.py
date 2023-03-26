# Generated by Django 4.1.7 on 2023-03-23 13:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0002_plan'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='plan',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='teams', to='team.plan'),
            preserve_default=False,
        ),
    ]
