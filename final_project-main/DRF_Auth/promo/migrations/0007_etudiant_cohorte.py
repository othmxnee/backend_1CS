# Generated by Django 4.0.1 on 2024-06-06 11:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('promo', '0006_cohorte'),
    ]

    operations = [
        migrations.AddField(
            model_name='etudiant',
            name='cohorte',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='promo.cohorte'),
            preserve_default=False,
        ),
    ]
