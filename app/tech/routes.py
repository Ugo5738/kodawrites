from flask import render_template, request, url_for, redirect

from app.tech import bp
from app.extensions import db
from app.models.tech import Techarticle
from app.forms.tech import ArticleForm

from app.utils.generate import write_up
from datetime import date


@bp.route('/write', methods=['GET', 'POST'])
def write_article():
    tech_form = ArticleForm()
    article = None
    title = None
    current_date = None

    if tech_form.validate_on_submit():
        current_date = date.today()
        title = tech_form.title.data
        keywords = tech_form.keywords.data
            
        # Get article
        article = write_up(title, keywords)
    
    return render_template('tech/index.html', tech_form=tech_form, 
                                              article=article,
                                              title=title,
                                              date=current_date
                           )


@bp.route('/show-articles', methods=['GET', 'POST'])
def show_articles():
    tech_articles = Techarticle.query.all()
    return render_template('tech/index.html', tech_articles=tech_articles)