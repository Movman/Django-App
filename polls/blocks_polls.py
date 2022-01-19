
from wagtail.core import blocks
from wagtail.snippets.blocks import SnippetChooserBlock
from .models import Question

class PollsBlock(blocks.StructBlock):
    # v blocku si vyberame s questions...pozivame SnippetChooserBlock (nie Panel)
    poll = SnippetChooserBlock(Question)
    class Meta:
        template = 'polls/snippets/poll_snippet.html'
        icon = 'edit'
        label = 'Poll'