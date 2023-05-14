from django.shortcuts import render
from django.views import View
from book.models import Book

from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator







# class BooksView(ListView):
#     template_name = 'books/list.html'
#     queryset = Book.objects.all()
#     context_object_name = 'books'
    
    
class BooksDetailView(DetailView):
    template_name = 'books/detail.html'
    pk_url_kwarg = 'id'
    model = Book
  
  
    
class BooksView(View):
    def get(self,request):
        books = Book.objects.all().order_by('id')
        
        page_size=request.GET.get('page_size',3)
        paginator = Paginator(books, page_size)
        
        page_num = request.GET.get('page', 1)
        print(request.GET)
        
        page_obj = paginator.get_page(page_num)
        
        context = {'page_obj':page_obj}
        
        return render(request,'books/list.html', context)
            
    
# class BooksDetailView(View):
#     def get(self, request, id):
#         book = Book.objects.get(id=id)
#         context = {'book':book }
#         return render(request, 'books/detail.html', context)