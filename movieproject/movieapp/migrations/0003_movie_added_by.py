# Generated by Django 4.2.10 on 2024-03-14 08:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movieapp', '0002_alter_category_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='added_by',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]