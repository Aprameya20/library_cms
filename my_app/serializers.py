from rest_framework import serializers

from .models import *

from django.db.models import fields


class BookSerialier(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title','author_id','total_copies','in_stock')


class TransactionSerialier(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('transaction_type','book_id','member_id','due_date','collection_date','is_closed')