from django.shortcuts import render

# Create your views here.
def register(request):
    return render(request,'df_user/register.html')