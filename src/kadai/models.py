from django.db import models

# Create your models here.

class ai_analysis_log(models.Model):
    image_path          = models.CharField(max_length=255,null=True, blank=True)
    success             = models.CharField(max_length=255,null=True, blank=True)
    message             = models.CharField(max_length=255,null=True, blank=True)
    class_value         = models.IntegerField(db_column='class',null=True, blank=True)
    confidence          = models.DecimalField(max_digits=5,decimal_places=4,null=True, blank=True)
    request_timestamp   = models.PositiveIntegerField(null=True, blank=True)
    response_timestamp  = models.PositiveIntegerField(null=True, blank=True)

# Table
#   `id` int(11) NOT NULL AUTO_INCREMENT,
#   `image_path` varchar(255) DEFAULT NULL,
#   `success` varchar(255) DEFAULT NULL,
#   `message` varchar(255) DEFAULT NULL,
#   `class` int(11) DEFAULT NULL,
#   `confidence` decimal(5,4) DEFAULT NULL,
#   `request_timestamp` int(10) unsigned DEFAULT NULL,
#   `response_timestamp` int(10) unsigned DEFAULT NULL,
#   PRIMARY KEY (`id`),