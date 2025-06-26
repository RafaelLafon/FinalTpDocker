FINAL TP - DOCKER

LAFON Rafael - B3 Cyber
--------------------------------------------------------
Ci-dessous, toutes les commandes réalisées par ordre chronologique ainsi que leur retour dans le termnal, le tout accompagné d'une note personnel sur l'utilité de chaque commandes :
--------------------------------------------------------

1.  ssh-keygen -t ed25519 -C "mon mail"

=>

Note : Génére une clé SSH



2.  cat ~/.ssh/id_ed25519.pub

=>

Note : Copie la clé publique



3.  ssh -T git@github.com

=>Hi RafaelLafon! You've successfully authenticated, but GitHub does not provide shell access.

Note : Test de la connexion



4.  Création manuel fichier python-app.yml

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



5.  Création manuel fichier simple_math.py

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



6.  Création manuel fichier requirements.txt

=>  unittest

Note : Workflow permettant de lancer les tests unitaires de mon app



7.  Création classe staticmethod

=>  @staticmethod
    def soustraction(a, b):
        return a - b

Note : Ajout de la soustraction



8.  Création manuel de test_simple_math.py

=>  from simple_math import SimpleMath  

    def test_soustraction(self):
    self.assertEqual(SimpleMath.soustraction(5, 3), 2)

Note : J'importe simple math et j'effectue un test



9.  Ajouter une étape de pylint dans requirement.txt

=> pylint

Note:



10. Modification du workflow 

=>       - name: Lint with pylint
        run: |
          pip install pylint
          pylint simple_math.py test_simple_math.py

Note : Analyse automatique du Python pour détecter les erreurs et assurer le respect des bonnes pratiques 



11. Création manuel du DOckerfile

=>  FROM python:3.10-slim

    WORKDIR /app
    COPY . .

    RUN pip install -r requirements.txt

    CMD ["python", "-m", "unittest"]

Note :



12. Modification du yml 

=>      - name: Build Docker image
        run: docker build -t simplemath-app .

Note : Lance le build docker