def my_view(request):
    print("i am heer")
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            # Redirect to a success page.
        else:
            # Return a 'disabled account' error message
            print("fuck")
    else:
        # Return an 'invalid login' error message.
        print("fuck2")