from django.db import models

from users.models import User

# Create your models here.

class Tasker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    address = models.CharField(max_length=100)
    bio = models.TextField()
    rating = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    tasks_done = models.IntegerField(default=0)

    skills = models.ManyToManyField('TaskerSkills', blank=True)
    certificate = models.ManyToManyField('TaskerCertificate', blank=True)
    work_cities = models.ManyToManyField('City', blank=True)

    is_available = models.BooleanField(default=True)

    # moderation
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Tasker"
        verbose_name_plural = "Taskers"

    def __str__(self):
        return self.user.email
    

class TaskerSkills(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=10)

    class Meta:
        verbose_name = "Tasker Skill"
        verbose_name_plural = "Tasker Skills"

    def __str__(self):
        return self.name
    
class TaskerCertificate(models.Model):
    title = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='images/', blank=True)

    class Meta:
        verbose_name = "Tasker Certificate"
        verbose_name_plural = "Tasker Certificates"

    def __str__(self):
        return self.title


class City(models.Model):
    city = models.CharField(max_length=50)

    class Meta:
        verbose_name = "City"
        verbose_name_plural = "Cities"

    def __str__(self):
        return self.city



class Blog(models.Model):
    author = models.ForeignKey(Tasker, on_delete=models.CASCADE)

    title = models.CharField(max_length=100)
    summary = models.TextField()
    thumbnail = models.ImageField(upload_to='images/', default='images/default_blog.png')

    full_text = models.TextField()

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"

    def __str__(self):
        return self.title















class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    living_city = models.ManyToManyField('City', blank=True)
    address = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"

    def __str__(self):
        return self.user.email
    




class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='images/', default='images/default_service.jpg')
    min_price = models.IntegerField(default=0, blank=True, null=True)

    is_active = models.BooleanField(default=True)
    created = models.DateTimeField("Created At", auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"

    def __str__(self):
        return self.title
    

class SubService(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="sub_service")
    title = models.CharField(max_length=100)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='images/', default='images/default_service.jpg')
    price = models.IntegerField(default=50)

    is_active = models.BooleanField(default=True)
    created = models.DateTimeField("Created At", auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Sub_Service"
        verbose_name_plural = "Sub_Services"

    def __str__(self):
        return self.title


# class ServiceChoice(models.Model):
#     SUB_SERVICE_CHOICES = [(s.id, str(s)) for s in SubService.objects.all()]

#     sub_service = models.IntegerField(choices=SUB_SERVICE_CHOICES)

class ServiceBook(models.Model):
    sub_service = models.ForeignKey(SubService, on_delete=models.CASCADE, related_name='choices')
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    address = models.CharField(max_length=100)
    issue = models.TextField()
    attachment = models.ImageField(upload_to='images/', blank=True, null=True)


    class Meta:
        verbose_name = 'Service Book'
        verbose_name_plural = 'Service Books'


class Order(models.Model):

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='order')
    tasker = models.ForeignKey(Tasker, on_delete=models.CASCADE)
    sub_service = models.ForeignKey(SubService, on_delete=models.CASCADE)

    start_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    address = models.CharField(max_length=100)
    task_detail = models.TextField()
    task_photo = models.ImageField(upload_to='images/', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    status = models.CharField(max_length=20, choices=[
        ('new', 'New'),
        ('assigned', 'Assigned'),
        ('in_progress', 'In Progress'),
        ('finished', 'Finished'),
        ('cancelled', 'Cancelled'),
    ], default='new')

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.sub_service.title
