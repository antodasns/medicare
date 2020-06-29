from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect 
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User,Group
from django.http import HttpResponse,HttpResponseRedirect
# from administration.models import user_details
from administration.forms import UserForm,UserForm2,UserFormdoctors
from administration.models import medical_details,user_details,doctor_details,appointment,prescription,results,specilizatin,rating,payments
from django.db.models import Q
# Create your views here.
# 


def user_logout(request):
	
	logout(request)
	return HttpResponseRedirect('/')
def index(request):
	return render(request,'administration/index.html')

def admin_management(request):
	form=UserForm()
	return render(request,'administration/registration.html',{'form':form})

def add_specilization(request):
	
	return render(request,'administration/add_specilization.html')


def user_login(request):
	if request.method == 'POST':
		
		user_name=request.POST.get('username')
		pass_word=request.POST.get('password')
		designation=request.POST.get('designation')
		current_user=1
		user = authenticate(username=user_name, password=pass_word)
		if user:
			login(request,user)
			current_user=request.user.id
		user_designation=Group.objects.values_list('name', flat=True).get(user=current_user)
		
		if designation==user_designation:

			if designation=='admin_group':
				if user:
					login(request,user)
					return HttpResponseRedirect('/doctor_registration')
				else:
					return render(request,'administration/login.html')
			
			elif designation=='doc_group':
				approval=doctor_details.objects.values_list('approval', flat=True).get(login_id=current_user)
				if approval=='yes':
					if user:
						login(request,user)
						return HttpResponseRedirect('/doctor_view_bookings')
					else:
						return render(request,'administration/login.html')
				else:
						return render(request,'administration/login.html')
			
			elif designation=='user_group':
				if user:
					login(request,user)
					return HttpResponseRedirect('/user_view_doctors')
				else:
					return render(request,'administration/login.html')
			else:
				return render(request,'administration/login.html')
		
		
	return render(request,'administration/login.html')

def user_registration(request):
	
	form=UserForm()
	log_id=User.objects.values_list('pk', flat=True).latest('id')	
	if request.method == 'POST':
		# return HttpResponse(request.POST['age'])
		form = UserForm(request.POST)
		
		if form.is_valid():
			cre_user=user_details(
			username=form.cleaned_data['username'],
			age=request.POST['age'],
			address=request.POST['address'],
			phone=request.POST['phone'],
			gender=request.POST['gender'],
			bloodgroup=request.POST['bloodgroup'],
			email=form.cleaned_data['email'],
			login_id=int(log_id)+1,
			approval="no"
			)
			cre_user.save()
			form.save()

			return HttpResponseRedirect('/')
	else:

		form=UserForm()
		
	return render(request,'administration/user_registration.html',{'form':form})



def registration(request):
	form=UserForm()
	log_id=User.objects.values_list('pk', flat=True).latest('id')	
	if request.method == 'POST':
		
		form = UserForm(request.POST)
		if form.is_valid():
			cre_user=user_details(
			username=form.cleaned_data['username'],
			age=request.POST['age'],
			address=request.POST['address'],
			phone=request.POST['phone'],
			gender=request.POST['gender'],
			bloodgroup=request.POST['bloodgroup'],
			email=form.cleaned_data['email'],
			login_id=int(log_id)+1,
			approval="no"
			)
			cre_user.save()
			form.save()

			return HttpResponseRedirect('/registration')
	else:

		form=UserForm()
	
	return render(request,'administration/registration.html',{'form':form})

def doctor_registration(request):
	
	form=UserFormdoctors()
	log_id=User.objects.values_list('pk', flat=True).latest('id')
	
	if request.method == 'POST':
		cre_medical=doctor_details(
			username=request.POST['username'],
			regno=request.POST['regno'],
			email=request.POST['email'],
			specialization=request.POST['specialisation'],
			photo=request.FILES['photo'],
			phone=request.POST['phone'],
			place=request.POST['place'],
			login_id=int(log_id)+1,
			approval="no"
			)
		cre_medical.save()
		
		form = UserFormdoctors(request.POST)
		if form.is_valid():
			form.save()

			return HttpResponseRedirect('/doctor_registration')
	else:

		form=UserFormdoctors()
	sp=specilizatin.objects.all()
	return render(request,'administration/doctor_registration.html',{'form':form,'sp':sp})

