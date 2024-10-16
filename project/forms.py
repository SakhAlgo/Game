from flask_wtf import FlaskForm
from wtforms import SelectField, IntegerField
from wtforms.validators import Email, NumberRange, DataRequired

class GameProfile(FlaskForm):
    way = SelectField(
    "Выберите сторону света в которую желаете отправиться",
    coerce = int,
    choises = [(0, 'Север'),
               (1, 'Юг'),
               (2, 'Запад'),
               (3, 'Восток'),
    ],
    render_kw = {'class': 'form-control'},
    number_steps = IntegerField(
        'Как далеко планируете продвинуться?',
        default = 1,
        render_kw = {
            'class': 'form-control'
        }
    )
)
    