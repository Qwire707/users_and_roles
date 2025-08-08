from django.template.defaulttags import comment

import django_setup

from blog.models import Post, Comment

# Post.objects.create(
#     title="My first post",
#     text="Some text for post #1"
# )

post1 = Post.objects.get(id=1)
Comment.objects.create(
    text="Uhuuuu",
    author="Author",
    post=post1
)

post1 = Post.objects.get(id=1)
comments = post1.posts.all()
print(comments)

post1.title = "Updated title"
post1.save()

post1.delete()

