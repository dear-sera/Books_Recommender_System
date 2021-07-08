from api.models.best import Bestseller
from api.serializers.best import BestsellerSerializer
from api.views.bestseller import Best
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from tqdm import tqdm


class BestsellerModelViewSet(viewsets.ModelViewSet):
    queryset = Bestseller.objects.all()
    serializer_class = BestsellerSerializer

    @action(detail=False, methods=["get"])
    def updateBests(self, request):
        b = Best()
        flags = b.url.keys()
        Bestseller.objects.all().delete()
        for f in flags:
            b.crawling(f)
        titles, authors, urls, images, flags = b.get_values()
        print(flags)
        bulk_list = [
            Bestseller(title=title, author=author, url=url, image=image, flag=flag)
            for title, author, url, image, flag in zip(titles, authors, urls, images, flags)
        ]
        Bestseller.objects.bulk_create(bulk_list)
        return Response({"str": "success"})
