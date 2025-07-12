TITLE: Integrating Import-Export with Django Admin (Python)
DESCRIPTION: Demonstrates how to integrate django-import-export with a Django model's admin interface by subclassing ImportExportModelAdmin and registering the model. It shows how to associate a Resource class with the admin.
SOURCE: https://github.com/django-import-export/django-import-export/blob/main/docs/admin_integration.rst#_snippet_0

LANGUAGE: Python
CODE:
```
# app/admin.py
from django.contrib import admin
from .models import Book
from import_export.admin import ImportExportModelAdmin

@admin.register(Book)
class BookAdmin(ImportExportModelAdmin):
    resource_classes = [BookResource]
```

----------------------------------------

TITLE: Install django-import-export via pip (basic)
DESCRIPTION: Standard installation command using pip to install the django-import-export library.
SOURCE: https://github.com/django-import-export/django-import-export/blob/main/docs/installation.rst#_snippet_0

LANGUAGE: Shell
CODE:
```
pip install django-import-export
```

----------------------------------------

TITLE: Add 'import_export' to INSTALLED_APPS
DESCRIPTION: Configures the Django project by adding 'import_export' to the list of installed applications in settings.py. This is required for admin integration.
SOURCE: https://github.com/django-import-export/django-import-export/blob/main/docs/installation.rst#_snippet_4

LANGUAGE: Python
CODE:
```
# settings.py
INSTALLED_APPS = (
    ...
    'import_export',
)
```

----------------------------------------

TITLE: Creating Import/Export Resource for Book Model - Python
DESCRIPTION: Defines a `ModelResource` subclass `BookResource` in `admin.py` to integrate the `Book` model with the `django-import-export` library, specifying how the model's data should be handled during import and export.
SOURCE: https://github.com/django-import-export/django-import-export/blob/main/docs/getting_started.rst#_snippet_1

LANGUAGE: python
CODE:
```
# app/admin.py

from import_export import resources
from core.models import Book

class BookResource(resources.ModelResource):

        class Meta:
            model = Book  # or 'core.Book'
```

----------------------------------------

TITLE: Explicitly Declaring Field with attribute and column_name (Python)
DESCRIPTION: Demonstrates how to explicitly declare a field using `import_export.fields.Field` to map a specific model attribute (`attribute`) to a different column header name (`column_name`) during import/export.
SOURCE: https://github.com/django-import-export/django-import-export/blob/main/docs/advanced_usage.rst#_snippet_4

LANGUAGE: Python
CODE:
```
from import_export.fields import Field

class BookResource(resources.ModelResource):
    published_field = Field(attribute='published', column_name='published_date')

    class Meta:
        model = Book
```

----------------------------------------

TITLE: Use ForeignKeyWidget for Related Model Lookup by Name (django-import-export)
DESCRIPTION: Shows how to define a `BookResource` that uses `ForeignKeyWidget` to look up a related `Author` model instance based on its 'name' field instead of the default 'pk' during data import.
SOURCE: https://github.com/django-import-export/django-import-export/blob/main/docs/advanced_usage.rst#_snippet_16

LANGUAGE: Python
CODE:
```
from import_export import fields
from import_export.widgets import ForeignKeyWidget

class BookResource(resources.ModelResource):
    author = fields.Field(
        column_name='author',
        attribute='author',
        widget=ForeignKeyWidget(Author, field='name'))

    class Meta:
        model = Book
        fields = ('author',)
```

----------------------------------------

TITLE: Registering Django Model Admin with Export Action
DESCRIPTION: This Python snippet registers the `Book` model with the custom `BookAdmin` class using Django's `admin.site.register`. This makes the `Book` model manageable in the Django Admin interface and enables the export action functionality defined in `BookAdmin`.
SOURCE: https://github.com/django-import-export/django-import-export/blob/main/docs/admin_integration.rst#_snippet_3

LANGUAGE: Python
CODE:
```
admin.site.register(Book, BookAdmin)
```

----------------------------------------

TITLE: Install django-import-export with all formats
DESCRIPTION: Installs the library including dependencies for all supported formats using pip.
SOURCE: https://github.com/django-import-export/django-import-export/blob/main/docs/installation.rst#_snippet_2

LANGUAGE: Shell
CODE:
```
pip install django-import-export[all]
```

----------------------------------------

TITLE: Use ManyToManyWidget for Related Model Import with Separator (django-import-export)
DESCRIPTION: Illustrates how to configure a `BookResource` to import many-to-many relationships (`Categories`) using `ManyToManyWidget`, specifying the related model, the lookup field ('name'), and a custom separator ('|') for the input data.
SOURCE: https://github.com/django-import-export/django-import-export/blob/main/docs/advanced_usage.rst#_snippet_17

LANGUAGE: Python
CODE:
```
class BookResource(resources.ModelResource):
    categories = fields.Field(
        column_name='categories',
        attribute='categories',
        widget=widgets.ManyToManyWidget(Category, field='name', separator='|')
    )

    class Meta:
        model = Book
```

----------------------------------------

TITLE: Create Non-Existent ForeignKey Relations During Import (django-import-export)
DESCRIPTION: Provides an example of subclassing `ForeignKeyWidget` and overriding its `clean` method to automatically create a related `Author` instance if a matching one is not found during the import process, preventing `DoesNotExist` errors.
SOURCE: https://github.com/django-import-export/django-import-export/blob/main/docs/advanced_usage.rst#_snippet_18

LANGUAGE: Python
CODE:
```
class AuthorForeignKeyWidget(ForeignKeyWidget):
    def clean(self, value, row=None, **kwargs):
        try:
            val = super().clean(value)
        except Author.DoesNotExist:
            val = Author.objects.create(name=row['author'])
        return val
```

----------------------------------------

TITLE: Filtering Resource Queryset Based on User in Django Import/Export
DESCRIPTION: This `ModelResource` (`BookResource`) demonstrates how to accept a `user` object in its constructor (passed from the `ModelAdmin`). It then overrides the `get_queryset` method to filter the data based on a property of the user (`user.publisher_id`), ensuring only relevant data is processed during import or export.
SOURCE: https://github.com/django-import-export/django-import-export/blob/main/docs/admin_integration.rst#_snippet_18

LANGUAGE: Python
CODE:
```
class BookResource(ModelResource):

    def __init__(self, user):
        self.user = user

    def get_queryset(self):
        return self._meta.model.objects.filter(publisher_id=self.user.publisher_id)

    class Meta:
        model = Book
```

----------------------------------------

TITLE: Implementing Custom Field Validation Widget - Python
DESCRIPTION: This snippet defines a custom `PositiveIntegerWidget` that extends the base `IntegerWidget`. It overrides the `clean` method to add custom validation logic. After calling the parent `clean` method, it checks if the resulting integer value is negative and raises a `ValueError` if it is, enforcing that the imported value must be positive.
SOURCE: https://github.com/django-import-export/django-import-export/blob/main/docs/advanced_usage.rst#_snippet_14

LANGUAGE: Python
CODE:
```
class PositiveIntegerWidget(IntegerWidget):
  """Returns a positive integer value"""

  def clean(self, value, row=None, **kwargs):
      val = super().clean(value, row=row, **kwargs)
      if val < 0:
          raise ValueError("value must be positive")
      return val
```

----------------------------------------

