TITLE: Retrieving a Single Django Model Object with get()
DESCRIPTION: Use the `get()` method on a Django Manager to retrieve a single object directly. This method raises `DoesNotExist` if no object matches or `MultipleObjectsReturned` if more than one object matches the query.
SOURCE: https://github.com/django/django/blob/main/docs/topics/db/queries.txt#_snippet_13

LANGUAGE: pycon
CODE:
```
>>> one_entry = Entry.objects.get(pk=1)
```

----------------------------------------

TITLE: Customize Display of Field-Specific Errors
DESCRIPTION: Shows how to iterate over individual errors for a specific form field (`form.subject.errors`) to customize their display, for example, rendering them as an ordered list.
SOURCE: https://github.com/django/django/blob/main/docs/topics/forms/index.txt#_snippet_12

LANGUAGE: html+django
CODE:
```
{% if form.subject.errors %}
    <ol>
    {% for error in form.subject.errors %}
        <li><strong>{{ error|escape }}</strong></li>
    {% endfor %}
    </ol>
{% endif %}
```

----------------------------------------

TITLE: Convert Python Objects to Query Values with `get_prep_value`
DESCRIPTION: Illustrates how to implement the `get_prep_value` method in a custom Django field. This method is responsible for converting a Python object (e.g., a `Hand` instance) back into a format suitable for database queries, such as a string representation.
SOURCE: https://github.com/django/django/blob/main/docs/howto/custom-model-fields.txt#_snippet_17

LANGUAGE: Python
CODE:
```
class HandField(models.Field):
    # ...

    def get_prep_value(self, value):
        return "".join(
            ["".join(l) for l in (value.north, value.east, value.south, value.west)]
        )
```

----------------------------------------

TITLE: Django FileField.upload_to Attribute
DESCRIPTION: This attribute provides a way of setting the upload directory and file name. It can be a string, a `pathlib.Path` object, or a callable function. String values can contain `time.strftime` formatting.
SOURCE: https://github.com/django/django/blob/main/docs/ref/models/fields.txt#_snippet_46

LANGUAGE: APIDOC
CODE:
```
FileField.upload_to
```

----------------------------------------

TITLE: Django Field.blank vs. Field.null Attributes
DESCRIPTION: Explains the difference between `blank` (validation-related) and `null` (database-related) attributes for Django model fields. `blank=True` allows empty values in forms, while `null=True` allows `NULL` in the database.
SOURCE: https://github.com/django/django/blob/main/docs/topics/db/models.txt#_snippet_5

LANGUAGE: APIDOC
CODE:
```
Field.blank:
  Description: If True, the field is allowed to be blank. Default is False.
  Note: Different than Field.null.
  Relationship to validation: blank is validation-related.
  Effect: If blank=True, form validation allows empty value. If blank=False, field is required.

Field.null:
  Description: Purely database-related.
```

----------------------------------------

TITLE: Instantiate and Iterate a Django Formset (Default Extra)
DESCRIPTION: This snippet shows how to instantiate the `ArticleFormSet` and iterate over its forms. By default, `formset_factory` creates one extra empty form, which is then printed to the console as HTML, demonstrating the structure of a single form within the formset.
SOURCE: https://github.com/django/django/blob/main/docs/topics/forms/formsets.txt#_snippet_2

LANGUAGE: Python
CODE:
```
>>> formset = ArticleFormSet()
>>> for form in formset:
...     print(form)
...
<div><label for="id_form-0-title">Title:</label><input type="text" name="form-0-title" id="id_form-0-title"></div>
<div><label for="id_form-0-pub_date">Pub date:</label><input type="text" name="form-0-pub_date" id="id_form-0-pub_date"></div>
```

----------------------------------------

TITLE: Mix Q objects and keyword arguments in Django QuerySet (valid order)
DESCRIPTION: Demonstrates the correct order for mixing Q objects and keyword arguments in a Django QuerySet method: Q objects must precede keyword arguments.
SOURCE: https://github.com/django/django/blob/main/docs/topics/db/queries.txt#_snippet_71

LANGUAGE: python
CODE:
```
Poll.objects.get(
    Q(pub_date=date(2005, 5, 2)) | Q(pub_date=date(2005, 5, 6)),
    question__startswith="Who",
)
```

----------------------------------------

TITLE: Save ModelFormset Instances Without Committing to Database in Django
DESCRIPTION: Explains how to save ModelFormset instances without immediately committing them to the database by passing `commit=False` to the `save()` method. This allows for pre-save operations on the instances before they are persisted. For ManyToMany fields, `formset.save_m2m()` must be called separately.
SOURCE: https://github.com/django/django/blob/main/docs/topics/forms/modelforms.txt#_snippet_38

LANGUAGE: pycon
CODE:
```
# don't save to the database
>>> instances = formset.save(commit=False)
>>> for instance in instances:
...     # do something with instance
...     instance.save()
...
```

----------------------------------------

TITLE: Create a Formset Class from a Django Form
DESCRIPTION: This snippet demonstrates how to create a formset class, `ArticleFormSet`, from an existing `ArticleForm` using the `formset_factory` function. The resulting class can then be instantiated to manage multiple instances of the `ArticleForm`.
SOURCE: https://github.com/django/django/blob/main/docs/topics/forms/formsets.txt#_snippet_1

LANGUAGE: Python
CODE:
```
>>> from django.forms import formset_factory
>>> ArticleFormSet = formset_factory(ArticleForm)
```

----------------------------------------

