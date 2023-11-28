from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=100)
    cours_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Author(models.Model):
    full_name = models.CharField(max_length=200)
    img = models.ImageField(upload_to='author')
    bio = models.CharField(max_length=300)
    course_count = models.IntegerField(default=0)
    is_top = models.BooleanField(default=False)

    def __str__(self):
        return self.full_name


types = (
    ('Boshlang`ich', 'Boshlang`ich'),
    ('O`rtacha', 'O`rtacha'),
    ('Yuqori', 'Yuqori')
)


class Lesson(models.Model):
    title = models.CharField(max_length=200)
    video_link = models.CharField(max_length=200)
    bio = models.CharField(max_length=200)
    full_watch = models.IntegerField(default=0)
    video_watch = models.IntegerField(default=0)

    view = models.BooleanField(default=False)
    # def watch_view(self, watch):
    #     self.video_watch += watch

    #     views = self.full_watch - self.video_watch
    #     if views * 1.25 >= self.full_watch:
    #         return self.view = True

    # def viw_user(self):
    #     counts = Lesson.objects.filter(view=True)
    #     return counts.count

    def __str__(self):
        return self.title


class Course(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='course')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='cours')

    title = models.CharField(max_length=200)
    img = models.ImageField(upload_to='course')
    type = models.CharField(max_length=50, choices=types)
    price = models.IntegerField(default=0)

    lesson = models.ManyToManyField(Lesson)
    student = models.ManyToManyField(User)

    # def student_count(self):
    #     return (User.count / self.student.count) * 100

    def __str__(self):
        return self.title

