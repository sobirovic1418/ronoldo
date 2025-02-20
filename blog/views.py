from django.shortcuts import render

from blog.models import (AboutMe, Education,Experience,Award,Desc,Son,Blog,Part,
                         Skill, Service, OurBlog, OurProject,Image,Set)


def index(request):
    about=AboutMe.objects.all()
    edu=Education.objects.all()
    skill=Skill.objects.all()
    service=Service.objects.all()
    our=OurBlog.objects.all()
    project=OurProject.objects.all()
    img=Image.objects.all()
    set=Set.objects.all()
    exp=Experience.objects.all()
    awr=Award.objects.all()
    desc=Desc.objects.all()
    son=Son.objects.all()
    blog=Blog.objects.all()
    part=Part.objects.all()
    cxt={
        'about':about,
        'edu':edu,
        'skill':skill,
        'service':service,
        'project':project,
        'our_blog':our,
        'image':img,
        'set':set,
        'exp':exp,
        'awr':awr,
        'desc':desc,
        'son':son,
        'blog':blog,
        'part':part,
    }
    return render(request,'index.html',cxt)

def index_2(request):
    return render(request,'single.html')