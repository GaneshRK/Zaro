from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.http import JsonResponse, HttpResponseForbidden
from .models import Course, Order
import razorpay
from django.views.decorators.csrf import csrf_exempt

# client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
# client.order.create({"amount": 100, "currency": "INR", "payment_capture": "1"})

def course_detail(request, slug):
    course = get_object_or_404(Course, slug=slug)
    return render(request, 'courses/course_detail.html', {'course': course})

@login_required
def create_order(request, slug):
    course = get_object_or_404(Course, slug=slug)
    client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
    amount_paise = int(course.price * 100)
    data = { 'amount': amount_paise, 'currency': 'INR', 'payment_capture': '1' }
    order = client.order.create(data=data)
    # Save an order record with razorpay_order_id (not yet paid)
    order_obj = Order.objects.create(user=request.user, course=course, razorpay_order_id=order['id'], amount=course.price)
    context = {'course': course, 'order': order, 'razorpay_key': settings.RAZORPAY_KEY_ID}
    return render(request, 'courses/checkout.html', context)

@csrf_exempt
def payment_success(request):
    if request.method == 'POST':
        payload = request.POST
        payment_id = payload.get('razorpay_payment_id')
        order_id = payload.get('razorpay_order_id')
        # find Order
        try:
            order = Order.objects.get(razorpay_order_id=order_id)
            order.razorpay_payment_id = payment_id
            order.paid = True
            order.save()
            return JsonResponse({'status':'ok'})
        except Order.DoesNotExist:
            return JsonResponse({'status':'error','message':'order not found'}, status=404)
    return HttpResponseForbidden()

@login_required
def course_content(request, slug):
    course = get_object_or_404(Course, slug=slug)
    # check if user purchased
    has = Order.objects.filter(user=request.user, course=course, paid=True).exists()
    if not has:
        return HttpResponseForbidden('You do not own this course.')
    return render(request, 'courses/course_content.html', {'course': course})
