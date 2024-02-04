from django.db import models

# Create your models here.
class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add =True)
    modified_at = models.DateTimeField(auto_now = True)


class Author(TimeStampedModel):

    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Book(TimeStampedModel):

    title = models.CharField(max_length=30)
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE)
    total_copies = models.IntegerField()
    in_stock = models.IntegerField()


    def __str__(self):
        return self.title



class Member(TimeStampedModel):
    
    name = models.CharField(max_length=30)
    total_fine = models.IntegerField(default=0)

    
    def __str__(self):
        return self.name

class Transaction(TimeStampedModel):

    TRANSACTION_TYPES = (
        ('CHECKOUT','checkout'),
        ('RESERVATION','reservation')
    )
    transaction_type = models.CharField(max_length=20, choices = TRANSACTION_TYPES)
    book_id = models.ForeignKey(Book,on_delete=models.CASCADE)
    member_id = models.ForeignKey(Member,on_delete=models.CASCADE)
    due_date = models.DateField()
    collection_date = models.DateField(null=True)
    is_closed = models.BooleanField(default=False)
