from haystack import indexes
from booktest.models import HeroInfo


class HeroInfoIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return HeroInfo

    # BookInfo.objects.all()
    def index_queryset(self, using=None):
        return self.get_model().objects.all()#.filter(isDelete=False)
