# Generated by Django 3.2.25 on 2024-12-12 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RawMaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('quantity', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='YeastBatch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('molasses_amount', models.FloatField()),
                ('grain_starch_amount', models.FloatField()),
                ('potato_starch_amount', models.FloatField()),
                ('water', models.FloatField()),
                ('nutrients_vitamins', models.FloatField()),
                ('emulsifiers', models.FloatField()),
                ('purity', models.FloatField()),
            ],
        ),
    ]
