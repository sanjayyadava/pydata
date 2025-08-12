from django.db.models import Count
from .models import Category, Page

def categories_and_pages(request):
    
    return {
         'all_categories': Category.objects.annotate(post_count=Count('post')),
        'all_pages': Page.objects.all()
       
        
    }
    
def base_url(request):
    return {
        'BASE_URL': f"{request.scheme}://{request.get_host()}"
    }
    