from django.db import models

class Question(models.Model):
    
    MAIN_TOPIC_CHOICES_GER = (
        ('Fischkunde und -hege','Fischkunde und -hege'),
        ('Pflege der Fischgewässer','Pflege der Fischgewässer'),
        ('Fanggeräte und deren Gebrauch','Fanggeräte und deren Gebrauch'),
        ('Behandlung der gefangenen Fische','Behandlung der gefangenen Fische'),
        ('Einschlägige Rechtsvorschriften','Einschlägige Rechtsvorschriften'),
    )

    MAIN_TOPIC_CHOICES_PL = (
        ('budowa ryb','budowa ryb'),
        ('dbanie o miejsca połowu','dbanie o miejsca połowu'),
        ('sprzęt wędkarski i jego użycie','sprzęt wędkarski i jego użycie'),
        ('obchodzenie się ze złapaną rybą','obchodzenie się ze złapaną rybą'),
        ('odpowiadające przepisy','odpowiadające przepisy'),
    )

    UNDER_TOPIC_CHOICES_GER = (
        ('Aufbau des Fischkörpers, Bau und Funktion der Fischorgane','Aufbau des Fischkörpers, Bau und Funktion der Fischorgane'),
        ('Unterscheidung einheimischer Fischarten','Unterscheidung einheimischer Fischarten'),
        ('häufig auftretende Fischkrankheite','häufig auftretende Fischkrankheiten'),
        ('Notwendigkeit von Besatzmaßnahme','Notwendigkeit von Besatzmaßnahme'),
        ('Naturnahrung, Sauerstoff und Temperaturverhältnisse','Naturnahrung, Sauerstoff und Temperaturverhältnisse'),
        ('Sonstiges-Fischkunde und -hege','Sonstiges-Fischkunde und -hege'),
        ('Fischereiliche Gewässerkunde','Fischereiliche Gewässerkunde'),
        ('Schutz der Gewässer vor Verunreinigung','Schutz der Gewässer vor Verunreinigung'),
        ('Ufer und Gelegeschutz','Ufer und Gelegeschutz'),
        ('Mittel und Geräte zur Gewässerinstandhaltung','Mittel und Geräte zur Gewässerinstandhaltung'),
        ('Sonstiges-Pflege der Fischgewässer','Sonstiges-Pflege der Fischgewässer'),
        ('Fanggeräte und deren Gebrauch','Fanggeräte und deren Gebrauch'),
        ('Betäuben, Töten und Schlachten von Fischen','Betäuben, Töten und Schlachten von Fischen'),
        ('Aufbewahrung von Fischen','Aufbewahrung von Fischen'),
        ('Tierschutz','Tierschutz'),
        ('Fischereiordnung des Landes Brandenburg (BbgFischO','Fischereiordnung des Landes Brandenburg (BbgFischO)'),
        ('Sonstiges-Behandlung der gefangenen Fische','Sonstiges-Behandlung der gefangenen Fische'),
        ('Landesfischereirecht','Landesfischereirecht'),
        ('Tierschutzrecht','Tierschutzrecht'),
        ('Naturschutzrecht','Naturschutzrecht'),
        ('Wasserrecht','Wasserrecht'),
        ('Sonstiges-Einschlägige Rechtsvorschriften','Sonstiges-Einschlägige Rechtsvorschriften'),
    )

    UNDER_TOPIC_CHOICES_PL = (
        ('budowa organów u ryb','budowa organów u ryb'),
        ('rozróżnianie rodzinych ryb','rozróżnianie rodzinych ryb'),
        ('najczęstrze choroby u ryb','najczęstrze choroby u ryb'),
        ('zarybianie','zarybianie'),
        ('naturalne warunki życia, tlen i temperatura','naturalne warunki życia, tlen i temperatura'),
        ('pozostałe-budowa ryb','pozostałe-budowa ryb'),
        ('hydrologia','hydrologia'),
        ('ochrona wód przed zanieczyszczeniem','ochrona wód przed zanieczyszczeniem'),
        ('ochrona brzegów i łowisk','ochrona brzegów i łowisk'),
        ('środki i sprzęt do utrzynania łowisk w dobrym stanie','środki i sprzęt do utrzynania łowisk w dobrym stanie'),
        ('pozostałe-dbanie o miejsca połowu','pozostałe-dbanie o miejsca połowu'),
        ('sprzęt wędkarski i jego użycie','sprzęt wędkarski i jego użycie'),
        ('ogłuszanie, uśmiercanie i szlachtowanie ryb','ogłuszanie, uśmiercanie i szlachtowanie ryb'),
        ('przechowywanie ryb','przechowywanie ryb'),
        ('ochrona zwierząt','ochrona zwierząt'),
        ('prawo dot. wędkarstwa w Brandenburgii','prawo dot. wędkarstwa w Brandenburgii'),
        ('pozostałe-obchodzenie się ze złapaną rybą','pozostałe-obchodzenie się ze złapaną rybą'),
        ('prawo połowu','prawo połowu'),
        ('prawo dot. ochrony zwierząt','prawo dot. ochrony zwierząt'),
        ('prawo dot. ochrony przyrody','prawo dot. ochrony przyrody'),
        ('prawo wodne','prawo wodne'),
        ('pozostałe-odpowiadające przepisy','pozostałe-odpowiadające przepisy'),
    )

    question_id = models.IntegerField()

    main_topic_ger = models.CharField(max_length=200, choices=MAIN_TOPIC_CHOICES_GER)
    main_topic_pl = models.CharField(max_length=200, choices=MAIN_TOPIC_CHOICES_PL)

    under_topic_ger = models.CharField(max_length=200, choices=UNDER_TOPIC_CHOICES_GER)
    under_topic_pl = models.CharField(max_length=200, choices=UNDER_TOPIC_CHOICES_PL)

    question_ger = models.TextField(max_length=400)
    question_pl = models.TextField(max_length=400)

    answer_a_ger = models.TextField(max_length=400)
    answer_a_pl = models.TextField(max_length=400)

    answer_b_ger = models.TextField(max_length=400)
    answer_b_pl = models.TextField(max_length=400)

    answer_c_ger = models.TextField(max_length=400)
    answer_c_pl = models.TextField(max_length=400)

    correct_answer_ger = models.TextField(max_length=400)
    correct_answer_pl = models.TextField(max_length=400)

    objects = models.Manager()

    def __str__(self):
        return f'{self.question_id} . {self.question_ger}'
    
    class Meta:
        ordering = ('question_id',)