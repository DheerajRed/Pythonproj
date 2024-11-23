from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.utils.crypto import get_random_string
# Create your models here.

class createtask(models.Model): 
    Title = models.CharField(max_length=100)
    Description = models.TextField()

    def _str_(self):
        return self.Title
    

def generate_unique_token():
    """Generate a unique random string of length 64 for the token field."""
    return get_random_string(64)

class Invite(models.Model):
    sender = models.ForeignKey(User,on_delete=models.CASCADE, related_name='sent_invites')
    email = models.EmailField()
    created_at = models.DateTimeField(default=now)
    is_accepted = models.BooleanField(default=False)
    token = models.CharField(max_length=64 , default=generate_unique_token, unique=True)
    def __str__(self):
        return f"Invite to {self.email} from {self.sender.username}"
