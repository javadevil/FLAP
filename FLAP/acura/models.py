from django.db import models

# Create your models here.
class Book(models.Model):
    name        = models.CharField("Book's name", max_length=256)
    desc        = models.CharField("Description", max_length=1024)
    
    def __unicode__(self):
        return self.name
        
class Statement(models.Model):
    statment    = models.CharField("Statement", max_length=256)
    book        = models.ForeignKey(Book)
    create_time = models.DateTimeField(auto_now_add=True)

class Code(models.Model):
    desc        = models.CharField("Code descriptions", max_length=1024)
    acc_code    = models.CharField("Accounting Code number", max_length=16, unique=True)
    parent_code = models.ForeignKey('self')
        
class Transaction(models.Model):
    desc        = models.CharField("Transaction description", max_length=256)
    code        = models.ForeignKey(Code)
    parent      = models.ForeignKey(Statement)
    debit       = models.DecimalField("Debit amount", max_digits=16, decimal_places=2)
    credit      = models.DecimalField("Credit amount", max_digits=16, decimal_places=2)