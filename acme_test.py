#!/usr/bin/env python

import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""

    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        """Test default product weight being 20."""
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)

    def test_product_explode(self):
        """Test  product explode method."""
        test_vectors = ((10, "...fizzle."), (40, "...boom!"),
                        (120, "...BABOOM!!"))

        for idx, tv in enumerate(test_vectors):
            self.assertEqual(
                Product(f'prod{idx}', weight=tv[0]).explode(), tv[1])


class AcmeReportTests(unittest.TestCase):
    """Making sure Acme reports are the tops!"""

    def test_default_num_products(self):
        """Test default num_products being 30."""
        self.assertEqual(len(generate_products()), 30)

    def test_legal_names(self):
        """Test generated product names are legal."""
        prod_names = [prod.name.split() for prod in generate_products()]

        for prod_name in prod_names:
            self.assertIn(prod_name[0], ADJECTIVES)
            self.assertIn(prod_name[1], NOUNS)


if __name__ == '__main__':
    unittest.main()