TITLE: Django QuerySet Partial Evaluation and Caching Behavior
DESCRIPTION: Explains that QuerySets do not cache results when only a part of the queryset is evaluated, such as when using array slicing or indexing. Repeated access to an index will query the database each time if the full queryset hasn't been evaluated.
SOURCE: https://github.com/django/django/blob/main/docs/topics/db/queries.txt#_snippet_47

LANGUAGE: pycon
CODE:
```
>>> queryset = Entry.objects.all()
>>> print(queryset[5])  # Queries the database
>>> print(queryset[5])  # Queries the database again
```

----------------------------------------

TITLE: APIDOC: ModelAdmin.list_filter Attribute
DESCRIPTION: Documentation for the `ModelAdmin.list_filter` attribute, used to activate filters in the right sidebar of the admin change list page. It explains the basic usage of providing a list or tuple of field names.
SOURCE: https://github.com/django/django/blob/main/docs/ref/contrib/admin/index.txt#_snippet_45

LANGUAGE: APIDOC
CODE:
```
ModelAdmin.list_filter
  Description: Set `list_filter` to activate filters in the right sidebar of the change list page of the admin.
  Basic Usage: Takes a list or tuple of field names to activate filtering upon. More advanced options are available.
```

----------------------------------------

TITLE: Configure Django STATICFILES_DIRS with absolute paths
DESCRIPTION: This setting defines additional locations where the staticfiles app will search for static files, beyond those in app subdirectories. It should be a list of strings, each representing a full path to a static files directory. Paths should use Unix-style forward slashes.
SOURCE: https://github.com/django/django/blob/main/docs/ref/settings.txt#_snippet_204

LANGUAGE: Python
CODE:
```
STATICFILES_DIRS = [
    "/home/special.polls.com/polls/static",
    "/home/polls.com/polls/static",
    "/opt/webfiles/common",
]
```

----------------------------------------

TITLE: Include Django Authentication URLs in Project URLconf
DESCRIPTION: Shows the simplest method to integrate Django's built-in authentication views by including the `django.contrib.auth.urls` URLconf directly into a project's main `urlpatterns`. This provides a set of predefined URLs for common authentication tasks.
SOURCE: https://github.com/django/django/blob/main/docs/topics/auth/default.txt#_snippet_39

LANGUAGE: Python
CODE:
```
urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
]
```

----------------------------------------

TITLE: Optimize Django QuerySet Evaluation and Caching
DESCRIPTION: This snippet demonstrates an optimal approach to handling Django QuerySets, showcasing how lazy evaluation and result caching can significantly reduce database queries. It illustrates efficient checks for membership, existence, and length, ensuring the QuerySet is evaluated only once when needed, avoiding redundant database calls.
SOURCE: https://github.com/django/django/blob/main/docs/topics/db/optimization.txt#_snippet_12

LANGUAGE: Python
CODE:
```
members = group.members.all()

if display_group_members:
    if members:
        if current_user in members:
            print("You and", len(members) - 1, "other users are members of this group.")
        else:
            print("There are", len(members), "members in this group.")

        for member in members:
            print(member.username)
    else:
        print("There are no members in this group.")
```

----------------------------------------

TITLE: Manage Related Objects in Django View using Inline Formset
DESCRIPTION: Provides a complete Django view example (`manage_books`) showing how to integrate an inline formset to allow users to edit related objects of a model. It handles both POST (form submission and saving) and GET (initial form display) requests, passing the model instance to the formset.
SOURCE: https://github.com/django/django/blob/main/docs/topics/forms/modelforms.txt#_snippet_59

LANGUAGE: python
CODE:
```
def manage_books(request, author_id):
    author = Author.objects.get(pk=author_id)
    BookInlineFormSet = inlineformset_factory(Author, Book, fields=["title"])
    if request.method == "POST":
        formset = BookInlineFormSet(request.POST, request.FILES, instance=author)
        if formset.is_valid():
            formset.save()
            # Do something. Should generally end with a redirect. For example:
            return HttpResponseRedirect(author.get_absolute_url())
    else:
        formset = BookInlineFormSet(instance=author)
    return render(request, "manage_books.html", {"formset": formset})
```

----------------------------------------

TITLE: Test setup for checking email content
DESCRIPTION: Illustrates the initial setup for a test method designed to check the content of an email, including defining subject, sender, and recipient.
SOURCE: https://github.com/django/django/blob/main/docs/topics/email.txt#_snippet_18

LANGUAGE: Python
CODE:
```
def test_contains_email_content(self):
    subject = "Hello World"
    from_email = "from@example.com"
    to = "to@example.com"
```

----------------------------------------

TITLE: Incrementing Field Value with F Expression in Django ORM Update
DESCRIPTION: Illustrates how to use Django's F() expressions within an `update()` call to increment a field's value based on its current state. This is particularly useful for atomic operations like incrementing counters directly in the database.
SOURCE: https://github.com/django/django/blob/main/docs/topics/db/queries.txt#_snippet_89

LANGUAGE: Python
CODE:
```
>>> Entry.objects.update(number_of_pingbacks=F("number_of_pingbacks") + 1)
```

----------------------------------------

TITLE: Forward ForeignKey Access Caching in Django ORM
DESCRIPTION: Explains how Django caches the related object when accessed via a ForeignKey for the first time. Subsequent accesses to the foreign key on the same object instance will use the cached version, avoiding additional database queries.
SOURCE: https://github.com/django/django/blob/main/docs/topics/db/queries.txt#_snippet_95

LANGUAGE: Python
CODE:
```
>>> e = Entry.objects.get(id=2)
>>> print(e.blog)  # Hits the database to retrieve the associated Blog.
>>> print(e.blog)  # Doesn't hit the database; uses cached version.
```

