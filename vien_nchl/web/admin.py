from aldryn_translation_tools.admin import AllTranslationsMixin
from cms.utils.i18n import get_current_language
from cms.utils.urlutils import admin_reverse
from django.contrib import admin

# Register your models here.
from parler.admin import TranslatableAdmin

from django.conf import settings
from vien_nchl.web.models import SlideForm, DoctorForm, Slide, Doctor
from django.utils.translation import force_text, ugettext as _


class BaseTranslastionMixin(AllTranslationsMixin):
    def all_translations(self, obj):
        """
        Adds a property to the list_display that lists all translations with
        links directly to their change forms. Includes CSS to style the links
        to looks like tags with color indicating current language, active and
        inactive translations.

        A similar capability is in HVAD, and now there is this for
        Parler-based projects.
        """
        available = list(obj.get_available_languages())
        current = get_current_language()
        langs = []
        for code, lang_name in settings.LANGUAGES:
            classes = ["lang-code", ]
            title = force_text(lang_name)
            if code == current:
                classes += ["current", ]
            if code in available:
                classes += ["active", ]
                title += " (translated)"
            else:
                title += " (untranslated)"
            change_form_url = admin_reverse(
                '{app_label}_{model_name}_change'.format(
                    app_label=obj._meta.app_label.lower(),
                    model_name=obj.__class__.__name__.lower(),
                ), args=(obj.id,)
            )
            link = ('<a class="{classes}" href="{url}?language={code}" ' +
                    'title="{title}">  {code}  </a> ').format(
                classes=' '.join(classes),
                url=change_form_url,
                code=code,
                title=title,
            )
            langs.append(link)
        return ''.join(langs)

    all_translations.short_description = 'Translations'
    all_translations.allow_tags = True


class SlideAdmin(BaseTranslastionMixin, TranslatableAdmin):
    form = SlideForm
    search_fields = ('translations__name', 'translations__description')
    list_filter = ('status',)
    ordering = ('-updated_at',)


class DoctorAdmin(BaseTranslastionMixin, TranslatableAdmin):
    form = DoctorForm
    search_fields = ('translation__name', 'translation__level')
    list_filter = ('status',)
    ordering = ('-updated_at',)


admin.site.register(Slide, SlideAdmin)
admin.site.register(Doctor, DoctorAdmin)