def doc_outside_registration(request):
	form=UserFormdoctors()
	log_id=User.objects.values_list('pk', flat=True).latest('id')
	if request.method == 'POST':
		
		cre_medical=doctor_details(
			username=request.POST['username'],
			regno=request.POST['regno'],
			email=request.POST['email'],
			specialization=request.POST['specialisation'],
			photo=request.FILES['photo'],
			phone=request.POST['phone'],
			place=request.POST['place'],
			login_id=int(log_id)+1,
			approval="no"
			)
		cre_medical.save()
		
		form = UserFormdoctors(request.POST)
		if form.is_valid():
			form.save()

			return HttpResponseRedirect('/')
	else:

		form=UserFormdoctors()
	sp=specilizatin.objects.all()
	return render(request,'administration/doc_outside_registration.html',{'form':form,'sp':sp})


@login_required(login_url='/user_login')
def add_medical(request):
	
		
	if request.method == 'POST':
		cre_medical=medical_details(
			name=request.POST['name'],
			address=request.POST['address'],
			phone=request.POST['phone'],
			pincode=request.POST['pincode'],
			)
		cre_medical.save()

	
	return render(request,'administration/add_medical.html')

def add_specilization(request):
	if request.method == 'POST':
		cre_spec=specilizatin(
			specilization=request.POST['specilization']
			)
		cre_spec.save()
	return render (request, 'administration/add_specilization.html')

def view_doctors(request):
	
	details=doctor_details.objects.all()
	
	return render(request,'administration/view_doctors.html',{'details':details})

def view_report(request):
	user=[]
	doc=[]
	date=[]

	appoint_details=appointment.objects.all()
	for x in appoint_details:
		try:
			sss=user_details.objects.values_list('username', flat=True).get(id=x.user_ref_id)
		except user_details.DoesNotExist:
			sss = None
		try:
			aaa=doctor_details.objects.values_list('username', flat=True).get(id=x.user_ref_id)
		except doctor_details.DoesNotExist:
			aaa = None
		user.append(sss)
		doc.append(aaa)
		date.append(x.date)
	zippy=zip(user,doc,date)
	return render(request,'administration/view_report.html',{'zippy':zippy})


def delete_doc(request,id):
	doc_delete=doctor_details.objects.get(pk=id)
	doc_delete.delete()
	return HttpResponseRedirect('/view_doctors')
def view_users(request):
	details=user_details.objects.all()

	return render(request,'administration/view_users.html',{'details':details})
def delete_user(request,id):
	use_delete=user_details.objects.get(pk=id)
	use_delete.delete()
	return HttpResponseRedirect('/view_users')
@login_required(login_url='/user_login')
def view_appointments(request):


	return render(request,'administration/view_appointments.html')
@login_required(login_url='/user_login')
def view_medicals(request):
	details=medical_details.objects.all()

	return render(request,'administration/view_medical.html',{'details':details})
@login_required(login_url='/user_login')
def view_prescriptions(request):


	return render(request,'administration/view_prescription.html')



@login_required(login_url='/user_login')
def doctor_view_bookings(request):
	user_name=[]
	date=[]
	user_id=[]
	appointment_id=[]

	doc_ref_id=doctor_details.objects.values_list('id', flat=True).get(login_id=request.user.id)
	appointements=appointment.objects.filter(doctor_ref_id=doc_ref_id)

	for x in appointements:
		user_name.append(user_details.objects.values_list('username', flat=True).get(pk=x.user_ref_id))
		date.append(x.date)
		user_id.append(x.user_ref_id)
		appointment_id.append(x.id)

	return render(request,'administration/doctor_view_bookings.html',{'zippy':zip(user_name,date,user_id,appointment_id)})
@login_required(login_url='/user_login')
def doctor_view_patients(request):
	user_name=[]
	date=[]
	user_id=[]
	prescription_id=[]
	doc_ref_id=doctor_details.objects.values_list('id', flat=True).get(login_id=request.user.id)
	prescriptions=prescription.objects.filter(doctor_ref_id=doc_ref_id)
	print(doc_ref_id)
	for x in prescriptions:
		user_name.append(user_details.objects.values_list('username', flat=True).get(pk=x.user_ref_id))
		date.append(x.date)
		user_id.append(x.user_ref_id)
		prescription_id.append(x.id)

	return render(request,'administration/doctor_view_patients.html',{'zippy':zip(user_name,date,prescription_id)})

