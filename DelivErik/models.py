from django.db import models
#from phonenumber_field.modelfields import PhoneNumberField
# from from django.contrib.gis.measure import D, Distance

class Customer(models.Model):
    customer_unique_ID = models.CharField(max_length=30, blank=False)
    customer_first_name = models.CharField(max_length=30, blank=False)
    customer_last_name = models.CharField(max_length=30, blank=False)
    customer_first_line_address = models.IntegerField(blank=False)
    customer_second_line_address = models.TextField(blank=False)
    customer_postcode = models.TextField(blank=False)
    customer_email_address = models.EmailField(blank=False)
    customer_phone_number = models.CharField(max_length=30, null=False, blank=False)

    def __str__(self):
        return self.customer_unique_ID
    

class Parcel(models.Model):
    STATUS_CHOICES = [('R', 'Recieved'), ('C', 'Collected'), ('D', 'Delivered'), ('X', 'Cancelled')]
    parcel_unique_ID = models.IntegerField(blank=False)
    parcel_width = models.IntegerField(blank=False)
    parcel_height = models.IntegerField(blank=False)
    parcel_length = models.IntegerField(blank=False)
    parcel_weight = models.IntegerField(blank=False)
    parcel_description = models.TextField(blank=False)
    parcel_status_update_time = models.DateField(blank=False)
    parcel_status = models.CharField(max_length=1, choices=STATUS_CHOICES, blank=False)
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)

