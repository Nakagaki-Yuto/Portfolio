# Generated by Django 3.1.1 on 2020-10-05 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='approved_comment',
            field=models.BooleanField(default=True),
        ),
        migrations.DeleteModel(
            name='Like',
        ),
    ]