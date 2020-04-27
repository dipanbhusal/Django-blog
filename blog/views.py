from django.shortcuts import render, get_object_or_404, redirect 
from django.http import HttpResponse ,HttpResponseRedirect 
from django.contrib import messages
from django.db.models import Q
from comments.forms import CommentForm
from comments.models import Comment
from django.contrib.contenttypes.models import ContentType
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    queryset = Post.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter( 
           Q(title__icontains =query) |
           Q(content__icontains=query)
        )
        if queryset:
            query_object = queryset
        else:
            messages.warning(request, 'Cannot found results')
    context = {
        'object_list' : queryset
    }
    return render(request, 'index.htm', context)


def postList(request ):
    queryset = Post.objects.all()
    q = request.GET.get('q')
    if q:
        search_result = Post.objects.filter(
            Q(title__icontains=q) |
            Q(content__icontains =q) 
        )
        return render(request, 'index.htm', {'object_list':search_result})

    
def postDetail(request, post_slug):
    queryset = get_object_or_404(Post, slug=post_slug)
    comments = queryset.comments 
    initial_data = {
        "content_type" :queryset.get_content_type,
        "object_id" : queryset.id, 
    }
    form = CommentForm(request.POST or None, initial= initial_data)
    if form.is_valid():
        c_type = form.cleaned_data.get('content_type')
        content_type = ContentType.objects.get(model = c_type)
        obj_id = form.cleaned_data.get('object_id')
        parent_obj =None 
        try:
            parent_id =int(request.POST.get("parent_id"))
        except:
            parent_id =None 

        if parent_id:
            parent_qs=Comment.objects.filter(id=parent_id)

            if parent_qs.exists() and parent_qs.count()==1:
                parent_obj = parent_qs.first()

                
        content = form.cleaned_data.get('content')
        print(form.cleaned_data)
        new_comment , created = Comment.objects.get_or_create(
            user=request.user,
            content_type=content_type,
            object_id=obj_id,
            content=content,
            parent=parent_obj
        )
        return HttpResponseRedirect(new_comment.content_object.get_absolute_url())
    context = {
        'post' : queryset,
        'comments' : comments,
        'comment_form' : form,
    }
    return render(request, 'post_detail.htm', context)
    
@login_required(login_url='/login/')
def postUpdate(request, post_slug=None):
    queryset = get_object_or_404(Post, slug=post_slug)
    if queryset.author != request.user:
        response = HttpResponse('You are not authorizd to update')
        response.status_code= 403
        return response 
    form = PostForm(request.POST or None,request.FILES or None , instance = queryset) 
    if form.is_valid():
        form.save()
        messages.success(request,'Post has been created ')
        return redirect('blog:post-detail', post_slug )
    
    context = {
        'post' : queryset,
        'form' : form,
    }
    return render(request, 'post_update.htm', context)
@login_required(login_url='/login/')
def PostCreate(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.author = request.user 
        instance.save()
    

        messages.success(request,'Post has been created ')
        return redirect('/')
    
    context = {
        'form': form
    }
    return render(request, 'form.htm', context)

@login_required(login_url='/login/')
def postDelete(request, post_slug):
    queryset = get_object_or_404(Post, slug=post_slug)
    if queryset.author == request.user:
        queryset.delete()
        messages.success(request,'Post has been deleted ')
    else:
        return HttpResponse('You are not authorized to delete.')
    return redirect('blog:home')