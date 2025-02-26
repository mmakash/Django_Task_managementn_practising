from django import forms
from tasks.models import Employee,Task,TaskDetails

class TaskForm(forms.Form):
    title = forms.CharField(max_length=100,label="Task Title")
    description = forms.CharField(widget=forms.Textarea,label="Task Description")
    due_date = forms.DateField(widget=forms.SelectDateWidget,label="Due Date")
    assigned_to = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,label="Assigned To",choices=[])

    def __init__(self, *args, **kwargs):
        # print(args,kwargs)
        employes = kwargs.pop("employes",[])
        super().__init__(*args, **kwargs)
        # list comprehension
        self.fields["assigned_to"].choices = [(emp.id,emp.name) for emp in employes]

class StyleFormMixin:
    """This mixin will add style to form fields"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_style_widgets() 

    default_classess = "border-2 border-gray-300 w-full p-3 rounded-lg shadow-sm focus:outline-none focus:border-rose-700 focus:ring-rose-500"
    
    def apply_style_widgets(self):
        for field_name, field in self.fields.items():
            if isinstance(field.widget, (forms.TextInput, forms.EmailInput, forms.PasswordInput)):
                field.widget.attrs.update({
                    'class': self.default_classess,
                    'placeholder': f"Enter {field.label.lower()}"
                })
            elif isinstance(field.widget, forms.Textarea):
                field.widget.attrs.update({
                    'class': self.default_classess,
                    'placeholder': f"Enter {field.label.lower()}",
                    'rows': 4
                })
            elif isinstance(field.widget, forms.SelectDateWidget):
                field.widget.attrs.update({
                    'class': self.default_classess
                })
            elif isinstance(field.widget, forms.CheckboxSelectMultiple):
                field.widget.attrs.update({
                    'class': 'space-y-2'
                })


# django model form
class TaskModelForm(StyleFormMixin,forms.ModelForm):
    class Meta:
        model = Task
        fields = ["tite","description","due_date","assigned_to"]

        # exclude = ["assigned_to","is_completed","created_at","updated_at"]

class TaskDetailsModelForm(StyleFormMixin,forms.ModelForm):
    class Meta:
        model = TaskDetails
        fields = ["priority","notes"]
    