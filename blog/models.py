from django.db import models

class AboutMe(models.Model):
    title=models.CharField(max_length=202)
    image=models.FileField(upload_to='about/')
    full_name=models.CharField(max_length=202)
    description=models.TextField()
    birthday=models.IntegerField()
    location=models.CharField(max_length=202)
    email=models.CharField(max_length=202)
    phone=models.IntegerField()

    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Image(models.Model):
    image=models.FileField(upload_to='web_image/')

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.image


class Education(models.Model):
    title=models.CharField(max_length=202)
    data_time=models.IntegerField()
    description=models.TextField()
    body=models.TextField()

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title



class Skill(models.Model):
    title=models.CharField(max_length=202)
    week=models.IntegerField()
    month=models.IntegerField()
    photoshop=models.IntegerField()
    jquery=models.IntegerField()
    web=models.IntegerField()
    css=models.IntegerField()
    wordpress=models.IntegerField()
    seo=models.IntegerField()

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Service(models.Model):
    title=models.CharField(max_length=202)
    body=models.TextField()

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class OurProject(models.Model):
    description=models.TextField()
    title=models.CharField(max_length=202)
    body=models.TextField()
    number=models.IntegerField()
    name=models.CharField(max_length=202)

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class OurBlog(models.Model):
    body=models.TextField()
    title=models.CharField(max_length=202)
    data=models.IntegerField()
    description=models.TextField()

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
