class Animal:
  """
  Kelas dasar untuk merepresentasikan seekor hewan.
  """
  def __init__(self, name: str, age: int, species: str):
    """
    Menginisialisasi instance baru dari kelas Animal.

    Args:
      name: Nama hewan.
      age: Umur hewan.
      species: Spesies hewan.
    """
    self.name = name
    self.age = age
    self.species = species

class Cat(Animal):
  """
  Kelas untuk merepresentasikan seekor kucing, turunan dari kelas Animal.
  """
  def deskripsi(self) -> str:
    """
    Mengembalikan deskripsi lengkap tentang kucing.

    Returns:
      String deskripsi kucing.
    """
    return f"{self.name} adalah kucing berjenis {self.species} yang sudah berumur {self.age} tahun"

  def suara(self) -> str:
    """
    Mengembalikan suara khas kucing.

    Returns:
      String "meow!".
    """
    return "meow!"

# Membuat instance dari kelas Cat
myCat = Cat(name="Neko", age=3, species="Persian")

# Menampilkan hasil dari method
print(myCat.deskripsi())
print(myCat.suara())