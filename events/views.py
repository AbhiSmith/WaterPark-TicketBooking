from pyexpat.errors import messages
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Event
from .forms import EventForm
from django.http import HttpResponse # for text file genaration
import csv
from django.http import FileResponse
import io 
from reportlab.pdfgen import canvas # for conver PDF Generation
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter




# Generate a PDF File
#  pip install reportlab
# check instal or not pip freeze

def event_pdf(request):
    # Create Bytestream Buffer
    buf = io.BytesIO()
    # Create A canvas
    c= canvas.Canvas(buf, pagesize=letter, bottomup=0)
    #Create a text object
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)

    # Add some line of text
    # lines = [
    #     "This is Line 1",
    #     "This is line 2",
    #     "This is line 3",
    # ]
    # Designate the model
    events = Event.objects.all()

    #Create blank list
    lines = []
    
    for event in events:
        lines.append(event.name)
        #lines.append(event.event_date)
        #lines.append(event.created_date)
        #lines.append(event.venue)
        lines.append(event.token_id)
        lines.append(event.mobile_no)
        lines.append(event.email_address)
        lines.append(" ")

    # LOOP
    # For line in lines:
    #     textob.textLine(line)
    for line in lines:
        textob.textLine(line)

    # Finish Up
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)
    # Return something 

    return FileResponse(buf, as_attachment=True, filename='event.pdf')



# Generate CSV file

def event_csv(request):
    response = HttpResponse( content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=booking.csv'

    #Create a csv writer
    writer = csv.writer(response)

    # Designate the model
    events = Event.objects.all()

    # Add column Heading to the CSV File
    writer.writerow(['Name', 'Booking Date', 'Date', 'Ticketno', 'Token ID', 'Mobile No', 'Email'])
   
    # Loop Thu and output
    for event in events:
        writer.writerow([event.name, event.event_date, event.created_date, event.venue, event.token_id, event.mobile_no, event.email_address])

    return response


#Generate Text File event list

def event_text(request):
    response = HttpResponse( content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename=booking.txt'

    # Designate the model
    events = Event.objects.all()

    # Create blank  list
    lines  = []
    # Loop Thu and output
    for event in events:
        lines.append(f'{event}\n{event.name }\n{event.event_date}\n{event.created_date}\n{event.venue}\n{event.token_id}\n{event.mobile_no}\n{event.email_address}')

    # lines = ["This is line 1\n",
    #          "This is line 2\n",
    #          "This is line 3\n"]
    
    # Write To Text File
    response.writelines(lines)
    return response

def search_event(request):
    if request.method == "POST":
        searched = request.POST['searched']
        event_s = Event.objects.filter(mobile_no__contains=searched)
        return render(request, 'events/search_event.html', {'searched':searched, 'event_s':event_s} )
    else:
        return render(request, 'events/search_event.html', {'event':event} )



def add_event(request):
    submitted = False
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_event?submitted=True')
    else:
        form = EventForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'events/add_event.html', {'form': form, 'submitted': submitted} )



def all_events(request):
    event_list = Event.objects.all().order_by('name')# order by 
    return render(request, 'events/event_list.html', {'event_list': event_list} )
    

def home(request):
    return render(request, 'events/home.html', {})


# deleting booking

def delete_event(request, pk):
     delete_it = Event.objects.get(id=pk)
     delete_it.delete()
     #messages.success(request, "You Delete Record...")
     return redirect('list-events')        

     
def update_event(request, pk):
    current_event = Event.objects.get(id=pk)
    form = EventForm(request.POST or None, instance=current_event)
    if form.is_valid():
        form.save()
        return redirect('list-events')
    return render(request, 'events/update_event.html', {'form': form})

    

