# Generated by Django 4.2.11 on 2024-04-19 08:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='boardparticipant',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='boardparticipant',
            name='board',
        ),
        migrations.RemoveField(
            model_name='boardparticipant',
            name='user',
        ),
        migrations.RemoveField(
            model_name='goal',
            name='category',
        ),
        migrations.RemoveField(
            model_name='goal',
            name='user',
        ),
        migrations.RemoveField(
            model_name='goalcomment',
            name='goal',
        ),
        migrations.RemoveField(
            model_name='goalcomment',
            name='user',
        ),
        migrations.RemoveField(
            model_name='goalcategory',
            name='board',
        ),
        migrations.DeleteModel(
            name='Board',
        ),
        migrations.DeleteModel(
            name='BoardParticipant',
        ),
        migrations.DeleteModel(
            name='Goal',
        ),
        migrations.DeleteModel(
            name='GoalComment',
        ),
    ]
