from bok_inventarie import Bokhandel


Lindas_bokhandel = Bokhandel('Lindas litterära lustgård')

Lindas_bokhandel.lägg_till_ny_bok('Harry Potter', 'JKR', 50, 2)
Lindas_bokhandel.lägg_till_ny_bok('Kalle Anka', 'Disney', 24, 10)
Lindas_bokhandel.lägg_till_ny_bok('Sagan om ringen', 'Tolkien', 90, 21)
Lindas_bokhandel.lägg_till_ny_bok('Beck', 'Joppe', 99, 1)
Lindas_bokhandel.lägg_till_ny_bok('Trasan', 'Herbert Jansson', 88, 12)
Lindas_bokhandel.lägg_till_ny_bok('Python för nybörjare', 'Sebastian Öhman', 9, 22)

# Lindas_bokhandel.söka_efter_bok('Lindas egna bok')
Lindas_bokhandel.skriv_ut_alla_böcker()