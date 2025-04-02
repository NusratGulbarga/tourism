from django.shortcuts import render, get_object_or_404
from .models import HeritageSite, Review

def home(request):
    sites = HeritageSite.objects.all()
    return render(request, 'heritagesites/home.html', {'sites': sites})

def site_detail(request, pk):
    site = get_object_or_404(HeritageSite, pk=pk)
    reviews = site.reviews.all()
    if request.method == "POST":
        name = request.POST.get('name')
        rating = int(request.POST.get('rating'))
        comment = request.POST.get('comment')
        Review.objects.create(site=site, name=name, rating=rating, comment=comment)
    return render(request, 'heritagesites/site_detail.html', {'site': site, 'reviews': reviews})
