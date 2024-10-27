from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from mediapp.auth import login_required
from mediapp.db import get_db

bp = Blueprint('media', __name__)

@bp.route('/')
@login_required
def index():
    return render_template('media/index.html')

@bp.route('/movies')
@login_required
def movies():
    db = get_db()
    movies = db.execute(
        'SELECT title, rating, review, added_on'
        ' FROM movies WHERE user_id = ?'
        ' ORDER BY rating DESC', (g.user['id'],)
    ).fetchall()
    return render_template('media/movies.html', movies=movies)

@bp.route('/series')
@login_required
def series():
    db = get_db()
    series = db.execute(
        'SELECT title, rating, review, episode, status, added_on'
        ' FROM series WHERE user_id = ?'
        ' ORDER BY rating DESC', (g.user['id'],)
    ).fetchall()
    return render_template('media/series.html', series=series)

@bp.route('/add_movie', methods=('GET', 'POST'))
@login_required
def add_movie():
    if request.method == 'POST':
        title = request.form['title']
        rating = request.form['rating']
        review = request.form.get('review')
        db = get_db()
        db.execute(
            'INSERT INTO movies (user_id, title, rating, review)'
            ' VALUES (?, ?, ?, ?)',
            (g.user['id'], title, rating, review)
        )
        db.commit()
        return redirect(url_for('media.movies'))

    return render_template('media/add_movie.html')

@bp.route('/add_series', methods=('GET', 'POST'))
@login_required
def add_series():
    if request.method == 'POST':
        title = request.form['title']
        rating = request.form['rating']
        review = request.form.get('review')
        episode = request.form.get('episode', 1)
        status = request.form.get('status', 'watching')
        db = get_db()
        db.execute(
            'INSERT INTO series (user_id, title, rating, review, episode, status)'
            ' VALUES (?, ?, ?, ?, ?, ?)',
            (g.user['id'], title, rating, review, episode, status)
        )
        db.commit()
        return redirect(url_for('media.series'))

    return render_template('media/add_series.html')