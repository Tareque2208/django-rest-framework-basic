# Generated by Django 3.2.6 on 2021-09-06 06:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_basic', '0002_articlerating_course_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='rating',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='api_basic.articlerating'),
        ),
    ]
