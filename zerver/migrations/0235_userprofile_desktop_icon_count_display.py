# Generated by Django 1.11.20 on 2019-06-29 18:22

from django.db import migrations, models


DESKTOP_ICON_COUNT_DISPLAY_MESSAGES = 1
class Migration(migrations.Migration):

    dependencies = [
        ('zerver', '0234_add_external_account_custom_profile_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='desktop_icon_count_display',
            field=models.PositiveSmallIntegerField(default=DESKTOP_ICON_COUNT_DISPLAY_MESSAGES),
        ),
    ]
