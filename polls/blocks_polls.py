from wagtail.core import blocks

class PollsBlock(blocks.StructBlock):
    question = blocks.CharBlock(required=True)

    class Meta:
        template = 'pages/blog_page.html'
        icon = 'edit'
        label = 'Polls'