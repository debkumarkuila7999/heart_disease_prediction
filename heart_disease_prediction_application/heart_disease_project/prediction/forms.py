from django import forms # type: ignore

class PredictionForm(forms.Form):
    age = forms.IntegerField(
        label='Age',
        min_value=0,
        max_value=120,
        error_messages={
            'required': 'This field is required.',
            'min_value': 'Age must be a positive number.',
            'max_value': 'Please enter a realistic age.'
        }
    )
    sex = forms.ChoiceField(
        choices=[(0, 'Female'), (1, 'Male')],
        label='Sex',
        error_messages={'required': 'Please select your sex.'}
    )
    cp = forms.ChoiceField(
        choices=[
            (0, 'Typical Angina'),
            (1, 'Atypical Angina'),
            (2, 'Non-Anginal'),
            (3, 'Asymptomatic')
        ],
        label='Chest Pain Type',
        error_messages={'required': 'Please select a chest pain type.'}
    )
    trestbps = forms.IntegerField(
        label='Resting Blood Pressure (mm Hg)',
        min_value=0,
        error_messages={
            'required': 'This field is required.',
            'min_value': 'Blood pressure cannot be negative.'
        }
    )
    chol = forms.IntegerField(
        label='Serum Cholesterol (mg/dl)',
        min_value=0,
        error_messages={
            'required': 'This field is required.',
            'min_value': 'Cholesterol cannot be negative.'
        }
    )
    thalch = forms.IntegerField(
        label='Maximum Heart Rate Achieved',
        min_value=0,
        error_messages={
            'required': 'This field is required.',
            'min_value': 'Heart rate cannot be negative.'
        }
    )
    restecg = forms.ChoiceField(
        choices=[
            (0, 'Normal'),
            (1, 'LV Hypertrophy'),
            (2, 'ST-T wave abnormality')
        ],
        label='Resting ECG',
        error_messages={'required': 'Please select a resting ECG type.'}
    )
    oldpeak = forms.FloatField(
        label='Oldpeak (ST depression)',
        min_value=0,
        error_messages={
            'required': 'This field is required.',
            'min_value': 'Oldpeak cannot be negative.'
        }
    )
    slope = forms.ChoiceField(
        choices=[
            (0, 'Upsloping'),
            (1, 'Flat'),
            (2, 'Downsloping')
        ],
        label='Slope',
        error_messages={'required': 'Please select a slope type.'}
    )
    ca = forms.IntegerField(
        label='Number of Major Vessels (0-3)',
        min_value=0,
        max_value=3,
        error_messages={
            'required': 'This field is required.',
            'min_value': 'Number of vessels cannot be negative.',
            'max_value': 'Please enter a realistic number (0-3).'
        }
    )
    thal = forms.ChoiceField(
        choices=[
            (0, 'Normal'),
            (1, 'Fixed Defect'),
            (2, 'Reversible Defect')
        ],
        label='Thalassemia',
        error_messages={'required': 'Please select a thalassemia type.'}
    )
