from django.shortcuts import render, get_object_or_404
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
    personal_data = get_object_or_404(PersonalData, user=request.user)
    resume1 = get_object_or_404(UserResume, user=request.user)
    print(personal_data)
    
    context = {
        'personal_data':personal_data,
        'username':request.user.username,
    }
    return render(request, 'pdfOutput.html', context)