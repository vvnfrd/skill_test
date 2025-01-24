from rest_framework.test import APITestCase
from rest_framework import status

from users.models import User

def create_supplier(client):
    data = {
        'name': 'testname',
        'level': 0,
        'email': 'test@gmail.com',
        'country': 'Russia',
        'city': 'Novosibirsk',
        'street': 'novosibirskaya',
        'house': '54',
        'debt': '0.00'}

    response = client.post(
        '/supplier/create/',
        data=data
    )

    return {'response': response, 'data': data}

def create_product(client):

    data = {'name': 'testname', 'model': 'testmodel'}
    response = client.post('/products/', data=data)

    return {'response': response, 'data': data}

class SupplierTestCase(APITestCase):

    def setUp(self) -> None:
        user = User.objects.create(
            email="user@gmail.com",
            first_name="user",
            last_name="user",
            job_title="user",
            password="user"
        )
        self.client.force_authenticate(user)


    def test_create_supplier(self):


        created_suppler = create_supplier(self.client)
        response = created_suppler['response']
        result = created_suppler['response'].json()
        data = created_suppler['data']

        data['created_at'] = result['created_at']
        data['supplier_of'] = result['supplier_of']
        data['id'] = result['id']
        data['products'] = result['products']

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(result, data)

    def test_list_supplier(self):
        response = self.client.get(
            '/supplier/'
        )
        result = response.json()['results']

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(result, [])

    def test_retrieve_supplier(self):

        created_suppler = create_supplier(self.client)
        result = created_suppler['response'].json()
        data = created_suppler['data']

        id = result['id']
        response_get = self.client.get(
            f'/supplier/{id}/'
        )

        data['created_at'] = result['created_at']
        data['supplier_of'] = result['supplier_of']
        data['id'] = result['id']
        data['products'] = result['products']

        self.assertEqual(response_get.status_code, status.HTTP_200_OK)
        self.assertEqual(result, data)

    def test_update_supplier(self):

        created_suppler = create_supplier(self.client)
        response_post = created_suppler['response']
        supplier_data = created_suppler['data']
        result = response_post.json()
        id = result['id']

        patch_data = {'city': 'Moscow'}
        response_patch = self.client.patch(
            f'/supplier/update/{id}/', data=patch_data
        )
        result = response_patch.json()

        supplier_data['city'] = patch_data['city']
        supplier_data['created_at'] = result['created_at']
        supplier_data['supplier_of'] = result['supplier_of']
        supplier_data['id'] = result['id']
        supplier_data['products'] = result['products']
        self.assertEqual(response_patch.status_code, status.HTTP_200_OK)
        self.assertEqual(result, supplier_data)

        patch_data = {'debt': '1000.00'}
        response_patch = self.client.patch(
            f'/supplier/update/{id}/', data=patch_data
        )
        self.assertEqual(response_patch.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response_patch.json()['debt'],
                         ['Нельзя обновлять параметр задолженности перед поставщиком'])

    def test_destroy_supplier(self):

        created_suppler = create_supplier(self.client)
        response_post = created_suppler['response']
        id = response_post.json()['id']

        response_destroy = self.client.delete(f'/supplier/destroy/{id}/',)

        self.assertEqual(response_destroy.status_code, status.HTTP_204_NO_CONTENT)


class ProductTestCase(APITestCase):

    def setUp(self) -> None:
        user = User.objects.create(
            email="user@gmail.com",
            first_name="user",
            last_name="user",
            job_title="user",
            password="user"
        )
        self.client.force_authenticate(user)

    def test_create_product(self):

        created_product = create_product(self.client)
        response = created_product['response']
        result = created_product['response'].json()
        data = created_product['data']

        data['id'] = result['id']
        data['created_at'] = result['created_at']

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(result, data)

    def test_list_product(self):
        response = self.client.get(
            '/products/'
        )
        result = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(result, [])

    def test_retrieve_product(self):

        created_product = create_product(self.client)
        result = created_product['response'].json()
        data = created_product['data']

        id = result['id']
        response_get = self.client.get(
            f'/products/{id}/'
        )

        data['created_at'] = result['created_at']
        data['id'] = result['id']

        self.assertEqual(response_get.status_code, status.HTTP_200_OK)
        self.assertEqual(result, data)

    def test_update_product(self):

        created_product = create_product(self.client)
        response_post = created_product['response']
        supplier_data = created_product['data']
        result = response_post.json()
        id = result['id']

        patch_data = {'name': 'testnameupdated'}
        response_patch = self.client.patch(
            f'/products/{id}/', data=patch_data
        )
        result = response_patch.json()

        supplier_data['name'] = patch_data['name']
        supplier_data['created_at'] = result['created_at']
        supplier_data['id'] = result['id']
        self.assertEqual(response_patch.status_code, status.HTTP_200_OK)
        self.assertEqual(result, supplier_data)

    def test_destroy_product(self):

        created_product = create_product(self.client)
        response_post = created_product['response']
        id = response_post.json()['id']

        response_destroy = self.client.delete(f'/products/{id}/',)

        self.assertEqual(response_destroy.status_code, status.HTTP_204_NO_CONTENT)