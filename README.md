# TrixTer - A Twitter-like Django App

TrixTer is a simple Twitter-style web application built with Django, allowing users to create posts (called "Trix") with text and optional images, view them in a list, edit or delete them. The app demonstrates core Django functionalities like models, views, forms, and templates.

## Features
- **User Authentication**: Create, edit, and delete Trix posts as an authenticated user.
- **Post Creation**: Users can create posts (Trix) with a text description and an optional image.
- **Edit & Delete**: Users can edit or delete their posts.
- **Admin Panel**: Manage posts through Django’s admin interface.


## Project Structure

```bash
TrixTer/
│
├── trixter/                 # Project folder
│   ├── settings.py          # Project settings
│   ├── urls.py              # URL configuration
│   └── ...
│
├── trix/                    # Main app folder
│   ├── models.py            # Data models for Trix
│   ├── forms.py             # Forms for creating/editing Trix
│   ├── views.py             # Logic for rendering templates and handling requests
│   ├── urls.py              # URL routing for the app
│   ├── templates/           # HTML templates (Bootstrap included)
│   │   ├── layout.html      # Base layout using Bootstrap
│   │   ├── trix_list.html   # Display all Trix
│   │   └── trix_form.html   # Form for creating and editing Trix
│   └── static/              # Static files (CSS, JS, images)
│
├── media/                   # Uploaded images
└── requirements.txt         # Dependencies
```

### Main Files
- **`manage.py`**: Standard Django file for running management commands.
- **`trixter/settings.py`**: Contains project settings such as the installed apps, middleware, database configuration, and static files configuration.
- **`trixter/urls.py`**: The main URL configuration for the app, routes to the `trix` app for handling posts.

### Trix App
- **`models.py`**: Defines the `Trix` model, which includes a `text` field for the post content, a `photo` field for an optional image, and a timestamp for creation and updates.
    ```python
    class Trix(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        text = models.TextField(max_length=250)
        photo = models.ImageField(upload_to='photos/', blank=True, null=True)
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)
    ```

- **`views.py`**: Contains the logic for listing, creating, editing, and deleting posts.
    - **`trix_list`**: Fetches and displays all posts.
    - **`trix_create`**: Handles creating new posts.
    - **`trix_edit`**: Handles editing an existing post.
    - **`trix_delete`**: Deletes a post.

    Example of the `trix_create` view:
    ```python
    def trix_create(request):
        if request.method == 'POST':
            form = TrixForm(request.POST, request.FILES)
            if form.is_valid():
                trix = form.save(commit=False)
                trix.user = request.user
                trix.save()
                return redirect('trix_list')
        else:
            form = TrixForm()
        return render(request, 'trix_form.html', {'form': form})
    ```

- **`forms.py`**: Defines the `TrixForm`, which is a form for creating and editing `Trix` posts.
    ```python
    class TrixForm(forms.ModelForm):
        class Meta:
            model = Trix
            fields = ['text', 'photo']
    ```

- **`urls.py`**: Defines the URLs for the app.
    ```python
    urlpatterns = [
        path('', views.trix_list, name='trix_list'),
        path('create/', views.trix_create, name='trix_create'),
        path('<int:trix_id>/edit/', views.trix_edit, name='trix_edit'),
        path('<int:trix_id>/del/', views.trix_delete, name='trix_delete'),
    ]
    ```

- **Templates**:
    - **`trix_list.html`**: Displays a list of posts with options to edit or delete.
    - **`trix_form.html`**: A form for creating and editing posts.
    - **`layout.html`**: A base layout with a navbar, extended by other templates.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/trixter.git
    cd trixter
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up the database:
    ```bash
    python manage.py migrate
    ```

5. Create a superuser to access the Django admin:
    ```bash
    python manage.py createsuperuser
    ```

6. Run the development server:
    ```bash
    python manage.py runserver
    ```

7. Access the app at `http://127.0.0.1:8000/` and the admin panel at `http://127.0.0.1:8000/admin`.

## Requirements

All dependencies are listed in `requirements.txt`. Install them using `pip`:
```
Django==5.1
```

## License

This project is licensed under trixsearch private applications , will release the whole license soon

Here's the updated README incorporating Bootstrap usage:


## Running the App

- To create a post, navigate to `http://127.0.0.1:8000/trix/create`.
- To view all posts, visit `http://127.0.0.1:8000/trix`.
- Admin interface: `http://127.0.0.1:8000/admin`.

---

