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
        'SELECT title, rating, review, season, episode, status, added_on'
        ' FROM series WHERE user_id = ?'
        ' ORDER BY rating DESC', (g.user['id'],)
    ).fetchall()
    return render_template('media/series.html', series=series)

@bp.route('/add_series', methods=('GET', 'POST'))
@login_required
def add_series():
    if request.method == 'POST':
        title = request.form['title']
        rating = request.form['rating']
        review = request.form.get('review')
        season = request.form.get('season', 1)
        episode = request.form.get('episode', 1)
        status = request.form.get('status', 'watching')
        db = get_db()
        db.execute(
            'INSERT INTO series (user_id, title, rating, review, season, episode, status)'
            ' VALUES (?, ?, ?, ?, ?, ?, ?)',
            (g.user['id'], title, rating, review, season, episode, status)
        )
        db.commit()
        return redirect(url_for('media.series'))

    return render_template('media/add_series.html')

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

@bp.route('/toggle_status/<int:id>', methods=['POST'])
@login_required
def toggle_status(id):
    db = get_db()
    serie = db.execute(
        'SELECT status FROM series WHERE id = ? AND user_id = ?',
        (id, g.user['id'])
    ).fetchone()

    # Cambia el estado a 'completado' si es 'viendo', y viceversa
    new_status = 'completed' if serie['status'] == 'watching' else 'watching'
    db.execute(
        'UPDATE series SET status = ? WHERE id = ? AND user_id = ?',
        (new_status, id, g.user['id'])
    )
    db.commit()
    return redirect(url_for('media.series'))