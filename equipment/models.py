from django.db import models


class GP(models.Model):
    number = models.CharField(max_length=10, blank=False, verbose_name='Номер по генплану')
    construction = models.CharField(max_length=255, blank=True, verbose_name='Наименование здания, сооружения')
    installation = models.CharField(max_length=255, blank=True, verbose_name='Установка')
    short = models.CharField(max_length=255, blank=True, verbose_name='Краткое обозначение установки')
    description = models.TextField(max_length=255, blank=True, verbose_name='Наименование объекта')

    def __str__(self):
        return self.number

    class Meta:
        verbose_name_plural = 'Поз. по генплану'


# начальники укпг2
class Approve(models.Model):
    name = models.CharField(max_length=30, verbose_name='ФИО утв.')
    job_title = models.CharField(max_length=255, verbose_name='Должность')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Утверждающие'


# начальники подрядных организаций
class Contractor(models.Model):
    name = models.CharField(max_length=30, verbose_name='ФИО')
    job_title = models.CharField(max_length=255, verbose_name='Должность')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Подрядные организации'


# работники КАиТ
class Kait(models.Model):
    name = models.CharField(max_length=30, verbose_name='ФИО')
    job_title = models.CharField(max_length=255, verbose_name='Должность')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Работники КАиТ'
        ordering = ('-job_title',)


# начальники по цеху
class Worker(models.Model):
    name = models.CharField(max_length=30, verbose_name='ФИО')
    job_title = models.CharField(max_length=255, verbose_name='Должность')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Мастера цеха'


class Kip(models.Model):
    number = models.CharField(max_length=255, blank=True, verbose_name='№ п/п')
    serial_number = models.CharField(max_length=255, blank=False, verbose_name='Заводской номер')
    defective_act = models.CharField(max_length=255, blank=True, verbose_name='№ дефектного акта')
    poz_GP = models.ForeignKey(GP, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='gps',
                               verbose_name='Поз. по ГП')
    tag = models.CharField(max_length=255, blank=True, verbose_name='ТЭГ')
    type = models.CharField(max_length=255, blank=True, verbose_name='Тип')
    name_of_equipment = models.TextField(blank=True, verbose_name='Наименование оборуования')
    equipment_acceptance_date_PNR = models.CharField(max_length=255, blank=True,
                                                     verbose_name='Дата приемки оборудования в ПНР')
    equipment_manufacturer = models.CharField(max_length=255, blank=True, verbose_name='Производитель оборудования')
    project = models.CharField(max_length=255, blank=True, verbose_name='Проект')
    date_at = models.DateField(auto_now_add=True, verbose_name='Дата добавления')
    date_of_detection = models.CharField(max_length=255, blank=True, verbose_name='Дата выявления')
    installation_location = models.CharField(max_length=255, blank=True, verbose_name='Место установки')
    description = models.TextField(blank=True, verbose_name='Краткое описание дефекта')
    reasons_for_failure = models.TextField(blank=True, verbose_name='Возможные причины выхода из строя')
    elimination_of_defects = models.CharField(max_length=255, blank=True,
                                              verbose_name='Для устранения выявленных дефектов необходимо')
    operating_time = models.CharField(max_length=255, blank=True, verbose_name='Время наработки, ч')
    executor_3 = models.ForeignKey(Contractor, on_delete=models.DO_NOTHING, blank=True, null=True,
                                   related_name='contractors',
                                   verbose_name='ФИО Исполнителя 3')
    executor_1 = models.ForeignKey(Kait, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='kaits',
                                   verbose_name='ФИО Исполнителя 1')
    executor_2 = models.ForeignKey(Worker, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='workers',
                                   verbose_name='ФИО Исполнителя 2')
    person_approving = models.ForeignKey(Approve, on_delete=models.DO_NOTHING, blank=True, null=True,
                                         related_name='approves',
                                         verbose_name='ФИО утвеждающего')
    approval_date = models.CharField(max_length=255, blank=True, verbose_name='Дата утверждения')
    number_letter_INVEST = models.CharField(max_length=255, blank=True, verbose_name='№ исходящего письма')
    letter_to_INVEST = models.CharField(max_length=255, blank=True, verbose_name='Дата отправки письма в Инвест')
    location = models.CharField(max_length=255, blank=True, verbose_name='Место нахождения')
    notes = models.CharField(max_length=255, blank=True, verbose_name='Примечания')
    fio_locksmith_1 = models.CharField(max_length=255, blank=True, verbose_name='ФИО слесаря')
    fio_locksmith_2 = models.CharField(max_length=255, blank=True, verbose_name='ФИО слесаря')
    elimination_date = models.CharField(max_length=255, blank=True, verbose_name='Дата устранения')
    fio_responsible = models.CharField(max_length=255, blank=True, verbose_name='ФИО отв.')
    mark_of_elimination = models.CharField(max_length=255, blank=True, null=True, verbose_name='Отметка об устранении')

    def __str__(self):
        return self.serial_number

    class Meta:
        verbose_name_plural = 'Оборудование КИП'
        ordering = ('-date_at',)
