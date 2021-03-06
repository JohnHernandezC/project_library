# Generated by Django 4.0.1 on 2022-03-15 01:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booksApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='autor',
            options={'ordering': ['nombre'], 'verbose_name': 'Autor', 'verbose_name_plural': 'Autores'},
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('fechaLanzamiento', models.DateField(auto_now_add=True)),
                ('autorId', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='booksApp.autor')),
            ],
            options={
                'verbose_name': 'libro',
                'verbose_name_plural': 'libros',
                'ordering': ['titulo'],
            },
        ),
    ]
