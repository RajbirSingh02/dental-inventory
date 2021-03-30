from django.db import models

# Create your models here.
category_choice = (
		('Examination instruments', 'Examination instruments'),
		('Retractor', 'Retractor'),
		('Local anesthesia', 'Local anesthesia'),
		('Dental hand piece', 'Dental hand piece'),
		('Dental laser', 'Dental laser'),
		('Dental torque wrench', 'Dental torque wrench'),
		('Burs', 'Burs'),
		('Restorative instruments', 'Restorative instruments'),
		('Burnishers', 'Burnishers'),
		('Pluggers', 'Pluggers'),
		('Periodontal', 'Periodontal'), 
		('Prosthodontic instruments', 'Prosthodontic instruments'),
		('Extraction and surgical instruments', 'Extraction and surgical instruments'),
		('Orthodontic instruments', 'Orthodontic instruments'),
		('Endodontic instruments', 'Endodontic instruments'),
		('Furniture', 'Furniture'),
		
	)

class Stock(models.Model):
	category = models.CharField(max_length=50, blank=True, null=True, choices=category_choice,)
	item_name = models.CharField(max_length=50, blank=True, null=True)
	quantity = models.IntegerField(default='0', blank=False, null=True)
	receive_quantity = models.IntegerField(default='0', blank=True, null=True)
	receive_by = models.CharField(max_length=50, blank=True, null=True)
	issue_quantity = models.IntegerField(default='0', blank=True, null=True)
	issue_by = models.CharField(max_length=50, blank=True, null=True)
	issue_to = models.CharField(max_length=50, blank=True, null=True)
	phone_number = models.CharField(max_length=50, blank=True, null=True)
	last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	date = models.DateTimeField(auto_now_add=False, auto_now=False)
	reorder_level = models.IntegerField(default='0', blank=False, null=True)



	def __str__(self):
			return self.item_name





