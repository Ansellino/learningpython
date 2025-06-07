class TestUser(unittest.TestCase):
    # Test Fixture
    def setUp(self):
        self.db = koneksi_ke_db()
        self.dicoding = User(self.db, "dicoding")
 
    def tearDown(self):
        putus_koneksi_db(self.db)
 
    # Test Case 1
    def test_user_default_not_active(self):
        self.assertFalse(self.dicoding.aktif)  # tidak aktif secara default
    # Test Case 2
    def test_user_is_active(self):
        self.dicoding.set_aktif()  # aktifkan user baru
        self.assertTrue(self.dicoding.aktif)