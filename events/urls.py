from django.urls import path
from events.views import EventSummaryAPIView, EventsApiView, BookTicketAPIView

urlpatterns = [
    path('events/', EventsApiView.as_view(), name='event-list-create'),
    path('events/<int:pk>/', EventsApiView.as_view(), name='event_operations'),
    path('events/summary/', EventSummaryAPIView.as_view(), name='event-summary-api'),
    path('events/book-ticket/', BookTicketAPIView.as_view(), name='book-ticket'),
]