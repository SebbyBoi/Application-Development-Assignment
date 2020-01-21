from wtforms import validators
from wtforms.fields import SubmitField, StringField, FileField, TextAreaField
from wtforms import Form

class ProductCreate(Form):
  id = StringField('ID', [validators.Length(min=1, max=150), validators.DataRequired()])
  title = StringField('Title', [validators.Length(min=1, max=150), validators.DataRequired()])
  stock = StringField('Stock', [validators.Length(min=1, max=150), validators.DataRequired()])
  file = FileField("Product image")
  costprice = StringField('Cost Price', [validators.Length(min=1, max=150), validators.DataRequired()])
  retailprice = StringField('Retail Price', [validators.Length(min=1, max=150), validators.DataRequired()])
  description = TextAreaField('Description', [validators.Length(min=1, max=150), validators.DataRequired()])

