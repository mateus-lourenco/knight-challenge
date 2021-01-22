from django.db import models
from django.utils.translation import gettext as _


class Piece(models.Model):

    TYPE_CHOICES = (('kg', 'king'),
                    ('qn', 'queen'),
                    ('rk', 'rook'),
                    ('bp', 'bishop'),
                    ('kt', 'knight'),
                    ('pn', 'pawn'),
                    )
    COLOR_CHOICES = (('bk', 'black'), ('wt', 'white'))

    name = models.CharField(_("piece's name/type"),
                            max_length=50,
                            choices=TYPE_CHOICES)

    color = models.CharField(_("piece's color"),
                             max_length=50,
                             choices=COLOR_CHOICES)

    class Meta:
        db_table = "piece"
