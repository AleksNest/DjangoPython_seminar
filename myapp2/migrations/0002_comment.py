# Generated by Django 4.2.5 on 2023-10-01 17:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp2', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=300)),
                ('create_at', models.DateField(auto_now_add=True)),
                ('change_at', models.DateField(auto_now_add=True)),
                ('article_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp2.article')),
                ('author_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp2.author')),
            ],
        ),
    ]
