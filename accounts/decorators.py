from django.shortcuts import redirect
from django.contrib import messages


def admin_required(view_func):

    def wrapper(request, *args, **kwargs):

        if not request.user.is_superuser:

            messages.warning(
                request,
                "Admin login required to access this feature."
            )

            return redirect('dashboard')

        return view_func(
            request,
            *args,
            **kwargs
        )

    return wrapper