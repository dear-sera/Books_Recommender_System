import pandas as pd
from tqdm import tqdm
from api.models.book import Book
from api.serializers.book import BookSerializer
from api.views.predictor import Predictor
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


class BookModelViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    @action(detail=False, methods=["post"])
    def predict(self, request):
        target = request.data["target"]
        print(target)
        predictor = Predictor()
        targetList = predictor.getRecommendation(target)
        queryset = Book.objects.filter(title__in=targetList)
        print(f"{queryset}")
        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=["get"])
    def updateDB(self, request):
        df = pd.read_csv("./data/raw_data_merged.csv")
        bulk_list = [
            Book(
                title=df.loc[i, "title"],
                summary=df.loc[i, "summary"],
                category=df.loc[i, "category"],
                author=df.loc[i, "author"],
                src=df.loc[i, "url"],
            )
            for i in tqdm(df.index)
            if len(Book.objects.filter(title=df.loc[i, "title"])) == 0
        ]
        Book.objects.bulk_create(bulk_list)
        return Response({"str": "success"})
