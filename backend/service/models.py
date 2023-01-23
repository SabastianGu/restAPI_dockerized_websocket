from django.db import models

class Camera(models.Model):
    description = models.CharField(max_length=999)
    ip_address = models.CharField(max_length=999)
    login = models.CharField(max_length=999)
    password = models.CharField(max_length=999)

    def __str__(self):
        return self.description

class Laurent2(models.Model):
    ip_address = models.CharField(max_length=999, db_index=True)
    description = models.CharField(max_length=999)

    def __str__(self):
        return self.description

class LEDBoard(models.Model):
    description = models.CharField(max_length=999)
    ip_address = models.CharField(max_length=999)

    def __str__(self):
        return self.description

class BlackListItem(models.Model):
    vehicle_plate = models.CharField(max_length=999, db_index=True)
    valid_until = models.DateTimeField(db_index=True)
    description = models.CharField(max_length=999)

    def __str__(self):
        return self.description

class CarParkItem(models.Model):
    vehicle_plate = models.CharField(max_length=999, db_index=True)
    valid_until = models.DateTimeField(db_index=True)
    description = models.CharField(max_length=999)

    def __str__(self):
        return self.description