----------------------------------------

TITLE: SimpleTestCase.assertJSONEqual: Assert JSON Equality
DESCRIPTION: Asserts that two JSON fragments (`raw` and `expected_data`) are equal, ignoring non-significant whitespace. Delegates comparison to the `json` library. Error output can be customized.
SOURCE: https://github.com/django/django/blob/main/docs/topics/testing/tools.txt#_snippet_97

LANGUAGE: APIDOC
CODE:
```
SimpleTestCase.assertJSONEqual(raw, expected_data, msg=None)
  raw: The first JSON fragment (string).
  expected_data: The second JSON fragment (string or Python object).
  msg: (Optional) Custom error message.
```

----------------------------------------

TITLE: Render Widget Media with ManifestStaticFilesStorage
DESCRIPTION: Illustrates the rendering of widget media when `django.contrib.staticfiles` is configured with `ManifestStaticFilesStorage`. This storage backend appends a content hash to static file names for cache busting, as shown in the generated script tag.
SOURCE: https://github.com/django/django/blob/main/docs/topics/forms/media.txt#_snippet_12

LANGUAGE: python
CODE:
```
>>> w = CalendarWidget()
>>> print(w.media)
<link href="/css/pretty.css" media="all" rel="stylesheet">
<script src="https://static.example.com/animations.27e20196a850.js"></script>
<script src="https://othersite.com/actions.js"></script>
```

----------------------------------------

TITLE: Implement Django PublisherDetailView with SingleObjectMixin and ListView
DESCRIPTION: This Python class demonstrates how to create a Django class-based view that combines `SingleObjectMixin` (for retrieving a single object, e.g., a Publisher) with `ListView` (for displaying a list of related objects, e.g., books by that Publisher). It overrides `get()` to set the object, `get_context_data()` to add the publisher to the context, and `get_queryset()` to retrieve the paginated list of books.
SOURCE: https://github.com/django/django/blob/main/docs/topics/class-based-views/mixins.txt#_snippet_11

LANGUAGE: python
CODE:
```
from django.views.generic import ListView
from django.views.generic.detail import SingleObjectMixin
from books.models import Publisher


class PublisherDetailView(SingleObjectMixin, ListView):
    paginate_by = 2
    template_name = "books/publisher_detail.html"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Publisher.objects.all())
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["publisher"] = self.object
        return context

    def get_queryset(self):
        return self.object.book_set.all()
```

----------------------------------------

TITLE: Bootstrap New Django Project
DESCRIPTION: Use the `django-admin` command-line utility to create a new Django project. This command generates a directory structure for a new project named 'mysite' within a parent directory 'djangotutorial'.
SOURCE: https://github.com/django/django/blob/main/docs/intro/tutorial01.txt#_snippet_1

LANGUAGE: Shell
CODE:
```
$ django-admin startproject mysite djangotutorial
```

----------------------------------------

TITLE: Access Django Form Validation Errors
DESCRIPTION: Illustrates how to retrieve validation errors from a Django Form instance using the `errors` attribute. This attribute returns a dictionary mapping field names to lists of error messages, which can be accessed after calling `is_valid()` or accessing `errors` itself.
SOURCE: https://github.com/django/django/blob/main/docs/ref/forms/api.txt#_snippet_11

LANGUAGE: python
CODE:
```
f.errors
# Expected output: {'sender': ['Enter a valid email address.'], 'subject': ['This field is required.']}
```

----------------------------------------

TITLE: Nested OuterRef Usage in Django ORM
DESCRIPTION: This example illustrates a scenario where nested `OuterRef` instances are required. It demonstrates how `OuterRef(OuterRef("pk"))` can be used within a deeply nested `Subquery` to reference a field from a containing queryset that is not the immediate parent.
SOURCE: https://github.com/django/django/blob/main/docs/ref/models/expressions.txt#_snippet_27

LANGUAGE: Python
CODE:
```
Book.objects.filter(author=OuterRef(OuterRef("pk")))
```

----------------------------------------

TITLE: Django DATABASES Setting Reference
DESCRIPTION: API documentation for Django's primary `DATABASES` setting, detailing its default empty dictionary value and its purpose as a nested dictionary for database configurations.
SOURCE: https://github.com/django/django/blob/main/docs/ref/settings.txt#_snippet_31

LANGUAGE: APIDOC
CODE:
```
DATABASES:
  Default: {} (Empty dictionary)
  Description: A dictionary containing the settings for all databases to be used with Django. It is a nested dictionary whose contents map a database alias to a dictionary containing the options for an individual database.
  Requirement: Must configure a "default" database.
```

----------------------------------------

TITLE: Specify Custom Field Class for ModelForm Field in Django (field_classes)
DESCRIPTION: This example shows how to assign a custom form field class to a model field in a Django ModelForm. By using the `field_classes` attribute in the `Meta` class, the 'slug' field will be rendered using `MySlugFormField` instead of its default form field type.
SOURCE: https://github.com/django/django/blob/main/docs/topics/forms/modelforms.txt#_snippet_13

LANGUAGE: python
CODE:
```
from django.forms import ModelForm
from kryptisk.models import Article


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ["pub_date", "headline", "content", "reporter", "slug"]
        field_classes = {
            "slug": MySlugFormField,
        }
```

----------------------------------------

TITLE: Define Django Model with Multiple Foreign Keys to Same Model
DESCRIPTION: Defines a `Friendship` model with two foreign keys (`from_friend`, `to_friend`) pointing to the same `Friend` model. This scenario highlights the need to use `fk_name` when creating formsets to resolve ambiguity.
SOURCE: https://github.com/django/django/blob/main/docs/topics/forms/modelforms.txt#_snippet_57

