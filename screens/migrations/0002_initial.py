# Generated by Django 4.1.1 on 2022-09-25 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('theatres', '0001_initial'),
        ('screens', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='screen',
            name='theatre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='screens', to='theatres.theatre'),
        ),
    ]
