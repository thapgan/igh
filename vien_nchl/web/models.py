import datetime
from uuid import uuid4

# Create your models here.
from django.db.models import Model, UUIDField, CharField, IntegerField, \
    ImageField, DateTimeField
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
from parler.forms import TranslatableModelForm
from parler.models import TranslatableModel, TranslatedFields

STATUS_FIELD = ((1, 'Active'), (0, 'Inactive'))


class Slide(TranslatableModel):
    id = UUIDField(primary_key=True, default=uuid4)
    translations = TranslatedFields(
        name=CharField(_("Tiêu đề"), max_length=500, null=True, blank=True),
        description=CharField(_("Mô tả"), max_length=1000, null=True,
                              blank=True)
    )
    status = IntegerField(choices=STATUS_FIELD, default=0)
    image = ImageField(upload_to='upload/images')
    created_on = DateTimeField(default=datetime.datetime.utcnow)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Slide ảnh"
        verbose_name_plural = "Slide ảnh"

    def __str__(self):
        return self.name


class SlideForm(TranslatableModelForm):
    class Meta:
        model = Slide
        exclude = ['id', 'created_on', 'updated_at']


class Doctor(TranslatableModel):
    id = UUIDField(primary_key=True, default=uuid4)
    translations = TranslatedFields(
        name=CharField(_("Tên"), max_length=500),
        level=CharField(_("Học hàm học vị"), max_length=500),
        description=CharField(_("Mô tả"), max_length=2000)
    )
    image = ImageField(upload_to='upload/images')
    status = IntegerField(choices=STATUS_FIELD, default=0)
    created_on = DateTimeField(default=datetime.datetime.utcnow)
    updated_at = DateTimeField(auto_now=True)


    class Meta:
        verbose_name = "Danh sách bác sỹ"
        verbose_name_plural = "Danh sách bác sỹ"

    def __str__(self):
        return self.name


class DoctorForm(TranslatableModelForm):
    class Meta:
        model = Doctor
        exclude = ['id', 'created_on', 'updated_at']
