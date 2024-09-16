from django.db import models
from datetime import date

# Create your models here.
class Donor(models.Model):
     # Personal Information
    first_name = models.CharField(max_length=100, verbose_name="First Name", blank=False)
    middle_name = models.CharField(max_length=100, verbose_name="Middle Name", blank=True)
    last_name = models.CharField(max_length=100, verbose_name="Last Name", blank=False)
    suffix = models.CharField(max_length=10, verbose_name="Suffix", blank=True)
    date_of_birth = models.DateField(verbose_name="Date of Birth", blank=True, null=True)
    age = models.PositiveIntegerField(blank=True, null=True, editable=False)

    # Additional Info
    nationality = models.CharField(max_length=100, verbose_name="Nationality", blank=True)
    ethnicity = models.CharField(max_length=100, verbose_name="Ethnicity", blank=True)
    height_cm = models.PositiveIntegerField(verbose_name="Height (cm)", blank=True, null=True)
    weight_kg = models.PositiveIntegerField(verbose_name="Weight (kg)", blank=True, null=True)
    blood_type = models.CharField(max_length=3, verbose_name="Blood Type", blank=True)
    natural_eye_color = models.CharField(max_length=50, verbose_name="Natural Eye Color", blank=True)
    natural_hair_color = models.CharField(max_length=50, verbose_name="Natural Hair Color", blank=True)
    allergies = models.TextField(verbose_name="Allergies", blank=True)
    asthma = models.BooleanField(default=False, verbose_name="Do you have asthma?")
    
    # Education
    college_university = models.CharField(max_length=200, verbose_name="College/University", blank=True)
    course = models.CharField(max_length=200, verbose_name="Course", blank=True)
    occupation = models.CharField(max_length=200, verbose_name="Occupation", blank=True)
    hobbies_talents = models.TextField(verbose_name="Hobbies and Talents", blank=True)

    # Vices
    smoke = models.BooleanField(default=False, verbose_name="Do you smoke?")
    alcohol = models.BooleanField(default=False, verbose_name="Do you drink alcohol?")
    
    # Menstrual Cycle
    first_day_last_cycle = models.DateField(verbose_name="First Day of Last Menstrual Cycle", blank=True, null=True)
    menstrual_cycle_type = models.CharField(max_length=50, choices=[('Regular', 'Regular'), ('Irregular', 'Irregular')], verbose_name="Type of Menstrual Cycle", blank=True)
    number_of_children = models.PositiveIntegerField(verbose_name="Number of Children", blank=True, null=True)

    # Additional Questions
    hospitalization_reason = models.TextField(verbose_name="If you have been hospitalized before, please state the reason/s.", blank=True)
    previous_egg_donor = models.BooleanField(default=False, verbose_name="Do you have previous experience being an Egg Donor?")
    egg_donation_details = models.TextField(verbose_name="If Yes, please list dates of egg donation and number of eggs retrieved", blank=True)
    reasons_for_donation = models.TextField(verbose_name="What are your reasons for being an Egg Donor?", blank=True)
    travel_experience = models.BooleanField(default=False, verbose_name="Do you have international travel experience?")
    travel_details = models.TextField(verbose_name="Please list down countries and dates of travel", blank=True)
    willing_to_travel = models.BooleanField(default=False, verbose_name="Are you willing to travel abroad for the duration of your Egg Donation?")
    
    # Contact
    current_location = models.CharField(max_length=200, verbose_name="Current Location", blank=True)
    contact_number = models.CharField(max_length=20, verbose_name="Contact Number", blank=True)
    email = models.EmailField(verbose_name="Email Address", blank=True)
    share_contact_details = models.BooleanField(default=False, verbose_name="Are you comfortable in sharing your contact details with Intended Parents?")
    post_donation_contact = models.BooleanField(default=False, verbose_name="Are you comfortable in keeping contact after donation?")
    
    # Status
    status = models.CharField(max_length=50, choices=[('For Approval', 'For Approval'), ('Approved', 'Approved'), ('Disapproved', 'Disapproved'), ('Not Approved', 'Not Approved'), ('Follow Up', 'Follow Up')], verbose_name="Status")
    category = models.CharField(max_length=50, choices=[('New', 'New'), ('Proven', 'Proven')], verbose_name="Category")

    # Social Media
    facebook_name = models.CharField(max_length=100, verbose_name="Facebook Name", blank=True)
    facebook_url = models.URLField(verbose_name="Facebook URL", blank=True)
    
    def save(self, *args, **kwargs):
        if self.date_of_birth:
            self.age = date.today().year - self.date_of_birth.year - ((date.today().month, date.today().day) < (self.date_of_birth.month, self.date_of_birth.day))
        super(Donor, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Donor"
        verbose_name_plural = "Donors"

