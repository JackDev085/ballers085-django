# Generated by Django 5.0 on 2024-07-06 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ballers085', '0005_alter_userprofile_link_foto_perfil'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='link_foto_perfil',
            field=models.CharField(default='imgs/usuarios/default.jpg', max_length=100),
        ),
    ]
