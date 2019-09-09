# Generated by Django 2.2.3 on 2019-08-09 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0008_auto_20190809_1227'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='sample4_detailAddress',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='sample4_extraAddress',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='sample4_jibunAddress',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='sample4_roadAddress',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='roomtype',
            field=models.CharField(choices=[('오피스텔', '오피스텔'), ('아파트', '아파트'), ('원룸', '원룸'), ('투룸', '투룸'), ('고시텔', '고시텔')], max_length=100),
        ),
    ]