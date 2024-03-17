from django.http import JsonResponse
from django.db.models import Count, Case, When, Q
from student.models import Student


# Create your views here.
def getAllStudents(request):
    """
    得到所有学生信息
    :param request:
    :return:
    """
    students = Student.objects.all()
    students_list = list(students.values())
    return JsonResponse(students_list, safe=False)


def getGender(request):
    """
    得到学生中男女数量
    :param request:
    :return:
    """

    male = len(list(Student.objects.filter(gender='男').values()))
    female = len(list(Student.objects.filter(gender='女')))
    return JsonResponse({"male": male,"female":female}, safe=False)
