from django.shortcuts import render

def privacy_policy(request):
    return render(request, 'privacy_policy.html')

def cookie_policy(request):
    return render(request, 'cookie_policy.html')

def terms_conditions(request):
    return render(request, 'terms_conditions.html')
