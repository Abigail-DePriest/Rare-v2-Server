from django.db import migrations, models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('bio', models.CharField(max_length=50)),
                ('profile_image_url', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('created_on', models.DateField()),
                ('active', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('uid', models.CharField(max_length=50)),
            ],
        ),
    ]