@login_required(login_url='/user_login')
def user_profiles(request):
	details=user_details.objects.get(login_id=request.user.id)
	# return HttpResponse(details.username)
	return render(request,'administration/user_profile.html',{'details':details})
	
	
@login_required(login_url='/user_login')
def doctor_settings(request):
	
	doc_update=doctor_details.objects.get(login_id=request.user.id)
	weeks=[]
	weekdays=['0','1','2','3','4','5','6']
	new_week=[]
	slots=[]
	
	if request.method == 'POST':
		if request.POST.get('mon') != None:
			weeks.append(request.POST.get('mon'))
		if request.POST.get('tue') != None:
			weeks.append(request.POST.get('tue'))
		if request.POST.get('wed') != None:
			weeks.append(request.POST.get('wed'))
		if request.POST.get('thu') != None:
			weeks.append(request.POST.get('thu'))
		if request.POST.get('fri') != None:
			weeks.append(request.POST.get('fri'))
		if request.POST.get('sat') != None:
			weeks.append(request.POST.get('sat'))
		if request.POST.get('sun') != None:
			weeks.append(request.POST.get('sun'))
		
		
		new_week=[item for item in weekdays if item not in weeks]



	if request.method == 'POST':
		if request.POST.get('slot1') != None:
			slots.append(request.POST.get('slot1'))
		if request.POST.get('slot2') != None:
			slots.append(request.POST.get('slot2'))
		if request.POST.get('slot3') != None:
			slots.append(request.POST.get('slot3'))
		if request.POST.get('slot4') != None:
			slots.append(request.POST.get('slot4'))
		if request.POST.get('slot5') != None:
			slots.append(request.POST.get('slot5'))
		if request.POST.get('slot6') != None:
			slots.append(request.POST.get('slot6'))
		if request.POST.get('slot7') != None:
			slots.append(request.POST.get('slot7'))
		if request.POST.get('slot8') != None:
			slots.append(request.POST.get('slot8'))
		if request.POST.get('slot9') != None:
			slots.append(request.POST.get('slot9'))
		if request.POST.get('slot10') != None:
			slots.append(request.POST.get('slot10'))
		if request.POST.get('slot11') != None:
			slots.append(request.POST.get('slot11'))
		if request.POST.get('slot12') != None:
			slots.append(request.POST.get('slot12'))
		
		doc_update.active_days=new_week
		doc_update.time_slots=slots
		doc_update.consolt_fee=request.POST['consul_fee']
		doc_update.appoint_limit=request.POST['app_limit']
		doc_update.save()
		return HttpResponseRedirect('/doctor_settings')

	return render(request,'administration/doctor_settings.html',{'doc_update':doc_update})
@login_required(login_url='/user_login')
def doctor_add_prescription(request,id):

	return render(request,'administration/doctor_add_prescription.html',{'id':id})
@login_required(login_url='/user_login')
def doctor_save_prescription(request):
	from datetime import date
	doc_ref_id=doctor_details.objects.values_list('id', flat=True).get(login_id=request.user.id)
	cre_prescr=prescription(
	user_ref_id=request.POST['user_id'],
	doctor_ref_id=doc_ref_id,
	prescription=request.POST['prescription'],
	diets_tips=request.POST['diets_tips'],
	date=date.today()
	)
	cre_prescr.save()

	return HttpResponseRedirect('/doctor_view_bookings')

@login_required(login_url='/user_login')
def doctor_view_prescription(request,id):
	prescriptions=prescription.objects.get(pk=id)

	return render(request,'administration/doctors_view_prescription.html',{'prescriptions':prescriptions})
@login_required(login_url='/user_login')
def doctor_view_result(request,id):
	# user_ref_id=user_details.objects.values_list('id', flat=True).get(login_id=request.user.id)
	result=results.objects.filter(user_ref_id=id)

	return render(request,'administration/doctors_view_results.html',{'id':id,'result':result})



@login_required(login_url='/user_login')
def user_view_doctors(request):
	details=doctor_details.objects.all().order_by('-id').filter(approval="yes")
	user_detail=user_details.objects.get(login_id=request.user.id)

	return render(request,'administration/user_view_doctors.html',{'details':details,'user_detail':user_detail})



