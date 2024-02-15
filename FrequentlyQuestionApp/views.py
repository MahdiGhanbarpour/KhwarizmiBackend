from django.http import JsonResponse

from FrequentlyQuestionApp.models import FrequentlyQuestion


# Get frequently asked questions based on the entered page
def getFrequentlyQuestions(request):
    page = request.GET.get('page')

    frequentlyQuestions = FrequentlyQuestion.objects.filter(page=page)

    # Creating json from the data taken from the database
    responseData = []
    for frequentlyQuestion in frequentlyQuestions:
        responseData.append({"question": frequentlyQuestion.question, "answer": frequentlyQuestion.answer,
                             "page": frequentlyQuestion.page})

    # Checking whether data is found or not
    if len(responseData):
        return JsonResponse(
            {"status": 200, "result": {"frequentlyQuestions": responseData}, "massage": "سوالات متداول یافت شدند"})
    else:
        return JsonResponse(
            {"status": 404, "result": {"frequentlyQuestions": responseData}, "massage": "سوالات متداولی یافت نشدند"})
