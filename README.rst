C'était trop choux
==================

Un petit recueil de truc trop choux.

Pour publier une nouvelle anecdote ? Ajouter un fichier, on la review,
on la merge et elle apparait en ligne sur :

http://cttc.trunat.fr/



Pour publier à partir du code source
====================================

Load and update plugins submodule::

    git submodule init
    git submodule update --recursive
    git submodule status

To build the blog, just run::

    make html

and to publish it::

    make publish