@login_required(login_url='/user_login')
def user_make_booking(request,id):
	user_detail=user_details.objects.get(login_id=request.user.id)
	import re
	import datetime
	from django.db.models import Count
	avail_list2=[]
	tag_option=''
	script_tag=''
	tag_slot_option=''
	avail_days=doctor_details.objects.values_list('active_days', flat=True).get(pk=id)
	time_slots=doctor_details.objects.values_list('time_slots', flat=True).get(pk=id)
	consol_fee=doctor_details.objects.values_list('consolt_fee', flat=True).get(pk=id)
	avail_list=re.findall(r'\d+', avail_days)
	slot_list=re.findall(r'\d+', time_slots)
	for x in avail_list:
		if x=='0':
			tag_option=tag_option+' && !isMonday(date)'
		if x=='1':
			tag_option=tag_option+' && !isTuesday(date)'
		if x=='2':
			tag_option=tag_option+' && !isWednesday(date)'
		if x=='3':
			tag_option=tag_option+' && !isThursday(date)'
		if x=='4':
			tag_option=tag_option+' && !isFriday(date)'
		if x=='5':
			tag_option=tag_option+' && !isSaturday(date)'
		if x=='6':
			tag_option=tag_option+' && !isSunday(date)'
	script_tag="<script>var disableddates = ['26-04-2018'];function DisableDates(date) {var selectable = !isDateDisabled(date)%s;return [selectable];\
	}function isMonday(date) {var day = date.getDa();return day === 0;}function isTuesday(date) {var day = date.getDay();return day === 1;}function \
	isWednesday(date) {var day = date.getDay();return day === 2;}function isThursday(date) {var day = date.getDay();return day === 3;}function \
	isFriday(date) {var day = date.getDay();return day === 4;}function isSaturday(date) {var day = date.getDay();return day === 5;}function \
	isSunday(date) {var day = date.getDay();return day === 6;}function isDateDisabled(date) {var m = date.getMonth() + 1;var d =\
	 date.getDate();var y = date.getFullYear();if(d < 10) d = '0' + d;if(m < 10) m = '0' + m;var currentdate = d + '-' + m + '-' + \
	 y;return disableddates.indexOf(currentdate) >= 0;}$('#datepicker').datepicker({dateFormat: 'dd-mm-yy',minDate: 1,beforeShowDay: DisableDates});</script>"%tag_option
	groupi=appointment.objects.values('date', 'slot_id').filter(doctor_ref_id=id).order_by().annotate(Count('date'), Count('slot_id'))
	print(slot_list)
	for x in groupi:
		if x['slot_id__count']>=4:
			
			rem=x['slot_id']
			
			try:
				slot_list.remove(rem)
			except Exception as e:
				pass
					
	
	print(slot_list)
	
	for x in slot_list:
		if x=='0':
			tag_slot_option=tag_slot_option+'<option value="0">9:00-10:00</option>'
		if x=='1':
			tag_slot_option=tag_slot_option+'<option value="1">10:00-11:00</option>'
		if x=='2':
			tag_slot_option=tag_slot_option+'<option value="2">11:00-12:00</option>'
		if x=='3':
			tag_slot_option=tag_slot_option+'<option value="3">12:00-1:00</option>'
		if x=='4':
			tag_slot_option=tag_slot_option+'<option value="4">1:00-2:00</option>'
		if x=='5':
			tag_slot_option=tag_slot_option+'<option value="5">2:00-3:00</option>'
		if x=='6':
			tag_slot_option=tag_slot_option+'<option value="6">3:00-4:00</option>'
		if x=='7':
			tag_slot_option=tag_slot_option+'<option value="7">4:00-5:00</option>'
		if x=='8':
			tag_slot_option=tag_slot_option+'<option value="8">5:00-6:00</option>'
		if x=='9':
			tag_slot_option=tag_slot_option+'<option value="9">6:00-7:00</option>'
		if x=='10':
			tag_slot_option=tag_slot_option+'<option value="10">7:00-8:00</option>'
		if x=='11':
			tag_slot_option=tag_slot_option+'<option value="11">8:00-9:00</option>'				

	return render(request,'administration/user_make_booking.html',{'script_tag':script_tag,'consol_fee':consol_fee,'tag_slot_option':tag_slot_option,'id':id,'user_detail':user_detail})

