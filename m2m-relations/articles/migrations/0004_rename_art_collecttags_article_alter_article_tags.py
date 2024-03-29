# Generated by Django 5.0 on 2024-02-20 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_rename_tag_tags_collecttags_alter_article_tags_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='collecttags',
            old_name='art',
            new_name='article',
        ),
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(related_name='article', through='articles.CollectTags', to='articles.tags'),
        ),
    ]
