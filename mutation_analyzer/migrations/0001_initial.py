# Generated by Django 4.0.2 on 2022-02-05 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnalyzedDna',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dna', models.TextField(unique=True, verbose_name='DNA')),
                ('type', models.CharField(choices=[('H', 'Humano'), ('M', 'Mutante')], max_length=1, verbose_name='Tipo de DNA')),
            ],
            options={
                'verbose_name': 'DNA Analisado',
                'verbose_name_plural': 'DNAs Analizados',
                'db_table': 'analyzed_dna',
            },
        ),
    ]
