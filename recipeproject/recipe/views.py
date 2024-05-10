from django.contrib.auth.models import User
from django.db.models import Q
from django.http import Http404
from django.shortcuts import render
from rest_framework import status, mixins, generics, viewsets
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from recipe.models import recipe,review
from recipe.serializers import RecipeSerializer,UserSerializer,ReviewSerializer
from rest_framework.views import APIView


# Create your views here.

#
# @api_view(['GET','POST'])
# def create(request):
#
#
#     if (request.method=='GET'):
#         s=recipe.objects.all()
#         stu=RecipeSerializer(s,many=True)
#         return Response(stu.data)
#
#     if(request.method=='POST'):
#         stu=RecipeSerializer(data=request.data)
#         return Response(stu.data,status=status.HTTP_201_CREATED)
#
#     return Response(status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET','PUT','DELETE'])
# def bookdetail(request,pk):
#     try:
#         s=recipe.objects.get(pk=pk)
#     except:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if(request.method=='GET'):
#         stu=RecipeSerializer(s)
#         return Response(stu.data)
#
#
#     elif (request.method=='PUT'):
#         s=RecipeSerializer(s,data=request.data)
#         if s.is_valid():
#             s.save()
#             return Response(s.data,status=status.HTTP_201_CREATED)
#     elif(request.method=='DELETE'):
#         s.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#     return Response(status=status.HTTP_400_BAD_REQUEST)



class Create(mixins.CreateModelMixin,mixins.ListModelMixin,generics.GenericAPIView):
    queryset=recipe.objects.all()
    serializer_class=RecipeSerializer

    def get(self,request):
        return self.list(request)

    def post(self,request):
        return  self.create(request)


class Details(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    # permission_classes = [IsAuthenticated]

    queryset = recipe.objects.all()
    serializer_class = RecipeSerializer

    def get(self,request,pk):
        return self.retrieve(request,pk)

    def put(self,request,pk):
        return self.update(request,pk)

    def delete(self,request,pk):
        return self.destroy(request,pk)



class Register(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class Logout(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        self.request.user.auth_token.delete()
        return Response({'msg':'Logout successfully'},status=status.HTTP_200_OK)



class createrev(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self,request):
        s=review.objects.all()
        stu=ReviewSerializer(s,many=True)
        return Response(stu.data)

    def post(self,request):
        r=ReviewSerializer(data=request.data)
        if (r.is_valid()):
            r.save()
            return Response(r.data,status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class detailrev(APIView):

    # permission_classes = [IsAuthenticated]

    def get_object(self,pk):
        try:
            return recipe.objects.get(pk=pk)
        except:
            raise Http404


    def get(self,request,pk):
        r=self.get_object(pk)
        rev=review.objects.filter(recipe_name=r)
        revdet=ReviewSerializer(rev,many=True)
        return Response(revdet.data)


class Cuisinfilter(APIView):
    def get(self,request):

        query=self.request.query_params.get('Cuisine')
        recipes=recipe.objects.filter(cuisine=query)
        r=RecipeSerializer(recipes,many=True)
        return Response(r.data)



class Mealfilter(APIView):
    def get(self,request):

        query=self.request.query_params.get('Mealtype')
        recipes=recipe.objects.filter(meal_type=query)

        s=RecipeSerializer(recipes,many=True)
        return Response(s.data)



class Ingredientsfilter(APIView):
    def get(self,request):

        query=self.request.query_params.get('Ingredients')
        recipes=recipe.objects.filter(recipe_ingredients=query)

        s=RecipeSerializer(recipes,many=True)
        return Response(s.data)


class Search(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self,request):

        query=self.request.query_params.get('search')
        recipes=recipe.objects.filter(Q(recipe_name__icontains=query) | Q(recipe_ingredients__icontains=query))

        stu=RecipeSerializer(recipes,many=True)

        return Response(stu.data)

