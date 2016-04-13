from django.shortcuts import render
from models import Entry,Comment
from forms import CommentForm


def render_homepage(request):
    entries = Entry.objects.all()
    context = {'entries': entries}
    return render(request, 'homepage.html', context)

def render_blogentry_page(request, entry_id):
    if (request.method == "POST"):
        form = CommentForm(request.POST, request.FILES)
        if(form.is_valid()):
            title = request.POST['name']
            message = request.POST['message']
            comment = Comment(article_id = entry_id, name = title, content = message)
            comment.save()
    else:      
        form = CommentForm()
    entry = Entry.objects.filter(id = entry_id)[0]
    comments = Comment.objects.filter(article_id = entry_id)
    context = {'entry': entry, 'comments': comments, 'form': form}
    return render(request, 'blog_entry.html', context)
    
