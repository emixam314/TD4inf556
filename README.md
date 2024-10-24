# TD4inf556

# Q2-Q3: 
  La méthode naïve utilise deux boucles imbriquées qui dans le pire des scénario engendre une complexité de O(m²).
  De plus la méthode fait appel à une fonction _add_columns_ qui compare deux à deux les éléments de chaque liste. Cette comparaison une complexité en O(m) qui mutipliée à la complexité précédente produit une complexité finale dans le pire des cas de O(m³).
  Dans la Q3, nous avons améliorer l'algorithme pour le meilleur cas bien qu'il reste en O(m³).

# Q7:
  Filtration A: 189 secondes 
  
  Filtration B: 4.99 secondes
  
  Filtration C: 10.91 secondes
  
  Filtration D: 486 secondes

  Ces temps sont bien supérieurs au temps théoriques annoncés dans l'énoncé.

# Q8:
  H0 indique les connexités des éléments.

  H1 nous renseigne sur les trous et les boucles.

  H2 nous renseigne sur les cavités.


Filtration A:

  H0: on observe beaucoup de points disconnectés au début puis qui finisse par se rassembler.

  H1: on observe de multiple boucles qui persistent puis s'évanouissent.

  H2: de meme que pour H1 on observe de nombreuses cavités.

  La filtration A doit provenir d'une surface complexe parsemée de cycle/trous et de cavité.



Filtration B:

  H0: on observe une connectivité persistente entre les éléments.

  H1: on observe cinq cycles qui s'évanouissent rapidement.

  H2: de nombreuses cavités apparaissent mais s'évanouissent rapidement.

 Cette filtration ressemble dans la structure globale à celle de A mais en plus épurée. Il doit s'agir d'une structure similaire possédant de nombreux cycles et cavités.



Filtration C:

  H0: on observe une connectivité persistente entre les éléments.

  H1: Une boucle unique et très persistente se distingue.

  H2: Une cavité initiale finit par se combler très rapidement.

  Au regard de ce barcode, on peut imaginer au départ un ruban fermé sur lui-même comme un tore coupé.


Filtration D:

  H0: on observe une connectivité persistente entre les éléments.

  H1: deux boucles se démarquent de cette structure.

  H2: une cavité persistente est révélée avec ce barcode

  les deux boucles accompagnées par une cavité persistente laissent fortement croire à une tore. 
