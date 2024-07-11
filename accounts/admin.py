from django.contrib import admin
from .models import UserLibraryAccount, BorrowingHistory

# Register your models here.
admin.site.register(UserLibraryAccount)
admin.site.register(BorrowingHistory)