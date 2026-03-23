from django.contrib import admin
from apps.core.models import (
    Intro, Service, ServiceOptions, Faq, FaqQuestions,
    ConnectSection, ConnectShortAnswers, GetInTouch,
    Contact, ContactLinks
)

# ==================== Intro ====================
@admin.register(Intro)
class IntroAdmin(admin.ModelAdmin):
    list_display = ('title', 'logo', 'name', 'number', 'cv_file','intro_image','wa_link','git_link','yt_link','description')
    search_fields = ('name', 'title', 'description')
    
    def has_add_permission(self, request):
        return not Intro.objects.exists()

# ==================== Service ====================
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'description')
    search_fields = ('title', 'subtitle', 'description')
    
    def has_add_permission(self, request):
        return not Service.objects.exists()

@admin.register(ServiceOptions)
class ServiceOptionsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'icon_class', 'button_text', 'button_link', 'order')
    search_fields = ('title', 'description', 'icon_class')
    list_filter = ('order',)

# ==================== FAQ ====================
@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle')
    search_fields = ('title', 'subtitle')
    
    def has_add_permission(self, request):
        return not Faq.objects.exists()

@admin.register(FaqQuestions)
class FaqQuestionsAdmin(admin.ModelAdmin):
    list_display = ('question','answer')
    search_fields = ('question', 'answer')

# ==================== ConnectSection ====================
@admin.register(ConnectSection)
class ConnectSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'commitment_title', 'question')
    search_fields = ('title', 'subtitle', 'description', 'commitment_title', 'question')
    
    def has_add_permission(self, request):
        return not ConnectSection.objects.exists()

@admin.register(ConnectShortAnswers)
class ConnectShortAnswersAdmin(admin.ModelAdmin):
    list_display = ('answer', 'order')
    search_fields = ('answer',)
    list_filter = ('order',)

# ==================== GetInTouch ====================
@admin.register(GetInTouch)
class GetInTouchAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email', 'message')
    list_filter = ('created_at',)

# ==================== ContactSection ====================
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'number', 'address', 'state_address')
    search_fields = ('email', 'address', 'state_address', 'number')
    
    def has_add_permission(self, request):
        return not Contact.objects.exists()

@admin.register(ContactLinks)
class ContactLinksAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon_class', 'order')
    search_fields = ('name', 'icon_class')
    list_filter = ('order',)