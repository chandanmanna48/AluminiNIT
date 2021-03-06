# Generated by Django 2.2.7 on 2020-01-03 13:01

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.FileField(upload_to='gallery')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('regdno', models.CharField(max_length=70)),
                ('passout_year', models.CharField(max_length=70)),
                ('branch', models.CharField(max_length=70)),
                ('profession', models.CharField(blank=True, max_length=70)),
                ('company', models.CharField(blank=True, max_length=70)),
                ('work_location', models.CharField(blank=True, max_length=70)),
                ('designation', models.CharField(blank=True, max_length=70)),
                ('work_country', models.CharField(blank=True, max_length=70)),
                ('contactno', models.CharField(blank=True, max_length=70, null=True)),
                ('profile_pic', models.ImageField(default='user.socialaccount_set.all.0.get_avatar_url', upload_to='profile_pic')),
                ('street_name', models.CharField(blank=True, max_length=70)),
                ('street_number', models.CharField(blank=True, max_length=70)),
                ('city', models.CharField(blank=True, max_length=70)),
                ('state', models.CharField(blank=True, max_length=70)),
                ('district', models.CharField(blank=True, max_length=70)),
                ('country', models.CharField(blank=True, max_length=70)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=40)),
                ('last_name', models.CharField(blank=True, max_length=40)),
                ('profile_image_url', models.URLField(blank=True, null=True)),
                ('is_staff', models.BooleanField(default=True)),
                ('is_active', models.BooleanField(default=True)),
                ('first_visit', models.BooleanField(default=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('is_master', models.BooleanField(default=False)),
                ('is_approved', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account_sec.Profile')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