LANGUAGE: python
CODE:
```
class Friendship(models.Model):
    from_friend = models.ForeignKey(
        Friend,
        on_delete=models.CASCADE,
        related_name="from_friends",
    )
    to_friend = models.ForeignKey(
        Friend,
        on_delete=models.CASCADE,
        related_name="friends",
    )
    length_in_months = models.IntegerField()
```

----------------------------------------

TITLE: Implement resolve_expression for custom query expression
DESCRIPTION: Handles the preprocessing and validation of nested expressions within a custom query expression. It creates a copy of the expression and recursively resolves its sub-expressions, ensuring they are ready for SQL compilation.
SOURCE: https://github.com/django/django/blob/main/docs/ref/models/expressions.txt#_snippet_58

LANGUAGE: python
CODE:
```
def resolve_expression(
    self, query=None, allow_joins=True, reuse=None, summarize=False, for_save=False
):
    c = self.copy()
    c.is_summary = summarize
    for pos, expression in enumerate(self.expressions):
        c.expressions[pos] = expression.resolve_expression(
            query, allow_joins, reuse, summarize, for_save
        )
    return c
```

----------------------------------------

TITLE: Create Database-Agnostic Fields with `db_type` in Django
DESCRIPTION: Achieve database-agnostic custom fields by checking `connection.vendor` within the `db_type` method. This allows the field to return different database column types (e.g., 'datetime' for MySQL, 'timestamp' for PostgreSQL) based on the active database backend, ensuring cross-database compatibility without hardcoding.
SOURCE: https://github.com/django/django/blob/main/docs/howto/custom-model-fields.txt#_snippet_12

LANGUAGE: Python
CODE:
```
class MyDateField(models.Field):
    def db_type(self, connection):
        if connection.vendor == "mysql":
            return "datetime"
        else:
            return "timestamp"
```

----------------------------------------

TITLE: Field.bound_field_class Attribute
DESCRIPTION: Introduced in Django 5.2, the `bound_field_class` attribute allows overriding the `Form.bound_field_class` on a per-field basis. This provides fine-grained control over the `BoundField` instance used for a specific field.
SOURCE: https://github.com/django/django/blob/main/docs/ref/forms/fields.txt#_snippet_26

LANGUAGE: APIDOC
CODE:
```
Field.bound_field_class
```

----------------------------------------

TITLE: Django Field.default API Reference
DESCRIPTION: API documentation for the `default` attribute of Django model fields. This attribute sets the default value for the field, which can be a static value or a callable object. For mutable objects (like lists or dictionaries), a callable must be used to prevent shared references. Lambda functions are not suitable due to migration serialization issues.
SOURCE: https://github.com/django/django/blob/main/docs/ref/models/fields.txt#_snippet_18

LANGUAGE: APIDOC
CODE:
```
Field.default: Any | Callable
  Description: The default value for the field. If callable, it will be called every time a new object is created.
  Constraint: Cannot be a mutable object (model instance, list, set, etc.) directly; wrap the desired default in a callable.
  Constraint: Lambdas cannot be used for field options like default because they can't be serialized by migrations.
  Usage: For ForeignKey fields, defaults should be the value of the field they reference (e.g., 'pk') instead of model instances.
  Behavior: Used when new model instances are created and a value isn't provided, or when a primary key field is set to None.
```

----------------------------------------

TITLE: Limiting Django QuerySet Results with Step Parameter
DESCRIPTION: Using the 'step' parameter in QuerySet slicing forces immediate query execution and returns a list of objects, for example, every second object of the first 10. Further filtering or ordering of such a sliced queryset is prohibited.
SOURCE: https://github.com/django/django/blob/main/docs/topics/db/queries.txt#_snippet_16

LANGUAGE: pycon
CODE:
```
>>> Entry.objects.all()[:10:2]
```

----------------------------------------

TITLE: Registering and Using Custom Django URL Path Converters
DESCRIPTION: Demonstrates how to register a custom path converter, like `FourDigitYearConverter`, using `django.urls.register_converter` and subsequently use it within Django's `urlpatterns` for defining URL patterns.
SOURCE: https://github.com/django/django/blob/main/docs/topics/http/urls.txt#_snippet_5

LANGUAGE: python
CODE:
```
from django.urls import path, register_converter

from . import converters, views

register_converter(converters.FourDigitYearConverter, "yyyy")

urlpatterns = [
    path("articles/2003/", views.special_case_2003),
    path("articles/<yyyy:year>/", views.year_archive),
    ...,
]
```

----------------------------------------

TITLE: Django Form.is_bound Attribute
DESCRIPTION: API documentation for the `is_bound` attribute of a Django Form instance. This boolean attribute indicates whether the form is currently bound to a set of data (`True`) or is unbound (`False`).
SOURCE: https://github.com/django/django/blob/main/docs/ref/forms/api.txt#_snippet_3

LANGUAGE: APIDOC
CODE:
```
Form.is_bound: bool
  Indicates whether a Form instance is bound to data (True) or unbound (False).
```

----------------------------------------

TITLE: Create Django Covering Index with Included Fields
DESCRIPTION: Demonstrates how to create a Django covering index using the `include` attribute. This allows for index-only scans by specifying non-key columns to be included in the index, improving query performance for specific field selections.
SOURCE: https://github.com/django/django/blob/main/docs/ref/models/indexes.txt#_snippet_10

LANGUAGE: Python
CODE:
```
Index(name="covering_index", fields=["headline"], include=["pub_date"])
```

----------------------------------------

