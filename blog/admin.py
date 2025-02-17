from django.contrib import admin

from .models import AboutMe, Education, Skill,OurBlog,OurProject,Service,Image

admin.site.register(AboutMe)
admin.site.register(Image)
admin.site.register(Education)
admin.site.register(Skill)
admin.site.register(Service)
admin.site.register(OurBlog)
admin.site.register(OurProject)