TITLE: Usage of Django Export Command (Bash)
DESCRIPTION: Provides the general command line syntax for using the Django import-export 'export' management command. It shows the required arguments for format and resource, and the optional encoding flag.
SOURCE: https://github.com/django-import-export/django-import-export/blob/main/docs/management_commands.rst#_snippet_0

LANGUAGE: bash
CODE:
```
python manage.py export <format> <resource> [--encoding ENCODING]
```

----------------------------------------

TITLE: Using import_id_fields to Identify Instances by ISBN
DESCRIPTION: Configures a `ModelResource` to use the 'isbn' field instead of the default 'id' for uniquely identifying existing instances during import. This is done by setting the `import_id_fields` attribute in the `Meta` class.
SOURCE: https://github.com/django-import-export/django-import-export/blob/main/docs/advanced_usage.rst#_snippet_26

LANGUAGE: Python
CODE:
```
class BookResource(resources.ModelResource):

    class Meta:
        model = Book
        import_id_fields = ('isbn',)
        fields = ('isbn', 'name', 'author', 'price',)
```

----------------------------------------

TITLE: Implementing Data Deletion Logic in Resource - Python
DESCRIPTION: Shows how to add a `for_delete` method to a `ModelResource` to enable deleting model instances based on a condition during the import process. This example uses a 'delete' field in the import data to flag rows for deletion.
SOURCE: https://github.com/django-import-export/django-import-export/blob/main/docs/getting_started.rst#_snippet_3

LANGUAGE: python
CODE:
```
class BookResource(resources.ModelResource):

        def for_delete(self, row, instance):
            return row["delete"] == "1"

        class Meta:
            model = Book
```

----------------------------------------

TITLE: Passing Request User to Import Resource in Django Admin
DESCRIPTION: This method override in a `ModelAdmin` (`BookAdmin`) demonstrates how to capture the authenticated user from the request object and pass it as a keyword argument (`user`) to the constructor of the import resource. This is useful for filtering data based on the user during import.
SOURCE: https://github.com/django-import-export/django-import-export/blob/main/docs/admin_integration.rst#_snippet_17

LANGUAGE: Python
CODE:
```
class BookAdmin(ImportExportMixin, admin.ModelAdmin):
    # attribute declarations not shown

    def get_import_resource_kwargs(self, request, *args, **kwargs):
        kwargs = super().get_resource_kwargs(request, *args, **kwargs)
        kwargs.update({"user": request.user})
        return kwargs
```

----------------------------------------

TITLE: Import Data into Django User Model from CSV (Bash)
DESCRIPTION: Example demonstrating how to use the Django import-export 'import' command to load data from a 'users.csv' file into the built-in 'auth.User' model using its default resource.
SOURCE: https://github.com/django-import-export/django-import-export/blob/main/docs/management_commands.rst#_snippet_4

LANGUAGE: bash
CODE:
```
python manage.py import auth.User users.csv
```

----------------------------------------

TITLE: Following Model Relationships with __ Syntax (Python)
DESCRIPTION: Shows how to access fields on related models (e.g., `Author.name` via the `Book` model) using the double underscore (`__`) syntax within the `fields` option. This is primarily for export; importing related fields requires a different approach.
SOURCE: https://github.com/django-import-export/django-import-export/blob/main/docs/advanced_usage.rst#_snippet_3

LANGUAGE: Python
CODE:
```
class BookResource(resources.ModelResource):

    class Meta:
        model = Book
        fields = ('author__name',)
```

----------------------------------------

TITLE: Importing Data Programmatically with django-import-export - Python
DESCRIPTION: Demonstrates how to programmatically import data into the `Book` model using `tablib` and the `import-export` library. It shows creating a resource, preparing a dataset, performing a dry-run import to check for errors, and then executing the actual import.
SOURCE: https://github.com/django-import-export/django-import-export/blob/main/docs/getting_started.rst#_snippet_2

LANGUAGE: python
CODE:
```
>>> import tablib
>>> from import_export import resources
>>> from core.models import Book
>>> book_resource = resources.modelresource_factory(model=Book)()
>>> dataset = tablib.Dataset(['', 'New book'], headers=['id', 'name'])
>>> result = book_resource.import_data(dataset, dry_run=True)
>>> print(result.has_errors())
False
>>> result = book_resource.import_data(dataset, dry_run=False)
```

----------------------------------------

TITLE: Export Django User Model to CSV (Bash)
DESCRIPTION: Example demonstrating how to use the Django import-export 'export' command to export data from the built-in 'auth.User' model into a CSV file format.
SOURCE: https://github.com/django-import-export/django-import-export/blob/main/docs/management_commands.rst#_snippet_1

LANGUAGE: bash
CODE:
```
python manage.py export CSV auth.User
```

----------------------------------------

TITLE: Customize Export Headers in Django Import Export (Python)
DESCRIPTION: This snippet demonstrates how to override the `get_export_headers` method in a `ModelResource` to change the column names that appear in the exported file. It iterates through the default headers and replaces a specific header ('name') with a new one ('NEW COLUMN NAME'). This is useful for providing more user-friendly or specific column labels in exports.
SOURCE: https://github.com/django-import-export/django-import-export/blob/main/docs/faq.rst#_snippet_2

LANGUAGE: Python
CODE:
```
class BookResource(ModelResource):

    def get_export_headers(self, fields=None):
      headers = super().get_export_headers(fields=fields)
      for i, h in enumerate(headers):
          if h == 'name':
            headers[i] = "NEW COLUMN NAME"
      return headers

    class Meta:
      model = Book
```

----------------------------------------

TITLE: Replace resource_class with resource_classes in Django Admin
DESCRIPTION: Demonstrates the change in Django Admin UI configuration in v4, replacing the single `resource_class` attribute with a list `resource_classes` for specifying resources.
SOURCE: https://github.com/django-import-export/django-import-export/blob/main/docs/release_notes.rst#_snippet_5

LANGUAGE: Python
CODE:
```
class BookAdmin(ImportExportModelAdmin):
  # remove this line
  # resource_class = BookResource
  # replace with this
  resource_classes = [BookResource]
```

----------------------------------------

TITLE: Create Resource Subclass for Export Filtering (Python)
DESCRIPTION: Defines a custom EBookResource class that inherits from ModelResource. Its constructor accepts **kwargs and stores an author_id attribute if provided. It overrides the filter_export method to filter the queryset based on the stored author_id, allowing exports to be limited to books by a specific author.
SOURCE: https://github.com/django-import-export/django-import-export/blob/main/docs/admin_integration.rst#_snippet_14

LANGUAGE: Python
CODE:
```
class EBookResource(ModelResource):
    def __init__(self, **kwargs):
        super().__init__()
        self.author_id = kwargs.get("author_id")

    def filter_export(self, queryset, **kwargs):
        return queryset.filter(author_id=self.author_id)

    class Meta:
        model = EBook
```

----------------------------------------

TITLE: Manipulate Export Data (dehydrate_<fieldname>)
DESCRIPTION: Illustrates how to define a dehydrate_<fieldname> method on a Resource to process data from the model instance into a desired format for export, creating a new field like 'full_title'.
SOURCE: https://github.com/django-import-export/django-import-export/blob/main/docs/advanced_usage.rst#_snippet_33

LANGUAGE: Python
CODE:
```
from import_export.fields import Field

    class BookResource(resources.ModelResource):
        full_title = Field()

        class Meta:
            model = Book

        def dehydrate_full_title(self, book):
            book_name = getattr(book, "name", "unknown")
            author_name = getattr(book.author, "name", "unknown")
            return '%s by %s' % (book_name, author_name)
```

