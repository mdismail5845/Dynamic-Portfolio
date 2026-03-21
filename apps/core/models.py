from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

# <===================== Intro ===========================>
class Intro(models.Model):
    title = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='core/images', blank=True, null=True)
    number = PhoneNumberField(region='BD')
    name = models.CharField(max_length=100)
    description = models.TextField()
    cv_file = models.FileField(upload_to='core/pdfs', blank=True, null=True)
    intro_image = models.ImageField(upload_to='core/images', blank=True, null=True)
    
    class Meta:
        verbose_name_plural = "Introduction"
    
    def __str__(self):
        return self.name
    
# <===================== Service ===========================>
class Service(models.Model):
    title = models.CharField(max_length=100, default='My Services')
    subtitle = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title
    
class ServiceOptions(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon_class = models.CharField(max_length=100, help_text='fas fa-paper-plane')
    image = models.ImageField(upload_to='core/images', blank=True, null=True)
    button_text = models.CharField(max_length=50, default='View Projects')
    button_link = models.URLField(blank=True, null=True)
    order = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['order']
        verbose_name_plural = "Service Option"
        
    def __str__(self):
        return self.title
    
# <===================== FAQ ===========================>
class Faq(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=255)
        
    def __str__(self):
        return self.title
    
class FaqQuestions(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField(
        help_text=""" <strong>I primarily work with <code>Python</code> and <code>Django</code></strong>, 
            along with front-end technologies like <code>HTML, CSS, JavaScript</code>.
        """)
    
    class Meta:
        verbose_name_plural = "Faq Question"
    
    def __str__(self):
        return self.question
    
# <===================== ConnectSection ===========================>    
class ConnectSection(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=100)
    commitment_title = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    question = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = "Connect Section"
        
    def __str__(self):
        return self.title
    
class ConnectShortAnswers(models.Model):
    answer = models.CharField(max_length=50)
    order = models.PositiveIntegerField(default=0,)
    
    class Meta:
        ordering = ['order']
        verbose_name_plural = "Connect Short Answer"
    
    def __str__(self):
        return self.answer

class GetInTouch(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "Get In Touch"
        
    
# <===================== ContactSection ===========================>
class Contact(models.Model):
    email = models.EmailField(max_length=100)
    number =  PhoneNumberField(region='BD')
    address = models.CharField(max_length=50)
    state_address = models.CharField(max_length=50, help_text='Dhaka,BD')
    
    def __str__(self):
        return self.email

class ContactLinks(models.Model):
    name = models.CharField(max_length=50, help_text='Facebook')
    icon_class = models.CharField(max_length=100, help_text='fab fa-facebook-f')
    link = models.URLField(blank=True, null=True)
    order = models.PositiveIntegerField(default=0,)
    
    class Meta:
        ordering = ['order']
        verbose_name_plural = "Contact Link"
        
    def __str__(self):
        return self.name
    