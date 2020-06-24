from django.shortcuts import render, redirect

def index(request):
    if 'visitCountCookie' not in request.session:  
        request.session['visitCountCookie'] = 1
    else:
        request.session['visitCountCookie'] += 1
    return render(request, 'index.html')

def logout(request):
    return redirect("/")

def register(request):
    request.session['firstname_cookie'] = request.POST['form_name']
    request.session['email_cookie'] = request.POST['form_email']
    request.session['color_cookie'] = request.POST['form_color']
    
    #print(request.POST) #full info from form is represented by request.POST
    print('\033[1;31;40m ======================================================')
    print('\033[0;37;42m *** DEBUG ***')
    print(f"\033[0;37;45m METHOD  : {request.method}")
    print(f"\033[0;37;45m NAME:{request.POST['form_name']}, EMAIL: {request.POST['form_email']}, COLOR: {request.POST['form_color']} ")
    print('\033[1;31;40m ======================================================')

    #never render a template on a post request
    return redirect("/showUser")

def show(request):
    print("in the def show(request):")
    print(f"METHOD  : {request.method}")
    print(request.POST) #not seen
    return render(request, 'userinfo.html')