TITLE: Simulate User Logout with Django Test Client
DESCRIPTION: Documents the `Client.logout()` and its asynchronous counterpart `Client.alogout()` methods, used to simulate a user logging out in Django's authentication system. Calling these methods clears test client cookies and session data, making subsequent requests appear from an `AnonymousUser`.
SOURCE: https://github.com/django/django/blob/main/docs/topics/testing/tools.txt#_snippet_25

LANGUAGE: APIDOC
CODE:
```
Client.logout()
Client.alogout()
  *Asynchronous version*: alogout()
  Description: If your site uses Django's authentication system, the logout() method can be used to simulate the effect of a user logging out of your site. After you call this method, the test client will have all the cookies and session data cleared to defaults. Subsequent requests will appear to come from an AnonymousUser.
```

----------------------------------------

TITLE: Django Widget.render Method
DESCRIPTION: Renders the widget to HTML using the specified renderer. If no renderer is provided, it defaults to the renderer configured in the FORM_RENDERER setting.
SOURCE: https://github.com/django/django/blob/main/docs/ref/forms/widgets.txt#_snippet_16

LANGUAGE: APIDOC
CODE:
```
Widget.render(name, value, attrs=None, renderer=None):
  name: The name of the widget.
  value: The current value of the widget.
  attrs: (Optional) HTML attributes to apply to the rendered widget.
  renderer: (Optional) The renderer to use; defaults to FORM_RENDERER setting.
  Returns: The HTML string representation of the widget.
```

----------------------------------------

TITLE: Django Field.widget Attribute Reference
DESCRIPTION: Documents the `Field.widget` attribute, which allows specifying a custom `Widget` class to control how a form field is rendered in HTML. It points to further documentation for detailed widget usage.
SOURCE: https://github.com/django/django/blob/main/docs/ref/forms/fields.txt#_snippet_14

LANGUAGE: APIDOC
CODE:
```
Field.widget:
  The `widget` argument lets you specify a `Widget` class to use when rendering this `Field`.
```

----------------------------------------

TITLE: Specifying Queryset for Django Generic Views
DESCRIPTION: This snippet introduces the `queryset` attribute as an alternative to the `model` attribute in Django generic views. While `model` specifies the database model, `queryset` allows you to provide a pre-filtered or custom QuerySet, enabling views to operate on specific subsets of objects.
SOURCE: https://github.com/django/django/blob/main/docs/topics/class-based-views/generic-display.txt#_snippet_6

LANGUAGE: python
CODE:
```
from django.views.generic import DetailView
from books.models import Publisher
```

----------------------------------------

TITLE: Slicing String/Array Fields with F() Expressions
DESCRIPTION: This snippet illustrates how F() expressions can be used with Python's array-slicing syntax for string-based, text-based, and ArrayField fields. The operation is performed at the database level, allowing for efficient substring extraction or array manipulation. Note that indices are 0-based and the 'step' argument to slice is not supported.
SOURCE: https://github.com/django/django/blob/main/docs/ref/models/expressions.txt#_snippet_7

LANGUAGE: Python
CODE:
```
# Replacing a name with a substring of itself.
writer = Writers.objects.get(name="Priyansh")
writer.name = F("name")[1:5]
writer.save()
writer.refresh_from_db()
writer.name
```

----------------------------------------

TITLE: Update a Django ForeignKey Field on a Model Instance
DESCRIPTION: This Python console example illustrates how to update a `ForeignKey` field on a Django model instance (`Entry`). It involves retrieving existing `Entry` and `Blog` objects, assigning the new `Blog` object to the `entry.blog` attribute, and then calling `.save()` to commit the change to the database.
SOURCE: https://github.com/django/django/blob/main/docs/topics/db/queries.txt#_snippet_3

LANGUAGE: pycon
CODE:
```
>>> from blog.models import Blog, Entry
>>> entry = Entry.objects.get(pk=1)
>>> cheese_blog = Blog.objects.get(name="Cheddar Talk")
>>> entry.blog = cheese_blog
>>> entry.save()
```

----------------------------------------

TITLE: Django Test Client User Login Methods
DESCRIPTION: The `Client.login()` and its asynchronous counterpart `Client.alogin()` simulate a user logging into a Django site that uses the authentication system. After calling this method, the test client will possess the necessary cookies and session data for login-based tests. The format of the `credentials` argument depends on the configured authentication backend, typically requiring username and password for Django's `ModelBackend`. It's crucial to create user accounts in the test database before using these methods, ensuring passwords are set with `set_password()` or `create_user()`.
SOURCE: https://github.com/django/django/blob/main/docs/topics/testing/tools.txt#_snippet_22

LANGUAGE: APIDOC
CODE:
```
Client.login(**credentials)
Client.alogin(**credentials) (Asynchronous version)
  credentials: Keyword arguments representing user credentials. The required credentials depend on the authentication backend (e.g., username and password for Django's ModelBackend).
Returns: True if the credentials were accepted and login was successful, False otherwise.
```

----------------------------------------

TITLE: Reference Transforms in Django Expressions
DESCRIPTION: Demonstrates how Django supports using transforms within expressions. This example finds all `Entry` objects published in the same year as they were last modified by comparing the `__year` transform of two date fields.
SOURCE: https://github.com/django/django/blob/main/docs/topics/db/queries.txt#_snippet_39

LANGUAGE: Python
CODE:
```
from django.db.models import F
Entry.objects.filter(pub_date__year=F("mod_date__year"))
```

----------------------------------------

TITLE: Django QuerySet Methods for Filtering
DESCRIPTION: Documentation for key methods used to refine Django QuerySets, including `filter()` and `exclude()`, which allow selecting or excluding objects based on lookup parameters.
SOURCE: https://github.com/django/django/blob/main/docs/topics/db/queries.txt#_snippet_8

