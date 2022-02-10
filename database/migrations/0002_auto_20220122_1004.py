# Generated by Django 3.2.8 on 2022-01-22 17:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='shopping',
            fields=[
                ('shopping_id', models.AutoField(primary_key=True, serialize=False)),
                ('itemname', models.CharField(default='default', max_length=20, verbose_name='Item Name')),
            ],
            options={
                'db_table': 'shopping',
            },
        ),
        migrations.AlterField(
            model_name='grocery',
            name='iid',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.DO_NOTHING, related_name='iID', to='database.recipe_ingredients', verbose_name='Ingredient ID'),
        ),
    ]
