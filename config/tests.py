# from rest_framework.test import APITestCase, APIRequestFactory, force_authenticate
# from django.core.files import File
# from collections import OrderedDict
# from .views import HotelViewSet
# from .models import Hotel, Comment, Amenities
# from account.models import User
# from django.contrib.auth import get_user_model

# User = get_user_model()


# class PostTest(APITestCase):

    # def setUp(self):
    #     self.factory = APIRequestFactory()
    #     self.amenities = Amenities.objects.create(amenity_name='cat1')
    #     user = User.objects.create_user(
    #         email='test@gmail.com',
    #         password='1234',
    #         is_active=True,
    #         name='Test',
    #         last_name='User')
        
    #     hotels = [
    #         Hotel(author=user, name='rixos', price=100, description='new hotel', room_count=1, country='kg' ),
    #         # Hotel(author=user, name='rixos1', price='100', description='new hotel', room_count='1', country='kg' ),
    #         # Hotel(author=user, name='rixos2', price='100', description='new hotel', room_count='1', country='kg' ),
    #     ]
    #     Hotel.objects.bulk_create(hotels)


    # def test_list(self):
    #     request = self.factory.get('hotels/')
    #     view = HotelViewSet.as_view({'get': 'list'})
    #     response = view(request)
    #     print(response.data)
        
    #     assert response.status_code == 200


    # def test_retrieve(self):
    #     id = Hotel.objects.all()[0].id
    #     request = self.factory.get( f'hotels/{id}/')
    #     view = HotelViewSet.as_view({'get':'retrieve'})
    #     response = view(request, pk=id)
    #     # print(response.data)

    #     assert response.status_code == 200

    # def test_create(self):
    #     user = User.objects.all()[0]
    #     data = {
    #         'body': 'vhkbl',
    #         'title': 'post4',
    #         'category': 'cat1'
    #     }
    #     request = self.factory.post('posts/', data, format='json')
    #     force_authenticate(request, user=user)
    #     view = PostViewSet.as_view( {'post': 'create'})
    #     response = view(request)
    #     print(response.data)

    #     assert response.status_code == 201
        

    # def test_update(self):
    #     user = User.objects.all()[0]
    #     data = {
    #         'body': 'update body'
    #     }
    #     post = Post.objects.all()[0]
    #     request = self.factory.patch(f'/posts/{post.pk}/', data, format='json')
    #     force_authenticate(request, user=user)
    #     view = PostViewSet.as_view({'patch': 'partial_update'})
    #     response = view(request, pk=post.pk)
    #     print(response.data)

    #     assert Post.objects.get(pk = post.pk).body == data['body']

    # def test_delete(self):
    #     user = User.objects.all()[0]
    #     hotel = Hotel.objects.all()[0]
    #     request = self.factory.delete(f'/hotels/{hotel.id}/')
    #     force_authenticate(request, user)
    #     view = HotelViewSet.as_view({'delete': 'destroy'})
    #     response = view(request, pk=hotel.id)
    #     print(response)

    #     assert response.status_code == 204
    #     assert not Hotel.objects.filter(id=hotel.id).exists()

