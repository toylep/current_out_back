# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from base.old_db.models import Companies, Faculty


class Theme(models.Model):
    name = models.CharField(
        max_length=255, db_collation="utf8mb3_general_ci", blank=True, null=True
    )
    company = models.ForeignKey(Companies, models.DO_NOTHING, blank=True, null=True,related_name="themes")
    
    def __str__(self):
        return self.name
    

class Practice(models.Model):

    company = models.ForeignKey(
        Companies, on_delete=models.CASCADE, related_name="practices"
    )
    faculty = models.ForeignKey(
        Faculty, on_delete=models.CASCADE, related_name="practices"
    )


class DocLink(models.Model):

    type = models.TextField()
    url = models.URLField(max_length=1000)
    practice = models.ForeignKey(
        Practice, on_delete=models.CASCADE, related_name="doc_links"
    )


class Speciality(models.Model):
    faculty = models.ForeignKey(
        Faculty, on_delete=models.CASCADE, related_name="specialities"
    )
    name = models.CharField(
        max_length=255, db_collation="utf8mb3_general_ci", blank=True, null=True
    )
    
    def __str__(self) -> str:
        return self.name