LANGUAGE: APIDOC
CODE:
```
filter(**kwargs)
    Returns a new QuerySet containing objects that match the given lookup parameters.

exclude(**kwargs)
    Returns a new QuerySet containing objects that do not match the given lookup parameters.
```

----------------------------------------

TITLE: Django render() Function API Reference
DESCRIPTION: Documents the `render()` shortcut function in Django, which combines a template with a context dictionary to return an `HttpResponse` object. It details required and optional parameters such as `request`, `template_name`, `context`, `content_type`, `status`, and `using`.
SOURCE: https://github.com/django/django/blob/main/docs/topics/http/shortcuts.txt#_snippet_0

LANGUAGE: APIDOC
CODE:
```
render(request, template_name, context=None, content_type=None, status=None, using=None)
  Combines a given template with a given context dictionary and returns an HttpResponse object with that rendered text.
  Required arguments:
    request: The request object used to generate this response.
    template_name: The full name of a template to use or sequence of template names. If a sequence is given, the first template that exists will be used.
  Optional arguments:
    context: A dictionary of values to add to the template context. By default, this is an empty dictionary. If a value in the dictionary is callable, the view will call it just before rendering the template.
    content_type: The MIME type to use for the resulting document. Defaults to 'text/html'.
    status: The status code for the response. Defaults to 200.
    using: The NAME of a template engine to use for loading the template.
```

----------------------------------------

TITLE: Django Admin list_display with Model Attribute/Method
DESCRIPTION: Illustrates how to include a method or attribute directly from the model class in `list_display`. This allows for displaying computed properties or custom formatted data directly from the model.
SOURCE: https://github.com/django/django/blob/main/docs/ref/contrib/admin/index.txt#_snippet_33

LANGUAGE: python
CODE:
```
from django.contrib import admin
from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=50)
    birthday = models.DateField()

    @admin.display(description="Birth decade")
    def decade_born_in(self):
        decade = self.birthday.year // 10 * 10
        return f"{decade}’s"


class PersonAdmin(admin.ModelAdmin):
    list_display = ["name", "decade_born_in"]
```

----------------------------------------

TITLE: Add Custom Fields to Django Formset Forms and Render
DESCRIPTION: Demonstrates how to extend a formset's forms by adding a custom field (`my_field`) within a `BaseArticleFormSet` subclass's `add_fields` method. It then shows how to instantiate the formset and iterate through its forms to print their HTML representation, including the newly added field.
SOURCE: https://github.com/django/django/blob/main/docs/topics/forms/formsets.txt#_snippet_41

LANGUAGE: pycon
CODE:
```
...         super().add_fields(form, index)
...         form.fields["my_field"] = forms.CharField()
...

>>> ArticleFormSet = formset_factory(ArticleForm, formset=BaseArticleFormSet)
>>> formset = ArticleFormSet()
>>> for form in formset:
...     print(form)
...
<div><label for="id_form-0-title">Title:</label><input type="text" name="form-0-title" id="id_form-0-title"></div>
<div><label for="id_form-0-pub_date">Pub date:</label><input type="text" name="form-0-pub_date" id="id_form-0-pub_date"></div>
<div><label for="id_form-0-my_field">My field:</label><input type="text" name="form-0-my_field" id="id_form-0-my_field"></div>
```

----------------------------------------

TITLE: Define Django Models for a Blog Application
DESCRIPTION: This Python code defines the `Blog`, `Author`, and `Entry` models using Django's ORM. These models represent the database tables and their relationships for a simple blog application, including fields like `CharField`, `TextField`, `DateField`, `ForeignKey`, and `ManyToManyField`.
SOURCE: https://github.com/django/django/blob/main/docs/topics/db/queries.txt#_snippet_0

LANGUAGE: python
CODE:
```
from datetime import date

from django.db import models


class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField(default=date.today)
    authors = models.ManyToManyField(Author)
    number_of_comments = models.IntegerField(default=0)
    number_of_pingbacks = models.IntegerField(default=0)
    rating = models.IntegerField(default=5)

    def __str__(self):
        return self.headline
```

----------------------------------------

TITLE: Demonstrating Django QuerySet Lazy Evaluation
DESCRIPTION: This example shows how Django QuerySets are lazy. Multiple filter and exclude calls do not hit the database until the QuerySet is evaluated, such as when printed or iterated over.
SOURCE: https://github.com/django/django/blob/main/docs/topics/db/queries.txt#_snippet_12

LANGUAGE: pycon
CODE:
```
>>> q = Entry.objects.filter(headline__startswith="What")
>>> q = q.filter(pub_date__lte=datetime.date.today())
>>> q = q.exclude(body_text__icontains="food")
>>> print(q)
```

----------------------------------------

TITLE: Demonstrating QuerySet Object Attribute Caching in Django
DESCRIPTION: This snippet illustrates how Django ORM objects cache non-callable attributes. Accessing `entry.blog` the first time triggers a database lookup, but subsequent accesses retrieve the cached version without further database interaction, improving performance.
SOURCE: https://github.com/django/django/blob/main/docs/topics/db/optimization.txt#_snippet_0

LANGUAGE: pycon
CODE:
```
entry = Entry.objects.get(id=1)
entry.blog  # Blog object is retrieved at this point
entry.blog  # cached version, no DB access
```

----------------------------------------

