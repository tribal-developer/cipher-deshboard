from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q


from .models import CipherRecord
from .forms import CipherRecordForm
from .models import UserVerification
from .forms import UserVerificationForm
from .forms import EditCipherRecordForm


@login_required
def admin_dashboard(request):

    if not request.user.is_superuser:
        return redirect('user_dashboard')

    records = CipherRecord.objects.all().order_by(
        '-uploaded_date'
    )

    search = request.GET.get(
        'search',
        ''
    )

    if search:
        records = records.filter(
            Q(name__icontains=search) |
            Q(agent_name__icontains=search) |
            Q(ip_address__icontains=search) |
            Q(section__icontains=search)
        )

    context = {
        'records': records,
        'authorise_access':
            UserVerification.objects.all(),
        'record_form':
            CipherRecordForm(),
        'user_form':
            UserVerificationForm(),
        'search': search,
    }

    return render(
        request,
        'dashboard/admin_dashboard.html',
        context
    )
    


@login_required
def user_dashboard(request):
    records = CipherRecord.objects.filter(created_by__is_superuser=True).order_by('-uploaded_date')
    
     # for search filters
    
    search = request.GET.get('search', '')
        
    if search:
        records = records.filter(
            Q(name__icontains=search) |
            Q(agent_name__icontains=search) |
            Q(ip_address__icontains=search) |
            Q(section__icontains=search)
        )
    
    
    return render(request, 'dashboard/user_dashboard.html',{'records': records, 'search': search })

@login_required
def add_record(request):
    if not request.user.is_superuser:
        return redirect('user_dashboard')

    if request.method == 'POST':
        form = CipherRecordForm( request.POST,request.FILES)

        if form.is_valid():
            txt_file = request.FILES['key_file']
            cipher_key = txt_file.read().decode('utf-8').strip()
            if CipherRecord.objects.filter(cipher_key=cipher_key).exists():
               form.add_error(None,'The Hash Key already exists.' )
               return render( request, 'dashboard/admin_dashboard.html', {
                        'records': CipherRecord.objects.all(), 'form': form, 'show_modal': True})                        
            record = form.save( commit=False )
            record.cipher_key = cipher_key
            record.created_by = request.user
            record.save()
            messages.success(request,'Record added successfully.')            
            return redirect('admin_dashboard')
        
    return render( request, 'dashboard/admin_dashboard.html', {
        'records': CipherRecord.objects.all(),'form': form,'show_modal': True})

#  save authorise user in db

@login_required
def authorise_user(request):
    if not request.user.is_superuser:
        return redirect('user_dashboard')
    
    if request.method == 'POST':
        form = UserVerificationForm(request.POST)

        if form.is_valid():
            authorise_access = form.save(commit=False)
            authorise_access.created_by = (request.user)
            authorise_access.save()
            messages.success(request, 'User added successfully.')
            return redirect('admin_dashboard')

        return render(request,'dashboard/admin_dashboard.html',
            {                
                'records':
                    CipherRecord.objects.all(),

                'authorise_access':
                    UserVerification.objects.all(),

                'user_form': form,

                'record_form':
                    CipherRecordForm(),

                'show_user_modal': True,
            }
        )
    return redirect('admin_dashboard')


# show authorise user in frontend

@login_required
def authorised_users(request):

    if not request.user.is_superuser:
        return redirect('user_dashboard')

    users = UserVerification.objects.all().order_by('-id')

    search = request.GET.get('search', '')

    if search:
        users = users.filter(
            Q(user_id__icontains=search) |
            Q(section__icontains=search) |
            Q(designation__icontains=search)
        )

    return render(request, 'dashboard/list_users.html',
        {'users': users, 'search': search})




@login_required
def edit_record(request, pk):

    if not request.user.is_superuser:
        return redirect('user_dashboard')

    record = get_object_or_404(
        CipherRecord,
        pk=pk
    )

    if request.method == 'POST':

        form = EditCipherRecordForm(
            request.POST,
            instance=record
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Record updated successfully.'
            )

            return redirect(
                'admin_dashboard'
            )

    else:

        form = EditCipherRecordForm(
            instance=record
        )

    return render(
        request,
        'dashboard/edit_record.html',
        {
            'form': form,
            'record': record
        }
    )


@login_required
def delete_record(request, pk):

    if not request.user.is_superuser:
        return redirect('user_dashboard')

    record = get_object_or_404(
        CipherRecord,
        pk=pk
    )

    record.delete()

    messages.success(
        request,
        'Deleted successfully.'
    )

    return redirect(
        'admin_dashboard'
    )


def help_page(request):
    return render(request, 'dashboard/help.html')

def auth_users(request):
    return render(request, 'dashboard/list_users.html')