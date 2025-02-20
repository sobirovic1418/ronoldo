from django.contrib import admin

from .models import (AboutMe, Education,Experience,Award,Desc,Son,Blog,Part,
                     Skill,OurBlog,OurProject,Service,Image,Set)

admin.site.register(AboutMe)
admin.site.register(Image)
admin.site.register(Education)
admin.site.register(Skill)
admin.site.register(Service)
admin.site.register(OurBlog)
admin.site.register(OurProject)
admin.site.register(Experience)
admin.site.register(Award)
admin.site.register(Desc)
admin.site.register(Son)
admin.site.register(Blog)
admin.site.register(Part)
