from django.db import models
from django.contrib.auth.models import User
from tm_app.models import Department
from PIL import Image

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    is_manager = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
