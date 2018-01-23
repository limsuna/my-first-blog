from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .models import Post

def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts':posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


#post_list라는 함수(def) 만들어 요청(request)을 넘겨받아 render메서드를 호출합니다.
#이 함수는 호출하여 받은(return) blog/post_list.html템플릿을 보여줍니다.