----------------------------------------

TITLE: Declaring Fields with fields Option (Python)
DESCRIPTION: Shows how to use the `fields` option within the `Meta` class of a `ModelResource` to explicitly list the model fields that should be included during import/export, effectively whitelisting them.
SOURCE: https://github.com/django-import-export/django-import-export/blob/main/docs/advanced_usage.rst#_snippet_0

LANGUAGE: Python
CODE:
```
class BookResource(resources.ModelResource):

    class Meta:
        model = Book
        fields = ('id', 'name', 'price',)
```

----------------------------------------

TITLE: Iterating Validation Errors (Raise False) - Python
DESCRIPTION: This code demonstrates how to process all rows in a dataset and collect all validation errors by setting `raise_errors` to `False`. After the import completes, the code iterates through the `invalid_rows` list in the `Result` object. For each invalid row, it prints the row number, the field causing the error, the error message, and the original row values.
SOURCE: https://github.com/django-import-export/django-import-export/blob/main/docs/advanced_usage.rst#_snippet_11

LANGUAGE: Python
CODE:
```
result = self.resource.import_data(self.dataset, raise_errors=False)
for row in result.invalid_rows:
    print(f"--- row {row.number} ---")
    for field, error in row.error.error_dict.items():
        print(f"{field}: {error} ({row.values})")
```

----------------------------------------

TITLE: Install django-import-export with xlsx support
DESCRIPTION: Installs the library along with dependencies required for xlsx format support using pip.
SOURCE: https://github.com/django-import-export/django-import-export/blob/main/docs/installation.rst#_snippet_1

LANGUAGE: Shell
CODE:
```
pip install django-import-export[xlsx]
```

----------------------------------------

TITLE: Implement Custom Workflow After Import Row in Django Import Export
DESCRIPTION: Provides an example of overriding the `after_import_row` method in a Resource to implement custom logic based on changes detected during the import process. It checks if the 'published' field changed from None to a value, indicating a one-off event.
SOURCE: https://github.com/django-import-export/django-import-export/blob/main/docs/advanced_usage.rst#_snippet_9

LANGUAGE: Python
CODE:
```
class BookResource(resources.ModelResource):

    def after_import_row(self, row, row_result, **kwargs):
        if getattr(row_result.original, "published") is None \
            and getattr(row_result.instance, "published") is not None:
            # import value is different from stored value.
            # exec custom workflow...

    class Meta:
        model = Book
        store_instance = True
```

----------------------------------------

TITLE: Set Value on Imported Instances (before_save_instance)
DESCRIPTION: Shows how to set a common value on all instances created during import by initializing the resource with a parameter and assigning it within the before_save_instance method.
SOURCE: https://github.com/django-import-export/django-import-export/blob/main/docs/advanced_usage.rst#_snippet_32

LANGUAGE: Python
CODE:
```
class BookResource(ModelResource):

        def __init__(self, publisher_id):
            self.publisher_id = publisher_id

        def before_save_instance(self, instance, row, **kwargs):
            instance.publisher_id = self.publisher_id

        class Meta:
            model = Book
```

----------------------------------------

TITLE: Exporting Data Programmatically with django-import-export - Python
DESCRIPTION: Illustrates how to export data from the `Book` model programmatically using the defined `BookResource`. It demonstrates creating a resource instance, calling the `export()` method, and accessing the exported data in CSV format.
SOURCE: https://github.com/django-import-export/django-import-export/blob/main/docs/getting_started.rst#_snippet_4

LANGUAGE: python
CODE:
```
>>> from core.admin import BookResource
>>> dataset = BookResource().export()
>>> print(dataset.csv)
id,name,author,author_email,imported,published,price,categories
2,Some book,1,,0,2012-12-05,8.85,1
```

----------------------------------------

TITLE: Iterating Generic Errors (Raise False) - Python
DESCRIPTION: This code shows how to continue the import process despite generic errors by setting `raise_errors` to `False`. After the import, it iterates through the `error_rows` list in the `Result` object. For each row with a generic error, it prints the row number and details about the error, including the exception type and the row data associated with the error.
SOURCE: https://github.com/django-import-export/django-import-export/blob/main/docs/advanced_usage.rst#_snippet_13

LANGUAGE: Python
CODE:
```
result = self.resource.import_data(self.dataset, raise_errors=False)
for row in result.error_rows:
    print(f"--- row {row.number} ---")
    for field, error in row.error.error_dict.items():
        print(f"{field}: {error} ({error.row})")
```

----------------------------------------

TITLE: Excluding Fields with exclude Option (Python)
DESCRIPTION: Demonstrates how to use the `exclude` option in the `Meta` class of a `ModelResource` to specify model fields that should be excluded from the import/export process, effectively blacklisting them.
SOURCE: https://github.com/django-import-export/django-import-export/blob/main/docs/advanced_usage.rst#_snippet_1

LANGUAGE: Python
CODE:
```
class BookResource(resources.ModelResource):

    class Meta:
        model = Book
        exclude = ('imported', )
```

----------------------------------------

TITLE: Defining Author Field and Meta Class in Django Import Export Resource
DESCRIPTION: Shows a basic definition of an 'author' field using a custom ForeignKeyWidget and the Meta class linking the resource to the Book model.
SOURCE: https://github.com/django-import-export/django-import-export/blob/main/docs/advanced_usage.rst#_snippet_19

LANGUAGE: Python
CODE:
```
        author = fields.Field(
            attribute="author",
            column_name="author",
            widget=AuthorForeignKeyWidget(Author, "name")
        )

        class Meta:
            model = Book
```

----------------------------------------

TITLE: Install django-import-export with all dependencies
DESCRIPTION: Provides the command line instruction to install the django-import-export library including all optional dependencies, ensuring compatibility with pre-v4 behavior.
SOURCE: https://github.com/django-import-export/django-import-export/blob/main/docs/release_notes.rst#_snippet_0

LANGUAGE: Shell
CODE:
```
django-import-export[all]
```

----------------------------------------

TITLE: Define Separate Import and Export Resources
DESCRIPTION: Shows the recommended approach for handling different field sets for import and export by defining two distinct ModelResource classes, one for import and one for export.
SOURCE: https://github.com/django-import-export/django-import-export/blob/main/docs/advanced_usage.rst#_snippet_35

LANGUAGE: Python
CODE:
```
class BookImportResource(ModelResource):
        class Meta:
            model = Book
            fields = ["id", "name"]


    class BookExportResource(ModelResource):
        class Meta:
            model = Book
            fields = ["id", "name", "published"]
```

----------------------------------------

TITLE: Configure CharField Widget for Null/Blank Handling - Python
DESCRIPTION: Demonstrates how to configure a Field's widget in a ModelResource to control how empty cells are handled during import. Setting `allow_blank=False` on a `CharWidget` ensures that empty strings are saved instead of `None` for Django CharFields that have `blank=True`, preventing 'NOT NULL' constraint errors.
SOURCE: https://github.com/django-import-export/django-import-export/blob/main/docs/faq.rst#_snippet_1

LANGUAGE: python
CODE:
```
class BookResource(resources.ModelResource):

    name = Field(widget=CharWidget(allow_blank=False))

    class Meta:
        model = Book
```

----------------------------------------

