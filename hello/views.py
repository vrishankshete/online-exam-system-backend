from django.shortcuts import render

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt   #from stackoverflow 
from hello import models 
from hello.models import *
from django.contrib import messages # to show massages 
# while integrate react with django
from rest_framework.views import APIView
from rest_framework.response import Response
from . serializer import *

#from .form import FormRegister


#*****************************************
#to call main login (home page)
def home(request):
    
    #this just for cross checking weather we can access primary key 
    '''
    if Teacher_details.objects.filter(login_id="shalmalee.chaudhari@teacher") :
        teacher = Teacher_details.objects.get(login_id= "shalmalee.chaudhari@teacher")
        print("primary key is : " , teacher.id)
    else:
        print("No account")

        '''
    return render(request,'home.html')



#**************************************
#Admin

#to go page login as admin
def loginAsAdmin(request):
    return render(request, 'loginAsAdmin.html')

#to call admin Dashboard
def adminpage(request):
    login_id = request.POST['login_id']
    password = request.POST['password']
    if login_id== 'admin@gmail.com' and password=='admin123':
        return render(request,'adminpage.html')
    else:
        messages.info(request,'invalid username or password')
    return render(request,'loginAsAdmin.html')

#to call page of create student account
def createStudent(request):
    return render(request, 'createStudent.html')

#to insert actual data after submit button
def result(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    middle_name = request.POST['middle_name']
    login_id = request.POST['login_id']
    password = request.POST['password']
    id_photo = request.POST['id_photo']
    year = request.POST['year']
    dept = request.POST['dept']
    roll_no = request.POST['roll_no']
    if RegisterForm.objects.filter(login_id=login_id):
        messages.info(request,'Such login_id already exist')
        return render(request, 'createStudent.html')
    else:
        #to save/ insert data into database
        ins = RegisterForm(first_name=first_name, middle_name=middle_name, last_name=last_name, login_id=login_id, password=password, id_photo=id_photo, year=year, dept=dept, roll_no=roll_no  )
        ins.save()
        messages.info(request,'Student account is succefully created')
    #print(first_name, middle_name, last_name, login_id, password, year, dept, roll_no)
    return render(request, 'adminpage.html')

#to call registration form for create teacher
def createTeacher(request):
    return render(request, 'createTeacher.html')

#to create actual account in database after click submit
def createTeacherAcc(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    middle_name = request.POST['middle_name']
    login_id = request.POST['login_id']
    password = request.POST['password']
    if Teacher_details.objects.filter(login_id=login_id):
        messages.info(request,'Such login_id already exist')
        return render(request, 'createTeacher.html')
    else:
        ins = Teacher_details(first_name=first_name, middle_name=middle_name, last_name=last_name, login_id=login_id, password=password)
        ins.save()
        #print(first_name, middle_name, last_name, login_id, password)
        messages.info(request,'Teacher account is succefully created')
        return render(request, 'adminpage.html')

#to open delete student html page
def deleteStudent(request):
    return render(request, 'deleteStudent.html')

#to delete actual account from database
def deleteStudentAcc(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    middle_name = request.POST['middle_name']
    login_id = request.POST['login_id']
    roll_no = request.POST['roll_no']
    if RegisterForm.objects.filter(login_id=login_id):
        Student = RegisterForm.objects.get(login_id=login_id)
        print(Student)
        Student.delete()
        messages.info(request,'Student account is succefully deleted')
        return render(request, 'adminpage.html')        
    else:
        messages.info(request,'Such login_id is not present')
        return render(request, 'deleteStudent.html')
        
# to call deleteTeacher page
def deleteTeacher(request):
    return render(request, 'deleteTeacher.html')

def deleteTeacherAcc(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    middle_name = request.POST['middle_name']
    login_id = request.POST['login_id']
    if Teacher_details.objects.filter(login_id=login_id):
        teacher = Teacher_details.objects.get(login_id=login_id)
        print(teacher)
        teacher.delete()
        messages.info(request,'Teacher account is succefully deleted')
        return render(request, 'adminpage.html')        
    else:
        messages.info(request,'Such login_id is not present')
        return render(request, 'deleteTeacher.html')




#***************************
#Teacher
#login as teacher
def loginAsTeacher(request):
    return render(request, 'loginAsTeacher.html')

#actual login to the account
def teacherDashboard(request):
    login_id = request.POST['login_id']
    password = request.POST['password']
    if Teacher_details.objects.filter(login_id=login_id) :
        teacher = Teacher_details.objects.get(login_id= login_id)
        if teacher.password == password :
            print("succesful login")
            return render(request, 'teacherDashboard.html')
    else:
        messages.info(request,'invalid username or password')
        return render(request,'loginAsAdmin.html')
    
def createTest(APIView):
    detail = [ {"exam_id": detail.exam_id,"subject_id": detail.subject_id ,
     "exam_date": detail.exam_date , "exam_time" : detail.exam_time} 
    for detail in Exam_details.objects.all()]
    return Response(detail)
    #return render(request, 'createTest.html')


#**************************************
#Student
def loginAsStudent(request):
    return render(request, "loginAsStudent")

def StudentDashboard(request):
    
    return render(request, "studentDashboard.html")

'''
class ReactView(APIView):
    
    serializer_class = ReactSerializer
  
    def get(self, request):
        detail = [ {"name": detail.name,"detail": detail.detail} 
        for detail in React.objects.all()]
        return Response(detail)
  
    def post(self, request):
  
        serializer = ReactSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return  Response(serializer.data)'''


'''def createStudent(request):
    form = FormRegister()
    if form.is_valid():
        form.save()
    context = {'FormRegister':FormRegister}
    return render(request, 'createStudent.html',context)'''
