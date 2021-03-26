from django.contrib import admin
from .models import Customer
from .models import Parcel

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer_unique_ID', 'customer_first_name', 
                    'customer_last_name', 'customer_first_line_address', 
                    'customer_second_line_address', 'customer_postcode', 
                    'customer_email_address', 'customer_phone_number'
                    ]

@admin.register(Parcel)
class ParcelAdmin(admin.ModelAdmin):
    list_display = ['parcel_unique_ID', 'parcel_width', 
                    'parcel_height', 'parcel_length', 
                    'parcel_weight', 'parcel_description', 
                    'parcel_status_update_time', 'parcel_status',
                    'customer' 
                    ]
