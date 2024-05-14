# Generated by Django 5.0.3 on 2024-05-03 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flashcard', '0004_desafio_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='desafio',
            name='status',
            field=models.CharField(choices=[('Pendente', 'Pendente'), ('Finalizado', 'Finalizado')], default='Pendente', max_length=20),
        ),
    ]