from django.db import models


# Create your models here.
class Basic(models.Model):
    MY_CHOICE = (
        ("A", "this is a."),
        ("B", "this is b."),
        ("C", "this is c.")
    )
    id = models.BigIntegerField(primary_key=True)
    big_integer_field = models.BigIntegerField(null=True)
    boolean_field = models.BooleanField(default=False)
    char_field = models.CharField(null=True, max_length=100)
    choice_field = models.CharField(max_length=1, choices=MY_CHOICE)
    date_field = models.DateField(null=True)
    date_time_field = models.DateTimeField(null=True)
    decimal_field = models.DecimalField(null=True, max_digits=5, decimal_places=2)
    duration_field = models.DurationField(null=True)
    email_field = models.EmailField(null=True)
    file_field = models.FileField(null=True)
    file_path_field = models.FilePathField(null=True)
    float_field = models.FloatField(null=True)
    image_field = models.ImageField(null=True)
    integer_field = models.IntegerField(null=True)
    generic_ip_address_field = models.GenericIPAddressField(null=True)
    null_boolean_field = models.NullBooleanField()
    positive_integer_field = models.PositiveIntegerField(null=True)
    positive_small_integer_field = models.PositiveSmallIntegerField(null=True)
    slug_field = models.SlugField(null=True)
    small_integer_field = models.SmallIntegerField(null=True)
    text_field = models.TextField(null=True)
    time_field = models.TimeField(null=True)
    url_field = models.URLField(null=True)
    uuid_field = models.UUIDField(null=True)


class ManyToOneOne(models.Model):
    id = models.BigIntegerField(primary_key=True)
    char_field = models.CharField(null=True, max_length=100)

    
class ManyToOneMany(models.Model):
    id = models.BigIntegerField(primary_key=True)
    char_field = models.CharField(null=True, max_length=100)
    many_to_one_one = models.ForeignKey(ManyToOneOne, on_delete=models.CASCADE)


class ManyToManyTo(models.Model):
    id = models.BigIntegerField(primary_key=True)
    char_field = models.CharField(null=True, max_length=100)

    
class ManyToOneFrom(models.Model):
    id = models.BigIntegerField(primary_key=True)
    char_field = models.CharField(null=True, max_length=100)
    many_to_many_to = models.ManyToManyField(ManyToManyTo)

