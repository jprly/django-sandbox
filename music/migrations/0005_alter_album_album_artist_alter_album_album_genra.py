# Generated by Django 4.2.4 on 2023-09-20 14:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0004_alter_album_album_artist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='album_artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.artist'),
        ),
        migrations.AlterField(
            model_name='album',
            name='album_genra',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, to='music.genra'),
        ),
    ]