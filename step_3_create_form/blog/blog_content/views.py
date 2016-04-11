from django.shortcuts import render
from models import Entry,Comment


def render_homepage(request):
    entries = Entry.objects.all()
    context = {'entries': entries}
    return render(request, 'homepage.html', context)

def render_blogentry_page(request, entry_id):
    entry = Entry.objects.filter(id = entry_id)[0]
    comments = Comment.objects.filter(article_id = entry_id)
    context = {'entry': entry, 'comments': comments}
    return render(request, 'blog_entry.html', context)
    
