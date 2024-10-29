from django.shortcuts import render
from .forms import FormName  # Ensure 'YourForm' matches the actual form name
from.models import Feedback


# Create your views here.
def form_name_view(request):
    form = FormName()
    profile_pic_url=None #instialize profile picture url


    if request.method == 'POST':
        form =FormName(request.POST,request.FILES)
        if form.is_valid():
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            feedback= form.cleaned_data['feedback']
            profile_pic=form.cleaned_data.get('profile_pic')

            #save the data to database
            feedback_instence=Feedback.objects.create(
                name=name,
                email=email,
                feedback=feedback,
                profile_pic=profile_pic
            )

            if profile_pic:
                profile_pic_url=feedback_instence.profile_pic

            #print header and top line
            print("\n" + "=" * 50)
            print("User Form Submission".center(50))
            print("=" * 50)
            print(f"Name:{name}")
            print(f"Email:{email}")
            print(f"Feedback: {feedback}")
            if profile_pic:
                print(f"profile picture:{profile_pic_url}")

            # print("=" * 50 + "\n")

            #iterate and print each field on a new line
            # for field,value in form.cleaned_data.items():
            #     print(f"{field.capitalize()}: {value}")


            #print bottom line
            print("=" * 50 + "\n")


    return render(request, 'forms_app/form_page.html', {
        'form': form,
        'profile_pic_url': profile_pic_url
    })