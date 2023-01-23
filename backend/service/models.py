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

class WorkingMode(models.Model):

    PASSMODE_CHOICES = [
        ('pay_by_hour', 'pay_by_hour'),
        ('pay_by_interval', 'pay_by_interval'),
        ('closed', 'closed'),
    ]

    time_lte_hour = models.IntegerField  # <
    time_gte_hour = models.IntegerField  # > от
    time_lte_min = models.IntegerField  # < до
    time_gte_min = models.IntegerField  # >
    pass_mode = models.CharField(max_length=999, choices=PASSMODE_CHOICES)  # pay_by_hour | pay_by_interval | closed
    free_time_min = models.IntegerField(default=0)
    interval = models.IntegerField(default=0)
    transit_block_time_min = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    entry_fee = models.IntegerField(default=0)
    description = models.CharField(max_length=999)
    access_points = models.ManyToManyField('AccessPoint')

class AccessPoint(models.Model):

    EXIT_CHOICES = [
        ('in', 'in'),
        ('out', 'out'),
    ]

    cam_id = models.ForeignKey('Camera', on_delete=models.PROTECT)
    laurent2_id = models.ForeignKey('Laurent2', on_delete=models.PROTECT)
    led_board_id = models.ForeignKey('LEDBoard', on_delete=models.PROTECT)
    relay_number = models.IntegerField
    out_number_magnet_loop_before = models.IntegerField
    out_number_magnet_loop_after = models.IntegerField
    working_modes = models.ManyToManyField('WorkingMode')

    direction = models.CharField(max_length=3, choices=EXIT_CHOICES, db_index=True)  # in, out
    description = models.CharField(max_length=999)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description
