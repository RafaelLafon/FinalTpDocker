FINAL TP - DOCKER

LAFON Rafael - B3 Cyber
--------------------------------------------------------
Ci-dessous, toutes les commandes réalisées par ordre chronologique ainsi que leur retour dans le termnal, le tout accompagné d'une note personnel sur l'utilité de chaque commandes :
--------------------------------------------------------

1.ssh-keygen -t ed25519 -C "mon mail"

=>

Note : Génére une clé SSH



2.cat ~/.ssh/id_ed25519.pub

=>

Note : Copie la clé publique



3.ssh -T git@github.com

=>Hi RafaelLafon! You've successfully authenticated, but GitHub does not provide shell access.

Note : Test de la connexion



4.Création manuel fichier python-app.yml

=>  name: Python application

    on: [push]

    jobs:
    build:
        runs-on: ubuntu-latest
        steps:
        - uses: actions/checkout@v4
        - name: Set up Python
            uses: actions/setup-python@v4
            with:
            python-version: '3.10'
        - name: Install dependencies
            run: pip install -r requirements.txt
        - name: Run tests
            run: python -m unittest

Note : Création d'un fichier de workflow 



5.Création manuel fichier simple_math.py

=>  import unittest
    from simple_math import SimpleMath


    class SimpleMath:
    @staticmethod
    def addition(a, b):
        return a + b

    class TestSimpleMath(unittest.TestCase):
        def test_addition(self):
            self.assertEqual(SimpleMath.addition(2, 3), 5)

    if __name__ == "__main__":
        unittest.main()


Note : Création de la classe SimpleMath et de la classe 



6.