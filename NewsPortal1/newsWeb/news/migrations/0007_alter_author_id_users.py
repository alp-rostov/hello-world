# Generated by Django 4.0.6 on 2022-07-22 17:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0006_alter_comments_id_users_alter_post_head_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='id_users',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
