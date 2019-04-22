from haystack import indexes
from booktest.models import BookInfo


class GoodsInfoIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return BookInfo

    # BookInfo.objects.all()
    def index_queryset(self, using=None):
        return self.get_model().objects.filter(isDelete=False)
