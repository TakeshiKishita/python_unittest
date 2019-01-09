import unittest


class TestStringMethods(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 個別のクラス内のテストが実行される前に呼び出される
        pass

    @classmethod
    def tearDownClass(cls):
        # 個別のクラス内のテストが実行された後に呼び出される
        pass

    def setUp(self):
        # テストメソッドの直前に呼び出される
        pass

    def tearDown(self):
        # テストメソッドが実行され、結果が記録された直後に呼び出される
        pass

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

