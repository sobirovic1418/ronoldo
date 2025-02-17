from django.shortcuts import render

from blog.models import AboutMe, Education, Skill, Service, OurBlog, OurProject,Image


def index(request):
    about=AboutMe.objects.all()
    edu=Education.objects.all()
    skill=Skill.objects.all()
    service=Service.objects.all()
    our=OurBlog.objects.all()
    project=OurProject.objects.all()
    img=Image.objects.all()
    cxt={
        'about':about,
        'edu':edu,
        'skill':skill,
        'service':service,
        'our':our,
        'project':project,
        'image':img,
    }
    return render(request,'index.html',cxt)

def index_2(request):
    return render(request,'single.html')