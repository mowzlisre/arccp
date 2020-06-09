from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.forms import modelformset_factory
from blog.models import *


@login_required
def tests(request):
    if request.user.is_superuser:
        context = {
            "drafts": Test.objects.filter(draft=True),
            "tests": Test.objects.filter(draft=False),
        }
        return render(request, "app/list_tests.html", context)
    else:
        context = {
            "tests":
            Test.objects.filter(draft=False).exclude(students=User.objects.get(
                id=request.user.id)),
            'reports':
            Report.objects.filter(user__id=request.user.id),
            "website": Website.objects.filter(id=1),
        }
    return render(request, "app/tests.html", context)


@login_required
def attend(request, pk):
    obj = Test.objects.get(id=pk)
    context = {
        "test": obj,
        'website': Website.objects.filter(id=1),
        }
    if User.objects.get(id=request.user.id) in obj.students.all():
        report = Report.objects.get(test=obj)
        if report.attempts <=0:
            return redirect("tests")
        
    else:
        report = Report()
        report.user = User.objects.get(id=request.user.id)
    report.attempts -= 1
    report.save()
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
    print(val)
    marks = ''
    mark = 0
    i = 1
    for question in obj.questions.all():
        if question.answer == request.POST.get("choice-" + str(i)):
            marks = marks + '1'
            mark += 1
            i += 1
        else:
            marks = marks + '0'
            i += 1
    print(marks)
    report = Report.objects.get(test=obj, user=request.user.id)
    report.test = obj
    report.choices = val
    report.marklist = marks
    report.marks = mark
    if report.attempts == None:
        report.attempts = obj.attempts
    else:
        report.attempts = report.attempts
    report.save()
    test = Test.objects.get(id=pk)
    test.students.add(User.objects.get(id=request.user.id))
    return redirect("tests")


@login_required
def report(request, pk):
    report = Report.objects.get(id=pk)
    context = {
        "reports": Report.objects.get(id=pk),
        "test": Test.objects.get(id=report.test.id),
        'website': Website.objects.filter(id=1),
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
    if request.user.is_superuser:
        context = {
            "formulas": Formula.objects.all(),
        }
        if request.method == "POST":
            counter = int(request.POST.get('counter'))
            if counter >= 1:
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
    else:
        return redirect("404")


@login_required
def editquestions(request, pk):
    if request.user.is_superuser:
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
                    if i <= test.questions.count():
                        question = test.questions.all()[i - 1]
                        print(True)
                    else:
                        question = Question()
                        print(False)
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
                if request.POST.get('draft') == "on":
                    messages.success(request, 'Question Paper has been published!')
                else:
                    messages.info(request,
                                'Question Paper has been saved in the drafts!')
                return redirect("tests")
        return render(request, "app/editquestions.html", context)
    else:
        return redirect("404")

@login_required
def deletequestion(request, pk):
    if request.user.is_superuser:
        test = Test.objects.get(id=pk)
        test.delete()
        return redirect("tests")
    else:
        return redirect("404")

@login_required
def listreports(request):
    if request.user.is_superuser:
        context = {
            "tests": Test.objects.filter(draft=False)
        }
        return render(request, "app/list_reports.html", context)
    else:
        return redirect("404")

@login_required
def detailreport(request, pk):
    if request.user.is_superuser:
        context = {
            "reports": Report.objects.filter(test__id=pk)
        }
        return render(request, "app/detail_report.html", context)
    else:
        return redirect("404")

@login_required
def userreports(request, pk1, pk2):
    if request.user.is_superuser:
        report = Report.objects.get(test=Test.objects.get(id=pk1), user=User.objects.get(id=pk2))
        context = {
            "report": report
        }
        if request.method == "POST":
            report.attempts = request.POST.get('quantity')
            report.save()            
        return render(request, "app/user_reports.html", context)
    else:
        return redirect("404")