@login_required(login_url='/user_login')
def user_create_appointment(request):
	user_detail=user_details.objects.get(login_id=request.user.id)
	import datetime
	user_ref_id=user_details.objects.values_list('id', flat=True).get(login_id=request.user.id)

	cre_appoi=appointment(
	user_ref_id=user_ref_id,
	doctor_ref_id=request.POST['id'],
	slot_id=request.POST['slot'],
	date=request.POST['selected_date']
	)
	cre_appoi.save()
	return HttpResponseRedirect('/payment%d'%int(request.POST['consul_fees']))
@login_required(login_url='/user_login')
def user_view_bookings(request):
	user_detail=user_details.objects.get(login_id=request.user.id)
	doct_name=[]
	doct_special=[]
	weekday=[]
	date=[]
	idss=[]
	weekday_list=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

	user_ref_id=user_details.objects.values_list('id', flat=True).get(login_id=request.user.id)
	appointements=appointment.objects.filter(user_ref_id=user_ref_id)
	for x in appointements:

		doct_name.append(doctor_details.objects.values_list('username', flat=True).get(pk=x.doctor_ref_id))
		doct_special.append(doctor_details.objects.values_list('specialization', flat=True).get(pk=x.doctor_ref_id))
		weekday.append(1)
		date.append(x.date)
		idss.append(x.id)
	return render(request,'administration/user_view_bookings.html',{'zippy':zip(doct_name,doct_special,weekday,date,idss),'user_detail':user_detail})

@login_required(login_url='/user_login')
def user_add_results(request):
	user_detail=user_details.objects.get(login_id=request.user.id)
	
	return render(request,'administration/user_add_results.html',{'user_detail':user_detail})
@login_required(login_url='/user_login')
def user_upload_results(request):
	user_detail=user_details.objects.get(login_id=request.user.id)
	if request.method == 'POST':
		user_ref_id=user_details.objects.values_list('id', flat=True).get(login_id=request.user.id)
		cre_res=results(
		user_ref_id=user_ref_id,
		result=request.FILES['result_file'],
		)
		cre_res.save()

	return render(request,'administration/user_add_results.html',{'user_detail':user_detail})
@login_required(login_url='/user_login')
def user_profile(request,id):
	user_detail=user_details.objects.get(pk=id)

	return render(request,'administration/user_profile.html',{'user_detail':user_detail})

@login_required(login_url='/user_login')
def user_view_prescription(request,id):
	user_detail=user_details.objects.get(login_id=request.user.id)
	prescriptions=prescription.objects.get(pk=id)

	return render(request,'administration/user_view_prescription.html',{'prescriptions':prescriptions,'user_detail':user_detail})

@login_required(login_url='/user_login')
def user_view_results(request):
	user_detail=user_details.objects.get(login_id=request.user.id)
	user_ref_id=user_details.objects.values_list('id', flat=True).get(login_id=request.user.id)
	result=results.objects.filter(user_ref_id=user_ref_id)

	return render(request,'administration/user_view_results.html',{'result':result,'user_detail':user_detail})

@login_required(login_url='/user_login')
def user_view_prescribed_doctors(request):
	user_detail=user_details.objects.get(login_id=request.user.id)
	doct_name=[]
	date=[]
	prescribe_id=[]
	user_ref_id=user_details.objects.values_list('id', flat=True).get(login_id=request.user.id)
	prescriptions=prescription.objects.filter(user_ref_id=user_ref_id)
	for x in prescriptions:

		doct_name.append(doctor_details.objects.values_list('username', flat=True).get(pk=x.doctor_ref_id))
		date.append(x.date)
		prescribe_id.append(x.id)
	return render(request,'administration/user_view_prescribed_doctors.html',{'zippy':zip(doct_name,date,prescribe_id),'user_detail':user_detail})

@login_required(login_url='/user_login')
def delete__prescribed_doctors(request,id):
	pre_delete=prescription.objects.get(pk=id)
	pre_delete.delete()

	return HttpResponseRedirect('/user_view_prescribed_doctors')
