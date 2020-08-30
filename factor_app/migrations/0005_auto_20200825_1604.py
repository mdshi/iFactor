# Generated by Django 3.1 on 2020-08-25 21:04

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('factor_app', '0004_auto_20200824_1151'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='passthrough',
            name='id',
        ),
        migrations.RemoveField(
            model_name='writeoff',
            name='id',
        ),
        migrations.AddField(
            model_name='passthrough',
            name='address_1',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='passthrough',
            name='address_2',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='passthrough',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=11),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='passthrough',
            name='beneficiary',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='passthrough',
            name='city',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='passthrough',
            name='country',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='passthrough',
            name='created_by',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='passthrough',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2020, 8, 25, 21, 3, 46, 876473, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='passthrough',
            name='description',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='passthrough',
            name='fee',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=11),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='passthrough',
            name='pass_through_id',
            field=models.AutoField(auto_created=True, default=0, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='passthrough',
            name='reason',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='passthrough',
            name='receipt',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='factor_app.receipt'),
        ),
        migrations.AddField(
            model_name='passthrough',
            name='state',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='passthrough',
            name='zip',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='pass_through',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='factor_app.passthrough'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='write_off',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='factor_app.writeoff'),
        ),
        migrations.AddField(
            model_name='writeoff',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=11),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='writeoff',
            name='client',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='factor_app.client'),
        ),
        migrations.AddField(
            model_name='writeoff',
            name='created_by',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='writeoff',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2020, 8, 25, 21, 4, 45, 484647, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='writeoff',
            name='description',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='writeoff',
            name='reason',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='writeoff',
            name='write_off_id',
            field=models.AutoField(auto_created=True, default=0, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]