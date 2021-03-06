# Generated by Django 4.0 on 2021-12-16 11:52

from django.db import migrations, models
import image_app.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('cover', models.ImageField(blank=True, null=True, upload_to='images/', validators=[image_app.validators.validate_file_extension, image_app.validators.validate_image])),
                ('Description', models.TextField(default='', max_length=1000)),
            ],
        ),
    ]
