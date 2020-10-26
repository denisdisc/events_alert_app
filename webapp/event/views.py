from flask import Blueprint, flash, render_template  # current_app выведем события
from flask_login import current_user, login_required
from webapp.event.forms import CommentForm
from webapp.event.models import Comment  # Event
from webapp.models import db


blueprint = Blueprint('event', __name__)


@blueprint.route('/')
def index():
    title = 'Куда сходить и чем заняться в Москве'
    # Вывести события 
    return render_template('event/index.html', page_title=title)


@blueprint.route('/news/comment', methods=['POST'])
@login_required
def add_comment():
    form = CommentForm()
    if form.validate_on_submit():
        comment = Comment(text=form.comment_text, event_id=form.event_id, user_id=current_user.id)  # ????
        db.session.add(comment)
        db.session.commit()
        flash('Комментарий успешно добавлен')