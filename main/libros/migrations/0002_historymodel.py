# Generated by Django 3.2.8 on 2021-10-06 12:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('libros', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='photos_historias/')),
                ('titulo', models.CharField(max_length=100)),
                ('categoria', models.CharField(choices=[('n', 'Novelas'), ('cu', 'Cuentos'), ('cf', 'Ciencia Ficción'), ('r', 'Romance'), ('co', 'Comedia'), ('p', 'Paranormal'), ('f', 'Fantasía'), ('ot', 'Otros')], default='ot', max_length=15)),
                ('descripcion', models.CharField(max_length=200)),
                ('autor', models.CharField(max_length=200)),
                ('text', models.TextField(max_length=6000)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
