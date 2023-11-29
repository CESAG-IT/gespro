# Generated by Django 4.2.7 on 2023-11-29 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.PositiveIntegerField(default=1000)),
                ('qty', models.PositiveIntegerField(default=1)),
                ('image', models.ImageField(default='default.jpg', upload_to='products/')),
                ('status', models.CharField(choices=[('A', 'Disponible'), ('U', 'Indisponible')], max_length=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
                'db_table': 'produts',
                'ordering': ['-created_at'],
            },
        ),
    ]
