# Generated by Django 4.1.3 on 2024-06-19 21:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rarev2api', '0003_rareusers_alter_posts_rare_user_delete_users'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='RareUsers',
            new_name='RareUser',
        ),
    ]