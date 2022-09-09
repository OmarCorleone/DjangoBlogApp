from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse
from memory.forms import MemoryForm
from django.contrib import messages
from memory.models import Memory,Comment
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url="user:login")
def memories(request):
    keyword=request.GET.get("keyword")

    if keyword:
        memories=Memory.objects.filter(title__contains=keyword)
        return render(request,"memories.html",{"memories":memories})
    memories=Memory.objects.all()

    return render(request,"memories.html",{"memories":memories})

def index(request):

    return render(request,"index.html")
def about(request):
    return render(request,"about.html")
@login_required(login_url="user:login")
def dashboard(request):
    memories= Memory.objects.filter(author=request.user)
    context={
        "memories":memories
    }
    return render(request,"dashboard.html",context)
@login_required(login_url="user:login")
def addMemory(request):
    form = MemoryForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        memory=form.save(commit=False)
        memory.author=request.user
        memory.save()
        messages.success(request,"Anı başarıyla oluşturuldu.")
        return redirect("memory:dashboard")

    return render(request,"addmemory.html",{"form":form})

def detail(request,id):
    #memory=Memory.objects.filter(id=id).first()
    memory=get_object_or_404(Memory,id=id)

    comments=memory.comments.all()

    return render(request,"detail.html",{"memory":memory,"comments":comments})
@login_required(login_url="user:login")
def updateMemory(request,id):
    memory= get_object_or_404(Memory,id=id)
    form=MemoryForm(request.POST or None,request.FILES or None,instance=memory)
    if form.is_valid():
        memory=form.save(commit=False)
        memory.author=request.user
        memory.save()
        messages.success(request,"Anı başarıyla güncellendi.")
        return redirect("memory:dashboard")

    return render(request,"update.html",{"form":form})

@login_required(login_url="user:login")
def deleteMemory(request,id):
    memory=get_object_or_404(Memory,id=id)
    memory.delete()
    messages.success(request,"Anı başarıyla silindi")
    return redirect("memory:dashboard")
def addComment(request,id):
    memory=get_object_or_404(Memory,id=id)




    if request.method=="POST":

        comment_content=request.POST.get("comment_content")
        newComment=Comment(comment_author=request.user,comment_content=comment_content)
        newComment.memory=memory

        newComment.save()
    return redirect(reverse("memory:detail",kwargs={"id":id}))
@login_required(login_url="user:login")
def deleteComment(request,id):

    comment=get_object_or_404(Comment,id=id)
    if comment.comment_author==request.user.username:
        comment.delete()
        messages.success(request,"Yorum silindi")
    else:
        messages.info(request,"Bu yorumu silmeye yetkiniz yok")



    return redirect("memory:dashboard")

