# Velkomin/n í Captain Console hjá hóp 32.

# Síðan er keyrð á debug = FALSE og keyra þarf forritið á runserver --insecure

# Hlutir sem þarf að pip installa áður en vefsíðan er skoðuð eru:
# - Django Countries (pip install django-countries)
# - Pillow (pip install pillow)
# - Crispy Forms (pip install django-crispy-forms)
# - Psycopg2 - (pip install psycopg2)
# - Credit card support - (pip install django-credit-cards)

# Aukavirkni fyrir utan verkefnalýsinguna sem má finna á vefsíðunni eru:
# - Recently added products á forsíðunni
# - Clear cart, eyða öllum vörum í körfunni
# - Left in Stock, ef vörur eru ekki til á lager er ekki hægt að bæta þeim í körfu
# - Orders, pantanir verða til við staðfestingu í checkout. Hægt er að skoða þær í gagnagrunninum
# - Ekki er hægt að staðfesta pöntun ef maður hefur ekki fyllt út allar upplýsingar
