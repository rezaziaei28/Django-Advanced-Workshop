## Challenges I Faced

### Profile bug in Post API tests

When I was writing tests for the Post API to check if a logged-in user can create a post, I got a MultipleObjectsReturned error. The error said that my query returned more than one Profile and it happened inside my PostSerializer when it was trying to find the author.

After looking at my code I understood the problem. I had a signal in my Profile model that automatically creates a profile for every new user. But in my test setUp I was also creating a profile manually for the user. So the user ended up with two profiles and Profile.objects.get() did not know which one to pick.

To fix this in the test I stopped creating the profile manually and used Profile.objects.get(user=self.user) to get the profile that the signal already created. This fixed the error and now all 13 tests pass and I can check that logged-in users get 201 when creating a post and anonymous users get 403.

## Notes and Things I Learned

### Testing in Django

I started learning testing in Django and I wrote my first test for the blog app. I used SimpleTestCase because my test does not need the database and it only checks if a URL resolves to the right view.

### Difference between TestCase and SimpleTestCase

SimpleTestCase is for tests that do not need a database. It is faster because it does not create a test database. I used it for my URL test because resolving a URL does not need any database access.

TestCase is for tests that need a database. It creates a test database for each test run and destroys it after. It is slower than SimpleTestCase but it is needed when my tests touch models or queries.

So the rule I follow is simple: if my test does not touch the database I use SimpleTestCase and if it does I use TestCase.

### Assertions I Learned

assertEqual checks if two values are equal and if they are not equal the test fails and shows both values so I can see what went wrong. I used it in my URL test like this:

```python
url = reverse('blog:index')
self.assertEqual(resolve(url).func.view_class, IndexView)
```

assertTrue checks if a value is True. assertFalse checks if a value is False. I will use these when I want to check boolean values like is_active or is_verified.

assertIn checks if a value is inside a list, tuple or string. I will use it when I want to check if a user is in a group or if a text contains a specific word.

assertNotIn is the opposite of assertIn and checks if a value is not inside a list, tuple or string.

assertContains checks if an HTTP response contains a specific text. I will use it when I test views and I want to check if a page shows the right content.

assertNotContains is the opposite of assertContains and checks if a response does not contain a text.

assertRedirects checks if a request redirects to a specific URL. I will use it when I test login and logout views or when I test if a user is redirected after creating a post.

assertRaises checks if a specific exception is raised. I will use it when I want to test if my code raises an error in the right situation.

assertGreater checks if the first value is greater than the second one. assertLess checks if the first value is less than the second one.

assertIsNone checks if a value is None. assertIsNotNone checks if a value is not None.

assertIsInstance checks if an object is an instance of a specific class. assertNotIsInstance is the opposite.

I am still learning and I will use these assertions as I write more tests for the project.