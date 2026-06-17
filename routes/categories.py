from flask import Blueprint, render_template
from helpers.data_loader import load_json

categories_bp = Blueprint("categories", __name__)

CATEGORIES = [
    ("dining", "dining.html"),
    ("housing", "housing.html"),
    ("transportation", "transportation.html"),
    ("academics", "academics.html"),
    ("student_orgs", "student_orgs.html"),
    ("events", "events.html"),
    ("health", "health.html"),
]


def _make_category_view(slug, template):
    """Return a view function that loads <slug>.json and renders <template>."""
    def view():
        """Render this category page."""
        data = load_json(f"{slug}.json")
        return render_template(template, data=data)
    view.__name__ = slug
    return view


for _slug, _template in CATEGORIES:
    categories_bp.add_url_rule(
        f"/{_slug.replace('_', '-')}",
        endpoint=_slug,
        view_func=_make_category_view(_slug, _template),
    )
