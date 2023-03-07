from django.http import HttpResponse
from django.shortcuts import render


def aboutus(request):
    return HttpResponse("welcome to baap")

def homePage(request):
    data={
        'title':'My Resume',
        'bdata':'My Resume',
        'name':'Sonali Kailas kadlag',
        'des':'Software Developer',
        'sum':'Summary',
        'skills':'i have skilled software developer with over 1 years of experience in building web applications using various technologies. have skills in HTML, CSS, JavaScript,BootStrap and python.',
        'edu':'Education',
        'bca':' BCA (Bachelor of Computer Application), Pune University, 2011',
        'mca':' MCA (Master of Computer Application), Pune University, 2013',
        'Skills':'Skills',
        'h':' HTML/CSS',
        'j':'JavaScript',
        'b':'Bootstrap',
        'r':'ReactJS',
        'p':'Python/Django',
        'ex':'Experience',
        'lec':'Lecturer at BST College,Sangamner  (2014-2016)',
        'ad':'Aditya Birla ,As a Agency Manager,Sangamner (2018-2020)',
        'dev':' Developed and maintained web applications using HTML, CSS, JavaScript, and Bootstrap.',
        'des1':'Designed and implemented user interfaces using Bootstrap and ReactJS.',
        'web':'Web Developer, Baap Company (2022-2023)',
        'css':'Designed and developed web applications using HTML, CSS, and JavaScript.',
        'sql':'Managed and maintained databases using SQL.'




    }
    return render(request, "index.html",data)