TITLE: Example Django Class-Based View for Testing
DESCRIPTION: Defines a simple `TemplateView` subclass, `HomeView`, with an overridden `get_context_data` method. This view serves as an example for demonstrating how to test class-based views directly, particularly their context data generation.
SOURCE: https://github.com/django/django/blob/main/docs/topics/testing/advanced.txt#_snippet_3

LANGUAGE: Python
CODE:
```
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "kryptisk/home.html"

    def get_context_data(self, **kwargs):
        kwargs["environment"] = "Production"
        return super().get_context_data(**kwargs)
```

----------------------------------------

TITLE: Deleting Django Model from a Specific Database
DESCRIPTION: This example demonstrates how to explicitly specify the database from which a model instance should be deleted by passing the `using` keyword argument to the `Model.delete()` method. This is useful for scenarios like migrating users between databases.
SOURCE: https://github.com/django/django/blob/main/docs/topics/db/multi-db.txt#_snippet_17

LANGUAGE: pycon
CODE:
```
>>> user_obj.save(using="new_users")
>>> user_obj.delete(using="legacy_users")
```

----------------------------------------

TITLE: Using a Custom Reverse Manager for Related Objects in Django
DESCRIPTION: This snippet demonstrates how to define and use a custom manager (`EntryManager`) for reverse relations. It shows how to specify the custom manager when querying related objects using `entry_set(manager="entries").all()`.
SOURCE: https://github.com/django/django/blob/main/docs/topics/db/queries.txt#_snippet_99

LANGUAGE: python
CODE:
```
from django.db import models


class Entry(models.Model):
    # ...
    objects = models.Manager()  # Default Manager
    entries = EntryManager()  # Custom Manager


b = Blog.objects.get(id=1)
b.entry_set(manager="entries").all()
```

----------------------------------------

TITLE: Delete Single Django Model Instance
DESCRIPTION: Demonstrates how deleting a single Django model instance using the `delete()` method triggers a cascade deletion of related objects by default, emulating SQL's `ON DELETE CASCADE`.
SOURCE: https://github.com/django/django/blob/main/docs/topics/db/queries.txt#_snippet_77

LANGUAGE: Python
CODE:
```
b = Blog.objects.get(pk=1)
# This will delete the Blog and all of its Entry objects.
b.delete()
```

----------------------------------------

TITLE: Add Errors to Django Form Fields
DESCRIPTION: Explains `Form.add_error()`, a method for programmatically adding errors to specific fields or as non-field errors from within `Form.clean()` or external contexts like views. Details the `field` and `error` arguments and its effect on `cleaned_data`.
SOURCE: https://github.com/django/django/blob/main/docs/ref/forms/api.txt#_snippet_16

LANGUAGE: APIDOC
CODE:
```
Form.add_error(field, error)
  field: The name of the field to which the errors should be added. If None, treated as a non-field error.
  error: A string or an instance of ValidationError.
  Returns: None.
```

----------------------------------------

TITLE: Send email with plain text and HTML alternatives
DESCRIPTION: Provides a complete Python example demonstrating how to construct and send an email that includes both a plain text version and an HTML version of the message body using Django's `EmailMultiAlternatives` class and its `attach_alternative` method.
SOURCE: https://github.com/django/django/blob/main/docs/topics/email.txt#_snippet_16

LANGUAGE: Python
CODE:
```
from django.core.mail import EmailMultiAlternatives

subject = "hello"
from_email = "from@example.com"
to = "to@example.com"
text_content = "This is an important message."
html_content = "<p>This is an <strong>important</strong> message.</p>"
msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
msg.attach_alternative(html_content, "text/html")
msg.send()
```

----------------------------------------

TITLE: Define Restaurant Model with Related Fields
DESCRIPTION: This Python code defines a `Restaurant` model with `ManyToManyField` to `Pizza` and a `ForeignKey` to `Pizza`, demonstrating the relationships used in subsequent prefetching examples.
SOURCE: https://github.com/django/django/blob/main/docs/ref/models/querysets.txt#_snippet_64

LANGUAGE: python
CODE:
```
class Restaurant(models.Model):
    pizzas = models.ManyToManyField(Pizza, related_name="restaurants")
    best_pizza = models.ForeignKey(
        Pizza, related_name="championed_by", on_delete=models.CASCADE
    )
```

----------------------------------------

TITLE: APIDOC: django.contrib.auth.mixins.UserPassesTestMixin
DESCRIPTION: API documentation for the `UserPassesTestMixin` class, designed for use with Django's class-based views to enforce access control. It requires overriding `test_func()` and allows for custom test function naming via `get_test_func()` to integrate custom access logic.
SOURCE: https://github.com/django/django/blob/main/docs/topics/auth/default.txt#_snippet_27

LANGUAGE: APIDOC
CODE:
```
UserPassesTestMixin
  test_func(): You have to override the test_func() method of the class to provide the test that is performed. Furthermore, you can set any of the parameters of AccessMixin to customize the handling of unauthorized users.
  get_test_func(): You can also override the get_test_func() method to have the mixin use a differently named function for its checks (instead of test_func).
```

----------------------------------------

TITLE: Define a Custom Even Number Validator in Django
DESCRIPTION: This Python function `validate_even` serves as a custom validator for Django. It checks if a given value is an even number and raises a `ValidationError` with a localized message if the value is odd, demonstrating a fundamental approach to creating reusable validation logic.
SOURCE: https://github.com/django/django/blob/main/docs/ref/validators.txt#_snippet_0

LANGUAGE: Python
CODE:
```
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(
            _("%(value)s is not an even number"),
            params={"value": value},
        )
```

----------------------------------------

