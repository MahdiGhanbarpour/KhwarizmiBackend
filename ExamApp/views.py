from django.http import JsonResponse

from ExamApp.models import Exam, Question, Option, Attachment


# Getting a list of exams based on the entered grade
def getExams(request):
    grade = request.GET.get('grade')

    exams = Exam.objects.filter(grade=grade)

    # Creating json from the data taken from the database
    responseData = []
    for exam in exams:
        responseData.append({"id": exam.id, "name": exam.name, "image": exam.image, "description": exam.description,
                             "authorName": exam.authorName, "authorPhoneNum": exam.authorPhoneNum,
                             "rating": exam.rating,
                             "difficulty": exam.difficulty, "grade": exam.grade, "price": exam.price,
                             "isVerified": exam.isVerified, })

    return JsonResponse({"status": 200, "result": {"exams": responseData}, "massage": "آزمون ها یافت شدند"})


# Getting the list of popular exams based on the entered grade
def getPopularExams(request):
    grade = request.GET.get('grade')

    exams = Exam.objects.filter(grade=grade).order_by("-rating")[0:5]

    # Creating json from the data taken from the database
    responseData = []
    for exam in exams:
        responseData.append({"id": exam.id, "name": exam.name, "image": exam.image, "description": exam.description,
                             "authorName": exam.authorName, "authorPhoneNum": exam.authorPhoneNum,
                             "rating": exam.rating,
                             "difficulty": exam.difficulty, "grade": exam.grade, "price": exam.price,
                             "isVerified": exam.isVerified, })

    return JsonResponse(
        {"status": 200, "result": {"exams": responseData}, "massage": "پرطرفدار ترین آزمون ها یافت شدند"})


# Getting exam questions based on the entered exam ID
def getExamsQuestion(request):
    examId = request.GET.get('exam')

    questions = Question.objects.filter(parentExamId=examId)

    # Creating json from the data taken from the database
    responseData = []
    for question in questions:
        options = Option.objects.filter(parentQuestionId=question.id)
        attachments = Attachment.objects.filter(parentQuestionId=question.id)

        optionsList = []
        for option in options:
            optionsList.append({"option": option.option, "isCorrect": option.isCorrect})

        attachmentsList = []
        for attachment in attachments:
            attachmentsList.append({"detail": attachment.detail, "image": attachment.image})

        responseData.append(
            {"question": question.question, "options": optionsList,
             "attachments": attachmentsList})

    return JsonResponse(
        {"status": 200, "result": {"questions": responseData}, "massage": "سوالات یافت شدند"})
