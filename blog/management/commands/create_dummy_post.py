from django.core.management.base import BaseCommand
from blog.models import Post
from django.utils import timezone

class Command(BaseCommand):
    help = 'Creates a dummy blog post for demonstration purposes'

    def handle(self, *args, **options):
        post = Post.objects.create(
            name='Demo Post',
            subject='This is a test post',
            body='This is the body content of the demo post. It shows how posts will appear in the blog.',
        )
        self.stdout.write(self.style.SUCCESS(f'Successfully created post: {post.name} (ID: {post.id})'))