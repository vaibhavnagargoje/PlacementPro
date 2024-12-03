from django.contrib import admin
from django.contrib.auth.models import User
from datetime import datetime

# Custom filter class for academic batches
class BatchFilter(admin.SimpleListFilter):
    title = 'Batch'  # The title of the filter that will be displayed in the admin sidebar
    parameter_name = 'batch'  # The parameter name used in the URL query string

    def lookups(self, request, model_admin):
        """
        This function defines the available options in the filter dropdown.
        It will calculate the current academic batch and show it as an option.
        """
        current_year = datetime.now().year
        next_year = current_year + 2
        
        # If current month is before April, adjust the batch to the previous academic year
        if datetime.now().month < 4:
            current_year -= 1
            next_year -= 1
        
        current_batch = f"{current_year}-{next_year}"  # Example: "2024-2025"

        # Return the options to filter
        return (
            (current_batch, f"Current Batch ({current_batch})"),
            ('all', 'All Batches'),
        )

    def queryset(self, request, queryset):
        """
        This method filters the queryset based on the batch selected in the dropdown.
        If the 'all' option is selected, return all users.
        Otherwise, filter users based on their admission date falling in the current batch.
        """
        if self.value() == 'all':
            return queryset  # Show all users if 'All Batches' is selected

        if self.value():
            # Calculate the start and end dates for the batch
            start_date = datetime(year=int(self.value().split('-')[0]), month=4, day=1)
            end_date = datetime(year=int(self.value().split('-')[1]), month=3, day=31)

            # Filter users based on their `date_joined` field falling between the batch dates
            return queryset.filter(date_joined__gte=start_date, date_joined__lte=end_date)

        return queryset
