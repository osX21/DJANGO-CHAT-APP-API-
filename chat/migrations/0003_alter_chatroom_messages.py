# Generated by Django 4.0.3 on 2022-06-10 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0001_initial'),
        ('chat', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatroom',
            name='messages',
            field=models.ManyToManyField(blank=True, null=True, related_name='messages', to='message.message'),
        ),
    ]
