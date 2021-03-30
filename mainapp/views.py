from django.shortcuts import render
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
    personal_data = UserResume.get_user_personal_data()
    career_ojective = UserResume.get_user_career_objective()
    educational_background = UserResume.get_user_educational_background()
    other_qu = UserResume.get_user_other_qualifications()
    employment = UserResume.get_user_employment()
    skills = UserResume.get_user_educational_background()
    interest = UserResume.get_user_interest()
    reference = UserResume.get_user_reference()
    
    context = {
        'personal_data':personal_data
    }
    
    html_string = render_to_string('pdfOutput.html', context)
    html = HTML(string=html_string)
    result = html.write_pdf()
    
    response = HttpResponse(content_type='application/pdf;')
    response['Content-Disposition'] = 'inline; filename=resume.pdf'
    response['Content-Transfer-Encoding'] = 'binary'
    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(result)
        output.flush()
        output = open(output.name, 'r')
        response.write(output.read())
    return response