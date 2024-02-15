from django.http import JsonResponse

import StudentApp
from StudentApp.models import Student


# Checking if there is a student with the entered phone number or not
def loginStudent(request):
    studentPhoneNum = request.GET.get('phone')

    try:
        student = Student.objects.get(phoneNumber=studentPhoneNum)

        # Creating json from the data taken from the database
        responseData = {"fullName": student.fullName, "birthday": student.birthday, "phoneNumber": student.phoneNumber,
                        "grade": student.grade}
        return JsonResponse({"status": 200, "result": {"student": responseData}, "massage": "دانش آموز یافت شد"})

    except StudentApp.models.Student.DoesNotExist:
        return JsonResponse({"status": 404, "result": {}, "massage": "دانش آموز یافت نشد"})


# Student registration
def registerStudent(request):
    studentFullName = request.GET.get('name')
    studentPhoneNum = request.GET.get('phone')
    studentBirthday = request.GET.get('birthday')
    studentGrade = request.GET.get('grade')

    if studentFullName and studentPhoneNum and studentBirthday and studentGrade:
        Student.objects.create(fullName=studentFullName, phoneNumber=studentPhoneNum,
                               birthday=studentBirthday,
                               grade=studentGrade)

        return JsonResponse({"status": 200, "result": {}, "massage": "دانش آموز ثبت نام شد"})
    else:
        return JsonResponse({"status": 400, "result": {}, "massage": "دیتا های ارسالی معتبر نمی باشد"})
