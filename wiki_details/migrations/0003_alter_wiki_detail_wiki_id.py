# Generated by Django 4.2.1 on 2023-05-22 16:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("wikis", "0002_remove_wiki_detail_id"),
        ("wiki_details", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="wiki_detail",
            name="wiki_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="wiki_details",
                to="wikis.wiki",
            ),
        ),
    ]
