import datetime
from django.db.models.query_utils import Q

from django.test import TestCase
from django.utils import timezone

from .models import Product
from django.urls import reverse



class ProductModelTests(TestCase):

    def test_was_published_recently_with_future_product(self):
        """
        was_published_recently() returns False for products whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_product = Product(pub_date=time)
        self.assertIs(future_product.was_published_recently(), False)
        
def test_was_published_recently_with_old_product(self):
    """
    was_published_recently() returns False for products whose pub_date
    is older than 1 day.
    """
    time = timezone.now() - datetime.timedelta(days=1, seconds=1)
    old_product = Product(pub_date=time)
    self.assertIs(old_product.was_published_recently(), False)

def test_was_published_recently_with_recent_product(self):
    """
    was_published_recently() returns True for products whose pub_date
    is within the last day.
    """
    time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
    recent_product = Product(pub_date=time)
    self.assertIs(recent_product.was_published_recently(), True)
    
def create_product(name, img, desc, price, offer, quantity, days):
    # """
    # Create a product with the given `product_text` and published the
    # given number of `days` offset to now (negative for products published
    # in the past, positive for products that have yet to be published).
    # """
    time = timezone.now() + datetime.timedelta(days=days)
    return Product.objects.create(name=name, img=img, desc=desc, price=price, offer=offer, quantity=quantity,pub_date=time)


class ProductIndexViewTests(TestCase):
    def test_no_products(self):
        """
        If no products exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('products:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_product_list'], [])

    def test_past_product(self):
        # """
        # products with a pub_date in the past are displayed on the
        # index page.
        # """
        product = create_product(name="Past product.", img="Past product.", desc="Past product.", price="Past product.", offer="Past product.",quantity="Past product.", days=-30)
        response = self.client.get(reverse('products:index'))
        self.assertQuerysetEqual(
            response.context['latest_product_list'],
            [product],
        )

    def test_future_product(self):
        """
        products with a pub_date in the future aren't displayed on
        the index page.
        """
        create_product(name="Future product.", img="Future product.", desc="Future product.", price="Future product.", offer="Future product.",quantity="Future product.", days=30)
        response = self.client.get(reverse('products:index'))
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_product_list'], [])

    def test_future_product_and_past_product(self):
        """
        Even if both past and future products exist, only past products
        are displayed.
        """
        product = create_product(name="Past product.",img="Past product.",desc="Past product.", price="Past product.", offer="Past product.",quantity="Past product.", days=-30)
        create_product(name="Future product.", img="Future product.", desc="Future product.", price="Future product.", offer="Future product.",quantity="Future product.",days=30)
        response = self.client.get(reverse('products:index'))
        self.assertQuerysetEqual(
            response.context['latest_product_list'],
            [product],
        )

    def test_two_past_products(self):
        """
        The products index page may display multiple products.
        """
        product1 = create_product(name="Past product 1.", img="Past product 1.",desc="Past product 1.", price="Past product 1.", offer="Past product 1.",quantity="Past product 1.", days=-30)
        product2 = create_product(name="Past product 2.", img="Past product 2.", desc="Past product 2.", price="Past product 2.", offer="Past product 2.", quantity="Past product 2.",days=-5)
        response = self.client.get(reverse('products:index'))
        self.assertQuerysetEqual(
            response.context['latest_product_list'],
            [product2, product1],
        )
        
class ProductDetailViewTests(TestCase):
    def test_future_product(self):
        """
        The detail view of a product with a pub_date in the future
        returns a 404 not found.
        """
        future_product = create_product(name="Future product.", img="Future product.",desc="Future product.", price="Future product.", offer="Future product.",quantity="Future product.", days=5)
        url = reverse('products:detail', args=(future_product.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_product(self):
        """
        The detail view of a product with a pub_date in the past
        displays the product's text.
        """
        past_product = create_product(name="Past product.", img="Past product.",  desc="Past product.", price="Past product.", offer="Past product.", quantity="Past product.",days=-5)
        url = reverse('products:detail', args=(past_product.id,))
        response = self.client.get(url)
        self.assertContains(response, past_product.name, past_product.img,past_product.desc, past_product.price, past_product.offer, past_product.quantity, days=-5)