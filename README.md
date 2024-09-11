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

README in Hindi:

---

# TrixTer - एक ट्विटर जैसा Django ऐप

TrixTer एक सरल ट्विटर-शैली का वेब एप्लिकेशन है जिसे Django के साथ बनाया गया है, जो उपयोगकर्ताओं को टेक्स्ट और वैकल्पिक चित्रों के साथ पोस्ट (जिसे "Trix" कहा जाता है) बनाने, उन्हें सूची में देखने, संपादित करने या हटाने की अनुमति देता है। यह एप्लिकेशन Django की मुख्य कार्यक्षमताओं जैसे मॉडल्स, व्यूज़, फॉर्म्स, और टेम्पलेट्स का प्रदर्शन करता है।

## विशेषताएँ
- **उपयोगकर्ता प्रमाणीकरण**: प्रमाणित उपयोगकर्ता के रूप में Trix पोस्ट बनाएं, संपादित करें और हटाएं।
- **पोस्ट निर्माण**: उपयोगकर्ता टेक्स्ट विवरण और वैकल्पिक चित्र के साथ पोस्ट (Trix) बना सकते हैं।
- **संपादन और हटाना**: उपयोगकर्ता अपनी पोस्ट को संपादित या हटाने की क्षमता रखते हैं।
- **एडमिन पैनल**: Django के एडमिन इंटरफेस के माध्यम से पोस्ट का प्रबंधन करें।

## परियोजना संरचना

```bash
TrixTer/
│
├── trixter/                 # प्रोजेक्ट फ़ोल्डर
│   ├── settings.py          # प्रोजेक्ट सेटिंग्स
│   ├── urls.py              # URL कॉन्फ़िगरेशन
│   └── ...
│
├── trix/                    # मुख्य ऐप फ़ोल्डर
│   ├── models.py            # Trix के लिए डेटा मॉडल्स
│   ├── forms.py             # Trix बनाने/संपादित करने के लिए फॉर्म्स
│   ├── views.py             # टेम्पलेट्स को प्रस्तुत करने और अनुरोधों को संभालने का लॉजिक
│   ├── urls.py              # ऐप के लिए URL रूटिंग
│   ├── templates/           # HTML टेम्पलेट्स (Bootstrap शामिल)
│   │   ├── layout.html      # Bootstrap के साथ बेस लेआउट
│   │   ├── trix_list.html   # सभी Trix दिखाएँ
│   │   └── trix_form.html   # Trix बनाने और संपादित करने के लिए फॉर्म
│   └── static/              # स्थिर फ़ाइलें (CSS, JS, छवियाँ)
│
├── media/                   # अपलोड की गई छवियाँ
└── requirements.txt         # निर्भरताएँ
```

### मुख्य फाइलें
- **`manage.py`**: प्रबंधन आदेश चलाने के लिए मानक Django फाइल।
- **`trixter/settings.py`**: परियोजना सेटिंग्स जिसमें इंस्टॉल किए गए ऐप्स, मिडलवेयर, डेटाबेस कॉन्फ़िगरेशन और स्थिर फ़ाइलों की कॉन्फ़िगरेशन शामिल हैं।
- **`trixter/urls.py`**: ऐप के लिए मुख्य URL कॉन्फ़िगरेशन, पोस्टों को संभालने के लिए `trix` ऐप के रूट्स।

### Trix ऐप
- **`models.py`**: `Trix` मॉडल को परिभाषित करता है, जिसमें पोस्ट सामग्री के लिए `text` फ़ील्ड, वैकल्पिक चित्र के लिए `photo` फ़ील्ड और निर्माण और अद्यतन के लिए टाइमस्टैम्प शामिल हैं।
    ```python
    class Trix(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        text = models.TextField(max_length=250)
        photo = models.ImageField(upload_to='photos/', blank=True, null=True)
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)
    ```

- **`views.py`**: पोस्टों को सूचीबद्ध, बनाने, संपादित करने, और हटाने का लॉजिक शामिल करता है।
    - **`trix_list`**: सभी पोस्टों को प्राप्त करता है और प्रदर्शित करता है।
    - **`trix_create`**: नई पोस्ट बनाने को संभालता है।
    - **`trix_edit`**: मौजूदा पोस्ट को संपादित करने को संभालता है।
    - **`trix_delete`**: पोस्ट को हटाता है।

    उदाहरण `trix_create` व्यू का:
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

- **`forms.py`**: `TrixForm` को परिभाषित करता है, जो Trix पोस्टों को बनाने और संपादित करने के लिए एक फॉर्म है।
    ```python
    class TrixForm(forms.ModelForm):
        class Meta:
            model = Trix
            fields = ['text', 'photo']
    ```

- **`urls.py`**: ऐप के लिए URLs को परिभाषित करता है।
    ```python
    urlpatterns = [
        path('', views.trix_list, name='trix_list'),
        path('create/', views.trix_create, name='trix_create'),
        path('<int:trix_id>/edit/', views.trix_edit, name='trix_edit'),
        path('<int:trix_id>/del/', views.trix_delete, name='trix_delete'),
    ]
    ```

- **टेम्पलेट्स**:
    - **`trix_list.html`**: पोस्टों की सूची प्रदर्शित करता है, संपादन या हटाने के विकल्प के साथ।
    - **`trix_form.html`**: पोस्टों को बनाने और संपादित करने के लिए एक फॉर्म।
    - **`layout.html`**: एक नेवबार के साथ बेस लेआउट, अन्य टेम्पलेट्स द्वारा विस्तारित।

## इंस्टॉलेशन

1. रिपॉजिटरी को क्लोन करें:
    ```bash
    git clone https://github.com/your-username/trixter.git
    cd trixter
    ```

2. एक वर्चुअल वातावरण बनाएं और इसे सक्रिय करें:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Windows पर `venv\Scripts\activate` का उपयोग करें
    ```

3. निर्भरताओं को इंस्टॉल करें:
    ```bash
    pip install -r requirements.txt
    ```

4. डेटाबेस सेट करें:
    ```bash
    python manage.py migrate
    ```

5. Django एडमिन को एक्सेस करने के लिए एक सुपरयूजर बनाएं:
    ```bash
    python manage.py createsuperuser
    ```

6. विकास सर्वर को चलाएं:
    ```bash
    python manage.py runserver
    ```

7. ऐप को `http://127.0.0.1:8000/` पर और एडमिन पैनल को `http://127.0.0.1:8000/admin` पर एक्सेस करें।

## आवश्यकताएँ

सभी निर्भरताएँ `requirements.txt` में सूचीबद्ध हैं। उन्हें `pip` का उपयोग करके इंस्टॉल करें:
```
Django==5.1
```

## लाइसेंस

यह परियोजना trixsearch प्राइवेट एप्लिकेशन के तहत लाइसेंस प्राप्त है, जल्द ही पूरा लाइसेंस जारी किया जाएगा।

## ऐप चलाना

- पोस्ट बनाने के लिए, `http://127.0.0.1:8000/trix/create` पर जाएँ।
- सभी पोस्ट देखने के लिए, `http://127.0.0.1:8000/trix` पर जाएँ।
- एडमिन इंटरफेस: `http://127.0.0.1:8000/admin`।

---

