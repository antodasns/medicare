from django import forms
# from staff.models import staffs_table
from django.contrib.auth.models import User,Group
from administration.models import medical_details,user_details,doctor_details
gender=(
	('male','male'), 
	('female','female')
	)
staff_designation=(
	('admin','Admin'),
	('manager','Manager'),
	('stock','Stock'),
	('sales','Sales'),
	)
salary_type=(
	('male','male'),
	('female','female')
	)



# class create_staffs(forms.ModelForm):


# 	class Meta:
# 		model=staffs_table
# 		fields=['staffs_gender','staffs_date_of_birth','staffs_phone','staffs_sale_type','staffs_salary']
# 		widgets = {
#             'staffs_gender': forms.Select(attrs={'class':'form-control',}),
#             'staffs_date_of_birth': forms.DateInput(attrs={'class':'form-control','type':'date','id':'example-date-input'}),
#             'staffs_phone': forms.NumberInput(attrs={'class':'form-control','max_length': '10','id':"example-number-input"}),
#             'staffs_sale_type': forms.Select(attrs={'class':'form-control',}),
#             'staffs_salary': forms.NumberInput(attrs={'class':'form-control','value':"0",'id':"example-number-input"}),
#         }




class UserForm2(forms.ModelForm):
	role=forms.ModelChoiceField(queryset=Group.objects.all(),widget=forms.Select(attrs={'class':'form-control',}))

	class Meta:
		model=User
		fields=['first_name','last_name','date_joined']
		widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter ...'}),
            'last_name': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter ...'}),
            'date_joined': forms.TextInput(attrs={'class':'form-control','type':'date'}),
        }
	# def save(self):
	# # # 	username=self.cleaned_data.pop('first_name')
	# 	role=self.cleaned_data.pop('role')
	# 	u=super().save()
	# 	u.user.set([role])
	# # # 	# u.set_username(username)
	# 	u.save()
	# 	return u

class UserForm(forms.ModelForm):
	password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'mdl-textfield__input','placeholder':'Password'}))
	role=forms.ModelChoiceField(queryset=Group.objects.all().exclude(name__in=['doc_group','admin_group']),initial=0,widget=forms.Select(attrs={'class':'mdl-selectfield__select','placeholder':'Designation','name':'designation'}))
	confirm_password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'mdl-textfield__input','placeholder':'Confirm Password'}))
	class Meta:
		model=User
		fields=['username','email','password']
		widgets = {
           
           
            'username': forms.TextInput(attrs={'class':'mdl-textfield__input','placeholder':'Username','name':'username'}),
            'email': forms.TextInput(attrs={'class':'mdl-textfield__input','placeholder':'Email','name':'email'}),
          
        }

		label={'password':'Password'}

	def clean(self):
		cleaned_data = super(UserForm, self).clean()
		password = cleaned_data.get("password")
		confirm_password = cleaned_data.get("confirm_password")


		min_length = 6
		if len(password) < min_length:
			msg = 'Password must be at least %s characters long.' %(str(min_length))
			self.add_error('password', msg)

		
		
		if password != confirm_password:
			raise forms.ValidationError(
				"password and confirm_password does not match"
				)
		return self.cleaned_data
	def __init__(self,*args,**kwargs):
		if kwargs.get('instance'):
			initial=kwargs.setdefault('initial',{})
			if kwargs['instance'].groups.all():
				initial['role']=kwargs['instance'].groups.all()[0]
			else:
				initial['role']=None 
		forms.ModelForm.__init__(self,*args,**kwargs)

	def save(self):
		password=self.cleaned_data.pop('password')
		role=self.cleaned_data.pop('role')
		
		u=super().save()
		u.groups.set([role])
		u.set_password(password)
		u.save()
		return u



 
class UserFormdoctors(forms.ModelForm):
	password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'mdl-textfield__input','placeholder':'Password'}))
	role=forms.ModelChoiceField(queryset=Group.objects.all().exclude(name__in=['user_group','admin_group']),initial=0,widget=forms.Select(attrs={'class':'mdl-selectfield__select','placeholder':'Designation','name':'designation'}))
	confirm_password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'mdl-textfield__input','placeholder':'Confirm Password'}))
	class Meta:
		model=User
		fields=['username','email','password']
		widgets = {
           
           
            'username': forms.TextInput(attrs={'class':'mdl-textfield__input','placeholder':'Username','name':'username'}),
            'email': forms.TextInput(attrs={'class':'mdl-textfield__input','placeholder':'Email','name':'email'}),
          
        }

		label={'password':'Password'}

	def clean(self):
		cleaned_data = super(UserFormdoctors, self).clean()
		password = cleaned_data.get("password")
		confirm_password = cleaned_data.get("confirm_password")


		min_length = 6
		if len(password) < min_length:
			msg = 'Password must be at least %s characters long.' %(str(min_length))
			self.add_error('password', msg)

		
		
		if password != confirm_password:
			raise forms.ValidationError(
				"password and confirm_password does not match"
				)
		return self.cleaned_data
	def __init__(self,*args,**kwargs):
		if kwargs.get('instance'):
			initial=kwargs.setdefault('initial',{})
			if kwargs['instance'].groups.all():
				initial['role']=kwargs['instance'].groups.all()[0]
			else:
				initial['role']=None 
		forms.ModelForm.__init__(self,*args,**kwargs)

	def save(self):
		password=self.cleaned_data.pop('password')
		role=self.cleaned_data.pop('role')
		
		u=super().save()
		u.groups.set([role])
		u.set_password(password)
		u.save()
		return u