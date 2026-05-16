# from django import forms
# from .models import Attendance

# class AttendanceForm(forms.ModelForm):

#     class Meta:

#         model = Attendance

#         fields = '__all__'

#         widgets = {

#             'date': forms.DateInput(
#                 attrs={'type': 'date'}
#             )

#         }

#     def clean(self):

#         cleaned_data = super().clean()

#         student = cleaned_data.get('student')

#         date = cleaned_data.get('date')

#         if Attendance.objects.filter(
#             student=student,
#             date=date
#         ).exists():

#             raise forms.ValidationError(
#                 "Attendance already marked for this student today."
#             )

#         return cleaned_data

from django import forms
from .models import Attendance


class AttendanceForm(forms.ModelForm):

    class Meta:

        model = Attendance

        fields = '__all__'

        widgets = {

            'date': forms.DateInput(

                attrs={

                    'type': 'date'

                }

            )

        }

    def clean(self):

        cleaned_data = super().clean()

        student = cleaned_data.get(
            'student'
        )

        date = cleaned_data.get(
            'date'
        )

        attendance_qs = Attendance.objects.filter(

            student=student,

            date=date

        )

        # EXCLUDE CURRENT RECORD DURING UPDATE

        if self.instance.pk:

            attendance_qs = attendance_qs.exclude(

                pk=self.instance.pk

            )

        # DUPLICATE VALIDATION

        if attendance_qs.exists():

            raise forms.ValidationError(

                "Attendance already marked for this student on this date."

            )

        return cleaned_data