# Generated by Django 4.0.3 on 2022-05-03 19:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0005_alter_note_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='contact',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='note', to='contacts.contact'),
        ),
    ]
