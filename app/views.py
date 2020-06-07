from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.forms import modelformset_factory


def home(request):
    return render(request, "app/home.html")


@login_required
def tests(request):
    context = {
        "tests":
        Test.objects.filter(draft=False).exclude(students=User.objects.get(
            id=request.user.id)),
        'reports':
        Report.objects.filter(user__id=request.user.id),
    }
    return render(request, "app/tests.html", context)


@login_required
def attend(request, pk):
    context = {"test": Test.objects.get(id=pk)}
    return render(request, "app/test.html", context)


@login_required
def submit(request, pk):
    obj = Test.objects.get(id=pk)
    count = int(request.POST.get("qcount")) + 1
    val = ''
    for x in range(1, count):
        if request.POST.get("choice-" + str(x)) != None:
            val = val + request.POST.get("choice-" + str(x))
        else:
            val = val + '0'
    marks = ''
    mark = 0
    for question in obj.questions.all():
        if question.answer == request.POST.get("choice-" + str(count - 1)):
            marks = marks + '1'
            mark += 1
            count += -1
        else:
            marks = marks + '0'
            count += -1
    if User.objects.get(id=request.user.id) in obj.students.all():
        print(True)
        report = Report.objects.get(test=obj)
    else:
        report = Report()
    report.user = User.objects.get(id=request.user.id)
    report.test = obj
    report.choices = val[::-1]
    report.marklist = marks[::-1]
    report.marks = mark
    if report.attempts == None:
        report.attempts = obj.attempts - 1
    else:
        report.attempts = report.attempts - 1
    report.save()
    test = Test.objects.get(id=pk)
    test.students.add(User.objects.get(id=request.user.id))
    return redirect("tests")


@login_required
def report(request, pk):
    report = Report.objects.get(id=pk)
    context = {
        "reports": Report.objects.get(id=pk),
        "test": Test.objects.get(id=report.test.id)
    }
    return render(request, "app/report.html", context)


@login_required
def newformula(request):
    if request.method == "POST":
        for i in range(1, 21):
            if request.POST.get("formula-" + str(i)) != "":
                formula = Formula()
                formula.formula = '\(\\' + request.POST.get("formula-" +
                                                            str(i)) + '\)'
                formula.catg = request.POST.get("catg")
                formula.save()
        return redirect('formula')
    return render(request, "app/formula.html")


@login_required
def setquestions(request):
    context = {
        "formulas": Formula.objects.all(),
    }
    if request.method == "POST":
        counter = int(request.POST.get('counter'))
        if counter >= 1:
            print("True")
            test = Test()
            test.subject = request.POST.get('subject')
            test.title = request.POST.get('title')
            test.time = request.POST.get('time')
            test.description = request.POST.get('description')
            test.attempts = request.POST.get('attempts')
            if request.POST.get('draft') == "on":
                test.draft = True
            else:
                test.draft = False
            test.save()
            for i in range(1, counter + 1):
                question = Question()
                question.question = request.POST.get("question-" + str(i))
                question.option1 = request.POST.get("question-" + str(i) +
                                                    '-1')
                question.option2 = request.POST.get("question-" + str(i) +
                                                    '-2')
                question.option3 = request.POST.get("question-" + str(i) +
                                                    '-3')
                question.option4 = request.POST.get("question-" + str(i) +
                                                    '-4')
                question.answer = request.POST.get("answer-" + str(i))
                question.save()
                test.questions.add(question)
                test.save()
            test.save()
            if request.POST.get('draft') == "on":
                messages.success(request, 'Question Paper has been published!')
            else:
                messages.info(request,
                              'Question Paper has been saved in the drafts!')
            return redirect("tests")
    return render(request, "app/setquestions.html", context)


@login_required
def editquestions(request, pk):
    test = Test.objects.get(id=pk)
    context = {"formulas": Formula.objects.all(), "test": test}
    if request.method == "POST":
        counter = int(request.POST.get('counter'))
        if counter >= 1:
            test.subject = request.POST.get('subject')
            test.title = request.POST.get('title')
            test.time = request.POST.get('time')
            test.description = request.POST.get('description')
            if request.POST.get('draft') == "on":
                test.draft = True
            else:
                test.draft = False
            test.save()
            for i in range(1, counter + 1):
                question = test.questions.all()[i - 1]
                question.question = request.POST.get("question-" + str(i))
                question.option1 = request.POST.get("question-" + str(i) +
                                                    '-1')
                question.option2 = request.POST.get("question-" + str(i) +
                                                    '-2')
                question.option3 = request.POST.get("question-" + str(i) +
                                                    '-3')
                question.option4 = request.POST.get("question-" + str(i) +
                                                    '-4')
                question.answer = request.POST.get("answer-" + str(i))
                question.save()
            test.save()
            if request.POST.get('draft') == "on":
                messages.success(request, 'Question Paper has been published!')
            else:
                messages.info(request,
                              'Question Paper has been saved in the drafts!')
            return redirect("tests")
    return render(request, "app/editquestions.html", context)