TITLE: Django Related Object Manager Methods API
DESCRIPTION: This section provides API documentation for additional methods available on the `ForeignKey`'s `Manager` for handling sets of related objects. These methods allow for direct manipulation of the relationship in the database.
SOURCE: https://github.com/django/django/blob/main/docs/topics/db/queries.txt#_snippet_102

LANGUAGE: APIDOC
CODE:
```
add(obj1, obj2, ...)
    Adds the specified model objects to the related object set.
create(**kwargs)
    Creates a new object, saves it and puts it in the related object set.
    Returns the newly created object.
remove(obj1, obj2, ...)
    Removes the specified model objects from the related object set.
clear()
    Removes all objects from the related object set.
set(objs)
    Replace the set of related objects.
```

----------------------------------------

TITLE: HttpRequest.get_signed_cookie Method API Reference
DESCRIPTION: API documentation for `HttpRequest.get_signed_cookie`, which retrieves a signed cookie value. It details parameters like `key`, `default`, `salt`, and `max_age`, explaining how to handle invalid signatures or expired cookies.
SOURCE: https://github.com/django/django/blob/main/docs/ref/request-response.txt#_snippet_21

LANGUAGE: APIDOC
CODE:
```
HttpRequest.get_signed_cookie(key, default=RAISE_ERROR, salt='', max_age=None)
  key: The name of the cookie to retrieve.
  default: (Optional) A value to return if the cookie is not found or signature is invalid, suppressing exceptions.
  salt: (Optional) A string to provide extra protection against brute force attacks on the secret key.
  max_age: (Optional) An integer representing the maximum age in seconds for the cookie to be considered valid.
Returns: The cookie value (string) or the default value if provided.
Raises: django.core.signing.BadSignature if signature is invalid and no default is provided.
        KeyError if cookie does not exist and no default is provided.
        SignatureExpired if max_age is exceeded and no default is provided.
```

----------------------------------------

TITLE: Atomically Incrementing Field Value with F Expressions
DESCRIPTION: Shows how to use Django's `F` expressions to perform atomic updates on model fields, such as incrementing a counter. This method is more robust and avoids race conditions compared to direct Python arithmetic, ensuring data integrity in concurrent operations.
SOURCE: https://github.com/django/django/blob/main/docs/ref/models/instances.txt#_snippet_32

LANGUAGE: pycon
CODE:
```
from django.db.models import F
product = Product.objects.get(name="Venezuelan Beaver Cheese")
product.number_sold = F("number_sold") + 1
product.save()
```

----------------------------------------

TITLE: Define Django Views with URL Arguments
DESCRIPTION: This Python code defines three Django view functions (`detail`, `results`, and `vote`) within `polls/views.py`. Each function takes a `request` object and a `question_id` argument, demonstrating how views can accept parameters from the URL. Currently, they return simple `HttpResponse` strings as placeholders.
SOURCE: https://github.com/django/django/blob/main/docs/intro/tutorial03.txt#_snippet_0

LANGUAGE: python
CODE:
```
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
```

----------------------------------------

TITLE: Implement Custom List Filter using SimpleListFilter
DESCRIPTION: Shows how to create a custom list filter by subclassing `django.contrib.admin.SimpleListFilter`. This involves defining `title` and `parameter_name` attributes, and overriding the `lookups` method to provide filter options and the `queryset` method to apply filtering logic based on the selected option.
SOURCE: https://github.com/django/django/blob/main/docs/ref/contrib/admin/filters.txt#_snippet_1

LANGUAGE: python
CODE:
```
from datetime import date

from django.contrib import admin
from django.utils.translation import gettext_lazy as _


class DecadeBornListFilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = _("decade born")

    # Parameter for the filter that will be used in the URL query.
    parameter_name = "decade"

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return [
            ("80s", _("in the eighties")),
            ("90s", _("in the nineties")),
        ]

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        # Compare the requested value (either '80s' or '90s')
        # to decide how to filter the queryset.
        if self.value() == "80s":
            return queryset.filter(
                birthday__gte=date(1980, 1, 1),
                birthday__lte=date(1989, 12, 31),
            )
        if self.value() == "90s":
            return queryset.filter(
                birthday__gte=date(1990, 1, 1),
                birthday__lte=date(1989, 12, 31),
            )


class PersonAdmin(admin.ModelAdmin):
    list_filter = [DecadeBornListFilter]
```

----------------------------------------

TITLE: Create Unbound Django Form Instance
DESCRIPTION: Demonstrates how to instantiate a Django Form class without any data, resulting in an unbound form. This form can render a blank HTML form but cannot perform validation.
SOURCE: https://github.com/django/django/blob/main/docs/ref/forms/api.txt#_snippet_1

LANGUAGE: python
CODE:
```
f = ContactForm()
```

----------------------------------------

TITLE: Django FilePathField Class API Reference
DESCRIPTION: API documentation for Django's FilePathField, a CharField subclass designed to limit choices to filenames within a specified directory. It supports filtering by regular expressions and including files from subdirectories.
SOURCE: https://github.com/django/django/blob/main/docs/ref/models/fields.txt#_snippet_57

LANGUAGE: APIDOC
CODE:
```
FilePathField(path='', match=None, recursive=False, allow_files=True, allow_folders=False, max_length=100, **options):
  Description: A CharField whose choices are limited to the filenames in a certain path.
  Parameters:
    path: str = '' - The directory path to limit choices to.
    match: str = None - A regular expression to filter filenames.
    recursive: bool = False - Whether to include files from subdirectories.
    allow_files: bool = True - Whether to allow files as choices.
    allow_folders: bool = False - Whether to allow folders as choices.
    max_length: int = 100 - The maximum length of the field.
    **options: dict - Additional CharField options.
```
