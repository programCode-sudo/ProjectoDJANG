# Generated by Django 5.0.6 on 2024-06-02 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MarketingModule', '0004_campañademarketing'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('fecha_inicio', models.DateTimeField()),
                ('fecha_fin', models.DateTimeField()),
                ('descripcion_breve', models.TextField()),
                ('imagen', models.ImageField(upload_to='eventos/')),
            ],
        ),
    ]