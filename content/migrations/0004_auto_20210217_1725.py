# Generated by Django 3.1.6 on 2021-02-17 17:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_homepageitem'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homepageitem',
            old_name='item_button_text',
            new_name='button_text',
        ),
        migrations.RenameField(
            model_name='homepageitem',
            old_name='item_content',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='homepageitem',
            old_name='item_heading',
            new_name='heading',
        ),
        migrations.RenameField(
            model_name='homepageitem',
            old_name='item_image',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='homepageitem',
            old_name='item_link',
            new_name='link',
        ),
    ]
