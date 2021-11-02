from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm,UpdateForm,AddCategoryForm
from django.urls import reverse_lazy,reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect


#def home(request):
 #   return render(request,'home.html', {})

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    #ordering= ['-id']
    ordering= ['-post_date']

    def get_context_data(self, *args,**kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView,self).get_context_data(*args,**kwargs)
        context ['cat_menu'] = cat_menu
        return context

    


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'
    def get_context_data(self, *args,**kwargs):
        context = super(ArticleDetailView,self).get_context_data(*args,**kwargs)
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked =True
        total_likes = stuff.total_likes()
        context ['total_likes']= total_likes
        context ['liked']= liked
        return context


class AddPostView(LoginRequiredMixin,CreateView):
    model= Post
    form_class= PostForm
    template_name= 'add_post.html'
    #fields= '__all__'
    #fields= ('title','body')

class UpdatePostView(LoginRequiredMixin,UpdateView):
    model= Post
    form_class= UpdateForm
    template_name= 'update_post.html'
    #fields= ('title','title_tag','body')


class DeletePostView(LoginRequiredMixin,DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url= reverse_lazy('home')


def CategoryView(request, pk):
    C=Category.objects.get(pk=pk)
    cats= C.name
    category_posts = Post.objects.filter(category__name=cats.replace('-', ' '))
    return render(request, 'categories.html', { 'cats':cats.title().replace('-', ' '), 'category_posts': category_posts })
    #return render(request,'home.html', {})


class AddCategoryView(LoginRequiredMixin,CreateView):
    model = Category
    form_class = AddCategoryForm
    template_name='add_category.html'
    success_url= reverse_lazy('home')
    

def likePostView(request, pk):
    post = get_object_or_404(Post,id= request.POST.get('post_id'))
    liked= False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
        liked= True



   
    return HttpResponseRedirect(reverse('article-detail', args= [str(pk)] ))