TITLE: Defining Multiple Resources in Django Admin
DESCRIPTION: This snippet shows how to define multiple `ModelResource` classes (`BookResource`, `BookNameResource`) and assign them to the `resource_classes` attribute of a `ModelAdmin` (`CustomBookAdmin`). This allows the user to choose which resource to use during import or export operations.
SOURCE: https://github.com/django-import-export/django-import-export/blob/main/docs/admin_integration.rst#_snippet_16

LANGUAGE: Python
CODE:
```
from import_export import resources
from core.models import Book


class BookResource(resources.ModelResource):

    class Meta:
        model = Book


class BookNameResource(resources.ModelResource):

    class Meta:
        model = Book
        fields = ['id', 'name']
        name = "Export/Import only book names"


class CustomBookAdmin(ImportMixin, admin.ModelAdmin):
    resource_classes = [BookResource, BookNameResource]
```

----------------------------------------

TITLE: Manipulate Export Data (Field dehydrate_method)
DESCRIPTION: Demonstrates using the 'dehydrate_method' argument of the Field constructor to specify a custom method or callable function for data manipulation during export.
SOURCE: https://github.com/django-import-export/django-import-export/blob/main/docs/advanced_usage.rst#_snippet_34

LANGUAGE: Python
CODE:
```
from import_export.fields import Field

    # Using method name
    class BookResource(resources.ModelResource):
        full_title = Field(dehydrate_method='custom_dehydrate_method')

        class Meta:
            model = Book

        def custom_dehydrate_method(self, book):
            return f"{book.name} by {book.author.name}"

    # Using a callable directly
    def custom_dehydrate_callable(book):
        return f"{book.name} by {book.author.name}"

    class BookResource(resources.ModelResource):
        full_title = Field(dehydrate_method=custom_dehydrate_callable)

        class Meta:
            model = Book
```

----------------------------------------

TITLE: Import Data Using Custom Resource with Error Handling (Bash)
DESCRIPTION: Example showing how to use the Django import-export 'import' command with a custom resource ('helper.MyUserResource') and the '--raise-errors' flag to import data from 'users.csv', ensuring any errors halt the process.
SOURCE: https://github.com/django-import-export/django-import-export/blob/main/docs/management_commands.rst#_snippet_5

LANGUAGE: bash
CODE:
```
python manage.py import --raise-errors helper.MyUserResource users.csv
```

----------------------------------------

TITLE: Customizing ForeignKeyWidget Lookup with Dynamic Value in Django Import Export
DESCRIPTION: Demonstrates how to pass a dynamic value (like publisher_id) to a ModelResource constructor and use it to initialize a custom ForeignKeyWidget field.
SOURCE: https://github.com/django-import-export/django-import-export/blob/main/docs/advanced_usage.rst#_snippet_20

LANGUAGE: Python
CODE:
```
    class BookResource(resources.ModelResource):

        def __init__(self, publisher_id):
            super().__init__()
            self.fields["author"] = fields.Field(
                attribute="author",
                column_name="author",
                widget=AuthorForeignKeyWidget(publisher_id),
            )
```

----------------------------------------

TITLE: Importing Data with Validation Errors (Raise True) - Python
DESCRIPTION: This snippet shows how to import data programmatically using `django-import-export` with `raise_errors` set to `True`. When a validation error occurs during processing (e.g., invalid date format), the `import_data` method will raise an `ImportError` and stop execution immediately at the problematic row. This is useful for quickly identifying the first issue in a dataset.
SOURCE: https://github.com/django-import-export/django-import-export/blob/main/docs/advanced_usage.rst#_snippet_10

LANGUAGE: Python
CODE:
```
rows = [
    (1, 'Lord of the Rings', '1996-01-01'),
    (2, 'The Hobbit', '1996-01-02x'),
]
dataset = tablib.Dataset(*rows, headers=['id', 'name', 'published'])
resource = BookResource()
self.resource.import_data(self.dataset, raise_errors=True)
```

----------------------------------------

TITLE: Connecting to Import-Export Signals (Python)
DESCRIPTION: Demonstrates how to connect to the `post_import` and `post_export` signals provided by django-import-export using Django's `@receiver` decorator. These signals allow custom logic to be executed after an import or export operation completes.
SOURCE: https://github.com/django-import-export/django-import-export/blob/main/docs/advanced_usage.rst#_snippet_37

LANGUAGE: Python
CODE:
```
from django.dispatch import receiver
from import_export.signals import post_import, post_export

@receiver(post_import, dispatch_uid='balabala...')
def _post_import(model, **kwargs):
    # model is the actual model instance which after import
    pass

@receiver(post_export, dispatch_uid='balabala...')
def _post_export(model, **kwargs):
    # model is the actual model instance which after export
    pass
```

----------------------------------------

TITLE: Setting Field Order with import_order and export_order (Python)
DESCRIPTION: Illustrates how to define specific ordering for fields during import using `import_order` and during export using `export_order` within the `Meta` class. These options take precedence over the `fields` declaration for ordering.
SOURCE: https://github.com/django-import-export/django-import-export/blob/main/docs/advanced_usage.rst#_snippet_2

LANGUAGE: Python
CODE:
```
class BookResource(resources.ModelResource):

    class Meta:
        model = Book
        fields = ('id', 'name', 'author', 'price',)
        import_order = ('id', 'price',)
        export_order = ('id', 'price', 'author', 'name')
```

----------------------------------------

TITLE: Importing Data with Generic Errors (Raise True) - Python
DESCRIPTION: This snippet illustrates importing data where a generic error might occur, such as attempting to save an invalid value to a model field (e.g., 'x' to a numeric field). With `raise_errors=True`, the import process will stop at the first row encountering such an error, raising an `ImportError` that includes the row number and the exception type. This helps pinpoint the initial generic error.
SOURCE: https://github.com/django-import-export/django-import-export/blob/main/docs/advanced_usage.rst#_snippet_12

LANGUAGE: Python
CODE:
```
rows = [
    (1, 'Lord of the Rings', '999'),
    (2, 'The Hobbit', 'x'),
]
dataset = tablib.Dataset(*rows, headers=['id', 'name', 'price'])
resource = BookResource()
result = resource.import_data(
    dataset,
    raise_errors=True
)
```

----------------------------------------

TITLE: Define Custom Export Form (Python)
DESCRIPTION: Defines a custom form CustomExportForm that extends ExportForm and AuthorFormMixin. It includes an author field using forms.ModelChoiceField to allow selecting an author from a queryset of all Author objects, making it a required field for filtering exports.
SOURCE: https://github.com/django-import-export/django-import-export/blob/main/docs/admin_integration.rst#_snippet_11

LANGUAGE: Python
CODE:
```
class CustomExportForm(AuthorFormMixin, ExportForm):
    """Customized ExportForm, with author field required."""
    author = forms.ModelChoiceField(
        queryset=Author.objects.all(),
        required=True)
```

----------------------------------------

TITLE: Enabling Natural Keys for All Foreign Keys in Django Import Export Resource Meta
DESCRIPTION: Demonstrates how to enable natural foreign key lookups for all applicable fields within a ModelResource by setting use_natural_foreign_keys = True in the Meta class.
SOURCE: https://github.com/django-import-export/django-import-export/blob/main/docs/advanced_usage.rst#_snippet_25

LANGUAGE: Python
CODE:
```
    # All widgets with foreign key functions use them.
    class BookResource(resources.ModelResource):

        class Meta:
            model = Book
            use_natural_foreign_keys = True
```

----------------------------------------

