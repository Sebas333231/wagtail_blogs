# Generated by Django 4.2.6 on 2023-11-02 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_author_caption_alter_author_author_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='correo',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
