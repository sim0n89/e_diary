COMPLIMENTS = [ 'Отлично!', 'Хорошо!', 'Красавчик!',  'Ты меня приятно удивил!', 'Великолепно!', 'Прекрасно!', 'Ты меня очень обрадовал!', 'Именно этого я давно ждал от тебя!', 'Сказано здорово – просто и ясно!', 'Ты, как всегда, точен!', 'Очень хороший ответ!', 'Талантливо!', 'Ты сегодня прыгнул выше головы!', 'Я поражен!', 'Уже существенно лучше!', 'Потрясающе!', 'Замечательно!', 'Прекрасное начало!', 'Так держать!', 'Ты на верном пути!', 'Здорово!', 'Это как раз то, что нужно!', 'Я тобой горжусь!', 'С каждым разом у тебя получается всё лучше!', 'Мы с тобой не зря поработали!', 'Я вижу, как ты стараешься!', 'Ты растешь над собой!', 'Ты многое сделал, я это вижу!', 'Теперь у тебя точно все получится!']



def get_subject(subject_name, study_year=None):
    from datacenter.models import Subject

    try:
        subject = Subject.objects.get(title=subject_name, year_of_study=study_year)
        return subject
    except Subject.DoesNotExist:
        print(f"Предмет {subject_name} {study_year} класс не найден")
        return
    except Subject.MultipleObjectsReturned:
        print(f"Найдено много предметов {subject_name} {study_year} класс")
        return


def get_child(name):
    from datacenter.models import Schoolkid
    try:
        student = Schoolkid.objects.get(full_name__contains=name)
        return student
    except Schoolkid.DoesNotExist:
        print("Никто не найден")
        return
    except Schoolkid.MultipleObjectsReturned:
        print("Найдено слишком много учеников")
        return



def fix_marks(child_name):
    from datacenter.models import Mark

    child = get_child(child_name)
    Mark.objects.filter(schoolkid=child, points__in=[2, 3]).update(
        points=5
    )


def remove_chastisements(child_name):
    from datacenter.models import Chastisement

    Chastisement.objects.filter(schoolkid=get_child(child_name)).delete()


def create_commendation(child_name, subject_name):
    import random
    from datacenter.models import Commendation
    from datacenter.models import Lesson

    child = get_child(child_name)
    if child:
        subject = get_subject(subject_name, child.year_of_study)
        if subject:
            lesson = Lesson.objects.filter(subject=subject).order_by("?").first()
            Commendation.objects.create(text=random.choice(COMPLIMENTS), created=lesson.date, schoolkid=child, subject=subject, teacher=lesson.teacher)