TITLE: Enabling Natural Keys for Specific Field in Django Import Export Resource
DESCRIPTION: Shows how to configure a specific field (author) in a ModelResource to use natural foreign keys by passing use_natural_foreign_keys=True to its ForeignKeyWidget.
SOURCE: https://github.com/django-import-export/django-import-export/blob/main/docs/advanced_usage.rst#_snippet_24

LANGUAGE: Python
CODE:
```
    # Only the author field uses natural foreign keys.
    class BookResource(resources.ModelResource):

        author = Field(
            column_name = "author",
            attribute = "author",
            widget = ForeignKeyWidget(Author, use_natural_foreign_keys=True)
        )

        class Meta:
            model = Book
```

----------------------------------------

TITLE: Handling Double Save in Django Import Export Signals (Python)
DESCRIPTION: Provides a workaround for the double-save issue when using post-save signals with the django-import-export Admin interface. It involves setting a temporary 'dry_run' flag on the instance during the 'confirm' step and checking this flag in the signal receiver to execute logic only during the final 'import' step.
SOURCE: https://github.com/django-import-export/django-import-export/blob/main/docs/faq.rst#_snippet_0

LANGUAGE: Python
CODE:
```
class BookResource(resources.ModelResource):

    def before_save_instance(self, instance, row, **kwargs):
        # during 'confirm' step, dry_run is True
        instance.dry_run = kwargs.get("dry_run", False)

    class Meta:
        model = Book
        fields = ('id', 'name')

@receiver(post_save, sender=Book)
def my_callback(sender, **kwargs):
    instance = kwargs["instance"]
    if getattr(instance, "dry_run"):
        # no-op if this is the 'confirm' step
        return
    else:
        # your custom logic here
        # this will be executed only on the 'import' step
        pass
```

----------------------------------------

TITLE: Usage of Django Import Command (Bash)
DESCRIPTION: Provides the general command line syntax for using the Django import-export 'import' management command. It shows required arguments for resource and file, and optional flags for format, encoding, dry-run, and raising errors.
SOURCE: https://github.com/django-import-export/django-import-export/blob/main/docs/management_commands.rst#_snippet_3

LANGUAGE: bash
CODE:
```
python manage.py import <resource> <import_file_name> [--format FORMAT] [--encoding ENCODING] [--dry-run] [--raise-errors]
```

----------------------------------------

TITLE: Enabling Admin Action Export for Django Model
DESCRIPTION: This Python snippet defines a Django Admin class `BookAdmin` that inherits from `ImportExportModelAdmin` and `ExportActionMixin`. Inheriting `ExportActionMixin` adds the functionality to select multiple items in the Admin list view and export them via an Admin action.
SOURCE: https://github.com/django-import-export/django-import-export/blob/main/docs/admin_integration.rst#_snippet_2

LANGUAGE: Python
CODE:
```
class BookAdmin(ImportExportModelAdmin, ExportActionMixin):
  # additional config can be supplied if required
  pass
```

----------------------------------------

TITLE: Configure Import Behavior (Skip/Report)
DESCRIPTION: Demonstrates how to configure the import process within a ModelResource's Meta class to skip unchanged records and control whether skipped records are reported in the Admin UI preview.
SOURCE: https://github.com/django-import-export/django-import-export/blob/main/docs/advanced_usage.rst#_snippet_31

LANGUAGE: Python
CODE:
```
class BookResource(resources.ModelResource):

        class Meta:
            model = Book
            skip_unchanged = True
            report_skipped = False
            fields = ('id', 'name', 'price',)
```

----------------------------------------

TITLE: Configure Custom ModelAdmin for Export (Python)
DESCRIPTION: Defines a custom ModelAdmin class, CustomBookAdmin, for export customization. This example inherits from ImportMixin and ImportExportModelAdmin. It specifies the EBookResource and assigns the CustomExportForm to the export_form_class attribute. Note: This appears to be a separate example or extension from the import customization, registering a different model (Book) later.
SOURCE: https://github.com/django-import-export/django-import-export/blob/main/docs/admin_integration.rst#_snippet_12

LANGUAGE: Python
CODE:
```
class CustomBookAdmin(ImportMixin, ImportExportModelAdmin):
    resource_classes = [EBookResource]
    export_form_class = CustomExportForm
```

----------------------------------------

TITLE: Prepare Import Data Keyword Arguments (Python)
DESCRIPTION: Adds the get_import_data_kwargs method to CustomBookAdmin. This method prepares keyword arguments that will be passed to the import_data method. It retrieves the selected author from the import form's cleaned data and adds it to the keyword arguments dictionary.
SOURCE: https://github.com/django-import-export/django-import-export/blob/main/docs/admin_integration.rst#_snippet_8

LANGUAGE: Python
CODE:
```
def get_import_data_kwargs(self, request, *args, **kwargs):
    """
    Prepare kwargs for import_data.
    """
    form = kwargs.get("form", None)
    if form and hasattr(form, "cleaned_data"):
        kwargs.update({"author": form.cleaned_data.get("author", None)})
    return kwargs
```

----------------------------------------

TITLE: Prepare Export Resource Keyword Arguments (Python)
DESCRIPTION: Adds the get_export_resource_kwargs method to the export CustomBookAdmin. This method prepares keyword arguments that will be passed to the Resource constructor during export. It retrieves the selected author's ID from the export form's cleaned data and adds it to the keyword arguments dictionary as author_id.
SOURCE: https://github.com/django-import-export/django-import-export/blob/main/docs/admin_integration.rst#_snippet_13

LANGUAGE: Python
CODE:
```
def get_export_resource_kwargs(self, request, **kwargs):
    export_form = kwargs.get("export_form")
    if export_form:
        kwargs.update(author_id=export_form.cleaned_data["author"].id)
    return kwargs
```

----------------------------------------

TITLE: Override Widget Format in Django Import Export Field
DESCRIPTION: Demonstrates how to explicitly declare a field in a Django Import Export Resource and override its default widget parameters, such as the date format for a DateWidget, which applies to both import and export.
SOURCE: https://github.com/django-import-export/django-import-export/blob/main/docs/advanced_usage.rst#_snippet_6

LANGUAGE: Python
CODE:
```
class BookResource(resources.ModelResource):
    published = Field(attribute='published', column_name='published_date',
        widget=DateWidget(format='%d.%m.%Y'))

    class Meta:
        model = Book
```

----------------------------------------

TITLE: Override Widget Parameters via Meta Widgets Dict
DESCRIPTION: Shows an alternative method to override widget parameters for a field by using the 'widgets' dictionary within the Resource's Meta class. This allows customizing widget initialization without explicitly declaring the field.
SOURCE: https://github.com/django-import-export/django-import-export/blob/main/docs/advanced_usage.rst#_snippet_7

LANGUAGE: Python
CODE:
```
class BookResource(resources.ModelResource):

    class Meta:
        model = Book
        widgets = {
            'published': {'format': '%d.%m.%Y'},
        }
```

----------------------------------------

TITLE: Set Instance Attribute After Init (Python)
DESCRIPTION: Adds the after_init_instance method to CustomBookAdmin. This method is called after an instance object is initialized during the import process. It checks if the author key exists in the provided keyword arguments (passed from get_import_data_kwargs) and, if so, sets the instance's author attribute to the selected author object.
SOURCE: https://github.com/django-import-export/django-import-export/blob/main/docs/admin_integration.rst#_snippet_9

