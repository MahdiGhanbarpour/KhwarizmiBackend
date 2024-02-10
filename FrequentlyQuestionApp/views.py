from django.http import JsonResponse

from FrequentlyQuestionApp.models import FrequentlyQuestion


# Create your views here.
def getFrequentlyQuestions(request):
    page = request.GET.get('page')

    frequentlyQuestions = FrequentlyQuestion.objects.filter(page=page)

    responseData = []
    for frequentlyQuestion in frequentlyQuestions:
        responseData.append({"question": frequentlyQuestion.question, "answer": frequentlyQuestion.answer,
                             "page": frequentlyQuestion.page})

    if len(responseData):
        return JsonResponse(
            {"status": 200, "result": {"frequentlyQuestions": responseData}, "massage": "سوالات متداول یافت شدند"})
    else:
        return JsonResponse(
            {"status": 404, "result": {"frequentlyQuestions": responseData}, "massage": "سوالات متداولی یافت نشدند"})
