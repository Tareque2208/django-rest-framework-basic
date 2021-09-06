# Generated by Django 3.2.6 on 2021-09-06 06:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_basic', '0003_article_rating'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tag',
            old_name='tagNumber',
            new_name='desc',
        ),
        migrations.RenameField(
            model_name='tag',
            old_name='tagTitle',
            new_name='title',
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api_basic.tag'),
        ),
    ]
