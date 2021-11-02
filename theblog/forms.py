from django import forms
from .models import Post,Category

choices= Category.objects.all().values_list('name','name')

choice_list= []
if choices:
  for item in choices:
       choice_list.append(item)

    
        


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields= ('title','title_tag','category' , 'author','body','snippet','header_image')
        widgets= {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'title_tag': forms.TextInput(attrs={'class':'form-control'}),
            'author': forms.TextInput(attrs={'class':'form-control','id':'user','value':'','type':'hidden'}),
            #'author': forms.Select(attrs={'class':'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
            'snippet': forms.Textarea(attrs={'class':'form-control'}),
            } 

class UpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields= ('title','title_tag','body','snippet')
        widgets= {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'title_tag': forms.TextInput(attrs={'class':'form-control'}),
            #'author': forms.Select(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
            'snippet': forms.Textarea(attrs={'class':'form-control'}),
            } 

class AddCategoryForm(forms.ModelForm):
    class Meta:
         model= Category
         fields= ('name',)
         widgets= {
                 'name': forms.TextInput(attrs={'class':'form-control'}),
                 }

                
               