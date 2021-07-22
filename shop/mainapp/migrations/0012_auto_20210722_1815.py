# Generated by Django 3.2.5 on 2021-07-22 15:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0011_order_cart'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='created_ad',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='smartphone',
            old_name='front_cam_pp',
            new_name='frontal_cam_mp',
        ),
        migrations.RenameField(
            model_name='smartphone',
            old_name='main_cam_pp',
            new_name='main_cam_mp',
        ),
        migrations.AlterField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(blank=True, related_name='related_cart', to='mainapp.CartProduct'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='orders',
            field=models.ManyToManyField(related_name='related_order', to='mainapp.Order', verbose_name='Заказы покупателя'),
        ),
        migrations.AlterField(
            model_name='notebook',
            name='time_without_charge',
            field=models.CharField(max_length=255, verbose_name='Время работы аккумулятора'),
        ),
        migrations.AlterField(
            model_name='order',
            name='comment',
            field=models.TextField(blank=True, null=True, verbose_name='Комментарий к заказу'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Дата получения заказа'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('new', 'Новый заказ'), ('in_progress', 'Заказ в обработке'), ('is_ready', 'Заказ готов'), ('completed', 'Заказ выполнен')], default='new', max_length=100, verbose_name='Статус заказ'),
        ),
        migrations.AlterField(
            model_name='smartphone',
            name='accum_volume',
            field=models.CharField(max_length=255, verbose_name='Объем батареи'),
        ),
        migrations.AlterField(
            model_name='smartphone',
            name='sd_volume_max',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Максимальный объем встраивамой памяти'),
        ),
    ]