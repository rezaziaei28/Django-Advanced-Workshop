# Filtering in PostModelViewSet

I am learning filtering in Django REST Framework and this is what I did in PostModelViewSet.

## Basic filtering

For simple filtering I can use a list of fields:

```python
filterset_fields = ['category', 'author', 'status']
```

This creates exact lookups for each field and I can filter like this:

    /post/?category=1
    /post/?status=true

## Advanced filtering with lookup expressions

I learned that I can also use a dictionary instead of a list and define multiple lookup expressions for each field:

```python
filterset_fields = {
    'category': ['exact', 'in'],
    'author': ['exact', 'in'],
    'status': ['exact', 'in'],
}
```

### What each lookup does

- **exact** — filters for an exact match. Example: `/post/?category=1` returns posts with category id 1.
- **in** — filters for multiple values separated by comma. Example: `/post/?category__in=1,2,3` returns posts that belong to category 1, 2 or 3.

### Why I use both

The `exact` lookup is useful when I want posts from one specific category or one specific author and the `in` lookup is useful when I want posts from multiple categories or multiple authors at the same time.

## Notes

- The `in` lookup expects comma separated values in the URL.
- The default lookup is always `exact` and django-filter adds it automatically if I do not specify any lookup.
- I can also use other lookups like `gte`, `lte`, `contains`, `icontains`, `isnull` and `range` depending on the field type.

## Example requests

    /post/?status=true
    /post/?category=1
    /post/?category__in=1,2,3
    /post/?author__in=5,7
    /post/?category__in=1,2&status=true
```