@login_required(login_url='/user_login')
def delete_bookings(request,id):
	# user_ref_id=user_details.objects.values_list('id', flat=True).get(login_id=request.user.id)
	book_delete=appointment.objects.get(pk=id)
	book_delete.delete()

	return HttpResponseRedirect('/user_view_bookings')

@login_required(login_url='/user_login')
def doctor_search(request):
	details=doctor_details.objects.all()
	search=request.POST.get('search')

    # Q(specialization__icontains=search) | Q(username__icontains=search) | Q(place__icontains=search)
	doct_details=doctor_details.objects.filter(Q(specialization__icontains=search) | Q(username__icontains=search) | Q(place__icontains=search))
	
	# return HttpResponse(search)
	return render(request,'administration/user_view_search_docs.html',{'details':doct_details})

@login_required(login_url='/user_login')
def doc_profile(request,id):
	# user_ref_id=user_details.objects.values_list('id', flat=True).get(login_id=request.user.id)
	doc=doctor_details.objects.get(pk=id)
	rate=rating.objects.filter(doc_id=id)
	print(id)
	
	return render(request,'administration/doc_profile.html',{'details':doc,'rate':rate})
def user_profile(request,id):
	user_detail=user_details.objects.get(pk=id)

	return render(request,'administration/user_profile.html',{'user_detail':user_detail})

@login_required(login_url='/user_login')
def doc_approval(request,id):
	doc_update=doctor_details.objects.get(id=id)
	doc_update.approval='yes'
	doc_update.save()
	return HttpResponseRedirect('/view_doctors')
@login_required(login_url='/user_login')
def doc_disapproval(request,id):
	doc_update=doctor_details.objects.get(id=id)
	doc_update.approval='no'
	doc_update.save()
	return HttpResponseRedirect('/view_doctors')


@login_required(login_url='/user_login')
def payment(request,id):
	return render(request,'administration/user_make_payment.html',{'consol_fee':id})

def user_payment(request):
	if request.method == 'POST':
		request.POST['consul_fee']
		# return HttpResponse(request.POST['cardno'])
		pay=payments(
		Amount=request.POST['consul_fee'],
		cardno=request.POST['cardno'],
		)
		pay.save()
	
	return HttpResponseRedirect('/user_view_bookings')
@login_required(login_url='/user_login')
def doc_del_book(request,id):
	book_delete=appointment.objects.get(pk=id)
	book_delete.delete()
	return HttpResponseRedirect('/doctor_view_bookings')
@login_required(login_url='/user_login')
def edit_doc(request,id):
	edit_doc=doctor_details.objects.get(login_id=id)
	sp=specilizatin.objects.all()
	if request.method == 'POST':
		user_update=doctor_details.objects.get(login_id=id)
		user_update.username=request.POST['username']
		user_update.regno=request.POST['regno']
		user_update.phone=request.POST['phone']
		user_update.place=request.POST['place']
		user_update.specilization=request.POST['specialisation']
		user_update.email=request.POST['email']
		user_update.photo=request.FILES['photo']
		user_update.save()
		
		use_up=User.objects.get(pk=id)
		use_up.username=request.POST['username']
		use_up.save()
		return HttpResponseRedirect('/doctor_settings')
	
	return render(request,'administration/edit_doctor.html',{'edit_doc':edit_doc,'sp':sp})

def edit_user(request,id):
	details=user_details.objects.get(login_id=id)
	if request.method == 'POST':
		user_update=user_details.objects.get(login_id=id)
		user_update.username=request.POST['username']
		user_update.address=request.POST['address']
		user_update.phone=request.POST['phone']
		user_update.age=request.POST['age']
		user_update.gender=request.POST['gender']
		user_update.email=request.POST['email']
		user_update.bloodgroup=request.POST['bloodgroup']
		user_update.save()

		use_up=User.objects.get(pk=id)
		use_up.username=request.POST['username']
		use_up.save()
		return HttpResponseRedirect('/user_profiles')
	return render(request,'administration/edit_user.html',{'details':details})

def rate(request,id):
	# return HttpResponse("jjj")
	if request.method == 'POST':
		
		
		cre_rating=rating(
		doc_id=id,
		rating=request.POST.get('rate'),
		review=request.POST.get('review'),
		)
		cre_rating.save()
	return render(request,'administration/rate_review.html',{'id':id})

