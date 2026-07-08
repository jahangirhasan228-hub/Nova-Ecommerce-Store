from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_order_address_order_city_order_customer_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook_url',     models.URLField(blank=True, null=True, verbose_name='Facebook Page URL')),
                ('instagram_url',    models.URLField(blank=True, null=True, verbose_name='Instagram Profile URL')),
                ('whatsapp_number',  models.CharField(blank=True, max_length=20, null=True, verbose_name='WhatsApp Number', help_text='Include country code, e.g. 8801XXXXXXXXX')),
                ('youtube_url',      models.URLField(blank=True, null=True, verbose_name='YouTube Channel URL')),
            ],
            options={
                'verbose_name': 'Site Settings',
                'verbose_name_plural': 'Site Settings',
            },
        ),
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(
                    choices=[('bkash', 'bKash'), ('nagad', 'Nagad'), ('rocket', 'Rocket'), ('upay', 'Upay')],
                    max_length=20, unique=True, verbose_name='Payment Gateway',
                )),
                ('is_enabled',      models.BooleanField(default=True, verbose_name='Enable this payment method')),
                ('merchant_number', models.CharField(blank=True, max_length=20, verbose_name='Merchant Mobile Number', help_text='The registered merchant/agent number')),
                ('merchant_id',     models.CharField(blank=True, max_length=100, verbose_name='Merchant ID / API Key', help_text='Optional — for API integration')),
            ],
            options={
                'verbose_name': 'Payment Method',
                'verbose_name_plural': 'Payment Methods',
            },
        ),
    ]
