from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import (
    PersonalData, CareerObjective, EducationBackground,
    OtherQualification, Employment, Skills,
    Interest, References, UserResume
)
from weasyprint import HTML
import tempfile
from django.http import HttpResponse
from django.template.loader import render_to_string
# Create your views here.


def IndexView(request, *args, **kwargs):
    return render(request, 'index.html')

def CreatePDataView(request, *args, **kwargs):
    if request.method == 'POST':
        user = request.user
        resume = UserResume.objects.get(user=user)
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        nationality = request.POST['nationality']
        id_no = request.POST['id_no']
        address_code = request.POST['address_code']
        address_box = request.POST['address_box']
        tel_no = request.POST['tel_no']
        email = request.POST['email']
        
        pData = PersonalData.objects.create(
            user = user,
            resume = resume,
            first_name = first_name,
            last_name = last_name,
            nationality = nationality,
            id_no = id_no,
            address_code = address_code,
            address_box = address_box,
            tel_no = tel_no,
            email = email
        )
        pData.save()
        return HttpResponseRedirect()
    return render(request, 'personal_data.html')

def CreateCareerObjectiveView(request, *args, **kwargs):
    if request.method == 'POST':
        user = request.user
        resume = UserResume.objects.get(user=user)
        content = request.POST['content']     
        carObjective = CareerObjective.objects.create(
            user = user,
            resume = resume,
            content = content
        )
        carObjective.save()
        return HttpResponseRedirect()
    return render(request, 'career_objective.html')

def CreateEducationBackgroundView(request, *args, **kwargs):
    if request.method == 'POST':
        start_date = request.POST['start_date']
        done_date = request.POST['done_date'] or None
        institution = request.POST['institution']
        
        edBackground = EducationBackground.objects.create(
            user = request.user,
            resume = UserResume.objects.get(user=request.user),
            start_date = start_date,
            done_date = done_date,
            institution = institution   
        )
        edBackground.save()
        return HttpResponseRedirect()
    return render(request, 'edu-background-form.html')

def CreateOtherQualificationView(request, *args, **kwargs):
    if request.method == 'POST':
        start_date = request.POST['start_date']
        done_date = request.POST['done_date'] or None
        institution = request.POST['institution']
        
        edBackground = EducationBackground.objects.create(
            user = request.user,
            resume = UserResume.objects.get(user=request.user),
            start_date = start_date,
            done_date = done_date,
            institution = institution   
        )
        edBackground.save()
        return HttpResponseRedirect()
    return render(request, 'other-qualification-form.html')

def CreateEmloymentView(request, *args, **kwargs):
    if request.method == 'POST':
        start_date = request.POST['start_date']
        done_date = request.POST['done_date'] or None
        institution = request.POST['institution']
        responsibility = request.POST['responsibility']
        duties = request.POST['duties']
        
        emp = Employment.objects.create(
            user = request.user,
            resume = UserResume.objects.get(user=request.user),
            start_date = start_date,
            done_date = done_date,
            institution = institution,
            responsibility = responsibility,
            duties = duties   
        )
        emp.save()
        return HttpResponseRedirect()
    return render(request, 'emp-history-form.html')

def CreateSkillsView(request, *args, **kwargs):
    if request.method == 'POST':
        skill = request.POST['skill']
        
        skillDb = Skills.objects.create(
            user = request.user,
            resume = UserResume.objects.get(user=request.user),
            skill = skill
        )
        skillDb.save()
        return HttpResponseRedirect()
    return render(request, 'skills-form.html')

def CreateInterestView(request, *args, **kwargs):
    if request.method == 'POST':
        interest = request.POST['interest']
        
        interestDb = Skills.objects.create(
            user = request.user,
            resume = UserResume.objects.get(user=request.user),
            interest = interest
        )
        interestDb.save()
        return HttpResponseRedirect()
    return render(request, 'interest-form.html')

def CreateReferenceView(request, *args, **kwargs):
    if request.method == 'POST':
        title = request.POST['title'],
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        work_title = request.POST['work_title']
        company = request.POST['company']
        tel_no = request.POST['tel_no']
        email = request.POST['email']
        town = request.POST['town']
        ref = References.objects.create(
            user = request.user,
            resume = UserResume.objects.get(user=request.user),
            title = title,
            first_name = first_name,
            last_name = last_name,
            work_title = work_title,
            company = company,
            tel_no = tel_no,
            email = email,
            town = town
        )
        ref.save()
        return HttpResponseRedirect()
    return render(request, 'references-form.html')

def GeneratePdf(request):
    resume = get_object_or_404(UserResume, user=request.user)
    
    personal_data = get_object_or_404(PersonalData, user=request.user)
    career_ojective = get_object_or_404(CareerObjective, user=request.user)
    educational_background = get_object_or_404(EducationBackground, user=request.user)
    other_qu = get_object_or_404(OtherQualification, user=request.user)
    employment = get_object_or_404(Employment, user=request.user)
    skills = Skills.objects.filter(user=request.user)
    interest = Interest.objects.filter(user=request.user)
    reference = References.objects.filter(user=request.user)
    
    context = {
        'personal_data':personal_data,
        'career_objective':career_ojective,
        'educational_background':educational_background,
        'other_qualifications':other_qu,
        'employment':employment,
        
    }
    
    html_string = render_to_string('pdfOutput.html', context)
    html = HTML(string=html_string)
    result = html.write_pdf()
    
    response = HttpResponse(content_type='application/pdf;')
    response['Content-Disposition'] = 'inline; filename=resume.pdf'
    response['Content-Transfer-Encoding'] = 'utf-8'
    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(result)
        output.flush()
        output = open(output.name, 'rb')
        response.write(output.read())
    return response

def ResumeView(request, *args, **kwargs):
    if request.user.is_authenticated:
        personal_data = get_object_or_404(PersonalData, user=request.user)
        resume1 = get_object_or_404(UserResume, user=request.user)
        print(personal_data)

        context = {
            'personal_data':personal_data,
            'username':request.user.username,
        }
        return render(request, 'pdfOutput.html', context)