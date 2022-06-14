from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, Http404
from boards.models import Board

# Create your views here.
def home(request):
   boards=Board.objects.all()
   context={
       'boards':boards
   }
   return render(request,'home.html',context)

def board_topics(request,pk):
    # try:
    #     board=Board.objects.get(pk=pk)
    # except Board.DoesNotExist:
    #     raise Http404

    board=get_object_or_404(Board,pk=pk)
    return render(request,'topics.html',{'board':board})