LANGUAGE: Python
CODE:
```
def after_init_instance(self, instance, new, row, **kwargs):
    if "author" in kwargs:
        instance.author = kwargs["author"]
```

----------------------------------------

TITLE: Export Data Using Custom Resource to XLSX (Bash)
DESCRIPTION: Example showing how to use the Django import-export 'export' command with a custom resource class ('mymodule.resources.MyResource') to export data into an XLSX file format.
SOURCE: https://github.com/django-import-export/django-import-export/blob/main/docs/management_commands.rst#_snippet_2

LANGUAGE: bash
CODE:
```
python manage.py export XLSX mymodule.resources.MyResource
```

----------------------------------------

TITLE: Register ModelAdmin for Export (Python)
DESCRIPTION: Registers the Book model with the customized CustomBookAdmin class (configured for export) in the Django admin site. This makes the custom export functionality, including author filtering, available for the Book model.
SOURCE: https://github.com/django-import-export/django-import-export/blob/main/docs/admin_integration.rst#_snippet_15

LANGUAGE: Python
CODE:
```
admin.site.register(Book, CustomBookAdmin)
```

----------------------------------------

TITLE: Define custom import permission for a model
DESCRIPTION: Demonstrates how to create a custom Django permission ('import_book') for a specific model (Book) to control access to the import action when IMPORT_EXPORT_IMPORT_PERMISSION_CODE is set. Requires django.contrib.auth and django.contrib.contenttypes.
SOURCE: https://github.com/django-import-export/django-import-export/blob/main/docs/installation.rst#_snippet_6

LANGUAGE: Python
CODE:
```
from core.models import Book
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

content_type = ContentType.objects.get_for_model(Book)
permission = Permission.objects.create(
  codename="import_book",
  name="Can import book",
  content_type=content_type,
)
```

----------------------------------------

TITLE: Configuring Django Import Export Temporary Storage with S3
DESCRIPTION: This snippet shows how to configure Django Import Export to use a custom temporary storage class, specifically integrating with `django-storages` to use Amazon S3 for temporary file storage during import/export operations. It defines the `IMPORT_EXPORT_TMP_STORAGE_CLASS` setting and configures the `STORAGES` dictionary to include an 'import_export' backend using `storages.backends.s3.S3Storage`.
SOURCE: https://github.com/django-import-export/django-import-export/blob/main/docs/admin_integration.rst#_snippet_1

LANGUAGE: Python
CODE:
```
IMPORT_EXPORT_TMP_STORAGE_CLASS = "import_export.tmp_storages.MediaStorage"

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "import_export": {
        "BACKEND": "storages.backends.s3.S3Storage",
        "OPTIONS": {
            "bucket_name": "<your bucket name>",
            "region_name": "<your region>",
            "access_key": "<your key>",
            "secret_key": "<your secret>"
        }
    }
}
```

----------------------------------------

TITLE: Instantiating Django Import Export Resource with Dynamic Value
DESCRIPTION: Shows how to create an instance of the custom BookResource, passing the required dynamic value (publisher_id) to its constructor.
SOURCE: https://github.com/django-import-export/django-import-export/blob/main/docs/advanced_usage.rst#_snippet_22

LANGUAGE: Python
CODE:
```
    >>> resource = BookResource(publisher_id=1)
```

----------------------------------------

TITLE: Implementing Custom ForeignKeyWidget for Dynamic Lookup in Django Import Export
DESCRIPTION: Provides the implementation of a custom ForeignKeyWidget subclass that accepts a dynamic value (publisher_id) during initialization and uses it to filter the queryset in get_queryset.
SOURCE: https://github.com/django-import-export/django-import-export/blob/main/docs/advanced_usage.rst#_snippet_21

LANGUAGE: Python
CODE:
```
    class AuthorForeignKeyWidget(ForeignKeyWidget):
        model = Author
        field = 'name'

        def __init__(self, publisher_id, **kwargs):
            super().__init__(self.model, field=self.field, **kwargs)
            self.publisher_id = publisher_id

        def get_queryset(self, value, row, *args, **kwargs):
            return self.model.objects.filter(publisher_id=self.publisher_id)
```

----------------------------------------

TITLE: Modify XLSX Export Output (get_export_data)
DESCRIPTION: Explains how to override the get_export_data method in an Admin class or Resource to intercept and modify the generated XLSX data blob using the openpyxl library before it is returned.
SOURCE: https://github.com/django-import-export/django-import-export/blob/main/docs/advanced_usage.rst#_snippet_36

LANGUAGE: Python
CODE:
```
def get_export_data(self, file_format, request, queryset, **kwargs):
        blob = super().get_export_data(file_format, request, queryset, **kwargs)
        workbook_data = BytesIO(blob)
        workbook_data.seek(0)
        wb = openpyxl.load_workbook(workbook_data)
        # modify workbook as required
        output = BytesIO()
        wb.save(output)
```

----------------------------------------

TITLE: Accessing Full Instance Data After Import with store_instance
DESCRIPTION: Demonstrates how to access the full Django model instance object for each row processed during import. This requires setting `store_instance = True` in the Resource's Meta class. The example shows accessing the instance's primary key.
SOURCE: https://github.com/django-import-export/django-import-export/blob/main/docs/advanced_usage.rst#_snippet_30

LANGUAGE: Python
CODE:
```
class BookResourceWithStoreInstance(resources.ModelResource):
    class Meta:
        model = Book
        store_instance = True

rows = [
    (1, 'Lord of the Rings'),
]
dataset = tablib.Dataset(*rows, headers=['id', 'name'])
resource = BookResourceWithStoreInstance()
result = resource.import_data(dataset)

for row_result in result:
    print(row_result.instance.pk)
```

----------------------------------------

TITLE: Configure Default Import/Export Formats (Python)
DESCRIPTION: Sets the default list of allowed file formats for both import and export operations globally in Django settings. This example restricts formats to only XLSX.
SOURCE: https://github.com/django-import-export/django-import-export/blob/main/docs/installation.rst#_snippet_7

LANGUAGE: python
CODE:
```
# settings.py
from import_export.formats.base_formats import XLSX
IMPORT_EXPORT_FORMATS = [XLSX]
```

----------------------------------------

TITLE: Define Custom Import Forms (Python)
DESCRIPTION: Defines custom forms CustomImportForm and CustomConfirmImportForm that extend the base import forms. These forms include an additional author field using forms.ModelChoiceField to allow selecting an author from a queryset of all Author objects, making it a required field.
SOURCE: https://github.com/django-import-export/django-import-export/blob/main/docs/admin_integration.rst#_snippet_5

LANGUAGE: Python
CODE:
```
class CustomImportForm(ImportForm):
    author = forms.ModelChoiceField(
        queryset=Author.objects.all(),
        required=True)

class CustomConfirmImportForm(ConfirmImportForm):
    author = forms.ModelChoiceField(
        queryset=Author.objects.all(),
        required=True)
```

----------------------------------------

TITLE: Configure Custom ModelAdmin for Import (Python)
DESCRIPTION: Defines a custom ModelAdmin class, CustomBookAdmin, that inherits from ImportMixin and admin.ModelAdmin. It specifies the BookResource to be used and assigns the previously defined CustomImportForm and CustomConfirmImportForm to the import_form_class and confirm_form_class attributes, respectively.
SOURCE: https://github.com/django-import-export/django-import-export/blob/main/docs/admin_integration.rst#_snippet_6

