from django.shortcuts import render


from .models import BlogPost

obj = BlogPost.objects.get(id=1)

def blog_post_detail_page(request):
    template_name = ''
    context = {}
    return render(request, '', {})