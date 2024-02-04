from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.views import APIView,Response
from .models import *
from .serializers import *
from datetime import datetime
# Create your views here.

def update_fines(request):
    all_default_members = Member.objects.filter(total_fine__gt=0)

    #loop and send member_id and total_fine pairs in params to show in frontend
    return params
    # print(all_default_trans)
    return HttpResponse('HI') 

def return_a_book(reuqest,pk):
    trans_id = int(pk)
    trans_object = Transaction.objects.get(id=trans_id)
    trans_object.is_closed =True
    # today = datetime.now()
    # if today.date> trans_object.due_date:
    #     diff = datetime.now()-trans_object.due_date
    #     fine = diff*50
    #     trans_object.member_id.total_fine += fine
    # add 1 count to the book object
    trans_object.save()

    return HttpResponse("Returned the book succesfully")

class BookView(APIView):
    
    def get(self,request):
        books = Book.objects.filter(id=5)
        all_books = Book.objects.all()
        print(books)
        if books:
            book_data = BookSerialier(all_books,many=True).data
            # print(serializer.data)
            response_data = {"datas":book_data}
            # response_data = {"datas":all_books}
        return Response(response_data,status=status.HTTP_200_OK)

    def post(self,request):
        title = request.data.get('title')
        my_author = request.data.get('author_id')
        author_object = Author.objects.filter(id=my_author)[0]
        total_copies = request.data.get('total_copies')
        in_stock = request.data.get('total_copies')

        Book.objects.create(title=title, author_id=author_object, total_copies=total_copies, in_stock=in_stock)

        response_data = {"response":"item Created"}
        return Response(response_data,status=status.HTTP_200_OK)


class TransactionView(APIView):

    def find_nearest_date(self,book_id):
        all_checkout_trans = Transaction.objects.filter(book_id=book_id,transaction_type="CHECKOUT").order_by('due_date')
        all_reservation_trans = Transaction.objects.filter(book_id=book_id,transaction_type="RESERVATION").order_by('collection_date')
        checkout_count = len(all_checkout_trans)
        reserv_count = len(all_reservation_trans)
        if checkout_count>reserv_count:
            return all_checkout_trans[reserv_count].due_date
        else:
            return all_reservation_trans[reserv_count-checkout_count].due_date


    def get(self,request):
        all_transactions = Transaction.objects.all()
        transaction_data = TransactionSerialier(all_transactions,many=True).data
        response_data = {"datas":transaction_data}
        return Response(response_data,status=status.HTTP_200_OK)

    def post(self,request):
        # {
        #     "transaction_type": "CHECKOUT",
        #     "book_id": 3,
        #     "member_id": 4,
        #     "due_date": "2024-02-26"
        # }
        # transaction_type = request.data.get('transaction_type')
        book_id = request.data.get('book_id')
        book_object = Book.objects.filter(id=book_id)[0]
        member_id = request.data.get('member_id')
        member_object = Member.objects.filter(id=member_id)[0]
        due_date = request.data.get('due_date')

        if book_object.in_stock==0:
            # case of reservation
            transaction_type = "RESERVATION"
            possible_date = self.find_nearest_date(book_id)
            collection_date = possible_date
            #add condition if due date is less than possible date, transaction not possible


        else:
            # case of checkout
            transaction_type = "CHECKOUT"
            book_object.in_stock = book_object.in_stock - 1
            book_object.save(update_fields = ['in_stock'])
            collection_date = None #ananya update this to today

        Transaction.objects.create(transaction_type=transaction_type, book_id=book_object, member_id=member_object, due_date=due_date, collection_date=collection_date)

        response_data = {"response":"item Created"}
        return Response(response_data,status=status.HTTP_200_OK)