LANGUAGE: Python
CODE:
```
class CustomBookAdmin(ImportMixin, admin.ModelAdmin):
    resource_classes = [BookResource]
    import_form_class = CustomImportForm
    confirm_form_class = CustomConfirmImportForm
```

----------------------------------------

TITLE: Configure Django Logging Settings for Import Export - Python
DESCRIPTION: This dictionary configures the standard Python logging system within a Django application. It sets up a console handler and defines loggers for 'django.db.backends' and 'import_export', specifying their respective log levels and handlers.
SOURCE: https://github.com/django-import-export/django-import-export/blob/main/docs/installation.rst#_snippet_11

LANGUAGE: Python
CODE:
```
LOGGING = {
    "version" 1,
    "handlers": {
        "console": {"level": "DEBUG", "class": "logging.StreamHandler"}
    },
    "loggers": {
        "django.db.backends": {"level": "INFO", "handlers": ["console"]},
        "import_export": {
            "handlers": ["console"],
            "level": "INFO"
        }
    }
}
```

----------------------------------------

TITLE: Updated Widget.render method signature (v4.2)
DESCRIPTION: Shows the updated method signature for the Widget.render method in v4.2, which now includes the **kwargs parameter. Subclasses overriding this method should update their signature to accommodate changes in rendering for spreadsheet formats.
SOURCE: https://github.com/django-import-export/django-import-export/blob/main/docs/release_notes.rst#_snippet_1

LANGUAGE: Python
CODE:
```
Widget.render(self, value, obj=None, **kwargs)
```

----------------------------------------

TITLE: Run Django Import Export Example App (Shell)
DESCRIPTION: Provides the sequence of shell commands required to set up and run the example Django application included with the django-import-export library. This includes changing directory, applying migrations, creating a superuser, loading initial data, and starting the development server.
SOURCE: https://github.com/django-import-export/django-import-export/blob/main/docs/installation.rst#_snippet_10

LANGUAGE: shell
CODE:
```
cd tests
./manage.py makemigrations
./manage.py migrate
./manage.py createsuperuser
./manage.py loaddata author.json category.json book.json
./manage.py runserver
```

----------------------------------------

TITLE: Handling Dynamic import_id_fields by Adding Header in before_import
DESCRIPTION: Correctly handles a dynamic field used for identification by adding its header to the dataset in the `before_import` method before processing rows. The field value is then generated per row in `before_import_row`.
SOURCE: https://github.com/django-import-export/django-import-export/blob/main/docs/advanced_usage.rst#_snippet_28

LANGUAGE: Python
CODE:
```
class BookResource(resources.ModelResource):

    def before_import(self, dataset, **kwargs):
        # mimic a 'dynamic field' - i.e. append field which exists on
        # Book model, but not in dataset
        dataset.headers.append("hash_id")
        super().before_import(dataset, **kwargs)

    def before_import_row(self, row, **kwargs):
        row["hash_id"] = hashlib.sha256(row["name"].encode()).hexdigest()

    class Meta:
        model = Book
        # A 'dynamic field' - i.e. is used to identify existing rows
        # but is not present in the dataset
        import_id_fields = ("hash_id",)
```

----------------------------------------

TITLE: Run collectstatic for import-export admin integration
DESCRIPTION: Collects static files for the 'import_export' app, necessary for its integration into the Django admin interface.
SOURCE: https://github.com/django-import-export/django-import-export/blob/main/docs/installation.rst#_snippet_5

LANGUAGE: Shell
CODE:
```
$ python manage.py collectstatic
```

----------------------------------------

TITLE: Restore Detailed Import Error Messages in Django Admin
DESCRIPTION: Illustrates how to restore the detailed import error message format (including row and traceback) by setting the `import_error_display` attribute on the Admin class.
SOURCE: https://github.com/django-import-export/django-import-export/blob/main/docs/release_notes.rst#_snippet_7

LANGUAGE: Python
CODE:
```
class BookAdmin(ImportExportModelAdmin):
  import_error_display = ("message", "row", "traceback")
```

----------------------------------------

TITLE: Accessing Instance Summary Data After Import
DESCRIPTION: Shows how to iterate through the results of an import operation and access summary information for each processed row, specifically the object's primary key (`object_id`) and its string representation (`object_repr`).
SOURCE: https://github.com/django-import-export/django-import-export/blob/main/docs/advanced_usage.rst#_snippet_29

LANGUAGE: Python
CODE:
```
rows = [
    (1, 'Lord of the Rings'),
]
dataset = tablib.Dataset(*rows, headers=['id', 'name'])
resource = BookResource()
result = resource.import_data(dataset)

for row_result in result:
    print("%d: %s" % (row_result.object_id, row_result.object_repr))
```

----------------------------------------

TITLE: Including Explicitly Declared Field in fields Option (Python)
DESCRIPTION: Shows that when an explicit field is declared on the `ModelResource` class (like `published_field`), it must also be included in the `fields` tuple within the `Meta` class if the `fields` option is used to control which fields are processed.
SOURCE: https://github.com/django-import-export/django-import-export/blob/main/docs/advanced_usage.rst#_snippet_5

LANGUAGE: Python
CODE:
```
class BookResource(ModelResource):
    published_field = Field(attribute='published', column_name='published_date')

    class Meta:
        fields = ("published_field",)
        model = Book
```

----------------------------------------

TITLE: Configure Allowed Export Formats (Python)
DESCRIPTION: Defines the list of file formats specifically allowed for export operations in Django settings. This overrides the global IMPORT_EXPORT_FORMATS for exports.
SOURCE: https://github.com/django-import-export/django-import-export/blob/main/docs/installation.rst#_snippet_9

LANGUAGE: python
CODE:
```
# settings.py
from import_export.formats.base_formats import XLSX
EXPORT_FORMATS = [XLSX]
```

----------------------------------------

TITLE: Configure Allowed Import Formats (Python)
DESCRIPTION: Defines the list of file formats specifically allowed for import operations in Django settings. This overrides the global IMPORT_EXPORT_FORMATS for imports.
SOURCE: https://github.com/django-import-export/django-import-export/blob/main/docs/installation.rst#_snippet_8

LANGUAGE: python
CODE:
```
# settings.py
from import_export.formats.base_formats import CSV, XLSX
IMPORT_FORMATS = [CSV, XLSX]
```

----------------------------------------

TITLE: Defining Django Model and Manager for Natural Keys in Import Export
DESCRIPTION: Illustrates the necessary Django model (Author) and manager (AuthorManager) setup to support natural key functionality, including get_by_natural_key and natural_key methods.
SOURCE: https://github.com/django-import-export/django-import-export/blob/main/docs/advanced_usage.rst#_snippet_23

LANGUAGE: Python
CODE:
```
    from import_export.fields import Field
    from import_export.widgets import ForeignKeyWidget

    class AuthorManager(models.Manager):

        def get_by_natural_key(self, name):
            return self.get(name=name)

    class Author(models.Model):

        objects = AuthorManager()

        name = models.CharField(max_length=100)
        birthday = models.DateTimeField(auto_now_add=True)

        def natural_key(self):
            return (self.name,)
```

----------------------------------------

TITLE: Updated Resource.export_resource method signature (v4.2)
DESCRIPTION: Shows the updated method signature for the Resource.export_resource method in v4.2, which now includes the **kwargs parameter. This parameter is used to pass context such as the list of selected fields.
SOURCE: https://github.com/django-import-export/django-import-export/blob/main/docs/release_notes.rst#_snippet_4

