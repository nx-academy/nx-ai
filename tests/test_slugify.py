import sys
import os

# Fix to make test work with import path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from nx_ai.utils.slugify import slugify_title


def test_slugify_short_title():
    title = "Un super titre"
    slugy_title = slugify_title(title)
    
    assert slugy_title == "un-super-titre"


def test_slugify_long_title():
    title = "GitHub Actions propose un nouveau cache distribué pour accélérer les workflows CI"
    slugy_title = slugify_title(title)
    
    assert slugy_title == "github-actions-propose-un-nouveau-cache-distribu-pour-acclrer-les-workflows-ci"


def test_slugify_with_apostrophe():
    title = "L’actualité de l’IA"
    slugy_title = slugify_title(title)
    assert slugy_title == "l-actualite-de-l-ia"


def test_slugify_truncation():
    title = "a " * 100 
    slugy_title = slugify_title(title)
    
    assert len(slugy_title) <= 80
