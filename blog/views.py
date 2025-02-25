from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import BlogPost, Category
from .forms import BlogPostForm

@login_required
def create_blog_post(request):
    if request.user.user_type == "doctor":  # Ensure only doctors can post
        if request.method == "POST":
            form = BlogPostForm(request.POST, request.FILES)
            if form.is_valid():
                blog_post = form.save(commit=False)
                blog_post.author = request.user
                blog_post.save()
                return redirect('doctor_blogs')
            else:
                print("Form is invalid:", form.errors)  # Debugging output
        else:
            form = BlogPostForm()

        return render(request, 'blog/create_blog.html', {'form': form, 'categories': Category.objects.all()})
    else:
        return redirect('doctor_dashboard')



@login_required
def doctor_blogs(request):
    blogs = BlogPost.objects.filter(author=request.user)
    return render(request, 'blog/doctor_blogs.html', {'blogs': blogs})

def patient_blog_list(request, category_id=None):
    if category_id:
        blogs = BlogPost.objects.filter(category_id=category_id, is_draft=False)
    else:
        blogs = BlogPost.objects.filter(is_draft=False)  # Show all published blogs
    
    return render(request, 'blog/patient_blogs.html', {'blogs': blogs})