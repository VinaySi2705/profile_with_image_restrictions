# Generated by Django 4.0 on 2021-12-16 12:28

from django.db import migrations, models
import image_app.validators


class Migration(migrations.Migration):

    dependencies = [
        ('image_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('profile_photo', models.ImageField(blank=True, null=True, upload_to='images/', validators=[image_app.validators.validate_file_extension, image_app.validators.validate_image])),
                ('email', models.EmailField(default='', max_length=1000)),
                ('mobile_no', models.IntegerField(max_length=100, validators=[image_app.validators.validate_no])),
            ],
        ),
        migrations.DeleteModel(
            name='Picture',
        ),
    ]
