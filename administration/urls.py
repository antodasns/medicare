from administration import views
from django.conf.urls import url
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
app_name='administration'
urlpatterns = [
	path('user_logout', views.user_logout,name='user_logout'),
	path('', views.index,name='index'),
	path('user_login', views.user_login,name='login'),
	path('admin_management', views.admin_management,name='admin_management'),
	path('add_specilization', views.add_specilization,name='add_specilization'),
	path('registration', views.registration,name='registration'),
	path('user_registration', views.user_registration,name='user_registration'),
	path('user_payment', views.user_payment,name='user_payment'),
	path('doctor_registration', views.doctor_registration,name='doctor_registration'),
	path('add_medical', views.add_medical,name='add_medical'),
	path('add_specilization', views.add_specilization,name='add_specilization'),
	path('view_doctors', views.view_doctors,name='view_doctors'),
	path('view_report', views.view_report,name='view_report'),
	path('view_users', views.view_users,name='view_users'),
	path('view_appointments', views.view_appointments,name='view_appointments'),
	path('view_medicals', views.view_medicals,name='view_medicals'),
	path('view_prescriptions', views.view_prescriptions,name='view_prescriptions'),


	path('doctor_view_bookings', views.doctor_view_bookings,name='doctor_view_bookings'),
	path('doctor_view_patients', views.doctor_view_patients,name='doctor_view_patients'),
	path('doctor_settings', views.doctor_settings,name='doctor_settings'),
	path('user_profile', views.user_profile,name='user_profile'),
	url(r'^doctor_add_prescription/(?P<id>\d+)$', views.doctor_add_prescription,name='doctor_add_prescription'),
	path('doctor_save_prescription', views.doctor_save_prescription,name='doctor_save_prescription'),
	url(r'^doctor_view_prescription/(?P<id>\d+)$', views.doctor_view_prescription,name='doctor_view_prescription'),
	url(r'^doctor_view_result/(?P<id>\d+)$', views.doctor_view_result,name='doctor_view_result'),
	
	path('user_view_bookings', views.user_view_bookings,name='user_view_bookings'),
	url(r'^user_make_booking/(?P<id>\d+)$', views.user_make_booking,name='user_make_booking'),
	path('user_create_appointment', views.user_create_appointment,name='user_create_appointment'),
	path('user_view_doctors', views.user_view_doctors,name='user_view_doctors'),
	url(r'^user_view_prescription/(?P<id>\d+)$', views.user_view_prescription,name='user_view_prescription'),
	path('user_view_prescribed_doctors', views.user_view_prescribed_doctors,name='user_view_prescribed_doctors'),
	path('user_view_results', views.user_view_results,name='user_view_results'),
	path('user_add_results', views.user_add_results,name='user_add_results'),
	path('user_upload_results', views.user_upload_results,name='user_upload_results'),
	url(r'^delete__prescribed_doctors(?P<id>\d+)$', views.delete__prescribed_doctors,name='delete__prescribed_doctors'),
	url(r'^delete_bookings(?P<id>\d+)$', views.delete_bookings,name='delete_bookings'),
	url(r'^delete_doc(?P<id>\d+)$', views.delete_doc,name='delete_doc'),

	url(r'^doc_del_book(?P<id>\d+)$', views.doc_del_book,name='doc_del_book'),
	url(r'^delete_user(?P<id>\d+)$', views.delete_user,name='delete_user'),

	path('doctor_search', views.doctor_search,name='doctor_search'),
	url(r'^doc_profile(?P<id>\d+)$', views.doc_profile,name='doc_profile'),
	path('user_profiles', views.user_profiles,name='user_profiles'),
	url(r'^doc_approval(?P<id>\d+)$', views.doc_approval,name='doc_approval'),
	url(r'^doc_disapproval(?P<id>\d+)$', views.doc_disapproval,name='doc_disapproval'),
	path('doc_outside_registration', views.doc_outside_registration,name='doc_outside_registration'),
	url(r'^rate(?P<id>\d+)$', views.rate,name='rate'),
	url(r'^payment(?P<id>\d+)$', views.payment,name='payment'),
	url(r'^edit_user(?P<id>\d+)$', views.edit_user,name='edit_user'),
	url(r'^edit_doc(?P<id>\d+)$', views.edit_doc,name='edit_doc'),
		
]+ static(settings.MEDIA_URL, 
                              document_root=settings.MEDIA_ROOT) 