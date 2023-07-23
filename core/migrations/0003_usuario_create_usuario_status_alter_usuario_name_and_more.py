# Generated by Django 4.2.3 on 2023-07-23 22:23

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_user_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='create',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AddField(
            model_name='usuario',
            name='status',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.CreateModel(
            name='Agendamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hour', models.CharField(blank=True, max_length=30, null=True)),
                ('date', models.CharField(blank=True, max_length=30, null=True)),
                ('usuario_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Userario_id', to='core.usuario')),
            ],
        ),
    ]