LANGUAGE: Python
CODE:
```
Resource.export_resource(self, instance, selected_fields=None, **kwargs)
```

----------------------------------------

TITLE: Register ModelAdmin for Import (Python)
DESCRIPTION: Registers the EBook model with the customized CustomBookAdmin class in the Django admin site. This makes the custom import functionality available for the EBook model.
SOURCE: https://github.com/django-import-export/django-import-export/blob/main/docs/admin_integration.rst#_snippet_10

LANGUAGE: Python
CODE:
```
admin.site.register(EBook, CustomBookAdmin)
```

----------------------------------------

TITLE: Field export - New Signature
DESCRIPTION: The updated signature for the `export` method in `Field` renames the instance parameter from `obj` to `instance`.
SOURCE: https://github.com/django-import-export/django-import-export/blob/main/docs/release_notes.rst#_snippet_61

LANGUAGE: python
CODE:
```
export(self, instance)
```

----------------------------------------

TITLE: BaseImportExportMixin export_resource - New Signature
DESCRIPTION: The updated signature for the `export_resource` method in `BaseImportExportMixin` renames the instance parameter from `obj` to `instance` and adds an optional `fields` keyword argument.
SOURCE: https://github.com/django-import-export/django-import-export/blob/main/docs/release_notes.rst#_snippet_31

LANGUAGE: python
CODE:
```
export_resource(self, instance, fields=None)
```

----------------------------------------

TITLE: Pass Data to Confirm Form Initial (Python)
DESCRIPTION: Overrides the get_confirm_form_initial method in CustomBookAdmin. This method is used to pass initial data to the confirmation form. It retrieves the selected author's ID from the cleaned data of the import form and includes it in the initial dictionary for the confirm form.
SOURCE: https://github.com/django-import-export/django-import-export/blob/main/docs/admin_integration.rst#_snippet_7

LANGUAGE: Python
CODE:
```
def get_confirm_form_initial(self, request, import_form):
    initial = super().get_confirm_form_initial(request, import_form)

    # Pass on the `author` value from the import form to
    # the confirm form (if provided)
    if import_form:
        initial['author'] = import_form.cleaned_data['author'].id
    return initial
```

----------------------------------------

TITLE: Disabling Change Form Export Button in Django Admin
DESCRIPTION: This Python snippet defines a Django Admin class `CategoryAdmin` that inherits from `ExportActionModelAdmin`. It sets the `show_change_form_export` attribute to `False` to disable the export button that would otherwise appear on the individual model instance change form.
SOURCE: https://github.com/django-import-export/django-import-export/blob/main/docs/admin_integration.rst#_snippet_4

LANGUAGE: Python
CODE:
```
class CategoryAdmin(ExportActionModelAdmin):
    show_change_form_export = False
```

----------------------------------------

TITLE: BaseImportMixin choose_import_resource_class - New Signature
DESCRIPTION: The updated signature for the `choose_import_resource_class` method in `BaseImportMixin` adds a `request` parameter.
SOURCE: https://github.com/django-import-export/django-import-export/blob/main/docs/release_notes.rst#_snippet_45

LANGUAGE: python
CODE:
```
choose_import_resource_class(self, form, request)
```

----------------------------------------

TITLE: Install django-import-export from Git repository
DESCRIPTION: Installs the development version directly from the Git repository using pip.
SOURCE: https://github.com/django-import-export/django-import-export/blob/main/docs/installation.rst#_snippet_3

LANGUAGE: Shell
CODE:
```
pip install -e git+https://github.com/django-import-export/django-import-export.git#egg=django-import-export
```

----------------------------------------

TITLE: Enable SQL Debug Logging (Python)
DESCRIPTION: Configures Django's `LOGGING` setting in `settings.py` to enable console output for SQL queries executed by the database backend at DEBUG level.
SOURCE: https://github.com/django-import-export/django-import-export/blob/main/docs/testing.rst#_snippet_4

LANGUAGE: python
CODE:
```
LOGGING = {
    "version": 1,
    "handlers": {"console": {"class": "logging.StreamHandler"}},
    "root": {
        "handlers": ["console"],
    },
    "loggers": {
        "django.db.backends": {"level": "DEBUG", "handlers": ["console"]},
    }
}
```

----------------------------------------

TITLE: Modify Widget Render Return Type in Django Import Export
DESCRIPTION: Illustrates how to configure a widget to return a native Python type instead of a string during export by setting the 'coerce_to_string' parameter to False. Note that Admin export might override this for certain file formats.
SOURCE: https://github.com/django-import-export/django-import-export/blob/main/docs/advanced_usage.rst#_snippet_8

LANGUAGE: Python
CODE:
```
class BookResource(resources.ModelResource):
    published = Field(widget=DateWidget(coerce_to_string=False))

    class Meta:
        model = Book
```

----------------------------------------

TITLE: before_export Method Parameter Change - Django Import Export Resource - Python
DESCRIPTION: Documents parameter changes for the `before_export` method in `import_export.resources.Resource`. The unused `*args` parameter list has been removed. This change standardizes method arguments.
SOURCE: https://github.com/django-import-export/django-import-export/blob/main/docs/release_notes.rst#_snippet_23

LANGUAGE: python
CODE:
```
before_export(self, queryset, *args, **kwargs)
```

LANGUAGE: python
CODE:
```
before_export(self, queryset, **kwargs)
```

----------------------------------------

TITLE: Override Model full_clean for Custom Validation (Django)
DESCRIPTION: Demonstrates how to override the `full_clean` method on a Django model to add custom validation logic at both the instance and field levels before saving.
SOURCE: https://github.com/django-import-export/django-import-export/blob/main/docs/advanced_usage.rst#_snippet_15

LANGUAGE: Python
CODE:
```
class Book(models.Model):

    def full_clean(self, exclude=None, validate_unique=True):
        super().full_clean(exclude, validate_unique)

        # non field specific validation
        if self.published < date(1900, 1, 1):
            raise ValidationError("book is out of print")

        # field specific validation
        if self.name == "Ulysses":
            raise ValidationError({"name": "book has been banned"})
```

----------------------------------------

TITLE: BaseImportExportMixin get_export_headers - New Signature
DESCRIPTION: The updated signature for the `get_export_headers` method in `BaseImportExportMixin` adds an optional `fields` keyword argument.
SOURCE: https://github.com/django-import-export/django-import-export/blob/main/docs/release_notes.rst#_snippet_35

LANGUAGE: python
CODE:
```
get_export_headers(self, fields=None)
```

----------------------------------------

TITLE: Generating Dynamic import_id_fields in before_import_row (Requires Header)
DESCRIPTION: Demonstrates generating a value for a field ('hash_id') in the `before_import_row` method. This field is intended for use as an `import_id_fields` identifier, but this specific implementation will raise an error if 'hash_id' is not present in the dataset headers.
SOURCE: https://github.com/django-import-export/django-import-export/blob/main/docs/advanced_usage.rst#_snippet_27

LANGUAGE: Python
CODE:
```
class BookResource(resources.ModelResource):

    def before_import_row(self, row, **kwargs):
        # generate a value for an existing field, based on another field
        row["hash_id"] = hashlib.sha256(row["name"].encode()).hexdigest()

    class Meta:
        model = Book
        # A 'dynamic field' - i.e. is used to identify existing rows
        # but is not present in the dataset
        import_id_fields = ("hash_id",)
```
